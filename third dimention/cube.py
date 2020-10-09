import tkinter
from math import *

master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=800, height=800, bg='white')
i = [0, 100, 0, 0, 100, 100, 0, 100]
j = [0, 0, 100, 0, 100, 0, 100, 100]
k = [0, 0, 0, 100, 0, 100, 100, 100]
edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6), (7, 6), (7, 5), (7, 4)]
r = 10
l = []
p = []
c = ['red', 'blue', 'green', 'yellow']
angle = 0
coordinates = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
coordinates1 = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]

for t in edges:
    l.append(canvas.create_line((t[1], t[0]), (t[1] + 1, t[0] + 1)))
    # p.append(canvas.create_oval((0,0),(1,t), fill=c[t%4]))


def game(event):
    global canvas
    print(event.x, event.y)
    for t in range(8):
        a = (event.x - 400) / 800 * 3 * pi + pi / 4
        b = (event.y - 400) / 800 * 3 * pi + pi / 4
        x = (i[t] - 50) * sin(a) - (j[t] - 50) * cos(a)
        y = ((i[t] - 50) * cos(a) + (j[t] - 50) * sin(a)) * cos(b) - (k[t] - 50) * sin(b)
        x1 = x * cos(angle) - y * sin(angle)

        y1 = x * sin(angle) + y * cos(angle)
        coordinates[t] = [x1 + 400, y1 + 400]
        coordinates1[t] = [x, y]
    for o in range(12):
        canvas.coords(l[o], coordinates[edges[o][0]][0], coordinates[edges[o][0]][1],   coordinates[edges[o][1]][0], coordinates[edges[o][1]][1])


def rot(event):
    global angle
    if event.keysym == 'ocircumflex':
        angle += (0.05)
    if event.keysym == 'acircumflex':
        angle -= (0.05)
    for t in range(8):
        x = coordinates1[t][0]
        y = coordinates1[t][1]
        x1 = x * cos(angle) - y * sin(angle)

        y1 = x * sin(angle) + y * cos(angle)
        coordinates[t] = [x1 + 400, y1 + 400]

    for o in range(12):
        canvas.coords(l[o], coordinates[edges[o][0]][0], coordinates[edges[o][0]][1],   coordinates[edges[o][1]][0], coordinates[edges[o][1]][1])


canvas.pack()
master.bind('<Motion>', game)
master.bind('<KeyPress>', rot)
master.mainloop()

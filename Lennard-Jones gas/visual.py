import tkinter
from math import *
from math import *
import numpy as np
all_coords = []
time = 0
scale = 30
with open('/Users/rmnmlv/PycharmProjects/OldPycharmProjects/Lennard-Jones gas/coordinates', 'r') as file_coords:
    for line in file_coords:
        coords = []
        x = line.split(' ')
        for i in x:
            dot = []
            for j in i.split(';'):
                if j!='\n':
                    dot.append(float(j))
            if dot != []:
                coords.append(dot)
        print(len(coords))
        all_coords.append(coords)

master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=800, height=800, bg='white')
print(all_coords[time])
cvordinates = list(np.array(all_coords[time]).transpose() * scale)
connections = []
edges = []
r = 10
l = []
dots = []
picked_points = []
n = len(cvordinates[0])
c = ['red', 'blue', 'green', 'yellow']
angle = 0
coordinates = []
for i in range(len(cvordinates[0])):
    if cvordinates[0][i]>5:
        dots.append(canvas.create_oval(1, 1, 1, 1, fill='blue'))
    else:
        dots.append(canvas.create_oval(1, 1, 1, 1, fill='red'))
    coordinates.append(0)
    # p.append(canvas.create_oval((0,0),(1,t), fill=c[t%4]))

X = 0
Y = 0


def game(event):
    global canvas
    global X, Y
    X = event.x
    Y = event.y
    for t in range(n):
        a = (event.x - 400) / 800 * 3 * pi + pi / 4
        b = (event.y - 400) / 800 * 3 * pi + pi / 4
        x = (cvordinates[0][t]) * sin(a) - (cvordinates[1][t]) * cos(a)
        y = ((cvordinates[0][t]) * cos(a) + (cvordinates[1][t]) * sin(a)) * cos(b) - (cvordinates[2][t]) * sin(b)
        x1 = x * cos(angle) - y * sin(angle)

        y1 = x * sin(angle) + y * cos(angle)
        coordinates[t] = [x1 + 400, y1 + 400]
        # coordinates1[t] = [x, y]
    for o in range(n):
        canvas.coords(dots[o], coordinates[o][0], coordinates[o][1], coordinates[o][0] + 5, coordinates[o][1] + 5)


def step(event):
    global angle
    global time
    global cvordinates
    global X, Y

    if event.char == 'd':
        time = time + 1
        cvordinates = list(np.array(all_coords[time]).transpose() * scale)
    if event.char == 'a':
        time = time - 1
        cvordinates = list(np.array(all_coords[time]).transpose() * scale)
    if event.char == 'l':
        time = time + 10
        cvordinates = list(np.array(all_coords[time]).transpose() * scale)
    if event.char == 'j':
        time = time - 10
        cvordinates = list(np.array(all_coords[time]).transpose() * scale)

    for t in range(n):
        a = (X - 400) / 800 * 3 * pi + pi / 4
        b = (Y - 400) / 800 * 3 * pi + pi / 4
        x = (cvordinates[0][t]) * sin(a) - (cvordinates[1][t]) * cos(a)
        y = ((cvordinates[0][t]) * cos(a) + (cvordinates[1][t]) * sin(a)) * cos(b) - (cvordinates[2][t]) * sin(b)
        x1 = x * cos(angle) - y * sin(angle)

        y1 = x * sin(angle) + y * cos(angle)
        coordinates[t] = [x1 + 400, y1 + 400]
        # coordinates1[t] = [x, y]
    for o in range(n):
        canvas.coords(dots[o], coordinates[o][0], coordinates[o][1], coordinates[o][0] + 5, coordinates[o][1] + 5)


def pick(event):
    x0 = event.x
    y0 = event.y
    l = 500
    pick_point = 0
    for j in range(n):
        i = coordinates[j]
        l1 = sqrt((i[0] - x0) ** 2 + (i[1] - y0) ** 2)
        if l1 < l:
            l = l1
            pick_point = j
    if pick_point not in picked_points:
        picked_points.append(pick_point)
        canvas.itemconfig(dots[pick_point], fill='red')
    else:
        picked_points.remove(pick_point)
        canvas.itemconfig(dots[pick_point], fill='blue')


def connect(event):
    if len(picked_points) >= 2:
        pass


canvas.pack()
master.bind('<Motion>', game)
master.bind('<KeyPress>', step)
master.bind('<Button-1>', pick)
master.mainloop()

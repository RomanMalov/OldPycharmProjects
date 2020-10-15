import tkinter
from math import *
from math import*
master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=800, height=800, bg='white')

i = []
j = []
k = []
for x in range(10):
    for y in range(10):
        z = 10*sin(0.5*x)*sin(0.5*y)
        i.append(30*x)
        j.append(30*y)
        k.append(30*z)
cvordinates = [i,j,k]
connections=[]
edges = []
picked_points = []
r = 10
l = []
dots=[]
n = len(cvordinates[0])
c = ['red', 'blue', 'green', 'yellow']
angle = 0
coordinates = []
for i in range(len(cvordinates[0])):
    dots.append(canvas.create_oval(1,1,1,1, fill = 'blue'))
    coordinates.append(0)
    # p.append(canvas.create_oval((0,0),(1,t), fill=c[t%4]))


def game(event):
    global canvas

    for t in range(n):
        a = (event.x - 400) / 800 * 3 * pi + pi / 4
        b = (event.y - 400) / 800 * 3 * pi + pi / 4
        x = (cvordinates[0][t] ) * sin(a) - (cvordinates[1][t]) * cos(a)
        y = ((cvordinates[0][t]) * cos(a) + (cvordinates[1][t] ) * sin(a)) * cos(b) - (cvordinates[2][t]) * sin(b)
        x1 = x * cos(angle) - y * sin(angle)

        y1 = x * sin(angle) + y * cos(angle)
        coordinates[t] = [x1 + 400, y1 + 400]
        #coordinates1[t] = [x, y]
    for o in range(n):
        canvas.coords(dots[o], coordinates[o][0], coordinates[o][1], coordinates[o][0]+5, coordinates[o][1]+5 )


def rot(event):
    global angle
    if event.char == 'd':
        angle += (0.05)
    if event.char == 'a':
        angle -= (0.05)

    for t in range(n):
        a = (event.x - 400) / 800 * 3 * pi + pi / 4
        b = (event.y - 400) / 800 * 3 * pi + pi / 4
        x = (cvordinates[0][t] ) * sin(a) - (cvordinates[1][t]) * cos(a)
        y = ((cvordinates[0][t]) * cos(a) + (cvordinates[1][t] ) * sin(a)) * cos(b) - (cvordinates[2][t]) * sin(b)
        x1 = x * cos(angle) - y * sin(angle)

        y1 = x * sin(angle) + y * cos(angle)
        coordinates[t] = [x1 + 400, y1 + 400]
        #coordinates1[t] = [x, y]
    for o in range(n):
        canvas.coords(dots[o], coordinates[o][0], coordinates[o][1], coordinates[o][0]+5, coordinates[o][1]+5 )

def pick(event):
    x0 = event.x
    y0 = event.y
    l=500
    pick_point=0
    for j in range(n):
        i = coordinates[j]
        l1 = sqrt((i[0]-x0)**2+(i[1]-y0)**2)
        if l1<l:
            l=l1
            pick_point=j
    if pick_point not in picked_points:
        picked_points.append(pick_point)
        canvas.itemconfig(dots[pick_point], fill = 'red')
    else:
        picked_points.remove(pick_point)
        canvas.itemconfig(dots[pick_point], fill = 'blue')


def connect(event):
    if len(picked_points)>=2:
        pass
canvas.pack()
master.bind('<Motion>', game)
master.bind('<KeyPress>', rot)
master.bind('<Button-1>', pick)
master.mainloop()

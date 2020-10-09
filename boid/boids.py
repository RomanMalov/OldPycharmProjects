from tkinter import*
import random
from math import*
master = Tk()
canvas = Canvas(master, height=800, width=800, bg='white')
s=500
rx=200
ry=200
r=100
koeff=0
def dist(a,b):
    ex=a-rx
    ey=b-ry
    l1 = (ex**2+ey**2)**(0.5)
    l=l1 if l1!=0 else r
    x1=-ex+ex*r/l
    y1=-ey+ey*r/l
    f = (x1**2+y1**2)**(0.5)
    angle = asin(y1/f) if x1>0 else (pi-asin(y1/f))
    angle+=0.01
    return f*cos(angle) ,f*sin(angle), l
list_boids=[]
for i in range(s):
    list_boids.append([random.randint(1,800), random.randint(1,800)])
list_direct=[]
for j in range(s):
    x=list_boids[(j+2)%s][0]-list_boids[j][0]
    y=list_boids[(j+2)%s][1]-list_boids[j][1]
    l = (x**2+y**2)**(0.5)
    list_direct.append(asin(y/l) if x>0 else (pi-asin(y/l)))
ovals=[]

for i in range(s):
    t=canvas.create_line(int(list_boids[i][0]),int(list_boids[i][1]),
                         int(list_boids[i][0]+5*cos(list_direct[i])),
                         int(list_boids[i][1]+5*sin(list_direct[i])))

    ovals.append(t)
def game(event):
    global list_direct
    global list_boids
    global r
    if event.char == 'a':
        r+=1
    if event.char == 'o':
        r-=1
    for i in range(s):
        list_boids[i][0] = (list_boids[i][0] + 5 * cos(list_direct[i]))%800
        list_boids[i][1] = (list_boids[i][1] + 5 * sin(list_direct[i]))%800
    for j in range(s):
        x1, y1, d = dist(*list_boids[j])

        x = list_boids[(j + 2) % s][0] - list_boids[j][0]+koeff*x1*r/(r+d)
        y = list_boids[(j + 2) % s][1] - list_boids[j][1]+koeff*y1*r/(r+d)
        l = (x ** 2 + y ** 2) ** (0.5)
        list_direct[j]=(asin(y / l) if x > 0 else (pi - asin(y / l)))
    for i in range(s):
        canvas.coords(ovals[i],int(list_boids[i][0]), int(list_boids[i][1]),
                               int(list_boids[i][0] + 5 * cos(list_direct[i])),
                               int(list_boids[i][1] + 5 * sin(list_direct[i])))


master.bind('<KeyPress>', game)
canvas.pack()
master.mainloop()


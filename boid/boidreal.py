from tkinter import *
import random
from math import *

s = 200
h = 650
w = 650
k1 = 7
k2=0.8
k3=40
master = Tk()
canvas = Canvas(master, height=h, width=w, bg='white')

list_coord = []
for i in range(s):
    list_coord.append([random.randint(1, w), random.randint(1, h)])
list_direct = []
for i in range(s):
    list_direct.append(random.random() * pi - pi)
ovals = []
for i in range(s):
    t = canvas.create_line(int(list_coord[i][0]), int(list_coord[i][1]),
                           int(list_coord[i][0] + 5 * cos(list_direct[i])),
                           int(list_coord[i][1] + 5 * sin(list_direct[i])))

    ovals.append(t)


def find(k):
    kk = []
    for i in range(s):
        if (k[0] % w - w // 10) < list_coord[i][0] < (k[0] % w + w // 10) and (k[1] % h - h // 10) < list_coord[i][
            1] < (k[1] % h + h // 10):
            kk.append(i)
    return kk
def lenth(a, b):
    return sqrt(a**2+b**2)

def game(event):
    for i in range(s):
        list_coord[i][0] = (list_coord[i][0] + 5 * cos(list_direct[i])) % w
        list_coord[i][1] = (list_coord[i][1] + 5 * sin(list_direct[i])) % h
    for i in range(s):
        x0 = list_coord[i][0]
        y0 = list_coord[i][1]
        kk = find(list_coord[i])
        angle = 0
        for j in kk:
            angle += list_direct[j]
        angle = angle / len(kk)
        x1 = k1 * cos(angle)
        y1 = k1 * sin(angle)
        x2 = 0
        y2 = 0
        x3 = 0
        y3 = 0

        for j in kk:
            x= list_coord[j][0]
            y= list_coord[j][1]
            if x0>=(w-w//10) and x<w//2:
                x=x+w
            if y0>=(h-h//10) and y<h//2:
                y=y+h
            if x0<w//10 and x>w//2:
                x=x-w
            if y0<h//10 and y>h//2:
                y=y-h
            x2+=(x-x0)
            y2+=(y-y0)
            x3+=-(x-x0)/(lenth(x-x0, y-y0)+5)
            y3 += -(y - y0) / (lenth(x - x0, y - y0) + 1)

        x2=x2*k2/len(kk)
        y2=y2*k2/len(kk)
        y3=y3*k3/len(kk)
        x3=x3*k3/len(kk)
        xs = x1+x2+x3
        ys = y1+y2+y3
        l = (xs ** 2 + ys ** 2) ** (0.5)
        list_direct[i]=(asin(ys / l) if xs > 0 else (pi - asin(ys / l)))
    for i in range(s):
        canvas.coords(ovals[i], int(list_coord[i][0]), int(list_coord[i][1]),
                      int(list_coord[i][0] + 5 * cos(list_direct[i])),
                      int(list_coord[i][1] + 5 * sin(list_direct[i])))




def start():
    game(1)
    master.after(10, start)
def meme(event):
    global k1 , k2, k3
    if event.char=='a':
        k1*=1.01
    if event.char=='z':
        k1*=0.99
    if event.char=='s':
        k2*=1.01
    if event.char=='x':
        k2*=0.99
    if event.char=='d':
        k3*=1.01
    if event.char=='c':
        k3*=0.99
    if event.char=='p':
        print(k1,k2,k3)

start()
master.bind('<KeyPress>', meme)
canvas.pack()
master.mainloop()

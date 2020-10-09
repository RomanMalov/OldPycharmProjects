import numpy as np
from tkinter import*
import random
def com(event):
    global a
    global kvadrat
    nb =  sum([
    np.roll(np.roll(a, -1, 1), 1, 0),
    np.roll(np.roll(a, 1, 1), -1, 0),
    np.roll(np.roll(a, 1, 1), 1, 0),
    np.roll(np.roll(a, -1, 1), -1, 0),
    np.roll(a, 1, 1),
    np.roll(a, -1, 1),
    np.roll(a, 1, 0),
    np.roll(a, -1, 0)])
    for x in range(20):
        for y in range(16):
            a[x, y] = 1 if ((nb[x, y] == 3) or (a[x, y] and (nb[x, y] == 2))) else 0
            cvet = 'white' if (a[x, y] == 0) else 'black'
            canvas.itemconfig(kvadrat[y][x], fill = cvet)
def func(evet):
    global a
    global kvadrat
    x = (evet.x//50)
    y = (evet.y//50)
    if a[x, y] == 0:
        canvas.itemconfig(kvadrat[y][x], fill = 'black')
        a[x, y] = 1
    else:
        canvas.itemconfig(kvadrat[y][x], fill = 'white')
        a[x, y] = 0
a = np.zeros(320).reshape(20, 16)
master = Tk()
canvas = Canvas(master, width = 1000, height = 800, bg = 'white')
kvadrat = []
x=  0
y = 0
for i in range(16):
    kv = []
    for  j in range(20):
        kvad = canvas.create_rectangle((x,y),(x+50, y+50), fill = 'white')
        x+=50
        kv.append(kvad)
    kvadrat.append(kv)
    y+=50
    x=0
canvas.pack()
master.bind('<KeyPress>', com)
master.bind('<ButtonPress>', func)
master.mainloop()
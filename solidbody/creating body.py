from tkinter import *
import random
from math import *

master1 = Tk()
canvas = Canvas(master1, height=800, width=800, bg='white')
coords_of_line = []


def game1(event):
    global coords_of_line
    x = event.x
    y = event.y
    if not (x, y) in coords_of_line:
        coords_of_line.append([x, y])
    if len(coords_of_line) > 1:
        canvas.create_line(coords_of_line[-2][0], coords_of_line[-2][1], x, y)


def inn(a, b, c):
    m = min(b, c)
    d = abs(b - c)
    return m <= a <= m + d


def cross(coords1A, coords1B, coords2A, coords2B):
    k1 = (coords1A[1] - coords1B[1]) / (coords1A[0] - coords1B[0])
    b1 = coords1A[1] - coords1A[0] * k1
    k2 = (coords2A[1] - coords2B[1]) / (coords2A[0] - coords2B[0])
    b2 = coords2A[1] - coords2A[0] * k2
    if k1-k2!=0:
        xroot = (b2 - b1) / (k1 - k2)
        yroot = k1 * xroot + b1
        if inn(xroot, coords1A[0], coords1B[0]) and inn(xroot, coords2A[0], coords2B[0]) and inn(yroot, coords2A[1],
                                                                                                 coords2B[1]) and inn(yroot,
                                                                                                                      coords1A[
                                                                                                                          1],
                                                                                                                      coords1B[
                                                                                                                          1]):
            return True
        else:
            return False
    else:
        return False

master1.bind( '<Button-1>' , game1)
canvas.pack()
master1.mainloop()
t=False
for i in range(len(coords_of_line)):
    for j in range(len(coords_of_line)):
        a1 = coords_of_line[i]
        a2 = coords_of_line[(i+1)%len(coords_of_line)]
        b1 = coords_of_line[j]
        b2 = coords_of_line[(j + 1) % len(coords_of_line)]
        t = t or cross(a1,a2,b1,b2)
print(t)



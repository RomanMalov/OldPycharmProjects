from tkinter import*
import random
from math import*
master1 = Tk()
canvas = Canvas(master1, height=800, width=800, bg='white')
coords_of_line = []
def game1(event):
    global coords_of_line
    x = event.x
    y = event.y
    if not (x,y) in coords_of_line:
        coords_of_line.append([x,y])
    if len(coords_of_line)>1:
        canvas.create_line(coords_of_line[-2][0], coords_of_line[-2][1], x, y)

master1.bind('<Button-1>', game1)
canvas.pack()
master1.mainloop()
from tkinter import *
import random
from math import *

master1 = Tk()
canvas1 = Canvas(master1, height=800, width=1000, bg='white')
coords_of_line = []


def game1(event):
    global coords_of_line
    x = event.x
    y = event.y
    if not (x, y) in coords_of_line:
        coords_of_line.append([x, y])
    if len(coords_of_line) > 1:
        canvas1.create_line((coords_of_line[-2][0], coords_of_line[-2][1]), (x, y))
master1.bind('<Button-1>', game1)
canvas1.pack()
master1.mainloop()
#coords_of_line=[[100, 400], [300, 600],[700, 200], [900, 400]]
if bool(coords_of_line):

    ugols = []


    def f3(a, b):
        x = b[0] - a[0]
        y = b[1] - a[1]
        l = sqrt(x ** 2 + y ** 2)
        return (asin(y / l) if x >= 0 else (pi - asin(y / l))), l

    ugol0 = f3(coords_of_line[0], coords_of_line[-1])[0]
    for i in range(len(coords_of_line) - 1):
        ugols.append(f3(coords_of_line[i], coords_of_line[i + 1])[0]-ugol0)

    lens = []
    for i in range(len(coords_of_line) - 1):
        lens.append(f3(coords_of_line[i], coords_of_line[i + 1])[1])

    master = Tk()
    canvas = Canvas(master, height=800, width=1000)


    # for i in range(len(coords_of_line)-1):
    #    canvas.create_line(coords_of_line[i], (coords_of_line[i][0]+lens[i]*cos(ugols[i]), coords_of_line[i][1]+lens[i]*sin(ugols[i])))

    class Line:
        def __init__(self, firstcoord, lenth, ugol):
            global canvas
            self.firstcoord = firstcoord
            self.size = lenth
            self.ugol = ugol
            self.lastcoord = [firstcoord[0] + lenth * cos(ugol), firstcoord[1] + lenth * sin(ugol)]
            self.thisline = canvas.create_line(int(firstcoord[0]), int(firstcoord[1]), int(self.lastcoord[0]), int(self.lastcoord[1]))


    def iteration(line):  # фракталы - это самоподобные структуры. Эта функция превращает объект во всю конструкцию в целом
        canvas.delete(line.thisline)  # тут я удаляю линию
        listofline = [Line(line.firstcoord, line.size * lens[0] / firstlenth, line.ugol + ugols[0])]
        for i in range(len(ugols)-1):
            listofline.append(Line(listofline[-1].lastcoord, line.size * lens[i+1] / firstlenth, line.ugol + ugols[i+1]))
        return listofline  # возвращает список линий


    firstlenth = f3(coords_of_line[0], coords_of_line[-1])[1]

    l = Line(coords_of_line[0], firstlenth, ugol0)

    numberiter = 0
    listline = []


    def nextiterat(event):  # функция для кнопки
        global numberiter
        global listline
        if numberiter == 0:
            listline = iteration(l)
        else:
            newlistline = []
            for i in listline:
                t=iteration(i)
                for j in t:
                    newlistline.append(j)
            listline = newlistline
        numberiter += 1
    master.bind('<KeyPress>', nextiterat)
    canvas.pack()
    master.mainloop()

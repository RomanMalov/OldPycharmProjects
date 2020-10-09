from tkinter import *
import random
from math import *

master1 = Tk()
canvas1 = Canvas(master1, height=500, width=500, bg='white')
coords_of_line = []


def game1(event):
    global coords_of_line
    x = event.x
    y = event.y
    if not (x, y) in coords_of_line:
        coords_of_line.append([x, y])
    if len(coords_of_line) > 1:
        canvas1.create_line(coords_of_line[-2][0], coords_of_line[-2][1], x, y)


master1.bind('<Button-1>', game1)
canvas1.pack()
master1.mainloop()
ugols = []


def f3(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    l = sqrt(x ** 2 + y ** 2)
    return asin(y / l) / (pi / 2) if x > 0 else (pi - asin(y / l)) / (pi / 2), l


for i in range(len(coords_of_line) - 1):
    ugols.append(f3(coords_of_line[i], coords_of_line[i + 1])[0])
lens = []
for i in range(len(coords_of_line) - 1):
    lens.append(f3(coords_of_line[i], coords_of_line[i + 1])[1])


def f1(coor, siz, ugo):  # функция для х(ТРИГОНОМЕТРИЯ)
    x = coor + int(cos(ugo * pi / 2) * siz)
    return x


def f2(coor, siz, ugo):  # то же самое для у
    y = coor + int(sin(ugo * pi / 2) * siz)
    return y



class Line:  # класс линия, передаём ей координаты начала, размер и угол(потом объясню что это)
    def __init__(self, coord1, coord2, size, ugol):
        self.firstcoord = (coord1, coord2)  # тут всё понятно
        self.ugol = ugol  # тут всё понятно
        self.size = size  # тут всё понятно
        self.lastcoord = (f1(coord1, size, ugol), f2(coord2, size,
                                                     ugol))  # это последние координаты линии, которые строятся через функции для х и y
        self.thisline = canvas.create_line((coord1, coord2), self.lastcoord)  # тут всё понятно


# теперь поясняю, что такое угол. В моей ситстеме это 90 градусов. +1 это + 90 градусов, -1 это -90 градусов, -2 это -180 градусов и тд
def iteration(line):  # фракталы - это самоподобные структуры. Эта функция превращает объект во всю конструкцию в целом
    canvas.delete(line.thisline)  # тут я удаляю линию
    listofline = [Line(*line.firstcoord, line.size*lens[0]/firstlenth, line.ugol+ugols[0])]
    for i in range(len(ugols)):
        listofline.append(Line(*listofline[-1].lastcoord, line.size*lens[i]/firstlenth, line.ugol+ugols[i]))
    return   listofline# возвращает список линий


'''def antiiteration(listlines):
    newline = Line(*listlines[0].firstcoord, listlines[0].size * 4, listlines[0].ugol)
    for i in listlines:
        canvas.delete(i.thisline)
    return newline'''


master = Tk()  # тут всё понятно
canvas = Canvas(master, height=500, width=500, bg='white')  # тут всё понятно
firstlenth= f3(coords_of_line[0], coords_of_line[-1])[1]
l = Line(*coords_of_line[0], firstlenth, f3(coords_of_line[0], coords_of_line[-1])[0])  # создаём объект
numberiter = 0
listline = []


def nextiterat():  # функция для кнопки
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


'''def previousiterat():
    global numberiter
    global listline
    if numberiter > 0:
        numberiter -= 1
        for i in range(len(listline)):
            listline[i] = antiiteration(listline[i])'''


'''previousiter = Button(master, text='Previous Iteration', command=previousiterat)'''
nextiter = Button(master, text='Next Iteration', height = 2, width = 20,command=nextiterat)
canvas.pack()
nextiter.pack()
# previousiter.pack() я до конца не разобрался, как должна работать эта кнопка
master.mainloop()

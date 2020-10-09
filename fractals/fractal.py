import tkinter
import math

def f1(coor, siz, ugo):#функция для х(ТРИГОНОМЕТРИЯ)
    x = coor+int(math.cos(ugo*math.pi/2)*siz)
    return x
def f2(coor, siz, ugo):#то же самое для у
    r = coor+int(math.sin(ugo*math.pi/2)*siz)
    return r
class Line: #класс линия, передаём ей координаты начала, размер и угол(потом объясню что это)
    def __init__(self, coord1, coord2, size, ugol):
        self.firstcoord = (coord1, coord2)#тут всё понятно
        self.ugol = ugol#тут всё понятно
        self.size = size#тут всё понятно
        self.lastcoord = (f1(coord1, size, ugol), f2(coord2, size, ugol))#это последние координаты линии, которые строятся через функции для х и y
        self.thisline = canvas.create_line((coord1, coord2), self.lastcoord)#тут всё понятно
#теперь поясняю, что такое угол. В моей ситстеме это 90 градусов. +1 это + 90 градусов, -1 это -90 градусов, -2 это -180 градусов и тд 
def iteration(line):#фракталы - это самоподобные структуры. Эта функция превращает объект во всю конструкцию в целом
    canvas.delete(line.thisline)#тут я удаляю линию
    l1 = Line(*line.firstcoord, line.size/3, line.ugol+1) #далее идут несколько линий, если посмотреть на картинку то можно понять, как изменяються углы
    l2 = Line(*l1.lastcoord, line.size/3, line.ugol)
    l3 = Line(*l2.lastcoord, line.size/3, line.ugol-1)
    l4 = Line(*l3.lastcoord, line.size/3, line.ugol)
    l5 = Line(*l4.lastcoord, line.size/3, line.ugol+1)
    l6 = Line(*l5.lastcoord, line.size/3, line.ugol)
    l7 = Line(*l6.lastcoord, line.size/3, line.ugol-1)
    return [l1, l2, l3, l4, l5, l6, l7] #возвращает список линий
def antiiteration(listlines):
    newline = Line(*listlines[0].firstcoord, listlines[0].size*4, listlines[0].ugol)
    for i in listlines:
        canvas.delete(i.thisline)
    return newline
master = tkinter.Tk()#тут всё понятно
canvas = tkinter.Canvas(master, height = 900, width = 1200, bg = 'white')#тут всё понятно
l = Line(150, 450, 729, 0)#создаём объект
numberiter = 0
listline = []
def nextiterat():#функция для кнопки
    global numberiter
    global listline
    if numberiter == 0:
        listline = iteration(l)
    elif numberiter == 1:
        newlistline = []
        for i in listline:
            newlistline.append(iteration(i))
        listline = newlistline
    else:
        newlistline = []
        for i in listline:
            for j in i:
                newlistline.append(iteration(j))
        listline = newlistline
    numberiter += 1
def previousiterat():
    global numberiter
    global listline
    if numberiter>0:
        numberiter-=1
        for i in range(len(listline)):
            listline[i] = antiiteration(listline[i])
previousiter = tkinter.Button(master, text = 'Previous Iteration', command = previousiterat)
nextiter = tkinter.Button(master, text = 'Next Iteration', command = nextiterat)
canvas.pack()
nextiter.pack()
#previousiter.pack() я до конца не разобрался, как должна работать эта кнопка
master.mainloop()

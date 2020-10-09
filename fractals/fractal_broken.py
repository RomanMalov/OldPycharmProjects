import tkinter
import math
class Line: 
    def __init__(self, coord1, coord2, size, ugol):
        self.firstcoord = (coord1, coord2)#С‚СѓС‚ РІСЃС‘ РїРѕРЅСЏС‚РЅРѕ
        self.ugol = ugol#С‚СѓС‚ РІСЃС‘ РїРѕРЅСЏС‚РЅРѕ
        self.size = size#С‚СѓС‚ РІСЃС‘ РїРѕРЅСЏС‚РЅРѕ
        self.lastcoord = (f1(coord1, size, ugol), f2(coord2, size, ugol))#СЌС‚Рѕ РїРѕСЃР»РµРґРЅРёРµ РєРѕРѕСЂРґРёРЅР°С‚С‹ Р»РёРЅРёРё, РєРѕС‚РѕСЂС‹Рµ СЃС‚СЂРѕСЏС‚СЃСЏ С‡РµСЂРµР· С„СѓРЅРєС†РёРё РґР»СЏ С… Рё y
        self.thisline = canvas.create_line((coord1, coord2), self.lastcoord)#С
    def reborn(self):
        canvas.create_line(self.firstcoord, self.lastcoord)
r = 2*1.414
def f1(coor,  siz, ugo):#С„СѓРЅРєС†РёСЏ РґР»СЏ С…(РўР Р�Р“РћРќРћРњР•РўР Р�РЇ)
    x = coor+int(math.cos(ugo*math.pi/2)*siz)
    return x
def f2(coor, siz, ugo):#С‚Рѕ Р¶Рµ СЃР°РјРѕРµ РґР»СЏ Сѓ
    y = coor+int(math.sin(ugo*math.pi/2)*siz)
    return y
base_fractal=[]
nowcoords=(100, 100)
created=False
def set_line(event):
    global l
    global nowcoords
    global base_fractal
    if not created:
        canvas.delete(l.thisline)
        if event.x!=nowcoords[0]:
            angle = 2*math.atan((event.y-nowcoords[1])/(event.x-nowcoords[0]))/math.pi
        else:
            if event.y>nowcoords[1]:
                angle = 1
            else:
                angle = -1
        if angle >0.9:
            l = Line(*nowcoords, 300, 1)
        elif angle <0-.9:
            l = Line(*nowcoords, 300, -1)
        elif -0.1<angle<0.1:
            l = Line(*nowcoords, 300, 0)
        else:
            l = Line(*nowcoords, 300, angle)
def save_line(event):
    global base_fractal
    global nowcoords
    
    nowcoords = l.lastcoord
    base_fractal.append(l)
    l.reborn()
def iteration(line):
    koeff = 300/math.sqrt((base_fractal[-1].lastcoord[0]-base_fractal[0].firstcoord[0])**2+(base_fractal[-1].lastcoord[1]-base_fractal[0].firstcoord[1])**2)
    canvas.create_line(base_fractal[-1].lastcoord, base_fractal[0].firstcoord, fill = 'red')
    print(koeff)
    canvas.delete(line.thisline)#С‚СѓС‚ СЏ СѓРґР°Р»СЏСЋ Р»РёРЅРёСЋ
    l1 = Line(*line.firstcoord, line.size*koeff, line.ugol+base_fractal[0].ugol)
    list_with_lines = [l1]
    for i in base_fractal[1:]:
        l2 = Line(*list_with_lines[-1].lastcoord, line.size*koeff,  i.ugol+line.ugol)
        list_with_lines.append(l2)
        
        
    return list_with_lines #РІРѕР·РІСЂР°С‰Р°РµС‚ СЃРїРёСЃРѕРє Р»РёРЅРёР№
def antiiteration(listlines):
    newline = Line(*listlines[0].firstcoord, listlines[0].size*4, listlines[0].ugol)
    for i in listlines:
        canvas.delete(i.thisline)
    return newline

def nextiterat():#С„СѓРЅРєС†РёСЏ РґР»СЏ РєРЅРѕРїРєРё СЃ Р·Р°РїРѕР»РЅРµРЅРёРµРј СЃРїРёСЃРєР°
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
master = tkinter.Tk()#С‚СѓС‚ РІСЃС‘ РїРѕРЅСЏС‚РЅРѕ
canvas = tkinter.Canvas(master, height = 800, width = 1000, bg = 'white')#С‚СѓС‚ РІСЃС‘ РїРѕРЅСЏС‚РЅРѕ
canvas.pack() 
numberiter = 0
l = Line(100, 100, 300, 0)
def main_f(event):
    global created
    global l
    l = base_fractal[0]
    created = True
    listline = []#СЃРїРёСЃРѕРє СЃРѕ РІСЃРµРјРё Р»РёРЅРёСЏРјРё
    previousiter = tkinter.Button(master, text = 'Previous Iteration', command = previousiterat)
    nextiter = tkinter.Button(master, text = 'Next Iteration', command = nextiterat)
    
    nextiter.pack()
#previousiter.pack() СЏ РґРѕ РєРѕРЅС†Р° РЅРµ СЂР°Р·РѕР±СЂР°Р»СЃСЏ, РєР°Рє РґРѕР»Р¶РЅР° СЂР°Р±РѕС‚Р°С‚СЊ СЌС‚Р° РєРЅРѕРїРєР°
master.bind('<Motion>', set_line)
master.bind('<Button-1>', save_line)
master.bind('<Button-3>', main_f)
master.mainloop()

from random import*
from tkinter import*
master = Tk()
canvas  = Canvas(master, width = 1000, heigh = 600, bg = 'white')
x=0
y=0
for i in range(600):
    for j in range(10):
        a = str('0'+str(hex(randint(0,255)))[2:])[-2:]
        for i in range(100):
            cvet = '#' + a+('000'+str(hex(randint(0, 16**4)))[2:])[-4:]
            canvas.create_rectangle((x,y),(x+1,y+1), outline = cvet, fill = cvet)
            x+=1
    x=0
    y+=1
canvas.pack()
master.mainloop()
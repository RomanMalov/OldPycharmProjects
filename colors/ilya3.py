from random import*
from tkinter import*
master = Tk()
canvas  = Canvas(master, width = 100, heigh = 100, bg = 'white')
x=0
y = 0
for i in range(100):
    for j in range(100):
        u=randint(1048576, 16777215)
        cvet = '#'+str(hex(u)[2:])
        de = canvas.create_rectangle((x,y),(x+1,y+1), outline = cvet, fill = cvet)
        x+=1
    x=0
    y+=1
canvas.pack()
master.mainloop()
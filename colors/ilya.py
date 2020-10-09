from tkinter import*
from random import*

x=[]
for i in range(600):
    x.append(i)
root = Tk()

canvas = Canvas(root, bg = 'white', height = 600, width = 600)


def headler(event):

    #while True:    #for i in range(1000):
    p1=x.pop()#choice(x)
    p2=x.pop()#choice(x)
    u=randint(1048576, 16777215)

    oval = canvas.create_oval((p1, p2), (p1+10, p2+10), fill='#'+str(hex(u)[2:]))
    for k in range(-600, 1200, 10):
        yu=randint(1048576, 16777215)
        oval = canvas.create_oval((p1, p2+k), (p1+10, p2+10+k), fill='#'+str(hex(yu)[2:]))
    return oval

canvas.grid()


#headler()
root.bind("<Motion>", headler)
root.bind("<KeyPress>", headler)
root.mainloop()


from tkinter import *
import random
x=[]
for i in range(600):
    x.append(i)

root = Tk()

canvas = Canvas(root, bg = 'white', height = 600, width = 600)

canvas.pack()
def headler(event):

    p1=random.choice(x)
    p2=random.choice(x)
    u=random.randint(1048576, 16777215)

    oval = canvas.create_oval((p1, p2), (p1+10, p2+10), fill='#'+str(hex(u)[2:]))
    oval2=canvas.create_oval((p1+10, p2), (p1+20, p2+10), fill='#'+str(hex(u)[2:]))
    oval3=canvas.create_oval((p1+5, p2-20), (p1+15, p2+2), fill='#'+str(hex(u)[2:]))
    return oval



root.bind("<Motion>", headler)
root.bind("<KeyPress>", headler)

root.mainloop()


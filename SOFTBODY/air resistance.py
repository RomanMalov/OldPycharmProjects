from tkinter import *
from math import *
import random
stiffness = 10
l0 = 100
gr=[]
dt=0.01
g=0
l1=105
resistance=0.0
class particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.randint(-100, 100)
        self.vy = random.randint(-100, 100)
        self.ax = 0
        self.ay = 0
        self.m = 1
        self.obj = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='yellow')
        #self.vectorv = canvas.create_line(x, y, x + self.vx, y + self.vy, fill='blue')
        #self.vectora = canvas.create_line(x, y, x + self.ax, y + self.ay, fill='red')
        self.potential_energy = 0
        self.kinetic_energy = 0
        self.time_graphic = []
        self.time_graphic1 = []
        self.time_graphic2 = []

    def __add__(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def reinit(self):
        canvas.coords(self.obj, self.x - 5, self.y - 5, self.x + 5, self.y + 5)
        #canvas.coords(self.vectorv, self.x, self.y, self.x + self.vx, self.y + 1 * self.vy)
        #canvas.coords(self.vectora, self.x, self.y, self.x + 10000 * self.ax, self.y + 10000 * self.ay)

    def acceleration(self):
        self.ax = 0
        self.ay = 0
        for i in particles:
            l = self + i
            xs = -(self.x - i.x)
            ys = -(self.y - i.y)
            if l != 0:
                angle = (asin(ys / l) if xs > 0 else (pi - asin(ys / l)))
                # acceleration = 1000*(-(l/10 + 0.99)**(-7)+(l/10+0.99)**(-13))
                if l<l1:
                    force = (l-l0)*stiffness
                else:
                    force = stiffness*l1**2*(l1-l0)/l**2
                acceleration = force/self.m
                self.ax += acceleration * cos(angle)
                self.ay += acceleration * sin(angle)
            self.ay+=g
            self.ay-=resistance*self.vy
            self.ax-=resistance*self.vx

        return self.ax, self.ay
    def energy(self):
        self.potential_energy=0
        for i in particles:
            l = self + i
            if l!=0:
                self.potential_energy+=stiffness*((l-l0)**2)/2
        self.kinetic_energy=self.m*(self.vx**2+self.vy**2)/2
        self.time_graphic.append(self.potential_energy)
        self.time_graphic1.append(self.kinetic_energy)
        self.time_graphic2.append(self.potential_energy/2+self.kinetic_energy)

        return self.kinetic_energy


def game():
    newvelosity = []
    newcoords = []
    full_energy = 0
    for i in particles:
        vx = i.vx + i.acceleration()[0]*dt
        vy = i.vy + i.acceleration()[1]*dt
        x = i.x + i.vx * dt
        y = i.y + i.vy * dt
        if i.x < 5:
            if i.vx < 0:
                vx = -i.vx
        if i.y < 5:
            if i.vy < 0:
                vy = -i.vy
        if i.x >= w-105:
            if vx > 0:
                vx = -i.vx
        if i.y > h-105:
            if i.vy > 0:
                vy = -0.5*i.vy
                y-=(i.y-(h-105))
        newcoords.append([x, y])
        newvelosity.append([vx, vy])
        full_energy += i.energy()
        label.config(text = str(full_energy))
    gr.append(full_energy)
    center_x = 0
    center_y = 0
    for i in range(len(particles)):
        p = particles[i]
        p.x = newcoords[i][0]
        p.y = newcoords[i][1]
        p.vx = newvelosity[i][0]
        p.vy = newvelosity[i][1]


def next():
    game()
    for i in particles:
        i.reinit()
    master.after(10, next)


w = 500
w1 = 300
h = 500
h1 = 300
particles = []
master = Tk()
canvas = Canvas(master, height=w, width=h, bg='white')
canvas.create_rectangle(0,0,w-100,h-100)
center = canvas.create_oval(0,0,0,0, fill = 'blue')
def meme(event):
    particles.append(particle(event.x, event.y))
def meme1(event):
    global stiffness , resistance, l0
    if event.char=='a':
        stiffness*=1.01
    if event.char=='z':
        stiffness*=0.99
    if event.char=='s':
        resistance*=1.01
    if event.char=='x':
        resistance*=0.99
    if event.char=='d':
        l0*=1.01
    if event.char=='c':
        l0*=0.99
    if event.char=='p':
        print(stiffness,g,l0)

next()
particles.append(particle(100,100))
particles.append(particle(100, 201))
label  = Label(master, text='0')
master.bind('<Button-1>', meme)
label.pack()
canvas.pack()
master.bind('<KeyPress>', meme1)

master.mainloop()
print(particles[1].time_graphic)
print(particles[1].time_graphic1)
print(particles[1].time_graphic2)
print(gr)
if len(gr)>=2:

    graphic1 = gr
else:
    graphic1=[1, 1]
if len(particles)>=2:
    graphic = particles[1].time_graphic
else:
    graphic = [1, 1]
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# Создание экземпляра Axes c помощью Figure-метода add_subplot()
ax = fig.add_subplot(111)
# или так
box = [0.25, 0.5, 0.25, 0.25]
# Создание экземпляра Axes c помощью Figure-метода add_axes()
l = []
x = np.arange(0.0, 1.0, 0.1)
y = graphic
z = graphic1

# Методы plot() вызываются через экземпляры ax, а не plt (интерфейс pyplot)
ax.plot(y)
ax.plot(z)

for ax in fig.axes:
    ax.grid(True)


plt.show()
from tkinter import*
import random
from math import*

master1 = Tk()
canvas = Canvas(master1, height=800, width=800, bg='white')
string = []
def game(event):
    global string
    x = event.x
    y = event.y
    if not (x,y) in string:
        string.append([x,y])
    if len(string)>1:
        canvas.create_line(string[-2][0], string[-2][1], x, y)

master1.bind('<Button-1>', game)
canvas.pack()
master1.mainloop()





master = Tk()
canvas = Canvas(master, height=800, width=800, bg='white')
s=1000
rx=200
ry=200
r=100
koeff=5
z=0.5
word = string
def dist(a,b, g):
    u = []
    '''if g%2==0:
        word = word1
    elif g%77==0:
        word = word3
    else:
        word = word2'''
    m=400
    n=0
    for i in range(len(word)):
        x1=a-word[i][0]
        y1=b-word[i][1]
        p=(x1**2+y1**2)**(0.5)
        if p<m:
            m=p
            n=i
    x2 = word[(n+1) % len(word)][0]
    y2 = word[(n + 1) % len(word)][1]
    f=((a-x2)**2+(b-y2)**2)**0.5
    return a-x2, b-y2, f if f!=0 else 1

list_boids=[]
for i in range(s):
    list_boids.append([random.randint(1,800), random.randint(1,800)])
list_direct=[]
for j in range(s):
    x=list_boids[(j+2)%s][0]-list_boids[j][0]
    y=list_boids[(j+2)%s][1]-list_boids[j][1]
    l = (x**2+y**2)**(0.5)
    list_direct.append(asin(y / l) if x > 0 else (pi - asin(y / l)))
ovals=[]

for i in range(s):
    t=canvas.create_line(int(list_boids[i][0]),int(list_boids[i][1]),
                         int(list_boids[i][0]+5*cos(list_direct[i])),
                         int(list_boids[i][1]+5*sin(list_direct[i])))

    ovals.append(t)
def game(event):
    global list_direct
    global list_boids
    global r
    if event.char == 'a':
        r+=1
    if event.char == 'o':
        r-=1
    for i in range(s):
        list_boids[i][0] = (list_boids[i][0] + 5 * cos(list_direct[i]))%800
        list_boids[i][1] = (list_boids[i][1] + 5 * sin(list_direct[i]))%800
    for j in range(s):
        x1, y1, d = dist(*list_boids[j], j)

        x = z*(list_boids[(j + 2) % s][0] - list_boids[j][0])-koeff*x1/d
        y = z*(list_boids[(j + 2) % s][1] - list_boids[j][1])-koeff*y1/d
        l = (x ** 2 + y ** 2) ** (0.5)
        list_direct[j]=(asin(y / l) if x > 0 else (pi - asin(y / l)))
    for i in range(s):
        canvas.coords(ovals[i],int(list_boids[i][0]), int(list_boids[i][1]),
                               int(list_boids[i][0] + 5 * cos(list_direct[i])),
                               int(list_boids[i][1] + 5 * sin(list_direct[i])))


master.bind('<KeyPress>', game)
canvas.pack()
master.mainloop()


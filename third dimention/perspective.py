from tkinter import *
from math import *
from angem import Matrix1, Vector
camera_width = 600
camera_height = 600
focal_length = 100
s_graphic = []





def get_coordinate(cam, n, point):
    if (point - cam) % n > 0:
        proect = (point - cam) * ((n % n) / ((point - cam) % n))
        i = Vector(1, 0, 0)
        j = Vector(0, 1, 0)
        k = Vector(0, 0, 1)


        f = (n*(1/focal_length))
        l = k ** f
        if (abs(l) >= -0.001 and abs(l) <= 0.001) :
            l = (Vector(sin(alpha), cos(alpha), 0))
        else:
            l = l * (1/abs(l))
        p = l ** (n * (1 / focal_length))
        s = Matrix1(p, l, n * (1 / focal_length))

        s_graphic.append(abs(l))
        new_project = s.trans().inverse().mat_vec(proect)
        return [new_project[0], new_project[1]]
    else:
        return 'error'


points = []
for t in range(200):

            #for z in range(5):
            #points.append(Vector(x, y, z)*80-Vector(150, 150, 150))
        z = 0
        x = t//10
        y = t%10
        points.append(Vector(x, y, z)*30-Vector(100, 100, 100))
i1 = [0, 100, 0, 0, 100, 100, 0, 100]
j1 = [0, 0, 100, 0, 100, 0, 100, 100]
k1 = [0, 0, 0, 100, 0, 100, 100, 100]
for a in range(8):
    pass
    #points.append(Vector(i1[a], j1[a], k1[a])*3+Vector(-150, -150, -150))
master = Tk()
canvas = Canvas(master, height=camera_height, width=camera_width)
alpha = 0
betta = pi / 2
camera = Vector(0, 0, -1000)
direction = Vector(0, 0, 0)
point_draw = []
for point in points:
    point_draw.append(canvas.create_oval(1, 1, 1, 1, fill='blue'))

time = 0
def game(event):
    global alpha
    global betta
    global time
    global direction
    time += 1
    alpha = event.x / 100
    betta = 1 * event.y / 100 + pi / 2
    direction = Vector(focal_length * cos(alpha) * cos(betta),
                       focal_length * sin(alpha) * cos(betta),
                       focal_length * sin(betta))
    for i, point in enumerate(points):
        coords = get_coordinate(camera, direction, point)
        if coords != 'error':
            canvas.coords(point_draw[i], coords[0] + camera_width / 2, coords[1] + camera_height / 2,
                          coords[0] + 5 + camera_width / 2, coords[1] + 5 + camera_height / 2)
            canvas.itemconfig(point_draw[i], fill = 'blue', outline = 'black')

        else:
            canvas.itemconfig(point_draw[i], fill = 'white', outline = 'white')
def meme(event):
    global camera
    game(event)
    camera+=direction*0.5


canvas.pack()
master.bind('<Motion>', game)
master.bind('<KeyPress>', meme)

master.mainloop()

'''import numpy as np
import matplotlib.pyplot as plt

x = list(range(len(s_graphic)))
plt.plot(x, s_graphic)
plt.show()
'''
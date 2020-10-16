from tkinter import *
from math import *
from angem import Matrix1, Vector
camera_width = 600
camera_height = 600
focal_length = 70
s_graphic = []





def get_coordinate(cam, n, point):
    if (point - cam) % n > 0:
        proect = (point - cam) * ((n % n) / ((point - cam) % n))
        i = Vector(1, 0, 0)
        j = Vector(0, 1, 0)
        k = Vector(0, 0, 1)
        if (i % n >= -0.001 and i % n <= 0.001) or (j % n >= -0.001 and j % n <= 0.001):
            l = (Vector(sin(alpha), cos(alpha), 0))
        else:
            l = k ** (n*(1/focal_length))

        p = l ** (n * (1 / focal_length))
        print(abs(l), abs(n)/focal_length, int((n % l)*100000)/100000)
        s = Matrix1(p*(1/abs(p)), l*(1/abs(l)), n * (1 / focal_length))

        s_graphic.append(abs(l))
        new_project = s.trans().inverse().mat_vec(proect)
        return [new_project[0], new_project[1]]
    else:
        return 'error'


points = []
for x in range(5):
    for y in range(5):
        for z in range(5):
            points.append(Vector(x, y, z)*80-Vector(150, 150, 150))
i1 = [0, 100, 0, 0, 100, 100, 0, 100]
j1 = [0, 0, 100, 0, 100, 0, 100, 100]
k1 = [0, 0, 0, 100, 0, 100, 100, 100]
for a in range(8):
    points.append(Vector(i1[a], j1[a], k1[a])*3+Vector(-150, -150, -150))
master = Tk()
canvas = Canvas(master, height=camera_height, width=camera_width)
alpha = 0
betta = pi / 2
camera = Vector(0, 0, -1000)
direction = Vector(focal_length * cos(alpha) * cos(betta),
                   focal_length * sin(alpha) * cos(betta),
                   focal_length * sin(betta))
point_draw = []
for point in points:
    point_draw.append(canvas.create_oval(1, 1, 1, 1, fill='blue'))


def game(event):
    global alpha
    global betta
    alpha = event.x / 100
    betta = 1 * event.y / 100 + pi / 2
    direction = Vector(focal_length * cos(alpha) * cos(betta),
                       focal_length * sin(alpha) * cos(betta),
                       focal_length * sin(betta))
    camera = direction*(-5)
    for i, point in enumerate(points):
        coords = get_coordinate(camera, direction, point)
        if coords != 'error':
            canvas.coords(point_draw[i], coords[0] + camera_width / 2, coords[1] + camera_height / 2,
                          coords[0] + 5 + camera_width / 2, coords[1] + 5 + camera_height / 2)


canvas.pack()
master.bind('<Motion>', game)
master.mainloop()

import numpy as np
import matplotlib.pyplot as plt

x = list(range(len(s_graphic)))
plt.plot(x, s_graphic)
plt.show()

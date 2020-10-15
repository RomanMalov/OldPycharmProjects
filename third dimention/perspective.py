from tkinter import *
from math import *

camera_width = 600
camera_height = 600
focal_length = 10


class Matrix:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def trans(self):
        X1 = Vector(self.X[0], self.Y[0], self.Z[0])
        Y1 = Vector(self.X[1], self.Y[1], self.Z[1])
        Z1 = Vector(self.X[2], self.Y[2], self.Z[2])
        return Matrix(X1, Y1, Z1)

    def __str__(self):
        return '(' + str(self.X) + '\n' + str(self.Y) + '\n' + str(self.Z) + ')'

    def __abs__(self):
        det = self.X[0] * (self.Y[1] * self.Z[2] - self.Y[2] * self.Z[1]) - \
              self.X[1] * (self.Y[0] * self.Z[2] - self.Y[2] * self.Z[0]) + \
              self.X[2] * (self.Y[0] * self.Z[1] - self.Y[1] * self.Z[0])
        return det

    def __mul__(self, other):
        X1 = self.X
        Y1 = self.Y
        Z1 = self.Z
        o = other.trans()
        X2 = o.X
        Y2 = o.Y
        Z2 = o.Z
        a = Vector(X1 % X2, X1 % Y2, X1 % Z2)
        b = Vector(Y1 % X2, Y1 % Y2, Y1 % Z2)
        c = Vector(Z1 % X2, Z1 % Y2, Z1 % Z2)
        return Matrix(a, b, c)

    def mat_vec(self, other):
        return Vector(self.X % other, self.Y % other, self.Z % other)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z

    def __pow__(self, other):
        x0, y0, z0 = self.x, self.y, self.z
        x1, y1, z1 = other.x, other.y, other.z
        return Vector(y0 * z1 - z0 * y1, z0 * x1 - x0 * z1, x0 * y1 - y0 * x1)

    def __str__(self):
        return str([self.x, self.y, self.z])

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mod__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return sqrt(self % self)

    def __floordiv__(self, other):
        if abs(self) * abs(other) != 0:
            return acos((self * other) / (abs(self) * abs(other)))
        else:
            return 0

    def __mul__(self, other):
        if type(self) == type(Vector(0, 0, 0)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return Vector(other.x * self, other.y * self, self * other.z)


def get_coordinate(cam, n, p):
    if (p - cam) % n > 0:
        proect = (p - cam) * ((n % n) / ((p - cam) % n))
        i = Vector(1, 0, 0)
        j = Vector(0, 1, 0)
        if i % n == 0 or j % n == 0:
            l = (Vector(sin(alpha), cos(alpha), 0))
        else:
            a = sqrt((i % n) ** 2 / ((i % n) ** 2 + (j % n) ** 2))
            b = sqrt((i % n) ** 2 / ((i % n) ** 2 + (j % n) ** 2))
            l = Vector(a, b, 0)
        p = (n ** l)*(1/focal_length)
        s = Matrix(l, p, n)
        new_project = s.mat_vec(proect)
        return [new_project[0], new_project[1]]
    else:
        return 'error'


points = []
for x in range(10):
    for y in range(10):
        z = 10 * sin(0.5 * x) * sin(0.5 * y)
        points.append(Vector(30 * x, 30 * y, 5 * z))
i1 = [0, 100, 0, 0, 100, 100, 0, 100]
j1 = [0, 0, 100, 0, 100, 0, 100, 100]
k1 = [0, 0, 0, 100, 0, 100, 100, 100]
for a in range(8):
    points.append(Vector(i1[a], j1[a], k1[a]))
master = Tk()
canvas = Canvas(master, height=camera_height, width=camera_width)
alpha = 0
betta = pi / 2
camera = Vector(500, 500, 100)
direction = Vector(focal_length * cos(alpha) * cos(betta),
                   focal_length * sin(alpha) * cos(betta),
                   focal_length * sin(betta))
point_draw = []
for point in points:
    point_draw.append(canvas.create_oval(1, 1, 1, 1, fill='blue'))


def game(event):
    alpha = 1 * event.x / 100
    betta = 1 * event.y / 100 + pi / 2
    direction = Vector(focal_length * cos(alpha) * cos(betta),
                       focal_length * sin(alpha) * cos(betta),
                       focal_length * sin(betta))
    for i, point in enumerate(points):
        coords = get_coordinate(camera, direction, point)
        if coords != 'error':
            canvas.coords(point_draw[i], coords[0] + camera_width / 2, coords[1] + camera_height / 2,
                          coords[0] + 5 + camera_width / 2, coords[1] + 5 + camera_height / 2)

    print(sin(alpha), sin(betta))
canvas.pack()
master.bind('<Motion>', game)
master.mainloop()

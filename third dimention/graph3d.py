import tkinter
import math

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=600, bg='white')
objects = []


class point2d:
    def __init__(self, x, y, name, color='black', r=2):
        self.x = x
        self.y = y
        self.r = r
        self.name = canvas.create_text(self.x + self.r + 4, self.y + self.r + 4, text=name)
        self.color = color
        self.body = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill=self.color)

    def destroy(self):
        canvas.delete(self.body)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        canvas.move(self.body, dx, dy)
        canvas.move(self.name, dx, dy)

    def rotate(self, centre, angel_xy):
        r_xy = math.sqrt((self.y - centre.y) ** 2 + (self.x - centre.x) ** 2)
        if r_xy != 0:
            cos_xy = (self.x - centre.x) / r_xy
            sin_xy = (self.y - centre.y) / r_xy
            dy = (sin_xy * math.cos(angel_xy) - cos_xy * math.sin(angel_xy) - sin_xy) * r_xy
            dx = (cos_xy * math.cos(angel_xy) + sin_xy * math.sin(angel_xy) - cos_xy) * r_xy
        else:
            dy = 0
            dx = 0
        self.move(dx, dy)


class point3d:
    def __init__(self, x, y, z, name, mass=0, color='black'):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.mass = mass
        self.color = color
        self.body2d = point2d(self.x, self.y, self.name, self.color)
        objects.append(self)

    def destroy(self):
        self.body2d.destroy()

    def __str__(self, x, y, z):
        print([self.x, self.y, self.z])

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
        self.body2d.move(dx, dy)

    def rotate(self, centre, angel_xy, angel_yz):
        # plot yz
        r_yz = math.sqrt((self.y - centre.y) ** 2 + (self.z - centre.z) ** 2)
        if r_yz != 0:
            cos_yz = (self.z - centre.z) / r_yz
            sin_yz = (self.y - centre.y) / r_yz
            dy = (sin_yz * math.cos(angel_yz) - cos_yz * math.sin(angel_yz) - sin_yz) * r_yz
            dz = (cos_yz * math.cos(angel_yz) + sin_yz * math.sin(angel_yz) - cos_yz) * r_yz
        else:
            dy = 0
            dz = 0
        # plot xy
        r_xy = math.sqrt((self.y - centre.y) ** 2 + (self.x - centre.x) ** 2)
        if r_xy != 0:
            cos_xy = (self.x - centre.x) / r_xy
            sin_xy = (self.y - centre.y) / r_xy
            dy += (sin_xy * math.cos(angel_xy) - cos_xy * math.sin(angel_xy) - sin_xy) * r_xy
            dx = (cos_xy * math.cos(angel_xy) + sin_xy * math.sin(angel_xy) - cos_xy) * r_xy
        else:
            dy += 0
            dx = 0
        self.move(dx, dy, dz)


class line2d:
    def __init__(self, start: point2d, end: point2d):
        self.start = start
        self.end = end
        self.body = canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y)

    def destroy(self):
        canvas.delete(self.body)

    def move(self, dx, dy):
        canvas.move(self.body, dx, dy)

    def rotate(self, centre, angel_xy):
        self.start.rotate(centre, angel_xy)
        self.end.rotate(centre, angel_xy)
        canvas.delete(self.body)
        self.body = canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y)


class line3d:
    def __init__(self, start: point3d, end: point3d):
        self.start = start
        self.end = end
        self.body2d = line2d(start.body2d, end.body2d)
        objects.append(self)

    def destroy(self):
        self.body2d.destroy()

    def move(self, dx, dy, dz):
        self.start.move(dx, dy, dz)
        self.end.move(dx, dy, dz)
        self.body2d.move(dx, dy)

    def rotate(self, centre, angel_xy, angel_yz):
        self.start.rotate(centre, angel_xy, angel_yz)
        self.end.rotate(centre, angel_xy, angel_yz)
        self.body2d.rotate(centre, angel_xy)


a = point3d(100, 100, 100, 'A')
b = point3d(200, 200, 200, 'B')
ln = line3d(a, b)


def iter():
    # b.move(1,1,1)
    # a.rotate(b,0.005,0.005)
    ln.rotate(b, 0.005, 0.005)
    root.after(10, iter)


iter()

canvas.pack()
root.mainloop()
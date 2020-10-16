import numpy as np
from numpy import linalg as LA
from math import *



class Matrix1:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def trans(self):
        X1 = Vector(self.X[0], self.Y[0], self.Z[0])
        Y1 = Vector(self.X[1], self.Y[1], self.Z[1])
        Z1 = Vector(self.X[2], self.Y[2], self.Z[2])
        return Matrix1(X1, Y1, Z1)

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
        return Matrix1(a, b, c)

    def mat_vec(self, other):
        return Vector(self.X % other, self.Y % other, self.Z % other)

    def inverse(self):
        m = np.array([[self.X[0], self.X[1], self.X[2]],
                     [self.Y[0], self.Y[1], self.Y[2]],
                     [self.Z[0], self.Z[1], self.Z[2]]])
        m1 = LA.inv(m)
        v1 = Vector(m1[0][0], m1[0][1], m1[0][2])
        v2 = Vector(m1[1][0], m1[1][1], m1[1][2])
        v3 = Vector(m1[2][0], m1[2][1], m1[2][2])
        return Matrix1(v1, v2, v3)


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
            return Vector(other.x * self, other.y * self, self.z * other.z)
if __name__=='__main__':
    a = Vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)
    b = Vector(-sqrt(3)/3, -sqrt(3)/3, sqrt(3)/3)
    print(a ** b, abs(a ** b), a % b)
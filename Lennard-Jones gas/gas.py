import numpy as np
import random

sigma = 1
epsilon = 1
dt = 0.001
all_coords = []
all_speeds = []
TIME  = 10000
L = 10
class System:
    def __init__(self, coords, speeds, L):
        self.L = L
        self.speeds = speeds
        self.coords = coords
        self.n = len(coords)
        self.accelerations = np.zeros((self.n, 3))
        self.shift = np.array([L / 2, L / 2, L / 2])
        self.energy1 = []
        self.energy2 = []
        self.energy = []
    def acceleration(self):
        accelerations = np.zeros((self.n, self.n, 3))
        E1 = 0
        E2 = 0
        for i in range(self.n):

            E1 +=  (np.dot(self.speeds[i], self.speeds[i]))/2
            for j in range(i + 1, self.n):
                a = self.coords[i]
                b = self.coords[j]
                D = (a - b + self.shift) % self.L - self.shift
                l = np.linalg.norm(D)
                if l != 0:
                    E2 +=  4 * epsilon * ((sigma / l) ** 12 - (sigma / l) ** 6)
                    F0 = 4 * epsilon * (-12 * (sigma / l) ** 14 + 6 * (sigma / l) ** 8)
                    accelerations[i][j] = -F0 * D
                    accelerations[j][i] = F0 * D

        self.accelerations = np.sum(accelerations, axis=1)
        self.energy1.append(E1)
        self.energy2.append(E2)
        self.energy.append(E1+E2)



'''class Particle:
    def __init__(self, x, y, z, vx, vy, vz):
        self.m = 1
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = 0
        self.ay = 0
        self.az = 0

    def __add__(self, other):
        x = (self.x - other.x - 5) % 10
        y = (self.y - other.y - 5) % 10

        z = (self.z - other.z - 5) % 10

        return np.sqrt(x ** 2 + y ** 2 + z ** 2), x, y, z

    def acceleration(self):
        self.ax = 0
        self.ay = 0
        self.az = 0
        for i in particles:
            l, dx, dy, dz = self + i
            F0 = 4 * sigma * (-12 * (1 / l) ** 14 + 6 * (1 / l) ** 8)
            self.ax += F0 * dx
            self.ay += F0 * dy
            self.az += F0 * dz
        return self.ax, self.ay, self.az
'''


def iteration(k):
    system.speeds += system.accelerations * dt / 2
    system.coords += system.speeds * dt / 2
    system.acceleration()
    system.speeds += system.accelerations * dt / 2
    '''for i in particles:
        a = (i.ax, i.ay, i.az)
        vx = i.vx + a[0] / 2 * dt
        vy = i.vy + a[1] / 2 * dt
        vz = i.vz + a[2] / 2 * dt
        newvelosity.append((vx, vy, vz))
        i.x = i.x + vx * dt
        i.y = i.y + vy * dt
        i.z = i.z + vz * dt
        coords.append([i.x % 10, i.y % 10, i.z % 10])
    for k, i in enumerate(particles):
        a = i.acceleration()
        vx, vy, vz = newvelosity[k]
        i.vx = vx + a[0] / 2 * dt
        i.vy = vy + a[1] / 2 * dt
        i.vz = vz + a[2] / 2 * dt
    all_coords.append(
        coords + [[0, 0, 0], [0, 0, 10], [0, 10, 0], [10, 0, 0], [10, 10, 0], [10, 0, 10], [0, 10, 10], [10, 10, 10]])'''
    list_coords = []
    list_speeds = []
    print(k)
    for i in system.coords:
        list_coords.append(list((i + np.array([5, 5, 5])) % 10 - np.array([5, 5, 5])))
    for j in system.speeds:
        list_speeds.append(list(j))
    all_coords.append(list_coords)
    all_speeds.append(list_speeds)

# + [[-5, -5, -5], [-5, -5, 5], [-5, 5, -5], [5, -5, -5], [-5, 5, 5], [5, -5, 5], [-5, 5, 5],
# [5, 5, 5]]
dots = [np.array([5.,5.,5.])]
speeds = [np.array([0,0,0])]
shift = np.array([L / 2, L / 2, L / 2])
def spawn(points):
    new_dot = np.array([random.random() * 10, random.random() * 10, random.random() * 10])
    flag = True
    print(new_dot, 'NEW')
    for i in points:
        print(i)
        D = (i - new_dot + shift) % L - shift
        flag*=(np.linalg.norm(i-new_dot)>1)
    if flag:
        return new_dot
    else:
        return spawn(points)
for l in range(100):
    dots.append(spawn(dots))
    speeds.append(np.array([random.random()-0.5 , random.random()-0.5, random.random()-0.5 ]))
system = System(np.array(dots), np.array(speeds), L)

'''system = System(np.array([[1., 0., 0.],
                          [2., 0., 0.]]),
                np.array([[1., 0., 0.],
                          [-1., 0., 0.]])
                , 10.)'''

for i in range(TIME):
    iteration(i)

'''import matplotlib.pyplot as plt
plt.plot(range(1000), system.energy)
plt.show()'''

with open('energy', 'w') as file_energy:
    for i in range(TIME):
        print(system.energy[i], file = file_energy)
    for j in range(TIME):
        print(system.energy1[j], file = file_energy)
    for k in range(TIME):
        print(system.energy2[k], file = file_energy)
with open('coordinates', 'w') as file_coords:
    for i in all_coords:
        for j in i:
            print(*j, sep = ';', end = ' ',file = file_coords)
        print('', file = file_coords)
with open('velocityes', 'w') as file_speeds:
    for i in all_speeds:
        for j in i:
            print(*j, sep = ';', end = ' ',file = file_speeds)
        print('', file = file_speeds)
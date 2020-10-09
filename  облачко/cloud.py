import random
import numpy as np
import matplotlib.pyplot as plt
pixels = np.ones((500,500))
def distance(coords1, coords2):
    return ((coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2)*(0.5)
dots=[]
n=25
for i in range(n):
    dots.append([random.randint(1,499),random.randint(1,499)])
for i in range(500):
    for j in range(500):
        dliny = []
        for k in range(n):
            dliny.append(distance(dots[k], [i,j]))
        x=sorted(dliny)
        pixels[i][j]=((0+x[0])/100)**(0.5)
plt.imshow(pixels, cmap='Greys')
plt.show()




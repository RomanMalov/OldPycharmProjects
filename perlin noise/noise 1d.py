import random

slopes = []
for i in range(8):
    slopes.append(random.random()*2-1)
values = []
galues = []
dalues = []
for i in range(700):
    x=i/100
    n = i//100
    a1 = slopes[n]
    a2 = slopes[n+1]
    y=(a1*(x-n)-(a1*(x-n)-a2*(x-(n+1)))*(x-n))**4
    y1= a1*(x-n)
    y2 = a2*(x-(n+1))
    dalues.append(y)
    values.append(y1)
    galues.append(y2)
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# Создание экземпляра Axes c помощью Figure-метода add_subplot()
ax = fig.add_subplot(111)
# или так
box = [0.25, 0.5, 0.25, 0.25]
# Создание экземпляра Axes c помощью Figure-метода add_axes()


ax.plot(dalues)

# Методы plot() вызываются через экземпляры ax, а не plt (интерфейс pyplot)


for ax in fig.axes:
    ax.grid(True)


plt.show()
import matplotlib.pyplot as plt
import numpy as np
all_speeds = []
time = 0
scale = 30
with open('/Users/rmnmlv/PycharmProjects/OldPycharmProjects/Lennard-Jones gas/velocityes', 'r') as file_coords:
    for line in file_coords:
        speeds = []
        x = line.split(' ')
        for i in x:
            dot = []
            for j in i.split(';'):
                if j!='\n':
                    dot.append(float(j))
            if dot != []:
                speeds.append(dot)
        all_speeds.append(speeds)
last_speeds = []
for j in range(5000, 9999):
    for i in all_speeds[j]:
        last_speeds.append(np.linalg.norm(np.array(i)))

max_speed = max(last_speeds)
min_speed = min(last_speeds)
histogram = []
gram = []
n = 20
step = (max_speed-min_speed)/n
print(min_speed, max_speed)

for i in range(n):
    count = 0
    for j in last_speeds:
        if j>(min_speed+step*(i-1)) and j<(min_speed+step*i):
            count+=1
    histogram.append(count)
    gram.append(min_speed+step*(i-0.5))
print(gram)
prob = np.array(histogram)
v = np.array(gram)
plt.plot(np.log(prob/(v**2)), v**2)
plt.show()
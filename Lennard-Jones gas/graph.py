import matplotlib.pyplot as plt
import numpy as np
energy0 = []


with open('/Users/rmnmlv/PycharmProjects/OldPycharmProjects/Lennard-Jones gas/energy', 'r') as file:
    for line in file:
        energy0.append(float(line))
energy = np.array(energy0[0:10000])
energy1 = np.array(energy0[10000:20000])
energy2 = np.array(energy0[20000:30000])

'''plt.plot(range(10000), energy, label = 'sum energy ')
plt.plot(range(10000), energy1, label = 'kinetik energy ')
plt.plot(range(10000), energy2, label = 'potential energy 2')'''
plt.plot(range(10000), energy1+2*energy2, label = 'kinetik+2*potential energy')

plt.legend()


plt.show()
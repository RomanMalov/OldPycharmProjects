from math import*
i = []
j = []
k = []
for x in range(100):
    for y in range(100):
        z = 10*sin(10*x)*sin(10*y)
        i.append(10*x)
        j.append(10*y)
        k.append(z)
print('i = '+str(i))
print('j = '+str(j))
print('k = '+str(k))


from math import*
for i in range(3001, 30000):

    if (sqrt(i-3000)==float(int(sqrt(i-3000)))) and (sqrt(i+3000)==float(int(sqrt(i+3000)))):
        print(i)

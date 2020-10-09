prime = []
for i in range(100000):
    p=0
    for j in range(i):
        if i%(j+1)==0:
            p+=1
    if p<=2:
        prime.append(i)

print(prime)
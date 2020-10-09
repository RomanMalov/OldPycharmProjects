prime = []
for t in range(100):
    i=t**2
    prime.append(str(i)+' '*(4-len(str(i))))

for k in range(len(prime)//10+1):

    print(' '.join(prime[k*10:(k*10+10)]))
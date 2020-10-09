x=[]
x.append(1)
for i in range(501):
    print(x[i], i+1)
    x.append(x[i]/((2*i+1)*x[i]+1))
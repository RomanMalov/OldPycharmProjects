solutions=[]
for x in range(95):
    for y in range(95):
        for z in range(95):
            if 3*x+12*y+16*z==95:
                solutions.append([x,y,z])
s=0
n=0
for i in solutions:
    x1 = i[0]
    y1=i[1]
    z1 = i[2]
    s1 = 30*x1+130*y1+170*z1
    if s1>s:
        s=s1
        n=i
print(n)

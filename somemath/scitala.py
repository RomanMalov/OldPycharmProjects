s =input().split()
d=input()
x = []
for i in range(len(s)):
    if len(s)%(i+1)==0:
         x.append(i+1)
print(len(x), *x)
for i in x:
    t=''
    for j in range(len(s)//i):
        st=''
        for k in range(i):
            st+=s[k*len(s)//i+j]
        t+=st+' '
    print(t)

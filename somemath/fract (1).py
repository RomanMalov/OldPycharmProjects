import numpy as np

arr = np.zeros(400).reshape(20, 20)
arr[0, 1] = 1
for i in range(len(arr)):
    if i!=0:
        for j in range(len(arr[1])):
            if j!=0:
                arr[i, j] =int(arr[i-1, j]+ arr[i-1, j-1])
print(sum(arr[16]))
c= 0
for i1 in range(3):
    for i2 in range(3):
        for i3 in range(3):
            for i4 in range(3):
                for i5 in range(3):
                    for i6 in range(3):
                        for i7 in range(3):
                            if 0 in [i1,i2,i3,i4,i5,i6,i7]:
                                if 1 in [i1,i2,i3,i4,i5,i6,i7]:
                                    c+=1
print(c)

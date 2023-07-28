


import math

for i in range(1,1000):
    a = i**2
    for j in range(1,2000):
        b = j**2
        c = math.sqrt(a+b)
        if((i+j+c) == 1000):
            print(f"{i} + {j} + {c} = {i+j+c}")
            print(int(i*j*c))
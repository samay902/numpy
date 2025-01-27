import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
a[:6:2]=100
print(a)
b=a[::-1]
print(b)
c=np.arange(1,11).reshape(2,5)

print(c)

for i in a:
    i+=i**(1/2)
    print(i)
bo=a[-1]
print(bo)


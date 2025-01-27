import numpy as np


def f(a,b):
    return a+b
a=np.fromfunction(f,(3,2),dtype=int)
b=a[2,1]
print(b)
print(a)
print(a[:3,1])
d=a[1,:]
print(d)
e=a[:]
print(e)
print(a[-1])



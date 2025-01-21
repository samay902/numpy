import numpy as np
a=np.full((2,3),4)
print(a)
b=np.asarray(a)
print(a+b)


e=np.array([1,2,3,4])

d=np.diag(e)
print(np.asarray(d))
c=(np.asarray(e))+(np.asarray(d))
print(c)
f=np.empty(4)
print(np.asarray(f))
g=np.random.rand(2,3)
print(g)
j=np.random.randint(2,4,size=(2,4))
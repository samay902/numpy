import numpy as np
a=np.full((2,3),4)
print(a)
b=np.asarray(a)
print(a+b)


e=np.array([1,2,3,4])

d=np.diag(e)
print(np.asarray(d))
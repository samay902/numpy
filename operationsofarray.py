import numpy as np 
a=np.array([[1,2,3],
           [ 2,3,1]])
b=np.array([[1,2,3],
           [2,3,4]])
print(b.ndim)
print(a.ndim)
c=a.dot(b)
print(c)
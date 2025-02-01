import numpy as np
a=np.arange(10)**3
b=np.array([1,2,3,4,2,3])
print(a[b])
#array can be indexed by another array
c=np.array([[1,2,3],
           [4,5,6]])
print(a[c])
#when the indexed are in a shape then the array takes the same shape

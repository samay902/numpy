import numpy as np
a=np.arange(2,16).reshape(7,2)
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.dtype)

b=np.zeros(8,dtype=complex).reshape(2,4)
print(b)

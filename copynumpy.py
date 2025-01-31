import numpy as np

a=np.array([1,2,3])
b=a.view()
print(b is a)
print(b.base is a )
print(a.flags.owndata)
b=a[:1].copy()
del a
print(b)

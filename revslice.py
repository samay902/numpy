import numpy as np
a=np.arange(1,19).reshape(2,3,3)
print(a)
d=a[1,1:3,2]
print(d)

b=np.arange(1,13).reshape(3,4)
print(b)
c=b[1:3,1:3]

print(c)

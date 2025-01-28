import numpy as np
rg = np.random.default_rng(1)
a=np.floor(3*(rg.random((3,4))))


print(a)
rg=np.random.default_rng(2)
b=np.floor(3*(rg.random((3,3))))

print(np.hstack((a,b)))








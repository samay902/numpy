import numpy as np
import matplotlib.pyplot as plt
a=np.full((2,3),fill_value=7)
b=np.array([2,3,8,8,6,9,0])
print(a)
print(np.size(a))
print(a.ndim)
plt.plot(b)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


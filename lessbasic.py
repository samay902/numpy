import numpy as np
a=np.arange(10)**3
b=np.array([1,2,3,4,2,3])
print(a[b])
#array can be indexed by another array
c=np.array([[1,2,3],
           [4,5,6]])
print(a[c])
#when the indexed are in a shape then the array takes the same shape
palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])
marks=np.array([
    [90],
    [80],
    [70],
])
std=np.array([
    [0,1],
    [2,1],
])
print(marks[std])



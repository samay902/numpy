import numpy as np
data = np.loadtxt("data.csv", delimiter=",", skiprows=1)
exp=data[:,1]
sal=data[:,2]
print(np.mean(sal).round(2))
print(np.)


import numpy as np

time=np.linspace(24,150,45)
data=np.sin(np.arange(50).reshape(5,10))
print(time,data)
yy=data.argmax(axis=0)
print(yy)
time_dd=time[yy]
print(time_dd)
act_data=data[yy,range(data.shape[1])]
print(act_data)

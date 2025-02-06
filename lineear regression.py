import numpy as np
import matplotlib.pyplot as plt
experience = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # X values
salary = np.array([28000,35000,39000,45000,52000,58000,63000,70000,76000,
                   82000,90000,97000,102000,110000,119000])
# y values
x=experience.reshape(-1,1)
y=salary


def cost():
    total_error=0
    for i in range(len(y)):
        total_error+=(y[i]-a*x[i]+b)**2
    return total_error/float(len(y))
def gradient_descent(a_now,b_now,l):
    a_grad=0
    b_grad=0
    l=0
    n=len(y)
    for i in range(len(y)):
        a_grad+=-(2/n)*(y[i]-(a_now*x[i]+b_now))
        b_grad+=-(2/n)*(y[i]-(a_now*x[i]+b_now))
    a=a_now-a_grad*l
    b=b_now-b_grad*l
    return a,b
epochs=100
a=0
b=0
l=0.1

for i in range(epochs):
    a,b=gradient_descent(a,b,l)
    print(a,b)



























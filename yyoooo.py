def gradient_descent(a_now,b_now,l):
    a_grad=0
    b_grad=0
    for i in range(len(y)):

        a_grad+=-(2/n)*(y[i]-a*x[i]+b)
        b_grad+=sameasabove
        a=a_now-a_grad*l
        b=same
    return a,b
a=0
b=0
l=0.001
epochs=100
for i in range(epochs):
    a,b=gradient_descent(a,b,l)
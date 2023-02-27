import numpy as np
import timeit

A = np.random.rand(100,200)
d1 = np.random.rand(100)
D1=np.diag(d1)
d1 = d1.reshape(100,1)
def fstar():
    print('d1 * A=\n', d1 * A)

def fad():
    print('D1@A=\n', D1 @ A)

t1 = timeit.timeit(fstar, number=100)/100
t2 = timeit.timeit(fad, number=1000)/100
print(t1)
print(t2)
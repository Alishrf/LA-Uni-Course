import numpy as np
import timeit

m,n,p = 100,50,2000
A = np.random.rand(m,n,p)
s = np.random.rand(p)

def fad():
    print('s*@A=\n', s.reshape(1,1,p) * A)

def fstar():
    for i in range(p):
        A[:,:,i] *= s[i]
    print('A=', A)

t2 = timeit.timeit(fad, number=1)
t1 = timeit.timeit(fstar, number=1)

print(t1)
print(t2)
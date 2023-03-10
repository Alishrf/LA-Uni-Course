import numpy as np
import matplotlib.pyplot as plt

n = 11

S1 = np.vstack((-np.cos(np.linspace(0,np.pi,n)),
                    -.7+np.sin(np.linspace(0,np.pi,n)))).T


S2 = np.vstack((np.linspace(-1.2,1.2,n),
                    np.zeros(n))).T


print(S1.shape)
print(S2.shape)

plt.plot(S1[:,0], S1[:,1], 'bo-')
plt.plot(S2[:,0], S2[:,1], 'ro-')

plt.axis('equal')                   
plt.xlim(-2,2)
plt.ylim(-2,2)
   
plt.show()

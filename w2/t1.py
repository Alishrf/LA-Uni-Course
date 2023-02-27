import numpy as np
import matplotlib.pyplot as plt
n = 11
S1 = np.vstack((-np.cos(np.linspace(0,np.pi,n)),
-.7+np.sin(np.linspace(0,np.pi,n)))).T
S2 = np.vstack((np.linspace(-1.2,1.2,n),
np.zeros(n))).T

plt.plot(S1[:,0], S1[:,1], 'bo-')
plt.plot(S2[:,0], S2[:,1], 'ro-')
plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-2,2)
rng = np.linspace(0,1,20)
for alpha in rng:
    print(alpha)
    S3 = (1-alpha) * S1 + alpha * S2
    plt.plot(S3[:,0], S3[:,1], 'ro-')
    plt.draw()
    plt.pause(.01)
    plt.cla()
plt.show()
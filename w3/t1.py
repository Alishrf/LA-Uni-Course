import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# create a 3 x 2 matrix
A = np.array([[1, 2],
 [3,4],
 [-2,-1]])
fig = plt.figure()
# A 1 by 2 subplot grid, subplot 1 (3D)
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax1.set_title('column space')

F = np.random.randn(2,200)
F = A @ F
ax1.plot(F[0,:], F[1,:], 'o')


# A 1 by 2 subplot grid, subplot 2 (2D)
ax2 = fig.add_subplot(1,2,2)
ax2.set_title('row space')

G = np.random.randn(200 , 3)
G = G @ A
ax2.plot(G[0,:],G[1,:], G[2,:], 'ro')



plt.show()
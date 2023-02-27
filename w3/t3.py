import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# create a 3 x 3 matrix
A = np.array([[1, 2 , 1],
 [2 ,-1,-1],
 [-1, 1, -2]])
fig = plt.figure()
# A 1 by 2 subplot grid, subplot 1 (3D)
ax1 = fig.add_subplot(2,3,1, projection='3d')
ax1.set_title('column space A')

F = np.random.randn(3,200)
F = A @ F
ax1.plot(F[0,:], F[1,:], 'o')


# A 1 by 2 subplot grid, subplot 2 (2D)
ax2 = fig.add_subplot(2,3,2)
ax2.set_title('row space A')

G = np.random.randn(200 , 3)
G = G @ A
ax2.plot(G[0,:],G[1,:], G[2,:], 'ro')


B = np.array([[1, 2 , -3],
 [3,1,1],
 [2,1,0]])
# A 1 by 2 subplot grid, subplot 1 (3D)
ax3 = fig.add_subplot(2,3,3, projection='3d')
ax3.set_title('column space B')

F = np.random.randn(3,200)
F = B @ F
ax3.plot(F[0,:], F[1,:], 'o')


# A 1 by 2 subplot grid, subplot 2 (2D)
ax4 = fig.add_subplot(2,3,4)
ax4.set_title('row space C')

G = np.random.randn(200 , 3)
G = G @ B
ax4.plot(G[0,:],G[1,:], G[2,:], 'ro')


C = np.array([[1, 2 , -3],
 [3 ,6,-9],
 [-2,-4 , 6]])
# A 1 by 2 subplot grid, subplot 1 (3D)
ax5 = fig.add_subplot(2,3,5, projection='3d')
ax5.set_title('column space C')

F = np.random.randn(3,200)
F = C @ F
ax5.plot(F[0,:], F[1,:], 'o')


# A 1 by 2 subplot grid, subplot 2 (2D)
ax6 = fig.add_subplot(2,3,6)
ax6.set_title('row space')

G = np.random.randn(200 , 3)
G = C @ A
ax6.plot(G[0,:],G[1,:], G[2,:], 'ro')


plt.show()
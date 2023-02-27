import matplotlib.pyplot as plt
import numpy as np
from face_data import Face1, Face2, Face3, edges
def plot_face(plt,X,edges,color='b'):
    plt.plot(X[:,0], X[:,1], 'o', color=color)
    for k in range(0,len(edges)):
        i,j = edges[k] # edge from node i to node j
        xi = X[i,0]
        yi = X[i,1]
        xj = X[j,0]
        yj = X[j,1]
        # draw a line between X[i] and X[j]
        plt.plot((xi,xj), (yi,yj), '-', color=color)
        plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
for k in np.linspace(-0.5,1.5,20):
    x = (1-k) * Face1 + (k) * Face2
    plot_face(plt, x, edges, color='b')
    plt.draw()
    plt.pause(.01)
    plt.cla()
for k in np.linspace(-0.5,1.5,20):
    x = (1-k) * Face2 + (k) * Face3
    plot_face(plt, x, edges, color='b')
    plt.draw()
    plt.pause(.01)
    plt.cla()
plt.show()
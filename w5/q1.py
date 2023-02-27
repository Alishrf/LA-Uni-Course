import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve

from face_data import Face1, Face2, Face3, TargetFace2, edges
def plot_face(plt,X,edges,color='b'):
    "plots a face"
    plt.plot(X[:,0], X[:,1], 'o', color=color, markersize=3)
    for i,j in edges:
        xi = X[i,0]
        yi = X[i,1]
        xj = X[j,0]
        yj = X[j,1]
        # draw a line between X[i] and X[j]
        plt.plot((xi,xj), (yi,yj), '-', color=color)
    plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)


face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = TargetFace2.ravel()
F = np.stack((face1, face2, face3), axis=1)

a1,b1,c1 = F[0]
a2,b2,c2 = F[1]
a3,b3,c3 = F[2]
a, b, c = symbols('a,b,c')
eq1 = Eq((a1 *a+b1 *b+ c1 *c), t[0])
eq2 = Eq((a2 *a+b2 *b+ c2 *c), t[1])
eq3 = Eq((a3 *a+b3 *b+ c3 *c), t[2])
d = solve((eq1, eq2, eq3), (a,b,c))

a , b , c = d[a],d[b],d[c]

Face = a * Face1 + b * Face2 + c * Face3


plot_face(plt, TargetFace2, edges, color='r')
plot_face(plt, Face, edges, color='g')
#change a,b,c until the two plots align
plt.show()
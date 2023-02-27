import matplotlib.pyplot as plt
import numpy as np
from face_data import Face1, Face2, Face3, TargetFace2, edges
from sympy import *


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


TargetFace = TargetFace2
NoisyTargetFace = TargetFace + 3 * np.random.randn(*TargetFace.shape)

face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = NoisyTargetFace.ravel();
F = np.stack((face1, face2, face3), axis=1)

for i in range(5):
    inds = np.random.choice(range(136), 3, replace=False)

    print(inds)
    a1,b1,c1 = F[inds[0]]
    a2,b2,c2 = F[inds[1]]
    a3,b3,c3 = F[inds[2]]
    a, b, c = symbols('a,b,c')
    eq1 = Eq((a1 *a+b1 *b+ c1 *c), t[0])
    eq2 = Eq((a2 *a+b2 *b+ c2 *c), t[1])
    eq3 = Eq((a3 *a+b3 *b+ c3 *c), t[2])
    d = solve((eq1, eq2, eq3), (a,b,c))


    A = F
    B = t
    B = (A.T).dot(B)
    A = A.T.dot(A)
    B.resize(3,1)
    H =np.concatenate([A,B], axis=1)
    x =Matrix(H).rref()
    x = x[0]


    print('x' ,x)
    xx=np.linalg.lstsq(A,B, rcond=None)
    print('xx' , xx[0])
    a , b , c = d[a],d[b],d[c] # solve 3 random equations
    a2,b2,c2 = x[3],x[7],x[11]
    Face_rnd = a * Face1 + b * Face2 + c * Face3
    Face_lsq = a2 * Face1 + b2 * Face2 + c2 * Face3
    #plot_face(plt, NoisyTargetFace, edges, color='r')
    plot_face(plt, TargetFace, edges, color='k')

    #plot_face(plt, Face_rnd, edges, color='g')
    plot_face(plt, Face_lsq, edges, color='b')
    plt.show()
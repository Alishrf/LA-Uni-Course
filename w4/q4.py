import imageio
import matplotlib.pyplot as plt
import numpy as np
G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')
G = np.dstack([G,G,G])
print('g=', G.shape)
print('I=', I.shape)



for alpha in np.linspace(0,1,20):
    zar = np.full((853), 1- alpha)
    zar1 = np.full((853), alpha)

    J = (zar.reshape(853 , 1 , 1) * G) + (zar1.reshape(853,1,1) * I) # combine G and I
    J= J.astype(int)

    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()
import imageio
import matplotlib.pyplot as plt
import numpy as np
G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')
G = np.dstack([G,G,G])
print('g=', G.shape)
print('I=', I.shape)



for alpha in np.linspace(0,np.pi,20):
    a = np.full((1, 1 , 1), np.sin(alpha))
    b = np.full((1, 1 , 1), np.sin(alpha + (np.pi/4)))
    c = np.full((1, 1 , 1), np.sin(alpha + (np.pi/2)))
    J = np.dstack([a,b,c])
    print('J=', J.shape)

    J =G *  J
    J= J.astype(np.uint8)

    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()
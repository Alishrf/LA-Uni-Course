import numpy as np
import imageio
import matplotlib.pyplot as plt
I = imageio.imread('nasir-al-mulk-gray.jpg')
print('I=\n', I)
print('I.dtype=\n', I.dtype)
print('I.shape=\n', I.shape)
Inv = I[::-1]
I=np.concatenate((np.array(I), np.array(Inv)), axis=0)
plt.imshow(I, cmap='gray')
plt.show()
#plt.imshow(I.T, cmap='gray')
#plt.show()
#plt.imshow(I[100:300, 400:1000], cmap='gray')
#plt.show()
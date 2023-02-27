import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

#revers data
data = data[::-1]


print('samping rate:', sampling_rate) # frequency (sample per second)
print('data type:', data.dtype)
print('data shape:', data.shape)

N, no_channels = data.shape # signal length and no. of channels

print('signal length:', N)

channel0 = data[:,0]
channel1 = data[:,1]

scale = 2**np.linspace(-2,4, N)

plt.plot(np.arange(N), channel0)
plt.plot(np.arange(N), channel1)
plt.show()


plt.plot(np.arange(N), data)
plt.show()

print('shape_old:', scale.shape)
scale.shape = (N,1)
print('shape_new:', scale.shape)

data_new = np.int16(scale * data)


plt.plot(np.arange(N), data_new)
plt.show()

#scipy.io.wavfile.write('output_rev.wav', sampling_rate, data_new)


import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

print('samping rate:', sampling_rate) # frequency (sample per second)
print('data type:', data.dtype)
print('data shape:', data.shape)

N, no_channels = data.shape # signal length and no. of channels

print('signal length:', N)

channel0 = data[:,0]
channel1 = data[:,1]

scale2x = 4**np.linspace(-2,4, N)
scalehalfx = 0.5**np.linspace(-2,4, N)


scale2x.shape = (N,1)
scalehalfx.shape = (N,1)


data_new_2x = np.int16(scale2x * data)
data_new_half = np.int16(scalehalfx * data)

scipy.io.wavfile.write('output2x.wav', sampling_rate * 2, data)
scipy.io.wavfile.write('output0.5x.wav', sampling_rate // 2, data)



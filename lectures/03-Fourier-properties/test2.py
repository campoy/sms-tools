import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models'))
import utilFunctions as UF

M = 501
hM1 = int(math.floor((M+1)/2.0))
hM2 = int(math.floor(M/2.0))

(fs, x) = UF.wavread('../../sounds/soprano-E4.wav')
x1 = x[5000:5000+M] * np.hamming(M)

N = 1024
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
mX = 20 * np.log10(abs(X))
pX = np.unwrap(np.angle(X))

plt.title('magnitude')
plt.plot(np.arange(N/2)* fs / N, mX[:N/2])
plt.figure()
plt.title('phase')
plt.plot(pX[:N/2])
plt.show()
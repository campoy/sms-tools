import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)
N = len(x)
fftbuffer = np.zeros(N)
fftbuffer[:N%2+N/2] = x[N/2:]
fftbuffer[N%2+N/2:] = x[:N/2]
X = fft(fftbuffer)
mX = abs(X)
pX = np.angle(X)
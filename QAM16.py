import matplotlib.pyplot as plt
import numpy as np

#00 -3
#01 -1
#11  1
#10 +3


BitsNumber = 1000
sigma = 0.2
level = np.array([-3,-1,3,1])

bits = np.random.randint(0,2,BitsNumber)
symbols = bits.reshape(-1,4)
I_raw = symbols[:,:2]
Q_raw = symbols[:,2:4]
I = np.zeros(int(BitsNumber/4))
Q = np.zeros(int(BitsNumber/4))
I = level[2*I_raw[:,0]+I_raw[:,1]]
Q = level[2*Q_raw[:,0]+Q_raw[:,1]]

noise = sigma * (np.random.randn(int(BitsNumber/4)) +1j*np.random.randn(int(BitsNumber/4)))
signal = I + 1j*Q + noise

plt.scatter(signal.real,signal.imag)
plt.show()
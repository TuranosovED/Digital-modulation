import matplotlib.pyplot as plt
import numpy as np

#00 -3
#01 -1
#11  1
#10 +3

BitsCountdownCount = 20 #количество отсчетов на бит
BitsNumber = 1000 # количество битового потока
sigma = 0.1
freq = 1000 # частота несущей
level = np.array([-3,-1,3,1])


bits = np.random.randint(0,2,BitsNumber)
bits_t = np.repeat(bits,BitsCountdownCount) #битовый поток во времени
symbols = bits.reshape(-1,4)
I_raw = symbols[:,:2]
Q_raw = symbols[:,2:4]
I = np.zeros(int(BitsNumber/4))
Q = np.zeros(int(BitsNumber/4))
I = level[2*I_raw[:,0]+I_raw[:,1]]
Q = level[2*Q_raw[:,0]+Q_raw[:,1]]
I_t = np.repeat(I,BitsCountdownCount) 
Q_t = np.repeat(Q,BitsCountdownCount)
T = np.linspace(0,1,len(I_t))

noise = sigma * (np.random.randn(int(BitsNumber/4)) +1j*np.random.randn(int(BitsNumber/4)))
signal = I + 1j*Q + noise

analog_signal = I_t*np.cos(2*np.pi * freq * T) - Q_t*np.sin(2*np.pi * freq * T) + sigma * np.random.randn(len(I_t))

plt.subplot(4,2,5)
plt.plot(T[:500],analog_signal[:500])

plt.subplot(4,2,6)
plt.step(T[:500],I_t[:500])

plt.subplot(4,2,7)
plt.step(T[:500],Q_t[:500])

Specter = np.fft.fft(analog_signal/len(analog_signal))
Specter = np.fft.fftshift(Specter)

freq_axis = np.fft.fftfreq(len(analog_signal),T[1]-T[0])
freq_axis = np.fft.fftshift(freq_axis)

plt.subplot(4,2,8)
plt.plot(freq_axis, np.abs(Specter))

plt.subplot(4,2,(1,4))
plt.scatter(signal.real,signal.imag)

plt.tight_layout()
plt.show()


import numpy as nm
import matplotlib.pyplot as plt

BitsNumber = 1000
sigma = nm.linspace(0,0.4,4)
bits = nm.random.randint(0,2,BitsNumber)
symbol = bits.reshape(-1,2)
I = 2 * symbol[:,0] - 1
Q = 2 * symbol[:,1] - 1


for i in range(0,4):
    plt.subplot(2,2,i+1)
    noise = sigma[i] * nm.random.randn(int(BitsNumber/2)) + sigma[i] * 1j*nm.random.randn(int(BitsNumber/2))
    Signal = I + 1j*Q + noise
    plt.scatter(Signal.real,Signal.imag)
    plt.title(f"sigma = {round(sigma[i],2)}")
plt.tight_layout()
plt.show()

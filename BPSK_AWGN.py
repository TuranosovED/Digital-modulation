import matplotlib.pyplot as plt
import numpy as nm
N = 20 #количество значений SNR
BitsNumber = 10000 #количество бит
SignalNoiseRatioDb = nm.linspace(-5,10,N) #SNR в дб
SignalNoiseRatio = nm.pow(10,SignalNoiseRatioDb/10) #SNR
sigma = 1/(nm.sqrt(SignalNoiseRatio)) #ско
bits = nm.random.randint(0,2,BitsNumber) #массив битов
b = 2*bits - 1  #перевод в -1 1
BitsErrorRate = nm.zeros(N) #массив BER
signal = nm.zeros(BitsNumber)

for i in range(0,N):
    noise = sigma[i]*nm.random.randn(BitsNumber) #расчет шума
    signal = b + noise #добавляем шум
    recive = nm.zeros(BitsNumber) #массив приема
    recive[signal>0] = 1 
    recive[signal<0] =0
    errors=0
    errors+= nm.sum(recive!=bits) #количество ошибок
    BitsErrorRate[i] = errors/BitsNumber #BER

plt.subplot(4,2,(1,4))
plt.plot(SignalNoiseRatioDb,BitsErrorRate)
plt.yscale('log')
plt.xlabel("SNR, dB")
plt.ylabel("BER")

signalCount = 100
index = [1,17,18,19]
graph = [5,6,7,8]
signal = nm.zeros(signalCount)
for i in range(len(index)):
    plt.subplot(4,2,graph[i])
    signal = b[:signalCount] + sigma[index[i]]*nm.random.randn(signalCount)
    plt.title(f"SNR, dB = {round(SignalNoiseRatioDb[index[i]],2)}")
    plt.scatter(signal,nm.zeros(signalCount))

plt.tight_layout()
plt.show()




import hardware.nidaq
import numpy as np
import matplotlib.pylab as plt

freq=100e3
N=10000

ai_measurement = hardware.nidaq.AITask('/Dev2/ai0', N, freq, read_timeout=1.0, range=(-10, 10))

ai_measurement.Start()



x=np.linspace(0.,1./freq*N,N)
y1,y2,y3 = ai_measurement.Read()



import matplotlib.pyplot as pyplot
plt.plot(x,y1)
#plt.plot(x,y2)
plt.show()

ai_measurement.Stop()


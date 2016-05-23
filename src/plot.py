import numpy as np
import time
import matplotlib.pyplot as plt

a=np.loadtxt('meas2/magnitude_0to40.0mA_freq_sweep.csv', delimiter=',')
c=np.loadtxt('meas2/phase_0to40.0mA_freq_sweep.csv', delimiter=',')
b=np.loadtxt('meas2/sweep_feq.csv', delimiter=',')

cstart=0 #start current 
cstop=40E-3 # stop current
cstep=5E-3 # current step
csteps=int((cstop-cstart)/cstep)

fig, (ax0,ax1)=plt.subplots(2,1, sharex=True)
for i in range(csteps):
	current=cstart+i*cstep
	ax0.plot(b,a[:,i], label="{0:d}mA".format(int((current)*1000)))
	ax1.plot(b,c[:,i], label="{0:d}mA".format(int((current)*1000)))

ax1.set_xlabel("Larmor frequency in kHz")
ax1.axhline(y=0, color='r', ls='--')
plt.legend(prop={'size':6})
#plt.savefig('meas2/phase_amplitude.png')
plt.show()
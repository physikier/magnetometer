import numpy as np
import time
import matplotlib.pyplot as plt

current=[0,10,20,30,40]
max_freq=[62.3,62.6,64.3,65.7,66.5]
Bfiel_gauss=[0,(max_freq[1]-max_freq[0])/0.7E3,(max_freq[2]-max_freq[0])/0.7E3, (max_freq[3]-max_freq[0])/0.7E3,(max_freq[4]-max_freq[0])/0.7E3 ]

fig,(ax0,ax1)=plt.subplots(2,1)
ax0.scatter(current,max_freq)
ax0.set_ylabel('Larmor frequency in kHz')
ax1.scatter(current, Bfiel_gauss)
ax1.set_ylabel('magnetic field in Gauss')
plt.show()
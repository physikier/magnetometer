import hardware.afg3000 as tek
import hardware.hameg as ha
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt
import os
import matplotlib.colors as cl


########################################################################
#CONNECT to hameg and tektronix


rm=pyvisa.ResourceManager()
lockin=rm.open_resource("GPIB0::10::INSTR")

tektronix=tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")
hameg=ha.HMP2030(device="hameg01", channel=1, voltage_max=20., current_max=1)

##########################################################################
#INITIALIZE measurement parameters

cell='4'
measno='156'
measurement='{0:s}_rb87_last trans_3_shields_isweep'.format(measno) 	
		#number and special features of the measurement

fstart=24.6E3 						#start frequency
fstep=0.2E3 						#frequency step
fstop=25.6E3 						#stop frequency
steps=int((fstop-fstart)/fstep+1) #frequency steps
print 'frequency steps:{0:d}'.format(steps)

cstart=300						#start current in mA
cstop=350							#stop current in mA
cstep=0.2						#current step in mA
csteps=int((cstop-cstart)/cstep+1)#amout of current steps
print 'current steps:{0:d}'.format(csteps)

amp1=600.0E-3					#amplitude for the oscillation of the small coils
offset1=0					#offset has to be half of the amplitude
amp2=900E-3 					#amplitude of the reference for lockin, max 1Vpp
offset2=0 						#zero offste for the reference 

accum=100						#accumulation steps per frequency
sleepf=3
sleepi=0.1

sensi='1uV'
timeconstant='100ms'



laserpower=500

filename='N:/data/emily/magnetometer/cell{0:s}/'.format(str(cell))



####################################################################################
#INITIALIZE devices 

hameg.set_current(cstart*10**(-3))  		#initialize hameg
tektronix.set_freq(fstart)		#initialize tektronix channel 1
tektronix.set_freq(fstart,ch=2) #initialize tektronix channel 2 as reference for lockin
tektronix.set_amp(amp1)
tektronix.set_offset(offset1)
tektronix.set_amp(amp2,ch=2)
tektronix.set_offset(offset2,ch=2)
tektronix.run(ch=1)
tektronix.run(ch=2)
hameg.run()

current=np.zeros((csteps,steps))
mag=np.zeros((csteps,steps))
pha=np.zeros((csteps,steps))

hsv=[(1.*j/steps,1,0.9+0.1*j/steps) for j in range(steps)]
rgb=cl.hsv_to_rgb(hsv)
fig, (ax0,ax1)=plt.subplots(1,2)

print 'measurement time: {0:s} s'.format(str(csteps*(sleepi+accum*0.045+0.04)*steps+steps*sleepf))

starttime=time.time()
i=0
for k in range(steps): 		#hameg current loop
   	freq=(fstart+k*fstep)
   	tektronix.set_freq(freq,1)
	tektronix.set_freq(freq,2)

	time.sleep(sleepf) 
	print '{0:s}kHz/ {1:s}kHz'.format(str(freq/1000),str(fstop/1000))
	for i in range(csteps):		#tektronix frequency loop
		curr=(cstart+(i)*cstep)*10**(-3)
		hameg.set_current(curr)
		time.sleep(sleepi)
		a=0
		b=0
		c=0
		d=0
		for j in range(accum):	#accumulation steps
			a=int(lockin.query("MAG"))
			c+=a
			#b=int(lockin.query("PHA"))
			#d=+b
		current[i,k]=hameg.get_current(ch=1)
		mag[i,k]=c/accum
		#pha[i,k]=d/accum
	ax0.plot(current[:,k], mag[:,k],  label="{0:.2f}kHz".format(freq/1000))
	ax1.plot(current[:,k], pha[:,k], label="{0:.2f}kHz".format(freq/1000))
np.savetxt(filename+"meas{0:s}_curr.csv".format(measno), current, delimiter=",")
np.savetxt(filename+"meas{11:s}_mag_{8:.0f}uW_{0:.1f}_{1:.1f}_{2:.1f}kHz_{3:.1f}mA_{4:.0f}_{5:.0f}mV_{6:.0f}_{7:.1f}s_{9:s}_{10:s}.csv".format(fstart/1000,fstop/1000,fstep/1000,cstep, amp1*1000, offset1*1000, accum, sleepi, laserpower, sensi, timeconstant, measurement), mag, delimiter=",")
#np.savetxt(filename+"/pha.csv", pha, delimiter=",")
hameg.stop()
tektronix.stop(ch=1)
ax0.set_title('amplitude')
ax1.set_title('phase')
stoptime=time.time()
print 'actual measurement time: {0:.1f}'.format(stoptime-starttime)
plt.legend()
plt.savefig(filename+'/meas{0:s}phase_amplitude.png'.format(measno))
plt.show()

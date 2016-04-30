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
measno='104'
measurement='{0:s}_locked_to_rb87_f1_with_2_shields_amplsweep'.format(measno) 	
		#number and special features of the measurement


cstart=460						#start current in mA
cstop=510							#stop current in mA
cstep=0.2						#current step in mA
csteps=int((cstop-cstart)/cstep+1)#amout of current steps
print 'current steps:{0:d}'.format(csteps)

bstart=50.0		#start amplitude in mVpp
bstop=450.0		#stop amplitude in mVpp
bstep=50.0
bsteps=int((bstop-bstart)/bstep+1)
print 'amplitude steps:{0:d}'.format(bsteps)
				#amplitude for the oscillation of the small coils
offset1=0 					#offset has to be half of the amplitude
amp2=900E-3 					#amplitude of the reference for lockin, max 1Vpp
offset2=0 						#zero offste for the reference 

freq=25.4E3

accum=1 						#accumulation steps per frequency
sleepb=0.5
sleepi=0.3

filename='N:/data/emily/magnetometer/cell{1:s}/meas{0:s}'.format(str(measurement), str(cell))

if not os.path.exists(filename):
	os.makedirs(filename) 		#create a directrory


####################################################################################
#INITIALIZE devices 

hameg.set_current(cstart*10**(-3))  		#initialize hameg
tektronix.set_freq(freq)		#initialize tektronix channel 1
tektronix.set_freq(freq,ch=2) #initialize tektronix channel 2 as reference for lockin
tektronix.set_amp(bstart*10**(-3))
tektronix.set_offset(offset1)
tektronix.set_amp(amp2,ch=2)
tektronix.set_offset(offset2,ch=2)
tektronix.run(ch=1)
tektronix.run(ch=2)
hameg.run()

current=np.zeros((csteps,bsteps))
mag=np.zeros((csteps,bsteps))
pha=np.zeros((csteps,bsteps))

hsv=[(1.*j/bsteps,1,0.9+0.1*j/bsteps) for j in range(bsteps)]
rgb=cl.hsv_to_rgb(hsv)
fig, (ax0,ax1)=plt.subplots(1,2)

print 'Messzeit: {0:s} s'.format(str(csteps*(sleepi+accum*0.08)*bsteps+bsteps*sleepb))


i=0
for k in range(bsteps): 		#hameg current loop
   	amplb1=(bstart+k*bstep)*10**(-3)
   	tektronix.set_amp(amplb1,ch=1)
	time.sleep(sleepb) 
	print '{0:s}mV/ {1:s}mV'.format(str(amplb1*1000),str(bstop))
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
	ax0.plot(current[:,k], mag[:,k],  label="{0:d}mV".format(int(amplb1*1000)))
	ax1.plot(current[:,k], pha[:,k], label="{0:d}mV".format(int(amplb1*1000)))
np.savetxt(filename+"/curr.csv", current, delimiter=",")
np.savetxt(filename+"/magnitude.csv", mag, delimiter=",")
#np.savetxt(filename+"/pha.csv", pha, delimiter=",")
hameg.stop()
tektronix.stop(ch=1)
ax0.set_title('amplitude')
ax1.set_title('phase')
plt.legend()
plt.savefig(filename+'/meas{0:s}phase_amplitude.png'.format(measno))
plt.show()

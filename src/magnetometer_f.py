import hardware.afg3000 as tek
import hardware.hameg as ha
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt
import os


########################################################################
#CONNECT to hameg and tektronix


rm=pyvisa.ResourceManager()
lockin=rm.open_resource("GPIB0::10::INSTR")

tektronix=tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")
hameg=ha.HMP2030(device="hameg01", channel=1, voltage_max=20., current_max=0.2)

##########################################################################
#INITIALIZE measurement parameters

measurement='20_locked_to_rb87_mF3_with_2_shields' 		#number and special features of the measurement

fstart=6E3 						#start frequency
fstep=1E3 						#frequency step
fstop=24E3 						#stop frequency
steps=int((fstop-fstart)/fstep+1) #frequency steps
print 'frequency steps:{0:d}'.format(steps)

cstart=1						#start current in mA
cstop=8							#stop current in mA
cstep=1						#current step in mA
csteps=int((cstop-cstart)/cstep+1)#amout of current steps
print 'current steps:{0:d}'.format(csteps)

amp1=50.0E-3					#amplitude for the oscillation of the small coils
offset1=amp1/2 					#offset has to be half of the amplitude
amp2=900E-3 					#amplitude of the reference for lockin, max 1Vpp
offset2=0 						#zero offste for the reference 

accum=10 						#accumulation steps per frequency


filename='N:/data/emily/magnetometer/meas{0:s}'.format(str(measurement))

if not os.path.exists(filename):
	os.makedirs(filename) 		#create a directrory


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



magnp=np.zeros([steps,csteps])	#create array containing all magnitude values of the lockin signal
phanp=np.zeros([steps,csteps])	#create array containing all phase values of the lockin signal
ui=np.zeros((csteps,2))


for k in range(csteps): 		#hameg current loop
	mag=[]
	pha=[]
   	curr=(cstart+k*cstep)*10**(-3)
	hameg.set_current(curr)
	if cstart==0 and k==0:
   		hameg.stop()
   	hameg.run()
	time.sleep(3)
	ui[k,0]=hameg.get_voltage(ch=1)
	ui[k,1]=hameg.get_current(ch=1)
	for i in range(steps):		#tektronix frequency loop
		frequency=fstart+(i)*fstep
		tektronix.set_freq(frequency,1)
		tektronix.set_freq(frequency,2)
		time.sleep(0.5)
		c=0
		d=0
		for j in range(accum):	#accumulation steps
			a=int(lockin.query("MAG"))
			c+=a
			b=int(lockin.query("PHA"))
			d=+b
		mag.append(c/accum)
		pha.append(d/accum)
		print 'loop {0:s} mA, {1:s}kHz'.format(str(curr*1000), str(frequency/1000))
	magnp[:,k]=mag
	phanp[:,k]=pha
	
current=np.linspace(cstart, cstop, num=csteps)
sweep_freq=np.linspace(fstart/1000,fstop/1000, num=steps)

np.savetxt("N:/data/emily/magnetometer/meas{2:s}/magnitude_{0:s}to{1:s}mA_{3:s}to{4:s}kHz.csv".format(str(cstart),str(cstop), str(measurement), str(fstart/1000), str(fstop/1000)), magnp, delimiter=",")
np.savetxt("N:/data/emily/magnetometer/meas{2:s}/phase_{0:s}to{1:s}mA{3:s}to{4:s}kHz.csv".format(str(cstart),str(cstop), str(measurement), str(fstart/1000), str(fstop/1000)), phanp, delimiter=",")
np.savetxt("N:/data/emily/magnetometer/meas{2:s}/current_and_voltage_coils_{0:s}to{1:s}mA.csv".format(str(cstart),str(cstop), str(measurement)), ui, delimiter=",")
np.savetxt("N:/data/emily/magnetometer/meas{2:s}/sweep_feq{0:s}to{1:s}kHz.csv".format(str(fstart/1000),str(fstop/1000), str(measurement)), sweep_freq)
#np.savetxt("N:/data/emily/magnetometer/meas{2:s}/current{0:s}to{1:s}mA.csv".format(str(fstart/1000),str(fstop/1000), str(measurement)), current)

hameg.stop()
tektronix.stop()
#tektronix.stop(ch=2)

fig, (ax0,ax1)=plt.subplots(2,1, sharex=True)
for i in range(csteps):
	current=cstart+i*cstep
	ax0.plot(sweep_freq,magnp[:,i], label="{0:d}mA".format(int((current))))
	ax1.plot(sweep_freq,phanp[:,i], label="{0:d}mA".format(int((current))))

ax1.set_xlabel("Larmor frequency in kHz")
ax1.axhline(y=0, color='r', ls='--')
plt.legend(prop={'size':6})
plt.savefig('N:/data/emily/magnetometer/meas{2:s}/phase_amplitude{0:s}to{1:s}kHz{3:s}to{4:s}mA.png'.format(str(fstart/1000),str(fstop/1000), str(measurement), str(cstart),str(cstop)))
plt.show()

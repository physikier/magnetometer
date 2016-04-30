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
measno='64'
measurement='64_locked_to_rb87_f2_with_1_shields_isweep' 	
		#number and special features of the measurement

f=25E3 						#start frequency


c=17						#start current in mA


amp1=50.0E-3					#amplitude for the oscillation of the small coils
offset1=0 					#offset has to be half of the amplitude
amp2=900E-3 					#amplitude of the reference for lockin, max 1Vpp
offset2=0 						#zero offste for the reference 

					#accumulation steps per frequency


filename='N:/data/emily/magnetometer/cell{1:s}/relaxationmeas{0:s}'.format(str(measurement), str(cell))

if not os.path.exists(filename):
	os.makedirs(filename) 		#create a directrory


####################################################################################
#INITIALIZE devices 

hameg.set_current(c*10**(-3))  		#initialize hameg
tektronix.set_freq(f)		#initialize tektronix channel 1
tektronix.set_freq(f,ch=2) #initialize tektronix channel 2 as reference for lockin
tektronix.set_amp(amp1)
tektronix.set_offset(offset1)
tektronix.set_amp(amp2,ch=2)
tektronix.set_offset(offset2,ch=2)
tektronix.run(ch=1)
tektronix.run(ch=2)
hameg.run()

num=100
mag=np.zeros((num,1))





tektronix.stop(ch=1)
start=time.time()

for i in range(num):
	mag[i,:]=int(lockin.query("MAG"))
end=time.time()
diff=end-start
print diff/num
timeline=np.linspace(0,diff,num=num)
plt.plot(timeline, mag)
plt.show()



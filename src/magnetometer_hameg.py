import hardware.hameg as ha
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt


rm=pyvisa.ResourceManager()
lockin=rm.open_resource("GPIB0::10::INSTR")


hameg=ha.HMP2030(device="hameg01", channel=1, voltage_max=20., current_max=0.2)



hameg.run()
mag=[]
pha=[]
cstart=0.00
cstep=0.001
cstop=0.08
steps=int((cstop-cstart)/cstep)
print steps

hameg.set_current(cstart,ch=1)

for i in range(steps):
	hameg.set_current(cstart+(i+1)*cstep)
	time.sleep(0.1)
	c=0
	d=0
	for j in range(10):
		a=int(lockin.query("MAG"))
		c+=a
		b=int(lockin.query("PHA"))
		d=+b
	mag.append(c/10)
	pha.append(d/10)
	print i
hameg.stop()


sweep_curr=np.linspace(cstart,cstop, num=steps)

plt.scatter(sweep_curr,mag, label="amplitude", color="red")
plt.scatter(sweep_curr,pha, label="phase", color="blue")
plt.xlabel("Current in Amps")
plt.legend()
plt.savefig("90kHz_1_with_resistance.png")
plt.show()
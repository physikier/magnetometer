import hardware.hameg as ha
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt




#hameg=ha.HMP2030(device="TCPIP0::129.69.46.236::5415::SOCKET", channel=1, voltage_max=20., current_max=0.1)
hameg=ha.HMP2030(device="hameg01", channel=1, voltage_max=20., current_max=1)


time.sleep(1)
cstep=0.1
for i in range(5):
	hameg.set_current(i*cstep)
	t=hameg.get_current()
	print t
	time.sleep(1)
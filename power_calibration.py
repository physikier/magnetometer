import hardware.Motordriver as mo
import hardware.power_meter as po
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.interpolate as si
import serial

motor1 = mo.Motordriver('COM4')
#powermeter = po.PM100D('USB0::0x1313::0x8078::PM002838::INSTR')
powermeter = po.PM100D('USB0::0x1313::0x80B0::P3000228::INSTR')


try:
	
	start = 0
	stop = 360
	step = 1
	step_new = 0.1
	motor1.moveToAbsolutePosition(motor=1, pos=0)
	while motor1.isMoving(motor=1):
		time.sleep(1)

	position = np.arange(start, stop+step, step)
	power = []
	for deg in position:
		motor1.moveToAbsolutePosition(motor=1, pos=deg)
		while motor1.isMoving(motor=1):
			time.sleep(1)
		a = powermeter.getMeanPower(t=1.)
		power.append(a)
	f = si.interp1d(position, power)
	xnew = np.arange(start, stop+step_new, step_new)
	ynew = f(xnew)
	int_values = np.transpose(np.array([xnew, ynew]))
	values = np.transpose([position, power])
	np.savetxt('power_calibration_interpolated_values.txt', int_values)
	np.savetxt('power_calibration.txt', values)
	plt.plot(position, power)
	plt.xlabel('Motordriver position in degree')
	plt.ylabel('Power in W')
	plt.show()
	plt.savefig('power_calibration.png', dpi=300)

finally:
	motor1.goHome()
	del motor1
	powermeter.disconnect()
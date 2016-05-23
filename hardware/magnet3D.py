'''
Created on 01.03.2012

@author: matthias n.
'''

import time
import threading
import numpy as np

import hameg
#import USBRelais
import dummy as USBRelais

from traits.api import SingletonHasTraits, Trait, Instance, Property, String, Range, Float, Int, Bool, Array, Enum, Button, on_trait_change, cached_property, Code, List, NO_COMPARE
from traitsui.api import View, Item, HGroup, VGroup, VSplit, Tabbed, EnumEditor, TextEditor, Group, RangeEditor

from tools.utility import GetSetItemsMixin

from threading import Thread,Lock
from Queue import Queue

import logging

def cartesian_to_spherical(r, unit='deg'):
    b = np.linalg.norm(r)
    if b==0:
        return np.array([0,0,0])
    theta = np.arccos(r[2]/b)
    phi = np.arctan2(r[1],r[0])
    if unit=='deg':
        theta = np.degrees(theta)
        phi = np.degrees(phi)
    elif unit!='rad':
        raise ValueError('Undefined unit.')
    return np.array([b,theta,phi])

def spherical_to_cartesian(r, unit='deg'):
    b, theta, phi = r 
    if unit=='deg':
        theta = np.radians(theta)
        phi = np.radians(phi)
    elif unit!='rad':
        raise ValueError('Undefined unit.')
    if not 0<=theta<=np.pi or not (-np.pi)<=phi<=(2*np.pi):
        raise ValueError('Wrong angle. Chose theta between 0..180(0..pi) and phi between -180..180(-pi..pi)')
    x = b*np.sin(theta)*np.cos(phi)
    y = b*np.sin(theta)*np.sin(phi)
    z = b*np.cos(theta)
    return np.array([x,y,z])

class Magnet3D(GetSetItemsMixin):

	polarity = [1,1,1]
	relais_lock = Lock()
	axis_current = [0.,0.,0.]

	
	current_max = Float(default_value=0.1)
	voltage_max = Float(default_value=31.9)

	voltage_max_vec = Array()
	current_max_vec = Array()

	stop = False
	stop_lock = Lock()


	def __init__(self,devicelist,relais_serial_port, diff_current, voltage_max_vector, current_max_vector, fuse_voltage_max, fuse_current_max, gauss_per_amp_vector=(1.,1.,1.), current_min=0.0005,ramp_down=False,reset=True):
		super(Magnet3D, self).__init__()

		self.devicesX = devicelist[0];
		self.devicesY = devicelist[1];
		self.devicesZ = devicelist[2];

		self.add_trait("set_current_1",Range(low=-current_max_vector[0],high=current_max_vector[0],value=0,mode='text',auto_set=False,enter_set=True,  desc='current of first coil [mA]', label='I_1 [mA]',width=-20))
		self.add_trait("set_current_2",Range(low=-current_max_vector[1],high=current_max_vector[1],value=0,mode='text',auto_set=False,enter_set=True,  desc='current of second coil [mA]', label='I_2 [mA]',width=-20))
		self.add_trait("set_current_3",Range(low=-current_max_vector[2],high=current_max_vector[2],value=0,mode='text',auto_set=False,enter_set=True,  desc='current of third coil [mA]', label='I_3 [mA]',width=-20))

		self.current_max_vec = current_max_vector
		self.voltage_max_vec = voltage_max_vector


		self.current_max = min(current_max_vector)
		self.voltage_max = min(voltage_max_vector)

		self.diff_current = diff_current
		self.gauss_per_amp_vector = gauss_per_amp_vector

		self.current_min = current_min

		self.ramp_down_enabled = ramp_down
		self.ramp_sleep = 0.1
		self.ramp_current_step = 50.e-3

		self.debug_lock = Lock()

		self.devices = {}
		self.axis = {1:'x-axis',2:'y-axis',3:'z-axis'}
		self.channel = {'x-axis':1,'x':1,'y-axis':2,'y':2,'z-axis':3,'z':3}

		for devicename,ch in self.devicesX:
			self.devices.setdefault(devicename,[]).append(("x-axis",ch))
		for devicename,ch in self.devicesY:
			self.devices.setdefault(devicename,[]).append(("y-axis",ch))		
		for devicename,ch in self.devicesZ:
			self.devices.setdefault(devicename,[]).append(("z-axis",ch))

		self.instances = dict()
		self.locks  =dict()
		for devicename in self.devices.keys():
			self.instances[devicename] = hameg.HMP2030(device=devicename,voltage_max=self.voltage_max, current_max=self.current_max, fuse_voltage_max=fuse_voltage_max, fuse_current_max=fuse_current_max)
			self.locks[devicename] = Lock() 
		
		self.relais = USBRelais.USBRelais(relais_serial_port)		
		
		self.set_max_currents()
		self.set_max_voltages()

		if reset:

			self.set_all_currents(0.,0.,0.) #A
			self.set_all_voltages(*self.voltage_max_vec) #V proper voltage has to be set\
			self.emergency_stop()
			

			#start polarity changer
			self.relais.reset()
			self.relais.setPort([1,0,1,0,1,0,0,0])

	
		if not self.relais.NOP():
			raise RuntimeError('NOP failed on relais card. Shut down the field, and try ONCE with reset=True passed to __init__. All your field settings will be lost.')
	
		bit = self.relais.getPort()
		if bit[0] == bit[1] or bit[2] == bit[3] or bit[4] == bit[5]: 
			raise RuntimeError('Bad port state on relais card. Shut down the field, and try ONCE with reset=True passed to __init__. All your field settings will be lost.')            
	

		self.update_all()


#on_rait_change(max_voltage_vec)
#.....---""----current max vec...
	def _lock(self, device):
		while self._locked(device):
			time.sleep(0.05)
		self.locks[device].acquire()

	def _locked(self,device):
		if self.locks[device].locked():
			return True
		else:
			return False

	def _unlock(self,device):
		self.locks[device].release()

	def _set_device_current_unchecked(self,device,channel,target_current,timeout=10):
		if not self.stop:
			self._lock(device)
			current = target_current
			instance = self.instances[device]
			turn_off = False
			if target_current < self.current_min/2.:
				current = self.current_min
				turn_off = True
			instance.set_current(current,channel)
			self._unlock(device)
			time.sleep(0.1)
			if turn_off:
				self._device_stop_single(device,channel)
			else:	
				self._device_run_single(device,channel)

	def _check_device_current(self, device, channel, current, timeout=10):
		start_time = time.time()
		while  abs(start_time-time.time()) <= timeout:
			if self.stop:
				return False
			if abs(self._get_device_current(device,channel) - current) <= self.diff_current:
				break
			time.sleep(0.1)
		else:
			self.stop_all()
			print "Current didn't settle to" ,current, "A in channel",channel,". Shutting down..."
			raise RuntimeError("Current didn't settle. Shutting down...")
		return True


	def _set_device_current(self, device, channel,current, timeout=10):
		if not self.stop:		
			self._set_device_current_unchecked(device,channel,current,timeout)
			t = Thread(name="_set_device_current",target=self._check_device_current,args=(device,channel,current, timeout))
			t.start()
			t.join(timeout)
			if t.isAlive():
				print "Warning: couldn't ramp current nicely!"

	def _set_device_voltage(self,device,channel,voltage):
		instance = self.instances[device]
		instance.set_voltage(voltage,channel)

	def _get_device_current(self, device, channel):
		self._lock(device)
		current = self.instances[device].get_current(channel)
		self._unlock(device)
		return current


	def _device_run_single(self, device, channel):
		if not self.stop:
			self._lock(device)
			self.instances[device].run(channel)
			self._unlock(device)

	def _device_run_all(self, device):
		for axis, channel in self.devices[device]:
			self._lock(device)
			self._device_run_single(device,channel)
			self._unlock(device)

	def _device_stop_single(self, device, channel):
		self._lock(device)
		self.instances[device].stop(channel)
		self._unlock(device)

	def _device_stop_axis(self, device,axis):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				self._device_stop_single(device,channel)

	def _device_run_axis(self,device,axis):
		if not self.stop:
			for device_axis,channel in self.devices.get(device):
				if device_axis == axis:
					self._device_run_single(device,channel)		


	def _device_stop_all(self, device):
		for axis, channel in self.devices.get(device):
			self._device_stop_single(device,channel)

	def run_all(self):
		if not self.stop:
			for device in self.devices:
				self._device_run_all(device)

	def stop_all(self):
		for device in self.devices:
			self._device_stop_all(device)

	def run_axis(self, axis):
		if not self.stop:
			t_list = []
			for device in self.devices.keys():
				t_list.append(Thread(name=device,target=self._device_run_axis,args=(device,axis)))
			for thread in t_list:
				thread.start()



	def stop_axis(self, axis):
		t_list = []
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._device_stop_axis,args=(device,axis,)))
		for thread in t_list:
			thread.start()
		

	def _set_device_axis_max_current(self,device,axis,max_current):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				self._set_device_max_current(device,channel,max_current)		

	def _set_device_max_current(self,device,channel,max_current):
		self.instances[device].set_max_current(channel,max_current)

	def _set_device_axis_max_voltage(self,device,axis,max_voltage):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				self._set_device_max_voltage(device,channel,max_voltage)		

	def _set_device_max_voltage(self,device,channel,max_voltage):
		self.instances[device].set_max_voltage(channel,max_voltage)

	def _set_device_all_currents(self, device, currents):
		for channel, current in enumerate(currents,start=1):
			self._set_device_current_unchecked(device, channel, current)
		for channel, current in enumerate(currents, start=1):
			self._check_device_current(device,channel,current)

	def _set_device_axis_current(self, device, axis, current):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				self._set_device_current_unchecked(device,channel,current)

	def _check_device_axis_current(self,device,axis,current):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				self._check_device_current(device,channel,current)

	def _get_device_axis_current(self, device, axis, queue):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				queue.put(self._get_device_current(device,channel))

	def _set_device_axis_voltage(self, device, axis, voltage):
		for device_axis,channel in self.devices.get(device):
			if device_axis == axis:
				self._set_device_voltage(device,channel,voltage)


	def _set_axis_current(self, axis, target_current):
		if self.axis_current[self.channel[axis]-1] == target_current:
			return
		if self.ramp_down_enabled:
			current = self.axis_current[self.channel[axis]-1]
			no_steps = abs(target_current-current)/self.ramp_current_step
			ramp_currents = np.linspace(current, target_current,no_steps,endpoint=False)
			ramp_currents = ramp_currents[1:]
			
			for i, current in enumerate(ramp_currents):
				if self.stop:
					return
				self._set_axis_current_unchecked(axis, current)
				self._check_axis_current(axis,current)
				time.sleep(self.ramp_sleep)

		if not self.stop:
			self._set_axis_current_unchecked(axis, target_current)
			self._check_axis_current(axis,target_current)
			self.axis_current[self.channel[axis]-1] = target_current


	def _set_axis_current_unchecked(self, axis, current):
		if self.stop:
			return
		t_list = []
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._set_device_axis_current,args=(device,axis,current,)))
		for thread in t_list:
			thread.start()	
		for thread in t_list:
			thread.join()

	def _check_axis_current(self, axis,current):
		if self.stop:
			return
		t_list = []
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._check_device_axis_current,args=(device,axis,current,)))
		for thread in t_list:
			thread.start()		
		for thread in t_list:
			thread.join()

	def _get_axis_current(self, axis,queue):
		t_list = []
		q = Queue()
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._get_device_axis_current,args=(device,axis,q)))
		for thread in t_list:
			thread.start()
		for thread in t_list:
			thread.join()
		result =[]
		while not q.empty():
			result.append(q.get())

		if len(result) == 0:
			axis_current = 0
		else:
			axis_current = sum(result)/float(len(result))
		queue.put(axis_current)
		return axis, axis_current
		

	def _set_axis_voltage(self, axis, voltage):
		if self.stop:
			return
		t_list = []
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._set_device_axis_voltage,args=(device,axis,voltage,)))
		for thread in t_list:
			if self.stop:
				return			
			thread.start()

	def _set_axis_max_current(self, axis, max_current):
		t_list = []
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._set_device_axis_max_current,args=(device,axis,max_current,)))
		for thread in t_list:
			thread.start()	
		for thread in t_list:
			thread.join()		

	def _set_axis_max_voltage(self, axis, max_voltage):
		t_list = []
		for device in self.devices.keys():
			t_list.append(Thread(name=device,target=self._set_device_axis_max_voltage,args=(device,axis,max_voltage,)))
		for thread in t_list:
			thread.start()		
		for thread in t_list:
			thread.join()		


	def _get_polarity(self,axis):
		"""returns the polarity p of a given channel ch.
				The polarity is 1 for (+ -> 1, - -> 2 | [1,0,1,0,1,0,0,0])
				and -1 for (+ -> 2, - -> 1 | [0,1,0,1,0,1,0,0])."""
		return self.polarity[self.channel[axis]-1]

	def _ask_polarity(self,axis):
		"""returns the polarity p of a given channel ch.
			The polarity is 1 for (+ -> 1, - -> 2 | [1,0,1,0,1,0,0,0])
			and -1 for (+ -> 2, - -> 1 | [0,1,0,1,0,1,0,0])."""
		self.relais_lock.acquire()
		r = self.relais.getPort()
		self.relais_lock.release()
		ch = self.channel[axis]

		if ch not in [1,2,3]:
			raise ValueError('Wrong channel number. Chose 1, 2 or 3.')
		elif r[2*ch-2]==r[2*ch-1]:
			raise ValueError('Undefined polarity.')
		elif r[2*ch-2]==1 and r[2*ch-1]==0:
			return 1
		elif r[2*ch-2]==0 and r[2*ch-1]==1:
			return -1
		else:
			raise ValueError("Couldn't get the polarity.") 

	def _set_polarity(self,axis,p):
		"""sets the polarity p of a given channel ch.
			It ramps down the current and changes the polarity.-
			The output is turned off when the polarity is switched"""
		ch = self.channel[axis]
		r = self._get_polarity(axis)

		if ch not in [1,2,3]:
			raise ValueError('Wrong channel number. Chose 1, 2 or 3.')
		elif p not in [-1,1]:
			raise ValueError('Undefined polarity.')                
		elif r != p:
			#ramp down current
			self._set_axis_current(axis,self.current_min)
			time.sleep(0.1)            
			self.stop_axis(axis)
			time.sleep(0.1)
			x = [0,0,0,0,0,0,0,0]
			x[2*ch-2] = 1
			x[2*ch-1] = 1
			self.relais_lock.acquire()
			self.relais.Toggle(x)
			self.relais_lock.release()
			#control
			time.sleep(0.1)
			s = self._ask_polarity(axis)

			if s != p:
				raise ValueError("cannot change polarity")
			self.polarity[ch-1] = p

	def set_current(self, axis, current):
		if self.stop_lock.locked():
			return
		self.stop_lock.acquire()
		self.stop = False
		self.stop_lock.release()
		#change of polarity p
		polarity = np.sign(current)
		if polarity == 0:
			polarity = 1
		self._set_polarity(axis, polarity)
		t = Thread(name=axis, target=self._set_axis_current,args=(axis,abs(current/1000.)))
		t.start()

	def set_voltage(self, axis, voltage):
		self._set_axis_voltage(axis,voltage)		

	def set_all_currents(self, c1,c2,c3):
		t_list = []
		currents = [c1,c2,c3]
		for axis,current in zip(['x-axis','y-axis','z-axis'],currents):
			t_list.append(Thread(name=axis,target=self.set_current,args=(axis,current,)))
		for thread in t_list:
			thread.start()

	def set_all_voltages(self, v1,v2,v3):
		t_list = []
		voltages = [v1,v2,v3]
		for axis,voltage in zip(['x-axis','y-axis','z-axis'],voltages):
			t_list.append(Thread(name=axis,target=self.set_voltage,args=(axis,voltage,)))
		for thread in t_list:
			thread.start()
		


	def get_all_currents(self):
		t_list = []
		q = Queue()
		for axis in ['x-axis','y-axis','z-axis']:
			t_list.append(Thread(name=axis,target=self._get_axis_current,args=(axis,q)))
		for thread in t_list:
			thread.start()
		for thread in t_list:
			thread.join()
		currents = []
		while not q.empty():
			currents.append(q.get())
		#Todo: sort by axis... (currents[i][0]=axis, currents[i][1]=currents)
		return currents

	def set_max_currents(self):
		for i,axis in self.axis.iteritems():
			self._set_axis_max_current(axis,self.current_max_vec[self.channel[axis]-1])

	def set_max_voltages(self):
		for i,axis in self.axis.iteritems():
			self._set_axis_max_voltage(axis,self.voltage_max_vec[self.channel[axis]-1])

		


	def save_stop(self):
		self.stop_lock.acquire()
		self.stop = True
		self.stop_lock.release()
		print "Shutting down current"
		self.set_all_currents(0.,0.,0.)
		time.sleep(0.3)
		print "Turning channels off."
		self.stop_all()

	def emergency_stop(self):
		self.stop_lock.acquire()
		self.stop = True
		self.stop_all()
		time.sleep(0.5)
		self.stop_lock.release()

	def off(self):
		self.save_stop()
		self.relais.setPort([0,0,0,0,0,0,0,0])
		for device in self.instances:
			device.close()

	def set_field(self,bx,by,bz):
		self.set_field_cartesian(bx,by,bz)


	#functions to control the b field in 3D
	def field_to_current(self, field):
		"""converts a b-field ([x,y,z]) to values of electrical current at all coils ([curr1,curr2,curr3])"""
		return np.asarray(self.gauss_per_amp_vector)*np.asarray(field)

	def current_to_field(self, current):
		"""converts the electrical current from all coils ([curr1,curr2,curr3]) to a b-field ([x,y,z])"""
		return np.asarray(self.gauss_per_amp_vector)*np.asarray(current)

	def set_field_cartesian(self, bx, by, bz):
		"""applies a b field in an arbitrary direction, which is specified via b1, b2 and b3 in crystal coordinates"""
		self.set_all_currents(*self.field_to_current([bx,by,bz]))

	def get_field_cartesian(self):
		"""gives the applied field in cartesian crystal coordinates"""
		return self.current_to_field(self.get_all_currents())

	def set_field_spherical(self, b, theta, phi, unit='deg'):
		"""applies a b field in an arbitrary direction, which is specified via theta and phi"""
		self.set_field_cartesian(*spherical_to_cartesian((b,theta,phi), unit=unit))

	def get_field_spherical(self, unit='deg'):
		"""gives the applied field in spherical crystal coordinates"""
		return cartesian_to_spherical(self.get_field_cartesian(), unit=unit)
		#return [round(b,3),round(theta,2),round(phi,2)]



	#Gui to control the magnetic field
	get_current_1 = Float(value=0.0, desc='actual current of first coil [A]', label='I_1 [A]')
	get_current_2 = Float(value=0.0, desc='actual current of second coil [A]', label='I_2 [A]')
	get_current_3 = Float(value=0.0, desc='actual current of third coil [A]', label='I_3 [A]')
	get_bx = Float(value=0.0, desc='actual magnitude of the x-component [G]', label='b_x [G]')
	get_by = Float(value=0.0, desc='actual magnitude of the y-component [G]', label='b_y [G]')
	get_bz = Float(value=0.0, desc='actual magnitude of the z-component [G]', label='b_z [G]')
	get_b = Float(value=0.0, desc='actual magnitude of the b-field [G]', label='|B| [G]')
	get_theta = Float(value=90.0, desc='actual theta angle of the b-field vector [deg]', label='theta [deg]')
	get_phi = Float(value=0.0, desc='actual phi angle of the b-field vector [deg]', label='phi [deg]')

	set_bx = Range(low=-40.0, high=40.0, value=0.0, desc='b_x component of the b-field in crystal coordinates [G]', label='b_x [G]', mode='text', auto_set=False, enter_set=True)
	set_by = Range(low=-40.0, high=40.0, value=0.0, desc='b_y component of the b-field in crystal coordinates [G]', label='b_y [G]', mode='text', auto_set=False, enter_set=True)
	set_bz = Range(low=-40.0, high=40.0, value=0.0, desc='b_z component of the b-field in crystal coordinates [G]', label='b_z [G]', mode='text', auto_set=False, enter_set=True)
	set_b = Range(low=0.0, high=70.0, value=0.0, desc='Magnitude of the b-field [G]', label='|B| [G]', mode='text', auto_set=False, enter_set=True)
	set_theta = Range(low=0.0, high=180.0, value=90.0, desc='theta angle of the b-field vector [deg]', label='theta [deg]', mode='text', auto_set=False, enter_set=True)
	set_phi = Range(low=-180.0, high=180.0, value=0.0, desc='phi angle of the b-field vector [deg]', label='phi [deg]', mode='text', auto_set=False, enter_set=True)
	
	set_currents_button = Button(label='Set I1,I2,I3', desc='Sets the coil currents.')
	set_field_button_cartesian = Button(label='Set B(bx,by,bz)', desc='Sets the b-field to the desired value in cartesian coordinates.')
	set_field_button_spherical = Button(label='Set B(|B|,theta, phi)', desc='Sets the b-field to the desired value in spherical coordinates.')

	save_stop_button = Button(label='Stop', desc='Safely stops the b-field.')
	emerg_stop_button = Button(label='Emerg-Stop', desc='Immediately stops the b-field. Without ramping down the current.')
	update_button = Button(label='Update', desc='readout current coil states and update magnetic field values')
	#off_button = Button(label='Off', desc='Turns the b-field off and closes the connection.')
	#calibration_button = Button(label='Calibration', desc='Opens the calibration window.')
	
	def update_all(self):
		currents = self.get_all_currents()
		cartesian = self.current_to_field(currents)
		spherical = cartesian_to_spherical(cartesian)
		self.get_current_1, self.get_current_2, self.get_current_3 = currents    
		self.get_bx, self.get_by, self.get_bz = cartesian
		self.get_b, self.get_theta, self.get_phi = spherical
	  
	def _set_currents_button_fired(self):
		self.set_all_currents(self.set_current_1, self.set_current_2, self.set_current_3)
		time.sleep(0.5)
		self.update_all()
	
	def _set_field_button_cartesian_fired(self):
		self.set_field_cartesian(self.set_bx, self.set_by, self.set_bz)
		self.update_all()
	
	def _set_field_button_spherical_fired(self):
		self.set_field_spherical(self.set_b, self.set_theta, self.set_phi)
		self.update_all()
	
	def _save_stop_button_fired(self):
		self.save_stop()
		self.get_field_cartesian()
		self.get_field_spherical()
	
	def _emerg_stop_button_fired(self):
		self.emergency_stop()
	
	#def _off_button_fired(self):
	#    self.off()
	
	def _update_button_fired(self):
		self.update_all()
	
#    def _calibration_button_fired(self):
#        from magcoil_calibration import MagCoilCalibration
#        magcoilcalib = MagCoilCalibration(mag_coil=self)
#        magcoilcalib.edit_traits()
	
	traits_view = View(VGroup(Group(
									Item('get_current_1', width=-70, style='readonly'),
									Item('get_current_2', width=-70, style='readonly'),
									Item('get_current_3', width=-70, style='readonly'),
									Item('get_bx', width=-70, style='readonly'),
									Item('get_by', width=-70, style='readonly'),
									Item('get_bz', width=-70, style='readonly'),
									#Item('get_b', width=-70, style='readonly'),
									#Item('get_theta', width=-70, style='readonly'),
									#Item('get_phi', width=-70, style='readonly'),                                    
									orientation='vertical', columns=3
									),
								HGroup(
									Item('update_button', show_label=False),
									),
								Group(
									Item('set_current_1',width=-28 ),
									Item('set_current_2',width=-28 ),
									Item('set_current_3',width=-28 ),
									Item('set_currents_button', show_label=False),
									Item('set_bx', width=-60),
									Item('set_by', width=-60),
									Item('set_bz', width=-60),
									Item('set_field_button_cartesian', show_label=False),
									Item('set_b', width=-60),
									Item('set_theta', width=-60),
									Item('set_phi', width=-60),
									Item('set_field_button_spherical', show_label=False),
									orientation='vertical', columns=4
									),
								HGroup(
									Item('save_stop_button', show_label=False),
									Item('emerg_stop_button', show_label=False),
									#Item('off_button', show_label=False),
									#Item('calibration_button', show_label=False),
									),
							),
						title='Magnetic field control', width=630, height=250, buttons=[], resizable=True
						)

	get_set_items = ['set_current_1', 'set_current_2', 'set_current_3',
					'set_bx', 'set_by', 'set_bz',
					'set_b', 'set_theta', 'set_phi',
					'__doc__']

import clr
import os

assembly_dir="C:\\Program Files (x86)\\Data Translation\\DotNet\\OLClassLib\\Framework 2.0 Assemblies\\"
assembly_name="OpenLayers.Base"

clr.AddReference(assembly_dir+assembly_name)

from OpenLayers.Base import DeviceMgr, DataFlow


dm = DeviceMgr.Get()

if dm.HardwareAvailable():
	print 'Found devices'
	for devicename in dm.GetDeviceNames():
		print devicename


device= dm.GetDevice(dm.GetDeviceNames()[0])
aiss=device.AnalogInputSubsystem(0)

aiss.DataFlow = DataFlow.SingleValue
#print aiss.DataFlow
aiss.Config()
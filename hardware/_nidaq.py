from ctypes import *

STRING = c_char_p
_stdcall_libraries = {}
_stdcall_libraries['nicaiu.dll'] = WinDLL('nicaiu.dll')
_libraries = {}
_libraries['nicaiu.dll'] = CDLL('nicaiu.dll')


int32 = c_long
TaskHandle = c_void_p
DAQmxLoadTask = _stdcall_libraries['nicaiu.dll'].DAQmxLoadTask
DAQmxLoadTask.restype = int32
DAQmxLoadTask.argtypes = [STRING, POINTER(TaskHandle)]
DAQmxLoadTask.__doc__ = \
"""int32 DAQmxLoadTask(unknown * taskName, TaskHandle * taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1853"""
DAQmxCreateTask = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTask
DAQmxCreateTask.restype = int32
DAQmxCreateTask.argtypes = [STRING, POINTER(TaskHandle)]
DAQmxCreateTask.__doc__ = \
"""int32 DAQmxCreateTask(unknown * taskName, TaskHandle * taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1854"""
DAQmxAddGlobalChansToTask = _stdcall_libraries['nicaiu.dll'].DAQmxAddGlobalChansToTask
DAQmxAddGlobalChansToTask.restype = int32
DAQmxAddGlobalChansToTask.argtypes = [TaskHandle, STRING]
DAQmxAddGlobalChansToTask.__doc__ = \
"""int32 DAQmxAddGlobalChansToTask(TaskHandle taskHandle, unknown * channelNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1856"""
DAQmxStartTask = _stdcall_libraries['nicaiu.dll'].DAQmxStartTask
DAQmxStartTask.restype = int32
DAQmxStartTask.argtypes = [TaskHandle]
DAQmxStartTask.__doc__ = \
"""int32 DAQmxStartTask(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1858"""
DAQmxStopTask = _stdcall_libraries['nicaiu.dll'].DAQmxStopTask
DAQmxStopTask.restype = int32
DAQmxStopTask.argtypes = [TaskHandle]
DAQmxStopTask.__doc__ = \
"""int32 DAQmxStopTask(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1859"""
DAQmxClearTask = _stdcall_libraries['nicaiu.dll'].DAQmxClearTask
DAQmxClearTask.restype = int32
DAQmxClearTask.argtypes = [TaskHandle]
DAQmxClearTask.__doc__ = \
"""int32 DAQmxClearTask(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1861"""
float64 = c_double
DAQmxWaitUntilTaskDone = _stdcall_libraries['nicaiu.dll'].DAQmxWaitUntilTaskDone
DAQmxWaitUntilTaskDone.restype = int32
DAQmxWaitUntilTaskDone.argtypes = [TaskHandle, float64]
DAQmxWaitUntilTaskDone.__doc__ = \
"""int32 DAQmxWaitUntilTaskDone(TaskHandle taskHandle, float64 timeToWait)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1863"""
uInt32 = c_ulong
bool32 = uInt32
DAQmxIsTaskDone = _stdcall_libraries['nicaiu.dll'].DAQmxIsTaskDone
DAQmxIsTaskDone.restype = int32
DAQmxIsTaskDone.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxIsTaskDone.__doc__ = \
"""int32 DAQmxIsTaskDone(TaskHandle taskHandle, bool32 * isTaskDone)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1864"""
DAQmxTaskControl = _stdcall_libraries['nicaiu.dll'].DAQmxTaskControl
DAQmxTaskControl.restype = int32
DAQmxTaskControl.argtypes = [TaskHandle, int32]
DAQmxTaskControl.__doc__ = \
"""int32 DAQmxTaskControl(TaskHandle taskHandle, int32 action)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1866"""
DAQmxGetNthTaskChannel = _stdcall_libraries['nicaiu.dll'].DAQmxGetNthTaskChannel
DAQmxGetNthTaskChannel.restype = int32
DAQmxGetNthTaskChannel.argtypes = [TaskHandle, uInt32, STRING, int32]
DAQmxGetNthTaskChannel.__doc__ = \
"""int32 DAQmxGetNthTaskChannel(TaskHandle taskHandle, uInt32 index, char * buffer, int32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1868"""
DAQmxGetNthTaskDevice = _stdcall_libraries['nicaiu.dll'].DAQmxGetNthTaskDevice
DAQmxGetNthTaskDevice.restype = int32
DAQmxGetNthTaskDevice.argtypes = [TaskHandle, uInt32, STRING, int32]
DAQmxGetNthTaskDevice.__doc__ = \
"""int32 DAQmxGetNthTaskDevice(TaskHandle taskHandle, uInt32 index, char * buffer, int32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1870"""
DAQmxGetTaskAttribute = _libraries['nicaiu.dll'].DAQmxGetTaskAttribute
DAQmxGetTaskAttribute.restype = int32
DAQmxGetTaskAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetTaskAttribute.__doc__ = \
"""int32 DAQmxGetTaskAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1872"""
DAQmxEveryNSamplesEventCallbackPtr = CFUNCTYPE(int32, TaskHandle, int32, uInt32, c_void_p)
DAQmxRegisterEveryNSamplesEvent = _stdcall_libraries['nicaiu.dll'].DAQmxRegisterEveryNSamplesEvent
DAQmxRegisterEveryNSamplesEvent.restype = int32
DAQmxRegisterEveryNSamplesEvent.argtypes = [TaskHandle, int32, uInt32, uInt32, DAQmxEveryNSamplesEventCallbackPtr, c_void_p]
DAQmxRegisterEveryNSamplesEvent.__doc__ = \
"""int32 DAQmxRegisterEveryNSamplesEvent(TaskHandle task, int32 everyNsamplesEventType, uInt32 nSamples, uInt32 options, DAQmxEveryNSamplesEventCallbackPtr callbackFunction, void * callbackData)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1878"""
DAQmxDoneEventCallbackPtr = CFUNCTYPE(int32, TaskHandle, int32, c_void_p)
DAQmxRegisterDoneEvent = _stdcall_libraries['nicaiu.dll'].DAQmxRegisterDoneEvent
DAQmxRegisterDoneEvent.restype = int32
DAQmxRegisterDoneEvent.argtypes = [TaskHandle, uInt32, DAQmxDoneEventCallbackPtr, c_void_p]
DAQmxRegisterDoneEvent.__doc__ = \
"""int32 DAQmxRegisterDoneEvent(TaskHandle task, uInt32 options, DAQmxDoneEventCallbackPtr callbackFunction, void * callbackData)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1879"""
DAQmxSignalEventCallbackPtr = CFUNCTYPE(int32, TaskHandle, int32, c_void_p)
DAQmxRegisterSignalEvent = _stdcall_libraries['nicaiu.dll'].DAQmxRegisterSignalEvent
DAQmxRegisterSignalEvent.restype = int32
DAQmxRegisterSignalEvent.argtypes = [TaskHandle, int32, uInt32, DAQmxSignalEventCallbackPtr, c_void_p]
DAQmxRegisterSignalEvent.__doc__ = \
"""int32 DAQmxRegisterSignalEvent(TaskHandle task, int32 signalID, uInt32 options, DAQmxSignalEventCallbackPtr callbackFunction, void * callbackData)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1880"""
DAQmxCreateAIVoltageChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIVoltageChan
DAQmxCreateAIVoltageChan.restype = int32
DAQmxCreateAIVoltageChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, STRING]
DAQmxCreateAIVoltageChan.__doc__ = \
"""int32 DAQmxCreateAIVoltageChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1887"""
DAQmxCreateAICurrentChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAICurrentChan
DAQmxCreateAICurrentChan.restype = int32
DAQmxCreateAICurrentChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, int32, float64, STRING]
DAQmxCreateAICurrentChan.__doc__ = \
"""int32 DAQmxCreateAICurrentChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 shuntResistorLoc, float64 extShuntResistorVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1888"""
DAQmxCreateAIVoltageRMSChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIVoltageRMSChan
DAQmxCreateAIVoltageRMSChan.restype = int32
DAQmxCreateAIVoltageRMSChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, STRING]
DAQmxCreateAIVoltageRMSChan.__doc__ = \
"""int32 DAQmxCreateAIVoltageRMSChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1889"""
DAQmxCreateAICurrentRMSChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAICurrentRMSChan
DAQmxCreateAICurrentRMSChan.restype = int32
DAQmxCreateAICurrentRMSChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, int32, float64, STRING]
DAQmxCreateAICurrentRMSChan.__doc__ = \
"""int32 DAQmxCreateAICurrentRMSChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 shuntResistorLoc, float64 extShuntResistorVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1890"""
DAQmxCreateAIThrmcplChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIThrmcplChan
DAQmxCreateAIThrmcplChan.restype = int32
DAQmxCreateAIThrmcplChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, STRING]
DAQmxCreateAIThrmcplChan.__doc__ = \
"""int32 DAQmxCreateAIThrmcplChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 thermocoupleType, int32 cjcSource, float64 cjcVal, unknown * cjcChannel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1891"""
DAQmxCreateAIRTDChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIRTDChan
DAQmxCreateAIRTDChan.restype = int32
DAQmxCreateAIRTDChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, int32, float64, float64]
DAQmxCreateAIRTDChan.__doc__ = \
"""int32 DAQmxCreateAIRTDChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 rtdType, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal, float64 r0)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1892"""
DAQmxCreateAIThrmstrChanIex = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIThrmstrChanIex
DAQmxCreateAIThrmstrChanIex.restype = int32
DAQmxCreateAIThrmstrChanIex.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, float64, float64, float64]
DAQmxCreateAIThrmstrChanIex.__doc__ = \
"""int32 DAQmxCreateAIThrmstrChanIex(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal, float64 a, float64 b, float64 c)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1893"""
DAQmxCreateAIThrmstrChanVex = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIThrmstrChanVex
DAQmxCreateAIThrmstrChanVex.restype = int32
DAQmxCreateAIThrmstrChanVex.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, float64, float64, float64, float64]
DAQmxCreateAIThrmstrChanVex.__doc__ = \
"""int32 DAQmxCreateAIThrmstrChanVex(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 a, float64 b, float64 c, float64 r1)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1894"""
DAQmxCreateAIFreqVoltageChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIFreqVoltageChan
DAQmxCreateAIFreqVoltageChan.restype = int32
DAQmxCreateAIFreqVoltageChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, float64, float64, STRING]
DAQmxCreateAIFreqVoltageChan.__doc__ = \
"""int32 DAQmxCreateAIFreqVoltageChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, float64 thresholdLevel, float64 hysteresis, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1895"""
DAQmxCreateAIResistanceChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIResistanceChan
DAQmxCreateAIResistanceChan.restype = int32
DAQmxCreateAIResistanceChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, STRING]
DAQmxCreateAIResistanceChan.__doc__ = \
"""int32 DAQmxCreateAIResistanceChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1896"""
DAQmxCreateAIStrainGageChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIStrainGageChan
DAQmxCreateAIStrainGageChan.restype = int32
DAQmxCreateAIStrainGageChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, float64, float64, float64, float64, float64, STRING]
DAQmxCreateAIStrainGageChan.__doc__ = \
"""int32 DAQmxCreateAIStrainGageChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 strainConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 gageFactor, float64 initialBridgeVoltage, float64 nominalGageResistance, float64 poissonRatio, float64 leadWireResistance, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1897"""
DAQmxCreateAIVoltageChanWithExcit = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIVoltageChanWithExcit
DAQmxCreateAIVoltageChanWithExcit.restype = int32
DAQmxCreateAIVoltageChanWithExcit.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, int32, int32, float64, bool32, STRING]
DAQmxCreateAIVoltageChanWithExcit.__doc__ = \
"""int32 DAQmxCreateAIVoltageChanWithExcit(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 bridgeConfig, int32 voltageExcitSource, float64 voltageExcitVal, bool32 useExcitForScaling, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1898"""
DAQmxCreateAITempBuiltInSensorChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAITempBuiltInSensorChan
DAQmxCreateAITempBuiltInSensorChan.restype = int32
DAQmxCreateAITempBuiltInSensorChan.argtypes = [TaskHandle, STRING, STRING, int32]
DAQmxCreateAITempBuiltInSensorChan.__doc__ = \
"""int32 DAQmxCreateAITempBuiltInSensorChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 units)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1899"""
DAQmxCreateAIAccelChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIAccelChan
DAQmxCreateAIAccelChan.restype = int32
DAQmxCreateAIAccelChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, float64, int32, int32, float64, STRING]
DAQmxCreateAIAccelChan.__doc__ = \
"""int32 DAQmxCreateAIAccelChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 currentExcitSource, float64 currentExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1900"""
DAQmxCreateAIMicrophoneChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIMicrophoneChan
DAQmxCreateAIMicrophoneChan.restype = int32
DAQmxCreateAIMicrophoneChan.argtypes = [TaskHandle, STRING, STRING, int32, int32, float64, float64, int32, float64, STRING]
DAQmxCreateAIMicrophoneChan.__doc__ = \
"""int32 DAQmxCreateAIMicrophoneChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, int32 units, float64 micSensitivity, float64 maxSndPressLevel, int32 currentExcitSource, float64 currentExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1902"""
DAQmxCreateAIPosLVDTChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIPosLVDTChan
DAQmxCreateAIPosLVDTChan.restype = int32
DAQmxCreateAIPosLVDTChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, float64, int32, int32, float64, float64, int32, STRING]
DAQmxCreateAIPosLVDTChan.__doc__ = \
"""int32 DAQmxCreateAIPosLVDTChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1903"""
DAQmxCreateAIPosRVDTChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIPosRVDTChan
DAQmxCreateAIPosRVDTChan.restype = int32
DAQmxCreateAIPosRVDTChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, float64, int32, int32, float64, float64, int32, STRING]
DAQmxCreateAIPosRVDTChan.__doc__ = \
"""int32 DAQmxCreateAIPosRVDTChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1904"""
DAQmxCreateAIPosEddyCurrProxProbeChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIPosEddyCurrProxProbeChan
DAQmxCreateAIPosEddyCurrProxProbeChan.restype = int32
DAQmxCreateAIPosEddyCurrProxProbeChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, float64, int32, STRING]
DAQmxCreateAIPosEddyCurrProxProbeChan.__doc__ = \
"""int32 DAQmxCreateAIPosEddyCurrProxProbeChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1905"""
DAQmxCreateAIDeviceTempChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAIDeviceTempChan
DAQmxCreateAIDeviceTempChan.restype = int32
DAQmxCreateAIDeviceTempChan.argtypes = [TaskHandle, STRING, STRING, int32]
DAQmxCreateAIDeviceTempChan.__doc__ = \
"""int32 DAQmxCreateAIDeviceTempChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 units)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1907"""
DAQmxCreateTEDSAIVoltageChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIVoltageChan
DAQmxCreateTEDSAIVoltageChan.restype = int32
DAQmxCreateTEDSAIVoltageChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, STRING]
DAQmxCreateTEDSAIVoltageChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIVoltageChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1909"""
DAQmxCreateTEDSAICurrentChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAICurrentChan
DAQmxCreateTEDSAICurrentChan.restype = int32
DAQmxCreateTEDSAICurrentChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, int32, float64, STRING]
DAQmxCreateTEDSAICurrentChan.__doc__ = \
"""int32 DAQmxCreateTEDSAICurrentChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 shuntResistorLoc, float64 extShuntResistorVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1910"""
DAQmxCreateTEDSAIThrmcplChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIThrmcplChan
DAQmxCreateTEDSAIThrmcplChan.restype = int32
DAQmxCreateTEDSAIThrmcplChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, float64, STRING]
DAQmxCreateTEDSAIThrmcplChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIThrmcplChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 cjcSource, float64 cjcVal, unknown * cjcChannel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1911"""
DAQmxCreateTEDSAIRTDChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIRTDChan
DAQmxCreateTEDSAIRTDChan.restype = int32
DAQmxCreateTEDSAIRTDChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64]
DAQmxCreateTEDSAIRTDChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIRTDChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1912"""
DAQmxCreateTEDSAIThrmstrChanIex = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIThrmstrChanIex
DAQmxCreateTEDSAIThrmstrChanIex.restype = int32
DAQmxCreateTEDSAIThrmstrChanIex.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64]
DAQmxCreateTEDSAIThrmstrChanIex.__doc__ = \
"""int32 DAQmxCreateTEDSAIThrmstrChanIex(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1913"""
DAQmxCreateTEDSAIThrmstrChanVex = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIThrmstrChanVex
DAQmxCreateTEDSAIThrmstrChanVex.restype = int32
DAQmxCreateTEDSAIThrmstrChanVex.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, float64]
DAQmxCreateTEDSAIThrmstrChanVex.__doc__ = \
"""int32 DAQmxCreateTEDSAIThrmstrChanVex(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 r1)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1914"""
DAQmxCreateTEDSAIResistanceChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIResistanceChan
DAQmxCreateTEDSAIResistanceChan.restype = int32
DAQmxCreateTEDSAIResistanceChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, STRING]
DAQmxCreateTEDSAIResistanceChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIResistanceChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1915"""
DAQmxCreateTEDSAIStrainGageChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIStrainGageChan
DAQmxCreateTEDSAIStrainGageChan.restype = int32
DAQmxCreateTEDSAIStrainGageChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, float64, float64, float64, STRING]
DAQmxCreateTEDSAIStrainGageChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIStrainGageChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, float64 initialBridgeVoltage, float64 leadWireResistance, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1916"""
DAQmxCreateTEDSAIVoltageChanWithExcit = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIVoltageChanWithExcit
DAQmxCreateTEDSAIVoltageChanWithExcit.restype = int32
DAQmxCreateTEDSAIVoltageChanWithExcit.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, int32, float64, STRING]
DAQmxCreateTEDSAIVoltageChanWithExcit.__doc__ = \
"""int32 DAQmxCreateTEDSAIVoltageChanWithExcit(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1917"""
DAQmxCreateTEDSAIAccelChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIAccelChan
DAQmxCreateTEDSAIAccelChan.restype = int32
DAQmxCreateTEDSAIAccelChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, int32, int32, float64, STRING]
DAQmxCreateTEDSAIAccelChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIAccelChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 currentExcitSource, float64 currentExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1918"""
DAQmxCreateTEDSAIMicrophoneChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIMicrophoneChan
DAQmxCreateTEDSAIMicrophoneChan.restype = int32
DAQmxCreateTEDSAIMicrophoneChan.argtypes = [TaskHandle, STRING, STRING, int32, int32, float64, int32, float64, STRING]
DAQmxCreateTEDSAIMicrophoneChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIMicrophoneChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 terminalConfig, int32 units, float64 maxSndPressLevel, int32 currentExcitSource, float64 currentExcitVal, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1920"""
DAQmxCreateTEDSAIPosLVDTChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIPosLVDTChan
DAQmxCreateTEDSAIPosLVDTChan.restype = int32
DAQmxCreateTEDSAIPosLVDTChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, float64, float64, int32, STRING]
DAQmxCreateTEDSAIPosLVDTChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIPosLVDTChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1921"""
DAQmxCreateTEDSAIPosRVDTChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTEDSAIPosRVDTChan
DAQmxCreateTEDSAIPosRVDTChan.restype = int32
DAQmxCreateTEDSAIPosRVDTChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, float64, float64, int32, STRING]
DAQmxCreateTEDSAIPosRVDTChan.__doc__ = \
"""int32 DAQmxCreateTEDSAIPosRVDTChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1922"""
DAQmxCreateAOVoltageChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAOVoltageChan
DAQmxCreateAOVoltageChan.restype = int32
DAQmxCreateAOVoltageChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, STRING]
DAQmxCreateAOVoltageChan.__doc__ = \
"""int32 DAQmxCreateAOVoltageChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1924"""
DAQmxCreateAOCurrentChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAOCurrentChan
DAQmxCreateAOCurrentChan.restype = int32
DAQmxCreateAOCurrentChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, STRING]
DAQmxCreateAOCurrentChan.__doc__ = \
"""int32 DAQmxCreateAOCurrentChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1925"""
DAQmxCreateAOFuncGenChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateAOFuncGenChan
DAQmxCreateAOFuncGenChan.restype = int32
DAQmxCreateAOFuncGenChan.argtypes = [TaskHandle, STRING, STRING, int32, float64, float64, float64]
DAQmxCreateAOFuncGenChan.__doc__ = \
"""int32 DAQmxCreateAOFuncGenChan(TaskHandle taskHandle, unknown * physicalChannel, unknown * nameToAssignToChannel, int32 type, float64 freq, float64 amplitude, float64 offset)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1926"""
DAQmxCreateDIChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateDIChan
DAQmxCreateDIChan.restype = int32
DAQmxCreateDIChan.argtypes = [TaskHandle, STRING, STRING, int32]
DAQmxCreateDIChan.__doc__ = \
"""int32 DAQmxCreateDIChan(TaskHandle taskHandle, unknown * lines, unknown * nameToAssignToLines, int32 lineGrouping)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1928"""
DAQmxCreateDOChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateDOChan
DAQmxCreateDOChan.restype = int32
DAQmxCreateDOChan.argtypes = [TaskHandle, STRING, STRING, int32]
DAQmxCreateDOChan.__doc__ = \
"""int32 DAQmxCreateDOChan(TaskHandle taskHandle, unknown * lines, unknown * nameToAssignToLines, int32 lineGrouping)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1930"""
DAQmxCreateCIFreqChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCIFreqChan
DAQmxCreateCIFreqChan.restype = int32
DAQmxCreateCIFreqChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, uInt32, STRING]
DAQmxCreateCIFreqChan.__doc__ = \
"""int32 DAQmxCreateCIFreqChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 edge, int32 measMethod, float64 measTime, uInt32 divisor, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1932"""
DAQmxCreateCIPeriodChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCIPeriodChan
DAQmxCreateCIPeriodChan.restype = int32
DAQmxCreateCIPeriodChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, float64, uInt32, STRING]
DAQmxCreateCIPeriodChan.__doc__ = \
"""int32 DAQmxCreateCIPeriodChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 edge, int32 measMethod, float64 measTime, uInt32 divisor, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1933"""
DAQmxCreateCICountEdgesChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCICountEdgesChan
DAQmxCreateCICountEdgesChan.restype = int32
DAQmxCreateCICountEdgesChan.argtypes = [TaskHandle, STRING, STRING, int32, uInt32, int32]
DAQmxCreateCICountEdgesChan.__doc__ = \
"""int32 DAQmxCreateCICountEdgesChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, int32 edge, uInt32 initialCount, int32 countDirection)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1934"""
DAQmxCreateCIPulseWidthChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCIPulseWidthChan
DAQmxCreateCIPulseWidthChan.restype = int32
DAQmxCreateCIPulseWidthChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, STRING]
DAQmxCreateCIPulseWidthChan.__doc__ = \
"""int32 DAQmxCreateCIPulseWidthChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 startingEdge, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1935"""
DAQmxCreateCISemiPeriodChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCISemiPeriodChan
DAQmxCreateCISemiPeriodChan.restype = int32
DAQmxCreateCISemiPeriodChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, STRING]
DAQmxCreateCISemiPeriodChan.__doc__ = \
"""int32 DAQmxCreateCISemiPeriodChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1936"""
DAQmxCreateCITwoEdgeSepChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCITwoEdgeSepChan
DAQmxCreateCITwoEdgeSepChan.restype = int32
DAQmxCreateCITwoEdgeSepChan.argtypes = [TaskHandle, STRING, STRING, float64, float64, int32, int32, int32, STRING]
DAQmxCreateCITwoEdgeSepChan.__doc__ = \
"""int32 DAQmxCreateCITwoEdgeSepChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, float64 minVal, float64 maxVal, int32 units, int32 firstEdge, int32 secondEdge, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1937"""
DAQmxCreateCILinEncoderChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCILinEncoderChan
DAQmxCreateCILinEncoderChan.restype = int32
DAQmxCreateCILinEncoderChan.argtypes = [TaskHandle, STRING, STRING, int32, bool32, float64, int32, int32, float64, float64, STRING]
DAQmxCreateCILinEncoderChan.__doc__ = \
"""int32 DAQmxCreateCILinEncoderChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, int32 decodingType, bool32 ZidxEnable, float64 ZidxVal, int32 ZidxPhase, int32 units, float64 distPerPulse, float64 initialPos, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1938"""
DAQmxCreateCIAngEncoderChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCIAngEncoderChan
DAQmxCreateCIAngEncoderChan.restype = int32
DAQmxCreateCIAngEncoderChan.argtypes = [TaskHandle, STRING, STRING, int32, bool32, float64, int32, int32, uInt32, float64, STRING]
DAQmxCreateCIAngEncoderChan.__doc__ = \
"""int32 DAQmxCreateCIAngEncoderChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, int32 decodingType, bool32 ZidxEnable, float64 ZidxVal, int32 ZidxPhase, int32 units, uInt32 pulsesPerRev, float64 initialAngle, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1939"""
DAQmxCreateCIGPSTimestampChan = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCIGPSTimestampChan
DAQmxCreateCIGPSTimestampChan.restype = int32
DAQmxCreateCIGPSTimestampChan.argtypes = [TaskHandle, STRING, STRING, int32, int32, STRING]
DAQmxCreateCIGPSTimestampChan.__doc__ = \
"""int32 DAQmxCreateCIGPSTimestampChan(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, int32 units, int32 syncMethod, unknown * customScaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1940"""
DAQmxCreateCOPulseChanFreq = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCOPulseChanFreq
DAQmxCreateCOPulseChanFreq.restype = int32
DAQmxCreateCOPulseChanFreq.argtypes = [TaskHandle, STRING, STRING, int32, int32, float64, float64, float64]
DAQmxCreateCOPulseChanFreq.__doc__ = \
"""int32 DAQmxCreateCOPulseChanFreq(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, int32 units, int32 idleState, float64 initialDelay, float64 freq, float64 dutyCycle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1942"""
DAQmxCreateCOPulseChanTime = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCOPulseChanTime
DAQmxCreateCOPulseChanTime.restype = int32
DAQmxCreateCOPulseChanTime.argtypes = [TaskHandle, STRING, STRING, int32, int32, float64, float64, float64]
DAQmxCreateCOPulseChanTime.__doc__ = \
"""int32 DAQmxCreateCOPulseChanTime(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, int32 units, int32 idleState, float64 initialDelay, float64 lowTime, float64 highTime)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1943"""
DAQmxCreateCOPulseChanTicks = _stdcall_libraries['nicaiu.dll'].DAQmxCreateCOPulseChanTicks
DAQmxCreateCOPulseChanTicks.restype = int32
DAQmxCreateCOPulseChanTicks.argtypes = [TaskHandle, STRING, STRING, STRING, int32, int32, int32, int32]
DAQmxCreateCOPulseChanTicks.__doc__ = \
"""int32 DAQmxCreateCOPulseChanTicks(TaskHandle taskHandle, unknown * counter, unknown * nameToAssignToChannel, unknown * sourceTerminal, int32 idleState, int32 initialDelay, int32 lowTicks, int32 highTicks)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1944"""
DAQmxGetAIChanCalCalDate = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalCalDate
DAQmxGetAIChanCalCalDate.restype = int32
DAQmxGetAIChanCalCalDate.argtypes = [TaskHandle, STRING, POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32)]
DAQmxGetAIChanCalCalDate.__doc__ = \
"""int32 DAQmxGetAIChanCalCalDate(TaskHandle taskHandle, unknown * channelName, uInt32 * year, uInt32 * month, uInt32 * day, uInt32 * hour, uInt32 * minute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1946"""
DAQmxSetAIChanCalCalDate = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalCalDate
DAQmxSetAIChanCalCalDate.restype = int32
DAQmxSetAIChanCalCalDate.argtypes = [TaskHandle, STRING, uInt32, uInt32, uInt32, uInt32, uInt32]
DAQmxSetAIChanCalCalDate.__doc__ = \
"""int32 DAQmxSetAIChanCalCalDate(TaskHandle taskHandle, unknown * channelName, uInt32 year, uInt32 month, uInt32 day, uInt32 hour, uInt32 minute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1947"""
DAQmxGetAIChanCalExpDate = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalExpDate
DAQmxGetAIChanCalExpDate.restype = int32
DAQmxGetAIChanCalExpDate.argtypes = [TaskHandle, STRING, POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32)]
DAQmxGetAIChanCalExpDate.__doc__ = \
"""int32 DAQmxGetAIChanCalExpDate(TaskHandle taskHandle, unknown * channelName, uInt32 * year, uInt32 * month, uInt32 * day, uInt32 * hour, uInt32 * minute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1948"""
DAQmxSetAIChanCalExpDate = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalExpDate
DAQmxSetAIChanCalExpDate.restype = int32
DAQmxSetAIChanCalExpDate.argtypes = [TaskHandle, STRING, uInt32, uInt32, uInt32, uInt32, uInt32]
DAQmxSetAIChanCalExpDate.__doc__ = \
"""int32 DAQmxSetAIChanCalExpDate(TaskHandle taskHandle, unknown * channelName, uInt32 year, uInt32 month, uInt32 day, uInt32 hour, uInt32 minute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1949"""
DAQmxGetChanAttribute = _libraries['nicaiu.dll'].DAQmxGetChanAttribute
DAQmxGetChanAttribute.restype = int32
DAQmxGetChanAttribute.argtypes = [TaskHandle, STRING, int32, c_void_p]
DAQmxGetChanAttribute.__doc__ = \
"""int32 DAQmxGetChanAttribute(TaskHandle taskHandle, unknown * channel, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1951"""
DAQmxSetChanAttribute = _libraries['nicaiu.dll'].DAQmxSetChanAttribute
DAQmxSetChanAttribute.restype = int32
DAQmxSetChanAttribute.argtypes = [TaskHandle, STRING, int32]
DAQmxSetChanAttribute.__doc__ = \
"""int32 DAQmxSetChanAttribute(TaskHandle taskHandle, unknown * channel, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1952"""
DAQmxResetChanAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetChanAttribute
DAQmxResetChanAttribute.restype = int32
DAQmxResetChanAttribute.argtypes = [TaskHandle, STRING, int32]
DAQmxResetChanAttribute.__doc__ = \
"""int32 DAQmxResetChanAttribute(TaskHandle taskHandle, unknown * channel, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1953"""
uInt64 = c_ulonglong
DAQmxCfgSampClkTiming = _stdcall_libraries['nicaiu.dll'].DAQmxCfgSampClkTiming
DAQmxCfgSampClkTiming.restype = int32
DAQmxCfgSampClkTiming.argtypes = [TaskHandle, STRING, float64, int32, int32, uInt64]
DAQmxCfgSampClkTiming.__doc__ = \
"""int32 DAQmxCfgSampClkTiming(TaskHandle taskHandle, unknown * source, float64 rate, int32 activeEdge, int32 sampleMode, uInt64 sampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1962"""
DAQmxCfgHandshakingTiming = _stdcall_libraries['nicaiu.dll'].DAQmxCfgHandshakingTiming
DAQmxCfgHandshakingTiming.restype = int32
DAQmxCfgHandshakingTiming.argtypes = [TaskHandle, int32, uInt64]
DAQmxCfgHandshakingTiming.__doc__ = \
"""int32 DAQmxCfgHandshakingTiming(TaskHandle taskHandle, int32 sampleMode, uInt64 sampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1964"""
DAQmxCfgBurstHandshakingTimingImportClock = _stdcall_libraries['nicaiu.dll'].DAQmxCfgBurstHandshakingTimingImportClock
DAQmxCfgBurstHandshakingTimingImportClock.restype = int32
DAQmxCfgBurstHandshakingTimingImportClock.argtypes = [TaskHandle, int32, uInt64, float64, STRING, int32, int32, int32]
DAQmxCfgBurstHandshakingTimingImportClock.__doc__ = \
"""int32 DAQmxCfgBurstHandshakingTimingImportClock(TaskHandle taskHandle, int32 sampleMode, uInt64 sampsPerChan, float64 sampleClkRate, unknown * sampleClkSrc, int32 sampleClkActiveEdge, int32 pauseWhen, int32 readyEventActiveLevel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1966"""
DAQmxCfgBurstHandshakingTimingExportClock = _stdcall_libraries['nicaiu.dll'].DAQmxCfgBurstHandshakingTimingExportClock
DAQmxCfgBurstHandshakingTimingExportClock.restype = int32
DAQmxCfgBurstHandshakingTimingExportClock.argtypes = [TaskHandle, int32, uInt64, float64, STRING, int32, int32, int32]
DAQmxCfgBurstHandshakingTimingExportClock.__doc__ = \
"""int32 DAQmxCfgBurstHandshakingTimingExportClock(TaskHandle taskHandle, int32 sampleMode, uInt64 sampsPerChan, float64 sampleClkRate, unknown * sampleClkOutpTerm, int32 sampleClkPulsePolarity, int32 pauseWhen, int32 readyEventActiveLevel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1968"""
DAQmxCfgChangeDetectionTiming = _stdcall_libraries['nicaiu.dll'].DAQmxCfgChangeDetectionTiming
DAQmxCfgChangeDetectionTiming.restype = int32
DAQmxCfgChangeDetectionTiming.argtypes = [TaskHandle, STRING, STRING, int32, uInt64]
DAQmxCfgChangeDetectionTiming.__doc__ = \
"""int32 DAQmxCfgChangeDetectionTiming(TaskHandle taskHandle, unknown * risingEdgeChan, unknown * fallingEdgeChan, int32 sampleMode, uInt64 sampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1969"""
DAQmxCfgImplicitTiming = _stdcall_libraries['nicaiu.dll'].DAQmxCfgImplicitTiming
DAQmxCfgImplicitTiming.restype = int32
DAQmxCfgImplicitTiming.argtypes = [TaskHandle, int32, uInt64]
DAQmxCfgImplicitTiming.__doc__ = \
"""int32 DAQmxCfgImplicitTiming(TaskHandle taskHandle, int32 sampleMode, uInt64 sampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1971"""
DAQmxCfgPipelinedSampClkTiming = _stdcall_libraries['nicaiu.dll'].DAQmxCfgPipelinedSampClkTiming
DAQmxCfgPipelinedSampClkTiming.restype = int32
DAQmxCfgPipelinedSampClkTiming.argtypes = [TaskHandle, STRING, float64, int32, int32, uInt64]
DAQmxCfgPipelinedSampClkTiming.__doc__ = \
"""int32 DAQmxCfgPipelinedSampClkTiming(TaskHandle taskHandle, unknown * source, float64 rate, int32 activeEdge, int32 sampleMode, uInt64 sampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1973"""
DAQmxGetTimingAttribute = _libraries['nicaiu.dll'].DAQmxGetTimingAttribute
DAQmxGetTimingAttribute.restype = int32
DAQmxGetTimingAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetTimingAttribute.__doc__ = \
"""int32 DAQmxGetTimingAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1975"""
DAQmxSetTimingAttribute = _libraries['nicaiu.dll'].DAQmxSetTimingAttribute
DAQmxSetTimingAttribute.restype = int32
DAQmxSetTimingAttribute.argtypes = [TaskHandle, int32]
DAQmxSetTimingAttribute.__doc__ = \
"""int32 DAQmxSetTimingAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1976"""
DAQmxResetTimingAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetTimingAttribute
DAQmxResetTimingAttribute.restype = int32
DAQmxResetTimingAttribute.argtypes = [TaskHandle, int32]
DAQmxResetTimingAttribute.__doc__ = \
"""int32 DAQmxResetTimingAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1977"""
DAQmxGetTimingAttributeEx = _libraries['nicaiu.dll'].DAQmxGetTimingAttributeEx
DAQmxGetTimingAttributeEx.restype = int32
DAQmxGetTimingAttributeEx.argtypes = [TaskHandle, STRING, int32, c_void_p]
DAQmxGetTimingAttributeEx.__doc__ = \
"""int32 DAQmxGetTimingAttributeEx(TaskHandle taskHandle, unknown * deviceNames, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1979"""
DAQmxSetTimingAttributeEx = _libraries['nicaiu.dll'].DAQmxSetTimingAttributeEx
DAQmxSetTimingAttributeEx.restype = int32
DAQmxSetTimingAttributeEx.argtypes = [TaskHandle, STRING, int32]
DAQmxSetTimingAttributeEx.__doc__ = \
"""int32 DAQmxSetTimingAttributeEx(TaskHandle taskHandle, unknown * deviceNames, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1980"""
DAQmxResetTimingAttributeEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetTimingAttributeEx
DAQmxResetTimingAttributeEx.restype = int32
DAQmxResetTimingAttributeEx.argtypes = [TaskHandle, STRING, int32]
DAQmxResetTimingAttributeEx.__doc__ = \
"""int32 DAQmxResetTimingAttributeEx(TaskHandle taskHandle, unknown * deviceNames, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1981"""
DAQmxDisableStartTrig = _stdcall_libraries['nicaiu.dll'].DAQmxDisableStartTrig
DAQmxDisableStartTrig.restype = int32
DAQmxDisableStartTrig.argtypes = [TaskHandle]
DAQmxDisableStartTrig.__doc__ = \
"""int32 DAQmxDisableStartTrig(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1989"""
DAQmxCfgDigEdgeStartTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgDigEdgeStartTrig
DAQmxCfgDigEdgeStartTrig.restype = int32
DAQmxCfgDigEdgeStartTrig.argtypes = [TaskHandle, STRING, int32]
DAQmxCfgDigEdgeStartTrig.__doc__ = \
"""int32 DAQmxCfgDigEdgeStartTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerEdge)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1990"""
DAQmxCfgAnlgEdgeStartTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgAnlgEdgeStartTrig
DAQmxCfgAnlgEdgeStartTrig.restype = int32
DAQmxCfgAnlgEdgeStartTrig.argtypes = [TaskHandle, STRING, int32, float64]
DAQmxCfgAnlgEdgeStartTrig.__doc__ = \
"""int32 DAQmxCfgAnlgEdgeStartTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerSlope, float64 triggerLevel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1991"""
DAQmxCfgAnlgWindowStartTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgAnlgWindowStartTrig
DAQmxCfgAnlgWindowStartTrig.restype = int32
DAQmxCfgAnlgWindowStartTrig.argtypes = [TaskHandle, STRING, int32, float64, float64]
DAQmxCfgAnlgWindowStartTrig.__doc__ = \
"""int32 DAQmxCfgAnlgWindowStartTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerWhen, float64 windowTop, float64 windowBottom)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1992"""
DAQmxCfgDigPatternStartTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgDigPatternStartTrig
DAQmxCfgDigPatternStartTrig.restype = int32
DAQmxCfgDigPatternStartTrig.argtypes = [TaskHandle, STRING, STRING, int32]
DAQmxCfgDigPatternStartTrig.__doc__ = \
"""int32 DAQmxCfgDigPatternStartTrig(TaskHandle taskHandle, unknown * triggerSource, unknown * triggerPattern, int32 triggerWhen)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1993"""
DAQmxDisableRefTrig = _stdcall_libraries['nicaiu.dll'].DAQmxDisableRefTrig
DAQmxDisableRefTrig.restype = int32
DAQmxDisableRefTrig.argtypes = [TaskHandle]
DAQmxDisableRefTrig.__doc__ = \
"""int32 DAQmxDisableRefTrig(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1995"""
DAQmxCfgDigEdgeRefTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgDigEdgeRefTrig
DAQmxCfgDigEdgeRefTrig.restype = int32
DAQmxCfgDigEdgeRefTrig.argtypes = [TaskHandle, STRING, int32, uInt32]
DAQmxCfgDigEdgeRefTrig.__doc__ = \
"""int32 DAQmxCfgDigEdgeRefTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerEdge, uInt32 pretriggerSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1996"""
DAQmxCfgAnlgEdgeRefTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgAnlgEdgeRefTrig
DAQmxCfgAnlgEdgeRefTrig.restype = int32
DAQmxCfgAnlgEdgeRefTrig.argtypes = [TaskHandle, STRING, int32, float64, uInt32]
DAQmxCfgAnlgEdgeRefTrig.__doc__ = \
"""int32 DAQmxCfgAnlgEdgeRefTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerSlope, float64 triggerLevel, uInt32 pretriggerSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1997"""
DAQmxCfgAnlgWindowRefTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgAnlgWindowRefTrig
DAQmxCfgAnlgWindowRefTrig.restype = int32
DAQmxCfgAnlgWindowRefTrig.argtypes = [TaskHandle, STRING, int32, float64, float64, uInt32]
DAQmxCfgAnlgWindowRefTrig.__doc__ = \
"""int32 DAQmxCfgAnlgWindowRefTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerWhen, float64 windowTop, float64 windowBottom, uInt32 pretriggerSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1998"""
DAQmxCfgDigPatternRefTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgDigPatternRefTrig
DAQmxCfgDigPatternRefTrig.restype = int32
DAQmxCfgDigPatternRefTrig.argtypes = [TaskHandle, STRING, STRING, int32, uInt32]
DAQmxCfgDigPatternRefTrig.__doc__ = \
"""int32 DAQmxCfgDigPatternRefTrig(TaskHandle taskHandle, unknown * triggerSource, unknown * triggerPattern, int32 triggerWhen, uInt32 pretriggerSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:1999"""
DAQmxDisableAdvTrig = _stdcall_libraries['nicaiu.dll'].DAQmxDisableAdvTrig
DAQmxDisableAdvTrig.restype = int32
DAQmxDisableAdvTrig.argtypes = [TaskHandle]
DAQmxDisableAdvTrig.__doc__ = \
"""int32 DAQmxDisableAdvTrig(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2001"""
DAQmxCfgDigEdgeAdvTrig = _stdcall_libraries['nicaiu.dll'].DAQmxCfgDigEdgeAdvTrig
DAQmxCfgDigEdgeAdvTrig.restype = int32
DAQmxCfgDigEdgeAdvTrig.argtypes = [TaskHandle, STRING, int32]
DAQmxCfgDigEdgeAdvTrig.__doc__ = \
"""int32 DAQmxCfgDigEdgeAdvTrig(TaskHandle taskHandle, unknown * triggerSource, int32 triggerEdge)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2002"""
DAQmxGetTrigAttribute = _libraries['nicaiu.dll'].DAQmxGetTrigAttribute
DAQmxGetTrigAttribute.restype = int32
DAQmxGetTrigAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetTrigAttribute.__doc__ = \
"""int32 DAQmxGetTrigAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2004"""
DAQmxSetTrigAttribute = _libraries['nicaiu.dll'].DAQmxSetTrigAttribute
DAQmxSetTrigAttribute.restype = int32
DAQmxSetTrigAttribute.argtypes = [TaskHandle, int32]
DAQmxSetTrigAttribute.__doc__ = \
"""int32 DAQmxSetTrigAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2005"""
DAQmxResetTrigAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetTrigAttribute
DAQmxResetTrigAttribute.restype = int32
DAQmxResetTrigAttribute.argtypes = [TaskHandle, int32]
DAQmxResetTrigAttribute.__doc__ = \
"""int32 DAQmxResetTrigAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2006"""
DAQmxSendSoftwareTrigger = _stdcall_libraries['nicaiu.dll'].DAQmxSendSoftwareTrigger
DAQmxSendSoftwareTrigger.restype = int32
DAQmxSendSoftwareTrigger.argtypes = [TaskHandle, int32]
DAQmxSendSoftwareTrigger.__doc__ = \
"""int32 DAQmxSendSoftwareTrigger(TaskHandle taskHandle, int32 triggerID)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2008"""
DAQmxReadAnalogF64 = _stdcall_libraries['nicaiu.dll'].DAQmxReadAnalogF64
DAQmxReadAnalogF64.restype = int32
DAQmxReadAnalogF64.argtypes = [TaskHandle, int32, float64, bool32, POINTER(float64), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadAnalogF64.__doc__ = \
"""int32 DAQmxReadAnalogF64(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, float64 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2016"""
DAQmxReadAnalogScalarF64 = _stdcall_libraries['nicaiu.dll'].DAQmxReadAnalogScalarF64
DAQmxReadAnalogScalarF64.restype = int32
DAQmxReadAnalogScalarF64.argtypes = [TaskHandle, float64, POINTER(float64), POINTER(bool32)]
DAQmxReadAnalogScalarF64.__doc__ = \
"""int32 DAQmxReadAnalogScalarF64(TaskHandle taskHandle, float64 timeout, float64 * value, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2017"""
int16 = c_short
DAQmxReadBinaryI16 = _stdcall_libraries['nicaiu.dll'].DAQmxReadBinaryI16
DAQmxReadBinaryI16.restype = int32
DAQmxReadBinaryI16.argtypes = [TaskHandle, int32, float64, bool32, POINTER(int16), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadBinaryI16.__doc__ = \
"""int32 DAQmxReadBinaryI16(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, int16 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2019"""
uInt16 = c_ushort
DAQmxReadBinaryU16 = _stdcall_libraries['nicaiu.dll'].DAQmxReadBinaryU16
DAQmxReadBinaryU16.restype = int32
DAQmxReadBinaryU16.argtypes = [TaskHandle, int32, float64, bool32, POINTER(uInt16), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadBinaryU16.__doc__ = \
"""int32 DAQmxReadBinaryU16(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, uInt16 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2021"""
DAQmxReadBinaryI32 = _stdcall_libraries['nicaiu.dll'].DAQmxReadBinaryI32
DAQmxReadBinaryI32.restype = int32
DAQmxReadBinaryI32.argtypes = [TaskHandle, int32, float64, bool32, POINTER(int32), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadBinaryI32.__doc__ = \
"""int32 DAQmxReadBinaryI32(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, int32 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2023"""
DAQmxReadBinaryU32 = _stdcall_libraries['nicaiu.dll'].DAQmxReadBinaryU32
DAQmxReadBinaryU32.restype = int32
DAQmxReadBinaryU32.argtypes = [TaskHandle, int32, float64, bool32, POINTER(uInt32), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadBinaryU32.__doc__ = \
"""int32 DAQmxReadBinaryU32(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, uInt32 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2025"""
uInt8 = c_ubyte
DAQmxReadDigitalU8 = _stdcall_libraries['nicaiu.dll'].DAQmxReadDigitalU8
DAQmxReadDigitalU8.restype = int32
DAQmxReadDigitalU8.argtypes = [TaskHandle, int32, float64, bool32, POINTER(uInt8), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadDigitalU8.__doc__ = \
"""int32 DAQmxReadDigitalU8(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, uInt8 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2027"""
DAQmxReadDigitalU16 = _stdcall_libraries['nicaiu.dll'].DAQmxReadDigitalU16
DAQmxReadDigitalU16.restype = int32
DAQmxReadDigitalU16.argtypes = [TaskHandle, int32, float64, bool32, POINTER(uInt16), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadDigitalU16.__doc__ = \
"""int32 DAQmxReadDigitalU16(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, uInt16 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2028"""
DAQmxReadDigitalU32 = _stdcall_libraries['nicaiu.dll'].DAQmxReadDigitalU32
DAQmxReadDigitalU32.restype = int32
DAQmxReadDigitalU32.argtypes = [TaskHandle, int32, float64, bool32, POINTER(uInt32), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadDigitalU32.__doc__ = \
"""int32 DAQmxReadDigitalU32(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, uInt32 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2029"""
DAQmxReadDigitalScalarU32 = _stdcall_libraries['nicaiu.dll'].DAQmxReadDigitalScalarU32
DAQmxReadDigitalScalarU32.restype = int32
DAQmxReadDigitalScalarU32.argtypes = [TaskHandle, float64, POINTER(uInt32), POINTER(bool32)]
DAQmxReadDigitalScalarU32.__doc__ = \
"""int32 DAQmxReadDigitalScalarU32(TaskHandle taskHandle, float64 timeout, uInt32 * value, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2030"""
DAQmxReadDigitalLines = _stdcall_libraries['nicaiu.dll'].DAQmxReadDigitalLines
DAQmxReadDigitalLines.restype = int32
DAQmxReadDigitalLines.argtypes = [TaskHandle, int32, float64, bool32, POINTER(uInt8), uInt32, POINTER(int32), POINTER(int32), POINTER(bool32)]
DAQmxReadDigitalLines.__doc__ = \
"""int32 DAQmxReadDigitalLines(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, bool32 fillMode, uInt8 * readArray, uInt32 arraySizeInBytes, int32 * sampsPerChanRead, int32 * numBytesPerSamp, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2031"""
DAQmxReadCounterF64 = _stdcall_libraries['nicaiu.dll'].DAQmxReadCounterF64
DAQmxReadCounterF64.restype = int32
DAQmxReadCounterF64.argtypes = [TaskHandle, int32, float64, POINTER(float64), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadCounterF64.__doc__ = \
"""int32 DAQmxReadCounterF64(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, float64 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2033"""
DAQmxReadCounterU32 = _stdcall_libraries['nicaiu.dll'].DAQmxReadCounterU32
DAQmxReadCounterU32.restype = int32
DAQmxReadCounterU32.argtypes = [TaskHandle, int32, float64, POINTER(uInt32), uInt32, POINTER(int32), POINTER(bool32)]
DAQmxReadCounterU32.__doc__ = \
"""int32 DAQmxReadCounterU32(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, uInt32 * readArray, uInt32 arraySizeInSamps, int32 * sampsPerChanRead, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2034"""
DAQmxReadCounterScalarF64 = _stdcall_libraries['nicaiu.dll'].DAQmxReadCounterScalarF64
DAQmxReadCounterScalarF64.restype = int32
DAQmxReadCounterScalarF64.argtypes = [TaskHandle, float64, POINTER(float64), POINTER(bool32)]
DAQmxReadCounterScalarF64.__doc__ = \
"""int32 DAQmxReadCounterScalarF64(TaskHandle taskHandle, float64 timeout, float64 * value, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2035"""
DAQmxReadCounterScalarU32 = _stdcall_libraries['nicaiu.dll'].DAQmxReadCounterScalarU32
DAQmxReadCounterScalarU32.restype = int32
DAQmxReadCounterScalarU32.argtypes = [TaskHandle, float64, POINTER(uInt32), POINTER(bool32)]
DAQmxReadCounterScalarU32.__doc__ = \
"""int32 DAQmxReadCounterScalarU32(TaskHandle taskHandle, float64 timeout, uInt32 * value, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2036"""
DAQmxReadRaw = _stdcall_libraries['nicaiu.dll'].DAQmxReadRaw
DAQmxReadRaw.restype = int32
DAQmxReadRaw.argtypes = [TaskHandle, int32, float64, c_void_p, uInt32, POINTER(int32), POINTER(int32), POINTER(bool32)]
DAQmxReadRaw.__doc__ = \
"""int32 DAQmxReadRaw(TaskHandle taskHandle, int32 numSampsPerChan, float64 timeout, void * readArray, uInt32 arraySizeInBytes, int32 * sampsRead, int32 * numBytesPerSamp, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2038"""
DAQmxGetNthTaskReadChannel = _stdcall_libraries['nicaiu.dll'].DAQmxGetNthTaskReadChannel
DAQmxGetNthTaskReadChannel.restype = int32
DAQmxGetNthTaskReadChannel.argtypes = [TaskHandle, uInt32, STRING, int32]
DAQmxGetNthTaskReadChannel.__doc__ = \
"""int32 DAQmxGetNthTaskReadChannel(TaskHandle taskHandle, uInt32 index, char * buffer, int32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2040"""
DAQmxGetReadAttribute = _libraries['nicaiu.dll'].DAQmxGetReadAttribute
DAQmxGetReadAttribute.restype = int32
DAQmxGetReadAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetReadAttribute.__doc__ = \
"""int32 DAQmxGetReadAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2042"""
DAQmxSetReadAttribute = _libraries['nicaiu.dll'].DAQmxSetReadAttribute
DAQmxSetReadAttribute.restype = int32
DAQmxSetReadAttribute.argtypes = [TaskHandle, int32]
DAQmxSetReadAttribute.__doc__ = \
"""int32 DAQmxSetReadAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2043"""
DAQmxResetReadAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadAttribute
DAQmxResetReadAttribute.restype = int32
DAQmxResetReadAttribute.argtypes = [TaskHandle, int32]
DAQmxResetReadAttribute.__doc__ = \
"""int32 DAQmxResetReadAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2044"""
DAQmxWriteAnalogF64 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteAnalogF64
DAQmxWriteAnalogF64.restype = int32
DAQmxWriteAnalogF64.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(float64), POINTER(int32), POINTER(bool32)]
DAQmxWriteAnalogF64.__doc__ = \
"""int32 DAQmxWriteAnalogF64(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2052"""
DAQmxWriteAnalogScalarF64 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteAnalogScalarF64
DAQmxWriteAnalogScalarF64.restype = int32
DAQmxWriteAnalogScalarF64.argtypes = [TaskHandle, bool32, float64, float64, POINTER(bool32)]
DAQmxWriteAnalogScalarF64.__doc__ = \
"""int32 DAQmxWriteAnalogScalarF64(TaskHandle taskHandle, bool32 autoStart, float64 timeout, float64 value, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2053"""
DAQmxWriteBinaryI16 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteBinaryI16
DAQmxWriteBinaryI16.restype = int32
DAQmxWriteBinaryI16.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(int16), POINTER(int32), POINTER(bool32)]
DAQmxWriteBinaryI16.__doc__ = \
"""int32 DAQmxWriteBinaryI16(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2055"""
DAQmxWriteBinaryU16 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteBinaryU16
DAQmxWriteBinaryU16.restype = int32
DAQmxWriteBinaryU16.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt16), POINTER(int32), POINTER(bool32)]
DAQmxWriteBinaryU16.__doc__ = \
"""int32 DAQmxWriteBinaryU16(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2056"""
DAQmxWriteBinaryI32 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteBinaryI32
DAQmxWriteBinaryI32.restype = int32
DAQmxWriteBinaryI32.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(int32), POINTER(int32), POINTER(bool32)]
DAQmxWriteBinaryI32.__doc__ = \
"""int32 DAQmxWriteBinaryI32(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2057"""
DAQmxWriteBinaryU32 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteBinaryU32
DAQmxWriteBinaryU32.restype = int32
DAQmxWriteBinaryU32.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt32), POINTER(int32), POINTER(bool32)]
DAQmxWriteBinaryU32.__doc__ = \
"""int32 DAQmxWriteBinaryU32(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2058"""
DAQmxWriteDigitalU8 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteDigitalU8
DAQmxWriteDigitalU8.restype = int32
DAQmxWriteDigitalU8.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt8), POINTER(int32), POINTER(bool32)]
DAQmxWriteDigitalU8.__doc__ = \
"""int32 DAQmxWriteDigitalU8(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2060"""
DAQmxWriteDigitalU16 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteDigitalU16
DAQmxWriteDigitalU16.restype = int32
DAQmxWriteDigitalU16.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt16), POINTER(int32), POINTER(bool32)]
DAQmxWriteDigitalU16.__doc__ = \
"""int32 DAQmxWriteDigitalU16(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2061"""
DAQmxWriteDigitalU32 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteDigitalU32
DAQmxWriteDigitalU32.restype = int32
DAQmxWriteDigitalU32.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt32), POINTER(int32), POINTER(bool32)]
DAQmxWriteDigitalU32.__doc__ = \
"""int32 DAQmxWriteDigitalU32(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2062"""
DAQmxWriteDigitalScalarU32 = _stdcall_libraries['nicaiu.dll'].DAQmxWriteDigitalScalarU32
DAQmxWriteDigitalScalarU32.restype = int32
DAQmxWriteDigitalScalarU32.argtypes = [TaskHandle, bool32, float64, uInt32, POINTER(bool32)]
DAQmxWriteDigitalScalarU32.__doc__ = \
"""int32 DAQmxWriteDigitalScalarU32(TaskHandle taskHandle, bool32 autoStart, float64 timeout, uInt32 value, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2063"""
DAQmxWriteDigitalLines = _stdcall_libraries['nicaiu.dll'].DAQmxWriteDigitalLines
DAQmxWriteDigitalLines.restype = int32
DAQmxWriteDigitalLines.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt8), POINTER(int32), POINTER(bool32)]
DAQmxWriteDigitalLines.__doc__ = \
"""int32 DAQmxWriteDigitalLines(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2064"""
DAQmxWriteCtrFreq = _stdcall_libraries['nicaiu.dll'].DAQmxWriteCtrFreq
DAQmxWriteCtrFreq.restype = int32
DAQmxWriteCtrFreq.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(float64), POINTER(float64), POINTER(int32), POINTER(bool32)]
DAQmxWriteCtrFreq.__doc__ = \
"""int32 DAQmxWriteCtrFreq(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * frequency, unknown * dutyCycle, int32 * numSampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2066"""
DAQmxWriteCtrFreqScalar = _stdcall_libraries['nicaiu.dll'].DAQmxWriteCtrFreqScalar
DAQmxWriteCtrFreqScalar.restype = int32
DAQmxWriteCtrFreqScalar.argtypes = [TaskHandle, bool32, float64, float64, float64, POINTER(bool32)]
DAQmxWriteCtrFreqScalar.__doc__ = \
"""int32 DAQmxWriteCtrFreqScalar(TaskHandle taskHandle, bool32 autoStart, float64 timeout, float64 frequency, float64 dutyCycle, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2067"""
DAQmxWriteCtrTime = _stdcall_libraries['nicaiu.dll'].DAQmxWriteCtrTime
DAQmxWriteCtrTime.restype = int32
DAQmxWriteCtrTime.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(float64), POINTER(float64), POINTER(int32), POINTER(bool32)]
DAQmxWriteCtrTime.__doc__ = \
"""int32 DAQmxWriteCtrTime(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * highTime, unknown * lowTime, int32 * numSampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2068"""
DAQmxWriteCtrTimeScalar = _stdcall_libraries['nicaiu.dll'].DAQmxWriteCtrTimeScalar
DAQmxWriteCtrTimeScalar.restype = int32
DAQmxWriteCtrTimeScalar.argtypes = [TaskHandle, bool32, float64, float64, float64, POINTER(bool32)]
DAQmxWriteCtrTimeScalar.__doc__ = \
"""int32 DAQmxWriteCtrTimeScalar(TaskHandle taskHandle, bool32 autoStart, float64 timeout, float64 highTime, float64 lowTime, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2069"""
DAQmxWriteCtrTicks = _stdcall_libraries['nicaiu.dll'].DAQmxWriteCtrTicks
DAQmxWriteCtrTicks.restype = int32
DAQmxWriteCtrTicks.argtypes = [TaskHandle, int32, bool32, float64, bool32, POINTER(uInt32), POINTER(uInt32), POINTER(int32), POINTER(bool32)]
DAQmxWriteCtrTicks.__doc__ = \
"""int32 DAQmxWriteCtrTicks(TaskHandle taskHandle, int32 numSampsPerChan, bool32 autoStart, float64 timeout, bool32 dataLayout, unknown * highTicks, unknown * lowTicks, int32 * numSampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2070"""
DAQmxWriteCtrTicksScalar = _stdcall_libraries['nicaiu.dll'].DAQmxWriteCtrTicksScalar
DAQmxWriteCtrTicksScalar.restype = int32
DAQmxWriteCtrTicksScalar.argtypes = [TaskHandle, bool32, float64, uInt32, uInt32, POINTER(bool32)]
DAQmxWriteCtrTicksScalar.__doc__ = \
"""int32 DAQmxWriteCtrTicksScalar(TaskHandle taskHandle, bool32 autoStart, float64 timeout, uInt32 highTicks, uInt32 lowTicks, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2071"""
DAQmxWriteRaw = _stdcall_libraries['nicaiu.dll'].DAQmxWriteRaw
DAQmxWriteRaw.restype = int32
DAQmxWriteRaw.argtypes = [TaskHandle, int32, bool32, float64, c_void_p, POINTER(int32), POINTER(bool32)]
DAQmxWriteRaw.__doc__ = \
"""int32 DAQmxWriteRaw(TaskHandle taskHandle, int32 numSamps, bool32 autoStart, float64 timeout, unknown * writeArray, int32 * sampsPerChanWritten, bool32 * reserved)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2073"""
DAQmxGetWriteAttribute = _libraries['nicaiu.dll'].DAQmxGetWriteAttribute
DAQmxGetWriteAttribute.restype = int32
DAQmxGetWriteAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetWriteAttribute.__doc__ = \
"""int32 DAQmxGetWriteAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2075"""
DAQmxSetWriteAttribute = _libraries['nicaiu.dll'].DAQmxSetWriteAttribute
DAQmxSetWriteAttribute.restype = int32
DAQmxSetWriteAttribute.argtypes = [TaskHandle, int32]
DAQmxSetWriteAttribute.__doc__ = \
"""int32 DAQmxSetWriteAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2076"""
DAQmxResetWriteAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteAttribute
DAQmxResetWriteAttribute.restype = int32
DAQmxResetWriteAttribute.argtypes = [TaskHandle, int32]
DAQmxResetWriteAttribute.__doc__ = \
"""int32 DAQmxResetWriteAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2077"""
DAQmxExportSignal = _stdcall_libraries['nicaiu.dll'].DAQmxExportSignal
DAQmxExportSignal.restype = int32
DAQmxExportSignal.argtypes = [TaskHandle, int32, STRING]
DAQmxExportSignal.__doc__ = \
"""int32 DAQmxExportSignal(TaskHandle taskHandle, int32 signalID, unknown * outputTerminal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2088"""
DAQmxGetExportedSignalAttribute = _libraries['nicaiu.dll'].DAQmxGetExportedSignalAttribute
DAQmxGetExportedSignalAttribute.restype = int32
DAQmxGetExportedSignalAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetExportedSignalAttribute.__doc__ = \
"""int32 DAQmxGetExportedSignalAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2090"""
DAQmxSetExportedSignalAttribute = _libraries['nicaiu.dll'].DAQmxSetExportedSignalAttribute
DAQmxSetExportedSignalAttribute.restype = int32
DAQmxSetExportedSignalAttribute.argtypes = [TaskHandle, int32]
DAQmxSetExportedSignalAttribute.__doc__ = \
"""int32 DAQmxSetExportedSignalAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2091"""
DAQmxResetExportedSignalAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSignalAttribute
DAQmxResetExportedSignalAttribute.restype = int32
DAQmxResetExportedSignalAttribute.argtypes = [TaskHandle, int32]
DAQmxResetExportedSignalAttribute.__doc__ = \
"""int32 DAQmxResetExportedSignalAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2092"""
DAQmxCreateLinScale = _stdcall_libraries['nicaiu.dll'].DAQmxCreateLinScale
DAQmxCreateLinScale.restype = int32
DAQmxCreateLinScale.argtypes = [STRING, float64, float64, int32, STRING]
DAQmxCreateLinScale.__doc__ = \
"""int32 DAQmxCreateLinScale(unknown * name, float64 slope, float64 yIntercept, int32 preScaledUnits, unknown * scaledUnits)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2100"""
DAQmxCreateMapScale = _stdcall_libraries['nicaiu.dll'].DAQmxCreateMapScale
DAQmxCreateMapScale.restype = int32
DAQmxCreateMapScale.argtypes = [STRING, float64, float64, float64, float64, int32, STRING]
DAQmxCreateMapScale.__doc__ = \
"""int32 DAQmxCreateMapScale(unknown * name, float64 prescaledMin, float64 prescaledMax, float64 scaledMin, float64 scaledMax, int32 preScaledUnits, unknown * scaledUnits)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2101"""
DAQmxCreatePolynomialScale = _stdcall_libraries['nicaiu.dll'].DAQmxCreatePolynomialScale
DAQmxCreatePolynomialScale.restype = int32
DAQmxCreatePolynomialScale.argtypes = [STRING, POINTER(float64), uInt32, POINTER(float64), uInt32, int32, STRING]
DAQmxCreatePolynomialScale.__doc__ = \
"""int32 DAQmxCreatePolynomialScale(unknown * name, unknown * forwardCoeffs, uInt32 numForwardCoeffsIn, unknown * reverseCoeffs, uInt32 numReverseCoeffsIn, int32 preScaledUnits, unknown * scaledUnits)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2102"""
DAQmxCreateTableScale = _stdcall_libraries['nicaiu.dll'].DAQmxCreateTableScale
DAQmxCreateTableScale.restype = int32
DAQmxCreateTableScale.argtypes = [STRING, POINTER(float64), uInt32, POINTER(float64), uInt32, int32, STRING]
DAQmxCreateTableScale.__doc__ = \
"""int32 DAQmxCreateTableScale(unknown * name, unknown * prescaledVals, uInt32 numPrescaledValsIn, unknown * scaledVals, uInt32 numScaledValsIn, int32 preScaledUnits, unknown * scaledUnits)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2103"""
DAQmxCalculateReversePolyCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxCalculateReversePolyCoeff
DAQmxCalculateReversePolyCoeff.restype = int32
DAQmxCalculateReversePolyCoeff.argtypes = [POINTER(float64), uInt32, float64, float64, int32, int32, POINTER(float64)]
DAQmxCalculateReversePolyCoeff.__doc__ = \
"""int32 DAQmxCalculateReversePolyCoeff(unknown * forwardCoeffs, uInt32 numForwardCoeffsIn, float64 minValX, float64 maxValX, int32 numPointsToCompute, int32 reversePolyOrder, float64 * reverseCoeffs)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2104"""
DAQmxGetScaleAttribute = _libraries['nicaiu.dll'].DAQmxGetScaleAttribute
DAQmxGetScaleAttribute.restype = int32
DAQmxGetScaleAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetScaleAttribute.__doc__ = \
"""int32 DAQmxGetScaleAttribute(unknown * scaleName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2106"""
DAQmxSetScaleAttribute = _libraries['nicaiu.dll'].DAQmxSetScaleAttribute
DAQmxSetScaleAttribute.restype = int32
DAQmxSetScaleAttribute.argtypes = [STRING, int32]
DAQmxSetScaleAttribute.__doc__ = \
"""int32 DAQmxSetScaleAttribute(unknown * scaleName, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2107"""
DAQmxCfgInputBuffer = _stdcall_libraries['nicaiu.dll'].DAQmxCfgInputBuffer
DAQmxCfgInputBuffer.restype = int32
DAQmxCfgInputBuffer.argtypes = [TaskHandle, uInt32]
DAQmxCfgInputBuffer.__doc__ = \
"""int32 DAQmxCfgInputBuffer(TaskHandle taskHandle, uInt32 numSampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2115"""
DAQmxCfgOutputBuffer = _stdcall_libraries['nicaiu.dll'].DAQmxCfgOutputBuffer
DAQmxCfgOutputBuffer.restype = int32
DAQmxCfgOutputBuffer.argtypes = [TaskHandle, uInt32]
DAQmxCfgOutputBuffer.__doc__ = \
"""int32 DAQmxCfgOutputBuffer(TaskHandle taskHandle, uInt32 numSampsPerChan)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2116"""
DAQmxGetBufferAttribute = _libraries['nicaiu.dll'].DAQmxGetBufferAttribute
DAQmxGetBufferAttribute.restype = int32
DAQmxGetBufferAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetBufferAttribute.__doc__ = \
"""int32 DAQmxGetBufferAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2118"""
DAQmxSetBufferAttribute = _libraries['nicaiu.dll'].DAQmxSetBufferAttribute
DAQmxSetBufferAttribute.restype = int32
DAQmxSetBufferAttribute.argtypes = [TaskHandle, int32]
DAQmxSetBufferAttribute.__doc__ = \
"""int32 DAQmxSetBufferAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2119"""
DAQmxResetBufferAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetBufferAttribute
DAQmxResetBufferAttribute.restype = int32
DAQmxResetBufferAttribute.argtypes = [TaskHandle, int32]
DAQmxResetBufferAttribute.__doc__ = \
"""int32 DAQmxResetBufferAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2120"""
DAQmxSwitchCreateScanList = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchCreateScanList
DAQmxSwitchCreateScanList.restype = int32
DAQmxSwitchCreateScanList.argtypes = [STRING, POINTER(TaskHandle)]
DAQmxSwitchCreateScanList.__doc__ = \
"""int32 DAQmxSwitchCreateScanList(unknown * scanList, TaskHandle * taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2127"""
DAQmxSwitchConnect = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchConnect
DAQmxSwitchConnect.restype = int32
DAQmxSwitchConnect.argtypes = [STRING, STRING, bool32]
DAQmxSwitchConnect.__doc__ = \
"""int32 DAQmxSwitchConnect(unknown * switchChannel1, unknown * switchChannel2, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2129"""
DAQmxSwitchConnectMulti = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchConnectMulti
DAQmxSwitchConnectMulti.restype = int32
DAQmxSwitchConnectMulti.argtypes = [STRING, bool32]
DAQmxSwitchConnectMulti.__doc__ = \
"""int32 DAQmxSwitchConnectMulti(unknown * connectionList, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2130"""
DAQmxSwitchDisconnect = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchDisconnect
DAQmxSwitchDisconnect.restype = int32
DAQmxSwitchDisconnect.argtypes = [STRING, STRING, bool32]
DAQmxSwitchDisconnect.__doc__ = \
"""int32 DAQmxSwitchDisconnect(unknown * switchChannel1, unknown * switchChannel2, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2131"""
DAQmxSwitchDisconnectMulti = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchDisconnectMulti
DAQmxSwitchDisconnectMulti.restype = int32
DAQmxSwitchDisconnectMulti.argtypes = [STRING, bool32]
DAQmxSwitchDisconnectMulti.__doc__ = \
"""int32 DAQmxSwitchDisconnectMulti(unknown * connectionList, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2132"""
DAQmxSwitchDisconnectAll = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchDisconnectAll
DAQmxSwitchDisconnectAll.restype = int32
DAQmxSwitchDisconnectAll.argtypes = [STRING, bool32]
DAQmxSwitchDisconnectAll.__doc__ = \
"""int32 DAQmxSwitchDisconnectAll(unknown * deviceName, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2133"""
DAQmxSwitchSetTopologyAndReset = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchSetTopologyAndReset
DAQmxSwitchSetTopologyAndReset.restype = int32
DAQmxSwitchSetTopologyAndReset.argtypes = [STRING, STRING]
DAQmxSwitchSetTopologyAndReset.__doc__ = \
"""int32 DAQmxSwitchSetTopologyAndReset(unknown * deviceName, unknown * newTopology)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2292"""
DAQmxSwitchFindPath = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchFindPath
DAQmxSwitchFindPath.restype = int32
DAQmxSwitchFindPath.argtypes = [STRING, STRING, STRING, uInt32, POINTER(int32)]
DAQmxSwitchFindPath.__doc__ = \
"""int32 DAQmxSwitchFindPath(unknown * switchChannel1, unknown * switchChannel2, char * path, uInt32 pathBufferSize, int32 * pathStatus)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2295"""
DAQmxSwitchOpenRelays = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchOpenRelays
DAQmxSwitchOpenRelays.restype = int32
DAQmxSwitchOpenRelays.argtypes = [STRING, bool32]
DAQmxSwitchOpenRelays.__doc__ = \
"""int32 DAQmxSwitchOpenRelays(unknown * relayList, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2297"""
DAQmxSwitchCloseRelays = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchCloseRelays
DAQmxSwitchCloseRelays.restype = int32
DAQmxSwitchCloseRelays.argtypes = [STRING, bool32]
DAQmxSwitchCloseRelays.__doc__ = \
"""int32 DAQmxSwitchCloseRelays(unknown * relayList, bool32 waitForSettling)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2298"""
DAQmxSwitchGetSingleRelayCount = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchGetSingleRelayCount
DAQmxSwitchGetSingleRelayCount.restype = int32
DAQmxSwitchGetSingleRelayCount.argtypes = [STRING, POINTER(uInt32)]
DAQmxSwitchGetSingleRelayCount.__doc__ = \
"""int32 DAQmxSwitchGetSingleRelayCount(unknown * relayName, uInt32 * count)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2300"""
DAQmxSwitchGetMultiRelayCount = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchGetMultiRelayCount
DAQmxSwitchGetMultiRelayCount.restype = int32
DAQmxSwitchGetMultiRelayCount.argtypes = [STRING, POINTER(uInt32), uInt32, POINTER(uInt32)]
DAQmxSwitchGetMultiRelayCount.__doc__ = \
"""int32 DAQmxSwitchGetMultiRelayCount(unknown * relayList, uInt32 * count, uInt32 countArraySize, uInt32 * numRelayCountsRead)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2301"""
DAQmxSwitchGetSingleRelayPos = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchGetSingleRelayPos
DAQmxSwitchGetSingleRelayPos.restype = int32
DAQmxSwitchGetSingleRelayPos.argtypes = [STRING, POINTER(uInt32)]
DAQmxSwitchGetSingleRelayPos.__doc__ = \
"""int32 DAQmxSwitchGetSingleRelayPos(unknown * relayName, uInt32 * relayPos)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2303"""
DAQmxSwitchGetMultiRelayPos = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchGetMultiRelayPos
DAQmxSwitchGetMultiRelayPos.restype = int32
DAQmxSwitchGetMultiRelayPos.argtypes = [STRING, POINTER(uInt32), uInt32, POINTER(uInt32)]
DAQmxSwitchGetMultiRelayPos.__doc__ = \
"""int32 DAQmxSwitchGetMultiRelayPos(unknown * relayList, uInt32 * relayPos, uInt32 relayPosArraySize, uInt32 * numRelayPossRead)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2305"""
DAQmxSwitchWaitForSettling = _stdcall_libraries['nicaiu.dll'].DAQmxSwitchWaitForSettling
DAQmxSwitchWaitForSettling.restype = int32
DAQmxSwitchWaitForSettling.argtypes = [STRING]
DAQmxSwitchWaitForSettling.__doc__ = \
"""int32 DAQmxSwitchWaitForSettling(unknown * deviceName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2307"""
DAQmxGetSwitchChanAttribute = _libraries['nicaiu.dll'].DAQmxGetSwitchChanAttribute
DAQmxGetSwitchChanAttribute.restype = int32
DAQmxGetSwitchChanAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetSwitchChanAttribute.__doc__ = \
"""int32 DAQmxGetSwitchChanAttribute(unknown * switchChannelName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2309"""
DAQmxSetSwitchChanAttribute = _libraries['nicaiu.dll'].DAQmxSetSwitchChanAttribute
DAQmxSetSwitchChanAttribute.restype = int32
DAQmxSetSwitchChanAttribute.argtypes = [STRING, int32]
DAQmxSetSwitchChanAttribute.__doc__ = \
"""int32 DAQmxSetSwitchChanAttribute(unknown * switchChannelName, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2310"""
DAQmxGetSwitchDeviceAttribute = _libraries['nicaiu.dll'].DAQmxGetSwitchDeviceAttribute
DAQmxGetSwitchDeviceAttribute.restype = int32
DAQmxGetSwitchDeviceAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetSwitchDeviceAttribute.__doc__ = \
"""int32 DAQmxGetSwitchDeviceAttribute(unknown * deviceName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2312"""
DAQmxSetSwitchDeviceAttribute = _libraries['nicaiu.dll'].DAQmxSetSwitchDeviceAttribute
DAQmxSetSwitchDeviceAttribute.restype = int32
DAQmxSetSwitchDeviceAttribute.argtypes = [STRING, int32]
DAQmxSetSwitchDeviceAttribute.__doc__ = \
"""int32 DAQmxSetSwitchDeviceAttribute(unknown * deviceName, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2313"""
DAQmxGetSwitchScanAttribute = _libraries['nicaiu.dll'].DAQmxGetSwitchScanAttribute
DAQmxGetSwitchScanAttribute.restype = int32
DAQmxGetSwitchScanAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetSwitchScanAttribute.__doc__ = \
"""int32 DAQmxGetSwitchScanAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2315"""
DAQmxSetSwitchScanAttribute = _libraries['nicaiu.dll'].DAQmxSetSwitchScanAttribute
DAQmxSetSwitchScanAttribute.restype = int32
DAQmxSetSwitchScanAttribute.argtypes = [TaskHandle, int32]
DAQmxSetSwitchScanAttribute.__doc__ = \
"""int32 DAQmxSetSwitchScanAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2316"""
DAQmxResetSwitchScanAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetSwitchScanAttribute
DAQmxResetSwitchScanAttribute.restype = int32
DAQmxResetSwitchScanAttribute.argtypes = [TaskHandle, int32]
DAQmxResetSwitchScanAttribute.__doc__ = \
"""int32 DAQmxResetSwitchScanAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2317"""
DAQmxConnectTerms = _stdcall_libraries['nicaiu.dll'].DAQmxConnectTerms
DAQmxConnectTerms.restype = int32
DAQmxConnectTerms.argtypes = [STRING, STRING, int32]
DAQmxConnectTerms.__doc__ = \
"""int32 DAQmxConnectTerms(unknown * sourceTerminal, unknown * destinationTerminal, int32 signalModifiers)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2325"""
DAQmxDisconnectTerms = _stdcall_libraries['nicaiu.dll'].DAQmxDisconnectTerms
DAQmxDisconnectTerms.restype = int32
DAQmxDisconnectTerms.argtypes = [STRING, STRING]
DAQmxDisconnectTerms.__doc__ = \
"""int32 DAQmxDisconnectTerms(unknown * sourceTerminal, unknown * destinationTerminal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2326"""
DAQmxTristateOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxTristateOutputTerm
DAQmxTristateOutputTerm.restype = int32
DAQmxTristateOutputTerm.argtypes = [STRING]
DAQmxTristateOutputTerm.__doc__ = \
"""int32 DAQmxTristateOutputTerm(unknown * outputTerminal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2327"""
DAQmxResetDevice = _stdcall_libraries['nicaiu.dll'].DAQmxResetDevice
DAQmxResetDevice.restype = int32
DAQmxResetDevice.argtypes = [STRING]
DAQmxResetDevice.__doc__ = \
"""int32 DAQmxResetDevice(unknown * deviceName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2335"""
DAQmxSelfTestDevice = _stdcall_libraries['nicaiu.dll'].DAQmxSelfTestDevice
DAQmxSelfTestDevice.restype = int32
DAQmxSelfTestDevice.argtypes = [STRING]
DAQmxSelfTestDevice.__doc__ = \
"""int32 DAQmxSelfTestDevice(unknown * deviceName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2337"""
DAQmxGetDeviceAttribute = _libraries['nicaiu.dll'].DAQmxGetDeviceAttribute
DAQmxGetDeviceAttribute.restype = int32
DAQmxGetDeviceAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetDeviceAttribute.__doc__ = \
"""int32 DAQmxGetDeviceAttribute(unknown * deviceName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2339"""
DAQmxCreateWatchdogTimerTask = _libraries['nicaiu.dll'].DAQmxCreateWatchdogTimerTask
DAQmxCreateWatchdogTimerTask.restype = int32
DAQmxCreateWatchdogTimerTask.argtypes = [STRING, STRING, POINTER(TaskHandle), float64, STRING, int32]
DAQmxCreateWatchdogTimerTask.__doc__ = \
"""int32 DAQmxCreateWatchdogTimerTask(unknown * deviceName, unknown * taskName, TaskHandle * taskHandle, float64 timeout, unknown * lines, int32 expState)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2346"""
DAQmxControlWatchdogTask = _stdcall_libraries['nicaiu.dll'].DAQmxControlWatchdogTask
DAQmxControlWatchdogTask.restype = int32
DAQmxControlWatchdogTask.argtypes = [TaskHandle, int32]
DAQmxControlWatchdogTask.__doc__ = \
"""int32 DAQmxControlWatchdogTask(TaskHandle taskHandle, int32 action)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2347"""
DAQmxGetWatchdogAttribute = _libraries['nicaiu.dll'].DAQmxGetWatchdogAttribute
DAQmxGetWatchdogAttribute.restype = int32
DAQmxGetWatchdogAttribute.argtypes = [TaskHandle, STRING, int32, c_void_p]
DAQmxGetWatchdogAttribute.__doc__ = \
"""int32 DAQmxGetWatchdogAttribute(TaskHandle taskHandle, unknown * lines, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2349"""
DAQmxSetWatchdogAttribute = _libraries['nicaiu.dll'].DAQmxSetWatchdogAttribute
DAQmxSetWatchdogAttribute.restype = int32
DAQmxSetWatchdogAttribute.argtypes = [TaskHandle, STRING, int32]
DAQmxSetWatchdogAttribute.__doc__ = \
"""int32 DAQmxSetWatchdogAttribute(TaskHandle taskHandle, unknown * lines, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2350"""
DAQmxResetWatchdogAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetWatchdogAttribute
DAQmxResetWatchdogAttribute.restype = int32
DAQmxResetWatchdogAttribute.argtypes = [TaskHandle, STRING, int32]
DAQmxResetWatchdogAttribute.__doc__ = \
"""int32 DAQmxResetWatchdogAttribute(TaskHandle taskHandle, unknown * lines, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2351"""
DAQmxSelfCal = _stdcall_libraries['nicaiu.dll'].DAQmxSelfCal
DAQmxSelfCal.restype = int32
DAQmxSelfCal.argtypes = [STRING]
DAQmxSelfCal.__doc__ = \
"""int32 DAQmxSelfCal(unknown * deviceName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2359"""
DAQmxPerformBridgeOffsetNullingCal = _stdcall_libraries['nicaiu.dll'].DAQmxPerformBridgeOffsetNullingCal
DAQmxPerformBridgeOffsetNullingCal.restype = int32
DAQmxPerformBridgeOffsetNullingCal.argtypes = [TaskHandle, STRING]
DAQmxPerformBridgeOffsetNullingCal.__doc__ = \
"""int32 DAQmxPerformBridgeOffsetNullingCal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2360"""
DAQmxPerformBridgeOffsetNullingCalEx = _stdcall_libraries['nicaiu.dll'].DAQmxPerformBridgeOffsetNullingCalEx
DAQmxPerformBridgeOffsetNullingCalEx.restype = int32
DAQmxPerformBridgeOffsetNullingCalEx.argtypes = [TaskHandle, STRING, bool32]
DAQmxPerformBridgeOffsetNullingCalEx.__doc__ = \
"""int32 DAQmxPerformBridgeOffsetNullingCalEx(TaskHandle taskHandle, unknown * channel, bool32 skipUnsupportedChannels)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2361"""
DAQmxPerformStrainShuntCal = _stdcall_libraries['nicaiu.dll'].DAQmxPerformStrainShuntCal
DAQmxPerformStrainShuntCal.restype = int32
DAQmxPerformStrainShuntCal.argtypes = [TaskHandle, STRING, float64, int32, bool32]
DAQmxPerformStrainShuntCal.__doc__ = \
"""int32 DAQmxPerformStrainShuntCal(TaskHandle taskHandle, unknown * channel, float64 shuntResistorValue, int32 shuntResistorLocation, bool32 skipUnsupportedChannels)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2362"""
DAQmxPerformBridgeShuntCal = _stdcall_libraries['nicaiu.dll'].DAQmxPerformBridgeShuntCal
DAQmxPerformBridgeShuntCal.restype = int32
DAQmxPerformBridgeShuntCal.argtypes = [TaskHandle, STRING, float64, int32, float64, bool32]
DAQmxPerformBridgeShuntCal.__doc__ = \
"""int32 DAQmxPerformBridgeShuntCal(TaskHandle taskHandle, unknown * channel, float64 shuntResistorValue, int32 shuntResistorLocation, float64 bridgeResistance, bool32 skipUnsupportedChannels)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2363"""
DAQmxGetSelfCalLastDateAndTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetSelfCalLastDateAndTime
DAQmxGetSelfCalLastDateAndTime.restype = int32
DAQmxGetSelfCalLastDateAndTime.argtypes = [STRING, POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32)]
DAQmxGetSelfCalLastDateAndTime.__doc__ = \
"""int32 DAQmxGetSelfCalLastDateAndTime(unknown * deviceName, uInt32 * year, uInt32 * month, uInt32 * day, uInt32 * hour, uInt32 * minute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2364"""
DAQmxGetExtCalLastDateAndTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetExtCalLastDateAndTime
DAQmxGetExtCalLastDateAndTime.restype = int32
DAQmxGetExtCalLastDateAndTime.argtypes = [STRING, POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32), POINTER(uInt32)]
DAQmxGetExtCalLastDateAndTime.__doc__ = \
"""int32 DAQmxGetExtCalLastDateAndTime(unknown * deviceName, uInt32 * year, uInt32 * month, uInt32 * day, uInt32 * hour, uInt32 * minute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2365"""
DAQmxRestoreLastExtCalConst = _stdcall_libraries['nicaiu.dll'].DAQmxRestoreLastExtCalConst
DAQmxRestoreLastExtCalConst.restype = int32
DAQmxRestoreLastExtCalConst.argtypes = [STRING]
DAQmxRestoreLastExtCalConst.__doc__ = \
"""int32 DAQmxRestoreLastExtCalConst(unknown * deviceName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2366"""
CalHandle = uInt32
DAQmxESeriesCalAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxESeriesCalAdjust
DAQmxESeriesCalAdjust.restype = int32
DAQmxESeriesCalAdjust.argtypes = [CalHandle, float64]
DAQmxESeriesCalAdjust.__doc__ = \
"""int32 DAQmxESeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2368"""
DAQmxMSeriesCalAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxMSeriesCalAdjust
DAQmxMSeriesCalAdjust.restype = int32
DAQmxMSeriesCalAdjust.argtypes = [CalHandle, float64]
DAQmxMSeriesCalAdjust.__doc__ = \
"""int32 DAQmxMSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2369"""
DAQmxSSeriesCalAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxSSeriesCalAdjust
DAQmxSSeriesCalAdjust.restype = int32
DAQmxSSeriesCalAdjust.argtypes = [CalHandle, float64]
DAQmxSSeriesCalAdjust.__doc__ = \
"""int32 DAQmxSSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2370"""
DAQmxSCBaseboardCalAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxSCBaseboardCalAdjust
DAQmxSCBaseboardCalAdjust.restype = int32
DAQmxSCBaseboardCalAdjust.argtypes = [CalHandle, float64]
DAQmxSCBaseboardCalAdjust.__doc__ = \
"""int32 DAQmxSCBaseboardCalAdjust(CalHandle calHandle, float64 referenceVoltage)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2371"""
DAQmxAOSeriesCalAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxAOSeriesCalAdjust
DAQmxAOSeriesCalAdjust.restype = int32
DAQmxAOSeriesCalAdjust.argtypes = [CalHandle, float64]
DAQmxAOSeriesCalAdjust.__doc__ = \
"""int32 DAQmxAOSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2372"""
DAQmxDeviceSupportsCal = _stdcall_libraries['nicaiu.dll'].DAQmxDeviceSupportsCal
DAQmxDeviceSupportsCal.restype = int32
DAQmxDeviceSupportsCal.argtypes = [STRING, POINTER(bool32)]
DAQmxDeviceSupportsCal.__doc__ = \
"""int32 DAQmxDeviceSupportsCal(unknown * deviceName, bool32 * calSupported)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2374"""
DAQmxGetCalInfoAttribute = _libraries['nicaiu.dll'].DAQmxGetCalInfoAttribute
DAQmxGetCalInfoAttribute.restype = int32
DAQmxGetCalInfoAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetCalInfoAttribute.__doc__ = \
"""int32 DAQmxGetCalInfoAttribute(unknown * deviceName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2376"""
DAQmxSetCalInfoAttribute = _libraries['nicaiu.dll'].DAQmxSetCalInfoAttribute
DAQmxSetCalInfoAttribute.restype = int32
DAQmxSetCalInfoAttribute.argtypes = [STRING, int32]
DAQmxSetCalInfoAttribute.__doc__ = \
"""int32 DAQmxSetCalInfoAttribute(unknown * deviceName, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2377"""
DAQmxInitExtCal = _stdcall_libraries['nicaiu.dll'].DAQmxInitExtCal
DAQmxInitExtCal.restype = int32
DAQmxInitExtCal.argtypes = [STRING, STRING, POINTER(CalHandle)]
DAQmxInitExtCal.__doc__ = \
"""int32 DAQmxInitExtCal(unknown * deviceName, unknown * password, CalHandle * calHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2379"""
DAQmxCloseExtCal = _stdcall_libraries['nicaiu.dll'].DAQmxCloseExtCal
DAQmxCloseExtCal.restype = int32
DAQmxCloseExtCal.argtypes = [CalHandle, int32]
DAQmxCloseExtCal.__doc__ = \
"""int32 DAQmxCloseExtCal(CalHandle calHandle, int32 action)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2380"""
DAQmxChangeExtCalPassword = _stdcall_libraries['nicaiu.dll'].DAQmxChangeExtCalPassword
DAQmxChangeExtCalPassword.restype = int32
DAQmxChangeExtCalPassword.argtypes = [STRING, STRING, STRING]
DAQmxChangeExtCalPassword.__doc__ = \
"""int32 DAQmxChangeExtCalPassword(unknown * deviceName, unknown * password, unknown * newPassword)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2381"""
DAQmxAdjustDSAAICal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjustDSAAICal
DAQmxAdjustDSAAICal.restype = int32
DAQmxAdjustDSAAICal.argtypes = [CalHandle, float64]
DAQmxAdjustDSAAICal.__doc__ = \
"""int32 DAQmxAdjustDSAAICal(CalHandle calHandle, float64 referenceVoltage)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2383"""
DAQmxAdjustDSAAICalEx = _stdcall_libraries['nicaiu.dll'].DAQmxAdjustDSAAICalEx
DAQmxAdjustDSAAICalEx.restype = int32
DAQmxAdjustDSAAICalEx.argtypes = [CalHandle, float64, bool32]
DAQmxAdjustDSAAICalEx.__doc__ = \
"""int32 DAQmxAdjustDSAAICalEx(CalHandle calHandle, float64 referenceVoltage, bool32 inputsShorted)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2384"""
DAQmxAdjustDSAAOCal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjustDSAAOCal
DAQmxAdjustDSAAOCal.restype = int32
DAQmxAdjustDSAAOCal.argtypes = [CalHandle, uInt32, float64, float64, float64, float64, float64]
DAQmxAdjustDSAAOCal.__doc__ = \
"""int32 DAQmxAdjustDSAAOCal(CalHandle calHandle, uInt32 channel, float64 requestedLowVoltage, float64 actualLowVoltage, float64 requestedHighVoltage, float64 actualHighVoltage, float64 gainSetting)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2385"""
DAQmxAdjustDSATimebaseCal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjustDSATimebaseCal
DAQmxAdjustDSATimebaseCal.restype = int32
DAQmxAdjustDSATimebaseCal.argtypes = [CalHandle, float64]
DAQmxAdjustDSATimebaseCal.__doc__ = \
"""int32 DAQmxAdjustDSATimebaseCal(CalHandle calHandle, float64 referenceFrequency)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2386"""
DAQmxAdjust4204Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust4204Cal
DAQmxAdjust4204Cal.restype = int32
DAQmxAdjust4204Cal.argtypes = [CalHandle, STRING, float64, bool32, float64]
DAQmxAdjust4204Cal.__doc__ = \
"""int32 DAQmxAdjust4204Cal(CalHandle calHandle, unknown * channelNames, float64 lowPassFreq, bool32 trackHoldEnabled, float64 inputVal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2388"""
DAQmxAdjust4220Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust4220Cal
DAQmxAdjust4220Cal.restype = int32
DAQmxAdjust4220Cal.argtypes = [CalHandle, STRING, float64, float64]
DAQmxAdjust4220Cal.__doc__ = \
"""int32 DAQmxAdjust4220Cal(CalHandle calHandle, unknown * channelNames, float64 gain, float64 inputVal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2389"""
DAQmxAdjust4224Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust4224Cal
DAQmxAdjust4224Cal.restype = int32
DAQmxAdjust4224Cal.argtypes = [CalHandle, STRING, float64, float64]
DAQmxAdjust4224Cal.__doc__ = \
"""int32 DAQmxAdjust4224Cal(CalHandle calHandle, unknown * channelNames, float64 gain, float64 inputVal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2390"""
DAQmxAdjust4225Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust4225Cal
DAQmxAdjust4225Cal.restype = int32
DAQmxAdjust4225Cal.argtypes = [CalHandle, STRING, float64, float64]
DAQmxAdjust4225Cal.__doc__ = \
"""int32 DAQmxAdjust4225Cal(CalHandle calHandle, unknown * channelNames, float64 gain, float64 inputVal)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2392"""
DAQmxSetup1102Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1102Cal
DAQmxSetup1102Cal.restype = int32
DAQmxSetup1102Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1102Cal.__doc__ = \
"""int32 DAQmxSetup1102Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2394"""
DAQmxAdjust1102Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1102Cal
DAQmxAdjust1102Cal.restype = int32
DAQmxAdjust1102Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1102Cal.__doc__ = \
"""int32 DAQmxAdjust1102Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2395"""
DAQmxSetup1104Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1104Cal
DAQmxSetup1104Cal.restype = int32
DAQmxSetup1104Cal.argtypes = [CalHandle, STRING]
DAQmxSetup1104Cal.__doc__ = \
"""int32 DAQmxSetup1104Cal(CalHandle calHandle, unknown * channelName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2397"""
DAQmxAdjust1104Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1104Cal
DAQmxAdjust1104Cal.restype = int32
DAQmxAdjust1104Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1104Cal.__doc__ = \
"""int32 DAQmxAdjust1104Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2398"""
DAQmxSetup1112Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1112Cal
DAQmxSetup1112Cal.restype = int32
DAQmxSetup1112Cal.argtypes = [CalHandle, STRING]
DAQmxSetup1112Cal.__doc__ = \
"""int32 DAQmxSetup1112Cal(CalHandle calHandle, unknown * channelName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2400"""
DAQmxAdjust1112Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1112Cal
DAQmxAdjust1112Cal.restype = int32
DAQmxAdjust1112Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1112Cal.__doc__ = \
"""int32 DAQmxAdjust1112Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2401"""
DAQmxSetup1122Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1122Cal
DAQmxSetup1122Cal.restype = int32
DAQmxSetup1122Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1122Cal.__doc__ = \
"""int32 DAQmxSetup1122Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2403"""
DAQmxAdjust1122Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1122Cal
DAQmxAdjust1122Cal.restype = int32
DAQmxAdjust1122Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1122Cal.__doc__ = \
"""int32 DAQmxAdjust1122Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2404"""
DAQmxSetup1124Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1124Cal
DAQmxSetup1124Cal.restype = int32
DAQmxSetup1124Cal.argtypes = [CalHandle, STRING, int32, uInt32]
DAQmxSetup1124Cal.__doc__ = \
"""int32 DAQmxSetup1124Cal(CalHandle calHandle, unknown * channelName, int32 range, uInt32 dacValue)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2406"""
DAQmxAdjust1124Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1124Cal
DAQmxAdjust1124Cal.restype = int32
DAQmxAdjust1124Cal.argtypes = [CalHandle, float64]
DAQmxAdjust1124Cal.__doc__ = \
"""int32 DAQmxAdjust1124Cal(CalHandle calHandle, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2407"""
DAQmxSetup1125Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1125Cal
DAQmxSetup1125Cal.restype = int32
DAQmxSetup1125Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1125Cal.__doc__ = \
"""int32 DAQmxSetup1125Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2409"""
DAQmxAdjust1125Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1125Cal
DAQmxAdjust1125Cal.restype = int32
DAQmxAdjust1125Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1125Cal.__doc__ = \
"""int32 DAQmxAdjust1125Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2410"""
DAQmxSetup1126Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1126Cal
DAQmxSetup1126Cal.restype = int32
DAQmxSetup1126Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1126Cal.__doc__ = \
"""int32 DAQmxSetup1126Cal(CalHandle calHandle, unknown * channelName, float64 upperFreqLimit)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2412"""
DAQmxAdjust1126Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1126Cal
DAQmxAdjust1126Cal.restype = int32
DAQmxAdjust1126Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1126Cal.__doc__ = \
"""int32 DAQmxAdjust1126Cal(CalHandle calHandle, float64 refFreq, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2413"""
DAQmxSetup1141Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1141Cal
DAQmxSetup1141Cal.restype = int32
DAQmxSetup1141Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1141Cal.__doc__ = \
"""int32 DAQmxSetup1141Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2415"""
DAQmxAdjust1141Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1141Cal
DAQmxAdjust1141Cal.restype = int32
DAQmxAdjust1141Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1141Cal.__doc__ = \
"""int32 DAQmxAdjust1141Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2416"""
DAQmxSetup1142Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1142Cal
DAQmxSetup1142Cal.restype = int32
DAQmxSetup1142Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1142Cal.__doc__ = \
"""int32 DAQmxSetup1142Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2417"""
DAQmxAdjust1142Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1142Cal
DAQmxAdjust1142Cal.restype = int32
DAQmxAdjust1142Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1142Cal.__doc__ = \
"""int32 DAQmxAdjust1142Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2418"""
DAQmxSetup1143Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1143Cal
DAQmxSetup1143Cal.restype = int32
DAQmxSetup1143Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1143Cal.__doc__ = \
"""int32 DAQmxSetup1143Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2419"""
DAQmxAdjust1143Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1143Cal
DAQmxAdjust1143Cal.restype = int32
DAQmxAdjust1143Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1143Cal.__doc__ = \
"""int32 DAQmxAdjust1143Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2420"""
DAQmxSetup1502Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1502Cal
DAQmxSetup1502Cal.restype = int32
DAQmxSetup1502Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1502Cal.__doc__ = \
"""int32 DAQmxSetup1502Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2423"""
DAQmxAdjust1502Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1502Cal
DAQmxAdjust1502Cal.restype = int32
DAQmxAdjust1502Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1502Cal.__doc__ = \
"""int32 DAQmxAdjust1502Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2424"""
DAQmxSetup1503Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1503Cal
DAQmxSetup1503Cal.restype = int32
DAQmxSetup1503Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1503Cal.__doc__ = \
"""int32 DAQmxSetup1503Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2426"""
DAQmxAdjust1503Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1503Cal
DAQmxAdjust1503Cal.restype = int32
DAQmxAdjust1503Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1503Cal.__doc__ = \
"""int32 DAQmxAdjust1503Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2427"""
DAQmxAdjust1503CurrentCal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1503CurrentCal
DAQmxAdjust1503CurrentCal.restype = int32
DAQmxAdjust1503CurrentCal.argtypes = [CalHandle, STRING, float64]
DAQmxAdjust1503CurrentCal.__doc__ = \
"""int32 DAQmxAdjust1503CurrentCal(CalHandle calHandle, unknown * channelName, float64 measCurrent)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2428"""
DAQmxSetup1520Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1520Cal
DAQmxSetup1520Cal.restype = int32
DAQmxSetup1520Cal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup1520Cal.__doc__ = \
"""int32 DAQmxSetup1520Cal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2430"""
DAQmxAdjust1520Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1520Cal
DAQmxAdjust1520Cal.restype = int32
DAQmxAdjust1520Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1520Cal.__doc__ = \
"""int32 DAQmxAdjust1520Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2431"""
DAQmxSetup1521Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1521Cal
DAQmxSetup1521Cal.restype = int32
DAQmxSetup1521Cal.argtypes = [CalHandle, STRING]
DAQmxSetup1521Cal.__doc__ = \
"""int32 DAQmxSetup1521Cal(CalHandle calHandle, unknown * channelName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2433"""
DAQmxAdjust1521Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1521Cal
DAQmxAdjust1521Cal.restype = int32
DAQmxAdjust1521Cal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust1521Cal.__doc__ = \
"""int32 DAQmxAdjust1521Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2434"""
DAQmxSetup153xCal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup153xCal
DAQmxSetup153xCal.restype = int32
DAQmxSetup153xCal.argtypes = [CalHandle, STRING, float64]
DAQmxSetup153xCal.__doc__ = \
"""int32 DAQmxSetup153xCal(CalHandle calHandle, unknown * channelName, float64 gain)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2436"""
DAQmxAdjust153xCal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust153xCal
DAQmxAdjust153xCal.restype = int32
DAQmxAdjust153xCal.argtypes = [CalHandle, float64, float64]
DAQmxAdjust153xCal.__doc__ = \
"""int32 DAQmxAdjust153xCal(CalHandle calHandle, float64 refVoltage, float64 measOutput)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2437"""
DAQmxSetup1540Cal = _stdcall_libraries['nicaiu.dll'].DAQmxSetup1540Cal
DAQmxSetup1540Cal.restype = int32
DAQmxSetup1540Cal.argtypes = [CalHandle, STRING, float64, float64]
DAQmxSetup1540Cal.__doc__ = \
"""int32 DAQmxSetup1540Cal(CalHandle calHandle, unknown * channelName, float64 excitationVoltage, float64 excitationFreq)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2439"""
DAQmxAdjust1540Cal = _stdcall_libraries['nicaiu.dll'].DAQmxAdjust1540Cal
DAQmxAdjust1540Cal.restype = int32
DAQmxAdjust1540Cal.argtypes = [CalHandle, float64, float64, int32]
DAQmxAdjust1540Cal.__doc__ = \
"""int32 DAQmxAdjust1540Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput, int32 inputCalSource)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2440"""
DAQmxConfigureTEDS = _stdcall_libraries['nicaiu.dll'].DAQmxConfigureTEDS
DAQmxConfigureTEDS.restype = int32
DAQmxConfigureTEDS.argtypes = [STRING, STRING]
DAQmxConfigureTEDS.__doc__ = \
"""int32 DAQmxConfigureTEDS(unknown * physicalChannel, unknown * filePath)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2447"""
DAQmxClearTEDS = _stdcall_libraries['nicaiu.dll'].DAQmxClearTEDS
DAQmxClearTEDS.restype = int32
DAQmxClearTEDS.argtypes = [STRING]
DAQmxClearTEDS.__doc__ = \
"""int32 DAQmxClearTEDS(unknown * physicalChannel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2448"""
DAQmxWriteToTEDSFromArray = _stdcall_libraries['nicaiu.dll'].DAQmxWriteToTEDSFromArray
DAQmxWriteToTEDSFromArray.restype = int32
DAQmxWriteToTEDSFromArray.argtypes = [STRING, POINTER(uInt8), uInt32, int32]
DAQmxWriteToTEDSFromArray.__doc__ = \
"""int32 DAQmxWriteToTEDSFromArray(unknown * physicalChannel, unknown * bitStream, uInt32 arraySize, int32 basicTEDSOptions)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2449"""
DAQmxWriteToTEDSFromFile = _stdcall_libraries['nicaiu.dll'].DAQmxWriteToTEDSFromFile
DAQmxWriteToTEDSFromFile.restype = int32
DAQmxWriteToTEDSFromFile.argtypes = [STRING, STRING, int32]
DAQmxWriteToTEDSFromFile.__doc__ = \
"""int32 DAQmxWriteToTEDSFromFile(unknown * physicalChannel, unknown * filePath, int32 basicTEDSOptions)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2450"""
DAQmxGetPhysicalChanAttribute = _libraries['nicaiu.dll'].DAQmxGetPhysicalChanAttribute
DAQmxGetPhysicalChanAttribute.restype = int32
DAQmxGetPhysicalChanAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetPhysicalChanAttribute.__doc__ = \
"""int32 DAQmxGetPhysicalChanAttribute(unknown * physicalChannel, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2451"""
DAQmxWaitForNextSampleClock = _stdcall_libraries['nicaiu.dll'].DAQmxWaitForNextSampleClock
DAQmxWaitForNextSampleClock.restype = int32
DAQmxWaitForNextSampleClock.argtypes = [TaskHandle, float64, POINTER(bool32)]
DAQmxWaitForNextSampleClock.__doc__ = \
"""int32 DAQmxWaitForNextSampleClock(TaskHandle taskHandle, float64 timeout, bool32 * isLate)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2458"""
DAQmxGetRealTimeAttribute = _libraries['nicaiu.dll'].DAQmxGetRealTimeAttribute
DAQmxGetRealTimeAttribute.restype = int32
DAQmxGetRealTimeAttribute.argtypes = [TaskHandle, int32, c_void_p]
DAQmxGetRealTimeAttribute.__doc__ = \
"""int32 DAQmxGetRealTimeAttribute(TaskHandle taskHandle, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2459"""
DAQmxSetRealTimeAttribute = _libraries['nicaiu.dll'].DAQmxSetRealTimeAttribute
DAQmxSetRealTimeAttribute.restype = int32
DAQmxSetRealTimeAttribute.argtypes = [TaskHandle, int32]
DAQmxSetRealTimeAttribute.__doc__ = \
"""int32 DAQmxSetRealTimeAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2460"""
DAQmxResetRealTimeAttribute = _stdcall_libraries['nicaiu.dll'].DAQmxResetRealTimeAttribute
DAQmxResetRealTimeAttribute.restype = int32
DAQmxResetRealTimeAttribute.argtypes = [TaskHandle, int32]
DAQmxResetRealTimeAttribute.__doc__ = \
"""int32 DAQmxResetRealTimeAttribute(TaskHandle taskHandle, int32 attribute)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2461"""
DAQmxIsReadOrWriteLate = _stdcall_libraries['nicaiu.dll'].DAQmxIsReadOrWriteLate
DAQmxIsReadOrWriteLate.restype = bool32
DAQmxIsReadOrWriteLate.argtypes = [int32]
DAQmxIsReadOrWriteLate.__doc__ = \
"""bool32 DAQmxIsReadOrWriteLate(int32 errorCode)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2464"""
DAQmxSaveTask = _stdcall_libraries['nicaiu.dll'].DAQmxSaveTask
DAQmxSaveTask.restype = int32
DAQmxSaveTask.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxSaveTask.__doc__ = \
"""int32 DAQmxSaveTask(TaskHandle taskHandle, unknown * saveAs, unknown * author, uInt32 options)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2471"""
DAQmxSaveGlobalChan = _stdcall_libraries['nicaiu.dll'].DAQmxSaveGlobalChan
DAQmxSaveGlobalChan.restype = int32
DAQmxSaveGlobalChan.argtypes = [TaskHandle, STRING, STRING, STRING, uInt32]
DAQmxSaveGlobalChan.__doc__ = \
"""int32 DAQmxSaveGlobalChan(TaskHandle taskHandle, unknown * channelName, unknown * saveAs, unknown * author, uInt32 options)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2472"""
DAQmxSaveScale = _stdcall_libraries['nicaiu.dll'].DAQmxSaveScale
DAQmxSaveScale.restype = int32
DAQmxSaveScale.argtypes = [STRING, STRING, STRING, uInt32]
DAQmxSaveScale.__doc__ = \
"""int32 DAQmxSaveScale(unknown * scaleName, unknown * saveAs, unknown * author, uInt32 options)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2473"""
DAQmxDeleteSavedTask = _stdcall_libraries['nicaiu.dll'].DAQmxDeleteSavedTask
DAQmxDeleteSavedTask.restype = int32
DAQmxDeleteSavedTask.argtypes = [STRING]
DAQmxDeleteSavedTask.__doc__ = \
"""int32 DAQmxDeleteSavedTask(unknown * taskName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2474"""
DAQmxDeleteSavedGlobalChan = _stdcall_libraries['nicaiu.dll'].DAQmxDeleteSavedGlobalChan
DAQmxDeleteSavedGlobalChan.restype = int32
DAQmxDeleteSavedGlobalChan.argtypes = [STRING]
DAQmxDeleteSavedGlobalChan.__doc__ = \
"""int32 DAQmxDeleteSavedGlobalChan(unknown * channelName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2475"""
DAQmxDeleteSavedScale = _stdcall_libraries['nicaiu.dll'].DAQmxDeleteSavedScale
DAQmxDeleteSavedScale.restype = int32
DAQmxDeleteSavedScale.argtypes = [STRING]
DAQmxDeleteSavedScale.__doc__ = \
"""int32 DAQmxDeleteSavedScale(unknown * scaleName)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2476"""
DAQmxGetPersistedTaskAttribute = _libraries['nicaiu.dll'].DAQmxGetPersistedTaskAttribute
DAQmxGetPersistedTaskAttribute.restype = int32
DAQmxGetPersistedTaskAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetPersistedTaskAttribute.__doc__ = \
"""int32 DAQmxGetPersistedTaskAttribute(unknown * taskName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2478"""
DAQmxGetPersistedChanAttribute = _libraries['nicaiu.dll'].DAQmxGetPersistedChanAttribute
DAQmxGetPersistedChanAttribute.restype = int32
DAQmxGetPersistedChanAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetPersistedChanAttribute.__doc__ = \
"""int32 DAQmxGetPersistedChanAttribute(unknown * channel, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2479"""
DAQmxGetPersistedScaleAttribute = _libraries['nicaiu.dll'].DAQmxGetPersistedScaleAttribute
DAQmxGetPersistedScaleAttribute.restype = int32
DAQmxGetPersistedScaleAttribute.argtypes = [STRING, int32, c_void_p]
DAQmxGetPersistedScaleAttribute.__doc__ = \
"""int32 DAQmxGetPersistedScaleAttribute(unknown * scaleName, int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2480"""
DAQmxGetSystemInfoAttribute = _libraries['nicaiu.dll'].DAQmxGetSystemInfoAttribute
DAQmxGetSystemInfoAttribute.restype = int32
DAQmxGetSystemInfoAttribute.argtypes = [int32, c_void_p]
DAQmxGetSystemInfoAttribute.__doc__ = \
"""int32 DAQmxGetSystemInfoAttribute(int32 attribute, void * value)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2487"""
DAQmxSetDigitalPowerUpStates = _libraries['nicaiu.dll'].DAQmxSetDigitalPowerUpStates
DAQmxSetDigitalPowerUpStates.restype = int32
DAQmxSetDigitalPowerUpStates.argtypes = [STRING, STRING, int32]
DAQmxSetDigitalPowerUpStates.__doc__ = \
"""int32 DAQmxSetDigitalPowerUpStates(unknown * deviceName, unknown * channelNames, int32 state)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2488"""
DAQmxSetAnalogPowerUpStates = _libraries['nicaiu.dll'].DAQmxSetAnalogPowerUpStates
DAQmxSetAnalogPowerUpStates.restype = int32
DAQmxSetAnalogPowerUpStates.argtypes = [STRING, STRING, float64, int32]
DAQmxSetAnalogPowerUpStates.__doc__ = \
"""int32 DAQmxSetAnalogPowerUpStates(unknown * deviceName, unknown * channelNames, float64 state, int32 channelType)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2489"""
DAQmxSetDigitalLogicFamilyPowerUpState = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigitalLogicFamilyPowerUpState
DAQmxSetDigitalLogicFamilyPowerUpState.restype = int32
DAQmxSetDigitalLogicFamilyPowerUpState.argtypes = [STRING, int32]
DAQmxSetDigitalLogicFamilyPowerUpState.__doc__ = \
"""int32 DAQmxSetDigitalLogicFamilyPowerUpState(unknown * deviceName, int32 logicFamily)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2490"""
DAQmxGetErrorString = _stdcall_libraries['nicaiu.dll'].DAQmxGetErrorString
DAQmxGetErrorString.restype = int32
DAQmxGetErrorString.argtypes = [int32, STRING, uInt32]
DAQmxGetErrorString.__doc__ = \
"""int32 DAQmxGetErrorString(int32 errorCode, char * errorString, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2497"""
DAQmxGetExtendedErrorInfo = _stdcall_libraries['nicaiu.dll'].DAQmxGetExtendedErrorInfo
DAQmxGetExtendedErrorInfo.restype = int32
DAQmxGetExtendedErrorInfo.argtypes = [STRING, uInt32]
DAQmxGetExtendedErrorInfo.__doc__ = \
"""int32 DAQmxGetExtendedErrorInfo(char * errorString, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2498"""
DAQmxGetBufInputBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetBufInputBufSize
DAQmxGetBufInputBufSize.restype = int32
DAQmxGetBufInputBufSize.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetBufInputBufSize.__doc__ = \
"""int32 DAQmxGetBufInputBufSize(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2507"""
DAQmxSetBufInputBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetBufInputBufSize
DAQmxSetBufInputBufSize.restype = int32
DAQmxSetBufInputBufSize.argtypes = [TaskHandle, uInt32]
DAQmxSetBufInputBufSize.__doc__ = \
"""int32 DAQmxSetBufInputBufSize(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2508"""
DAQmxResetBufInputBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetBufInputBufSize
DAQmxResetBufInputBufSize.restype = int32
DAQmxResetBufInputBufSize.argtypes = [TaskHandle]
DAQmxResetBufInputBufSize.__doc__ = \
"""int32 DAQmxResetBufInputBufSize(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2509"""
DAQmxGetBufInputOnbrdBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetBufInputOnbrdBufSize
DAQmxGetBufInputOnbrdBufSize.restype = int32
DAQmxGetBufInputOnbrdBufSize.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetBufInputOnbrdBufSize.__doc__ = \
"""int32 DAQmxGetBufInputOnbrdBufSize(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2511"""
DAQmxGetBufOutputBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetBufOutputBufSize
DAQmxGetBufOutputBufSize.restype = int32
DAQmxGetBufOutputBufSize.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetBufOutputBufSize.__doc__ = \
"""int32 DAQmxGetBufOutputBufSize(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2513"""
DAQmxSetBufOutputBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetBufOutputBufSize
DAQmxSetBufOutputBufSize.restype = int32
DAQmxSetBufOutputBufSize.argtypes = [TaskHandle, uInt32]
DAQmxSetBufOutputBufSize.__doc__ = \
"""int32 DAQmxSetBufOutputBufSize(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2514"""
DAQmxResetBufOutputBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetBufOutputBufSize
DAQmxResetBufOutputBufSize.restype = int32
DAQmxResetBufOutputBufSize.argtypes = [TaskHandle]
DAQmxResetBufOutputBufSize.__doc__ = \
"""int32 DAQmxResetBufOutputBufSize(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2515"""
DAQmxGetBufOutputOnbrdBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetBufOutputOnbrdBufSize
DAQmxGetBufOutputOnbrdBufSize.restype = int32
DAQmxGetBufOutputOnbrdBufSize.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetBufOutputOnbrdBufSize.__doc__ = \
"""int32 DAQmxGetBufOutputOnbrdBufSize(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2517"""
DAQmxSetBufOutputOnbrdBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetBufOutputOnbrdBufSize
DAQmxSetBufOutputOnbrdBufSize.restype = int32
DAQmxSetBufOutputOnbrdBufSize.argtypes = [TaskHandle, uInt32]
DAQmxSetBufOutputOnbrdBufSize.__doc__ = \
"""int32 DAQmxSetBufOutputOnbrdBufSize(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2518"""
DAQmxResetBufOutputOnbrdBufSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetBufOutputOnbrdBufSize
DAQmxResetBufOutputOnbrdBufSize.restype = int32
DAQmxResetBufOutputOnbrdBufSize.argtypes = [TaskHandle]
DAQmxResetBufOutputOnbrdBufSize.__doc__ = \
"""int32 DAQmxResetBufOutputOnbrdBufSize(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2519"""
DAQmxGetSelfCalSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetSelfCalSupported
DAQmxGetSelfCalSupported.restype = int32
DAQmxGetSelfCalSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetSelfCalSupported.__doc__ = \
"""int32 DAQmxGetSelfCalSupported(unknown * deviceName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2523"""
DAQmxGetSelfCalLastTemp = _stdcall_libraries['nicaiu.dll'].DAQmxGetSelfCalLastTemp
DAQmxGetSelfCalLastTemp.restype = int32
DAQmxGetSelfCalLastTemp.argtypes = [STRING, POINTER(float64)]
DAQmxGetSelfCalLastTemp.__doc__ = \
"""int32 DAQmxGetSelfCalLastTemp(unknown * deviceName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2525"""
DAQmxGetExtCalRecommendedInterval = _stdcall_libraries['nicaiu.dll'].DAQmxGetExtCalRecommendedInterval
DAQmxGetExtCalRecommendedInterval.restype = int32
DAQmxGetExtCalRecommendedInterval.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetExtCalRecommendedInterval.__doc__ = \
"""int32 DAQmxGetExtCalRecommendedInterval(unknown * deviceName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2527"""
DAQmxGetExtCalLastTemp = _stdcall_libraries['nicaiu.dll'].DAQmxGetExtCalLastTemp
DAQmxGetExtCalLastTemp.restype = int32
DAQmxGetExtCalLastTemp.argtypes = [STRING, POINTER(float64)]
DAQmxGetExtCalLastTemp.__doc__ = \
"""int32 DAQmxGetExtCalLastTemp(unknown * deviceName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2529"""
DAQmxGetCalUserDefinedInfo = _stdcall_libraries['nicaiu.dll'].DAQmxGetCalUserDefinedInfo
DAQmxGetCalUserDefinedInfo.restype = int32
DAQmxGetCalUserDefinedInfo.argtypes = [STRING, STRING, uInt32]
DAQmxGetCalUserDefinedInfo.__doc__ = \
"""int32 DAQmxGetCalUserDefinedInfo(unknown * deviceName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2531"""
DAQmxSetCalUserDefinedInfo = _stdcall_libraries['nicaiu.dll'].DAQmxSetCalUserDefinedInfo
DAQmxSetCalUserDefinedInfo.restype = int32
DAQmxSetCalUserDefinedInfo.argtypes = [STRING, STRING]
DAQmxSetCalUserDefinedInfo.__doc__ = \
"""int32 DAQmxSetCalUserDefinedInfo(unknown * deviceName, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2532"""
DAQmxGetCalUserDefinedInfoMaxSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetCalUserDefinedInfoMaxSize
DAQmxGetCalUserDefinedInfoMaxSize.restype = int32
DAQmxGetCalUserDefinedInfoMaxSize.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetCalUserDefinedInfoMaxSize.__doc__ = \
"""int32 DAQmxGetCalUserDefinedInfoMaxSize(unknown * deviceName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2534"""
DAQmxGetCalDevTemp = _stdcall_libraries['nicaiu.dll'].DAQmxGetCalDevTemp
DAQmxGetCalDevTemp.restype = int32
DAQmxGetCalDevTemp.argtypes = [STRING, POINTER(float64)]
DAQmxGetCalDevTemp.__doc__ = \
"""int32 DAQmxGetCalDevTemp(unknown * deviceName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2536"""
DAQmxGetAIMax = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIMax
DAQmxGetAIMax.restype = int32
DAQmxGetAIMax.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIMax.__doc__ = \
"""int32 DAQmxGetAIMax(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2540"""
DAQmxSetAIMax = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIMax
DAQmxSetAIMax.restype = int32
DAQmxSetAIMax.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIMax.__doc__ = \
"""int32 DAQmxSetAIMax(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2541"""
DAQmxResetAIMax = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIMax
DAQmxResetAIMax.restype = int32
DAQmxResetAIMax.argtypes = [TaskHandle, STRING]
DAQmxResetAIMax.__doc__ = \
"""int32 DAQmxResetAIMax(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2542"""
DAQmxGetAIMin = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIMin
DAQmxGetAIMin.restype = int32
DAQmxGetAIMin.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIMin.__doc__ = \
"""int32 DAQmxGetAIMin(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2544"""
DAQmxSetAIMin = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIMin
DAQmxSetAIMin.restype = int32
DAQmxSetAIMin.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIMin.__doc__ = \
"""int32 DAQmxSetAIMin(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2545"""
DAQmxResetAIMin = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIMin
DAQmxResetAIMin.restype = int32
DAQmxResetAIMin.argtypes = [TaskHandle, STRING]
DAQmxResetAIMin.__doc__ = \
"""int32 DAQmxResetAIMin(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2546"""
DAQmxGetAICustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxGetAICustomScaleName
DAQmxGetAICustomScaleName.restype = int32
DAQmxGetAICustomScaleName.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAICustomScaleName.__doc__ = \
"""int32 DAQmxGetAICustomScaleName(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2548"""
DAQmxSetAICustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxSetAICustomScaleName
DAQmxSetAICustomScaleName.restype = int32
DAQmxSetAICustomScaleName.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAICustomScaleName.__doc__ = \
"""int32 DAQmxSetAICustomScaleName(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2549"""
DAQmxResetAICustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxResetAICustomScaleName
DAQmxResetAICustomScaleName.restype = int32
DAQmxResetAICustomScaleName.argtypes = [TaskHandle, STRING]
DAQmxResetAICustomScaleName.__doc__ = \
"""int32 DAQmxResetAICustomScaleName(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2550"""
DAQmxGetAIMeasType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIMeasType
DAQmxGetAIMeasType.restype = int32
DAQmxGetAIMeasType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIMeasType.__doc__ = \
"""int32 DAQmxGetAIMeasType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2553"""
DAQmxGetAIVoltageUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIVoltageUnits
DAQmxGetAIVoltageUnits.restype = int32
DAQmxGetAIVoltageUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIVoltageUnits.__doc__ = \
"""int32 DAQmxGetAIVoltageUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2556"""
DAQmxSetAIVoltageUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIVoltageUnits
DAQmxSetAIVoltageUnits.restype = int32
DAQmxSetAIVoltageUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIVoltageUnits.__doc__ = \
"""int32 DAQmxSetAIVoltageUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2557"""
DAQmxResetAIVoltageUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIVoltageUnits
DAQmxResetAIVoltageUnits.restype = int32
DAQmxResetAIVoltageUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIVoltageUnits.__doc__ = \
"""int32 DAQmxResetAIVoltageUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2558"""
DAQmxGetAIVoltagedBRef = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIVoltagedBRef
DAQmxGetAIVoltagedBRef.restype = int32
DAQmxGetAIVoltagedBRef.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIVoltagedBRef.__doc__ = \
"""int32 DAQmxGetAIVoltagedBRef(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2560"""
DAQmxSetAIVoltagedBRef = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIVoltagedBRef
DAQmxSetAIVoltagedBRef.restype = int32
DAQmxSetAIVoltagedBRef.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIVoltagedBRef.__doc__ = \
"""int32 DAQmxSetAIVoltagedBRef(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2561"""
DAQmxResetAIVoltagedBRef = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIVoltagedBRef
DAQmxResetAIVoltagedBRef.restype = int32
DAQmxResetAIVoltagedBRef.argtypes = [TaskHandle, STRING]
DAQmxResetAIVoltagedBRef.__doc__ = \
"""int32 DAQmxResetAIVoltagedBRef(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2562"""
DAQmxGetAIVoltageACRMSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIVoltageACRMSUnits
DAQmxGetAIVoltageACRMSUnits.restype = int32
DAQmxGetAIVoltageACRMSUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIVoltageACRMSUnits.__doc__ = \
"""int32 DAQmxGetAIVoltageACRMSUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2565"""
DAQmxSetAIVoltageACRMSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIVoltageACRMSUnits
DAQmxSetAIVoltageACRMSUnits.restype = int32
DAQmxSetAIVoltageACRMSUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIVoltageACRMSUnits.__doc__ = \
"""int32 DAQmxSetAIVoltageACRMSUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2566"""
DAQmxResetAIVoltageACRMSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIVoltageACRMSUnits
DAQmxResetAIVoltageACRMSUnits.restype = int32
DAQmxResetAIVoltageACRMSUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIVoltageACRMSUnits.__doc__ = \
"""int32 DAQmxResetAIVoltageACRMSUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2567"""
DAQmxGetAITempUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAITempUnits
DAQmxGetAITempUnits.restype = int32
DAQmxGetAITempUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAITempUnits.__doc__ = \
"""int32 DAQmxGetAITempUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2570"""
DAQmxSetAITempUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAITempUnits
DAQmxSetAITempUnits.restype = int32
DAQmxSetAITempUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAITempUnits.__doc__ = \
"""int32 DAQmxSetAITempUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2571"""
DAQmxResetAITempUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAITempUnits
DAQmxResetAITempUnits.restype = int32
DAQmxResetAITempUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAITempUnits.__doc__ = \
"""int32 DAQmxResetAITempUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2572"""
DAQmxGetAIThrmcplType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmcplType
DAQmxGetAIThrmcplType.restype = int32
DAQmxGetAIThrmcplType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIThrmcplType.__doc__ = \
"""int32 DAQmxGetAIThrmcplType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2575"""
DAQmxSetAIThrmcplType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmcplType
DAQmxSetAIThrmcplType.restype = int32
DAQmxSetAIThrmcplType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIThrmcplType.__doc__ = \
"""int32 DAQmxSetAIThrmcplType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2576"""
DAQmxResetAIThrmcplType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmcplType
DAQmxResetAIThrmcplType.restype = int32
DAQmxResetAIThrmcplType.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmcplType.__doc__ = \
"""int32 DAQmxResetAIThrmcplType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2577"""
DAQmxGetAIThrmcplScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmcplScaleType
DAQmxGetAIThrmcplScaleType.restype = int32
DAQmxGetAIThrmcplScaleType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIThrmcplScaleType.__doc__ = \
"""int32 DAQmxGetAIThrmcplScaleType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2580"""
DAQmxSetAIThrmcplScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmcplScaleType
DAQmxSetAIThrmcplScaleType.restype = int32
DAQmxSetAIThrmcplScaleType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIThrmcplScaleType.__doc__ = \
"""int32 DAQmxSetAIThrmcplScaleType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2581"""
DAQmxResetAIThrmcplScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmcplScaleType
DAQmxResetAIThrmcplScaleType.restype = int32
DAQmxResetAIThrmcplScaleType.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmcplScaleType.__doc__ = \
"""int32 DAQmxResetAIThrmcplScaleType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2582"""
DAQmxGetAIThrmcplCJCSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmcplCJCSrc
DAQmxGetAIThrmcplCJCSrc.restype = int32
DAQmxGetAIThrmcplCJCSrc.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIThrmcplCJCSrc.__doc__ = \
"""int32 DAQmxGetAIThrmcplCJCSrc(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2585"""
DAQmxGetAIThrmcplCJCVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmcplCJCVal
DAQmxGetAIThrmcplCJCVal.restype = int32
DAQmxGetAIThrmcplCJCVal.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIThrmcplCJCVal.__doc__ = \
"""int32 DAQmxGetAIThrmcplCJCVal(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2587"""
DAQmxSetAIThrmcplCJCVal = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmcplCJCVal
DAQmxSetAIThrmcplCJCVal.restype = int32
DAQmxSetAIThrmcplCJCVal.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIThrmcplCJCVal.__doc__ = \
"""int32 DAQmxSetAIThrmcplCJCVal(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2588"""
DAQmxResetAIThrmcplCJCVal = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmcplCJCVal
DAQmxResetAIThrmcplCJCVal.restype = int32
DAQmxResetAIThrmcplCJCVal.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmcplCJCVal.__doc__ = \
"""int32 DAQmxResetAIThrmcplCJCVal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2589"""
DAQmxGetAIThrmcplCJCChan = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmcplCJCChan
DAQmxGetAIThrmcplCJCChan.restype = int32
DAQmxGetAIThrmcplCJCChan.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAIThrmcplCJCChan.__doc__ = \
"""int32 DAQmxGetAIThrmcplCJCChan(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2591"""
DAQmxGetAIRTDType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRTDType
DAQmxGetAIRTDType.restype = int32
DAQmxGetAIRTDType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIRTDType.__doc__ = \
"""int32 DAQmxGetAIRTDType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2594"""
DAQmxSetAIRTDType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRTDType
DAQmxSetAIRTDType.restype = int32
DAQmxSetAIRTDType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIRTDType.__doc__ = \
"""int32 DAQmxSetAIRTDType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2595"""
DAQmxResetAIRTDType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRTDType
DAQmxResetAIRTDType.restype = int32
DAQmxResetAIRTDType.argtypes = [TaskHandle, STRING]
DAQmxResetAIRTDType.__doc__ = \
"""int32 DAQmxResetAIRTDType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2596"""
DAQmxGetAIRTDR0 = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRTDR0
DAQmxGetAIRTDR0.restype = int32
DAQmxGetAIRTDR0.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRTDR0.__doc__ = \
"""int32 DAQmxGetAIRTDR0(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2598"""
DAQmxSetAIRTDR0 = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRTDR0
DAQmxSetAIRTDR0.restype = int32
DAQmxSetAIRTDR0.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRTDR0.__doc__ = \
"""int32 DAQmxSetAIRTDR0(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2599"""
DAQmxResetAIRTDR0 = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRTDR0
DAQmxResetAIRTDR0.restype = int32
DAQmxResetAIRTDR0.argtypes = [TaskHandle, STRING]
DAQmxResetAIRTDR0.__doc__ = \
"""int32 DAQmxResetAIRTDR0(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2600"""
DAQmxGetAIRTDA = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRTDA
DAQmxGetAIRTDA.restype = int32
DAQmxGetAIRTDA.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRTDA.__doc__ = \
"""int32 DAQmxGetAIRTDA(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2602"""
DAQmxSetAIRTDA = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRTDA
DAQmxSetAIRTDA.restype = int32
DAQmxSetAIRTDA.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRTDA.__doc__ = \
"""int32 DAQmxSetAIRTDA(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2603"""
DAQmxResetAIRTDA = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRTDA
DAQmxResetAIRTDA.restype = int32
DAQmxResetAIRTDA.argtypes = [TaskHandle, STRING]
DAQmxResetAIRTDA.__doc__ = \
"""int32 DAQmxResetAIRTDA(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2604"""
DAQmxGetAIRTDB = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRTDB
DAQmxGetAIRTDB.restype = int32
DAQmxGetAIRTDB.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRTDB.__doc__ = \
"""int32 DAQmxGetAIRTDB(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2606"""
DAQmxSetAIRTDB = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRTDB
DAQmxSetAIRTDB.restype = int32
DAQmxSetAIRTDB.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRTDB.__doc__ = \
"""int32 DAQmxSetAIRTDB(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2607"""
DAQmxResetAIRTDB = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRTDB
DAQmxResetAIRTDB.restype = int32
DAQmxResetAIRTDB.argtypes = [TaskHandle, STRING]
DAQmxResetAIRTDB.__doc__ = \
"""int32 DAQmxResetAIRTDB(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2608"""
DAQmxGetAIRTDC = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRTDC
DAQmxGetAIRTDC.restype = int32
DAQmxGetAIRTDC.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRTDC.__doc__ = \
"""int32 DAQmxGetAIRTDC(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2610"""
DAQmxSetAIRTDC = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRTDC
DAQmxSetAIRTDC.restype = int32
DAQmxSetAIRTDC.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRTDC.__doc__ = \
"""int32 DAQmxSetAIRTDC(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2611"""
DAQmxResetAIRTDC = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRTDC
DAQmxResetAIRTDC.restype = int32
DAQmxResetAIRTDC.argtypes = [TaskHandle, STRING]
DAQmxResetAIRTDC.__doc__ = \
"""int32 DAQmxResetAIRTDC(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2612"""
DAQmxGetAIThrmstrA = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmstrA
DAQmxGetAIThrmstrA.restype = int32
DAQmxGetAIThrmstrA.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIThrmstrA.__doc__ = \
"""int32 DAQmxGetAIThrmstrA(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2614"""
DAQmxSetAIThrmstrA = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmstrA
DAQmxSetAIThrmstrA.restype = int32
DAQmxSetAIThrmstrA.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIThrmstrA.__doc__ = \
"""int32 DAQmxSetAIThrmstrA(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2615"""
DAQmxResetAIThrmstrA = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmstrA
DAQmxResetAIThrmstrA.restype = int32
DAQmxResetAIThrmstrA.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmstrA.__doc__ = \
"""int32 DAQmxResetAIThrmstrA(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2616"""
DAQmxGetAIThrmstrB = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmstrB
DAQmxGetAIThrmstrB.restype = int32
DAQmxGetAIThrmstrB.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIThrmstrB.__doc__ = \
"""int32 DAQmxGetAIThrmstrB(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2618"""
DAQmxSetAIThrmstrB = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmstrB
DAQmxSetAIThrmstrB.restype = int32
DAQmxSetAIThrmstrB.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIThrmstrB.__doc__ = \
"""int32 DAQmxSetAIThrmstrB(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2619"""
DAQmxResetAIThrmstrB = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmstrB
DAQmxResetAIThrmstrB.restype = int32
DAQmxResetAIThrmstrB.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmstrB.__doc__ = \
"""int32 DAQmxResetAIThrmstrB(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2620"""
DAQmxGetAIThrmstrC = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmstrC
DAQmxGetAIThrmstrC.restype = int32
DAQmxGetAIThrmstrC.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIThrmstrC.__doc__ = \
"""int32 DAQmxGetAIThrmstrC(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2622"""
DAQmxSetAIThrmstrC = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmstrC
DAQmxSetAIThrmstrC.restype = int32
DAQmxSetAIThrmstrC.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIThrmstrC.__doc__ = \
"""int32 DAQmxSetAIThrmstrC(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2623"""
DAQmxResetAIThrmstrC = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmstrC
DAQmxResetAIThrmstrC.restype = int32
DAQmxResetAIThrmstrC.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmstrC.__doc__ = \
"""int32 DAQmxResetAIThrmstrC(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2624"""
DAQmxGetAIThrmstrR1 = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIThrmstrR1
DAQmxGetAIThrmstrR1.restype = int32
DAQmxGetAIThrmstrR1.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIThrmstrR1.__doc__ = \
"""int32 DAQmxGetAIThrmstrR1(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2626"""
DAQmxSetAIThrmstrR1 = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIThrmstrR1
DAQmxSetAIThrmstrR1.restype = int32
DAQmxSetAIThrmstrR1.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIThrmstrR1.__doc__ = \
"""int32 DAQmxSetAIThrmstrR1(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2627"""
DAQmxResetAIThrmstrR1 = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIThrmstrR1
DAQmxResetAIThrmstrR1.restype = int32
DAQmxResetAIThrmstrR1.argtypes = [TaskHandle, STRING]
DAQmxResetAIThrmstrR1.__doc__ = \
"""int32 DAQmxResetAIThrmstrR1(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2628"""
DAQmxGetAIForceReadFromChan = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIForceReadFromChan
DAQmxGetAIForceReadFromChan.restype = int32
DAQmxGetAIForceReadFromChan.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIForceReadFromChan.__doc__ = \
"""int32 DAQmxGetAIForceReadFromChan(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2630"""
DAQmxSetAIForceReadFromChan = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIForceReadFromChan
DAQmxSetAIForceReadFromChan.restype = int32
DAQmxSetAIForceReadFromChan.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIForceReadFromChan.__doc__ = \
"""int32 DAQmxSetAIForceReadFromChan(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2631"""
DAQmxResetAIForceReadFromChan = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIForceReadFromChan
DAQmxResetAIForceReadFromChan.restype = int32
DAQmxResetAIForceReadFromChan.argtypes = [TaskHandle, STRING]
DAQmxResetAIForceReadFromChan.__doc__ = \
"""int32 DAQmxResetAIForceReadFromChan(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2632"""
DAQmxGetAICurrentUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAICurrentUnits
DAQmxGetAICurrentUnits.restype = int32
DAQmxGetAICurrentUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAICurrentUnits.__doc__ = \
"""int32 DAQmxGetAICurrentUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2635"""
DAQmxSetAICurrentUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAICurrentUnits
DAQmxSetAICurrentUnits.restype = int32
DAQmxSetAICurrentUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAICurrentUnits.__doc__ = \
"""int32 DAQmxSetAICurrentUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2636"""
DAQmxResetAICurrentUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAICurrentUnits
DAQmxResetAICurrentUnits.restype = int32
DAQmxResetAICurrentUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAICurrentUnits.__doc__ = \
"""int32 DAQmxResetAICurrentUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2637"""
DAQmxGetAICurrentACRMSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAICurrentACRMSUnits
DAQmxGetAICurrentACRMSUnits.restype = int32
DAQmxGetAICurrentACRMSUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAICurrentACRMSUnits.__doc__ = \
"""int32 DAQmxGetAICurrentACRMSUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2640"""
DAQmxSetAICurrentACRMSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAICurrentACRMSUnits
DAQmxSetAICurrentACRMSUnits.restype = int32
DAQmxSetAICurrentACRMSUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAICurrentACRMSUnits.__doc__ = \
"""int32 DAQmxSetAICurrentACRMSUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2641"""
DAQmxResetAICurrentACRMSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAICurrentACRMSUnits
DAQmxResetAICurrentACRMSUnits.restype = int32
DAQmxResetAICurrentACRMSUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAICurrentACRMSUnits.__doc__ = \
"""int32 DAQmxResetAICurrentACRMSUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2642"""
DAQmxGetAIStrainUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIStrainUnits
DAQmxGetAIStrainUnits.restype = int32
DAQmxGetAIStrainUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIStrainUnits.__doc__ = \
"""int32 DAQmxGetAIStrainUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2645"""
DAQmxSetAIStrainUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIStrainUnits
DAQmxSetAIStrainUnits.restype = int32
DAQmxSetAIStrainUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIStrainUnits.__doc__ = \
"""int32 DAQmxSetAIStrainUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2646"""
DAQmxResetAIStrainUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIStrainUnits
DAQmxResetAIStrainUnits.restype = int32
DAQmxResetAIStrainUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIStrainUnits.__doc__ = \
"""int32 DAQmxResetAIStrainUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2647"""
DAQmxGetAIStrainGageGageFactor = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIStrainGageGageFactor
DAQmxGetAIStrainGageGageFactor.restype = int32
DAQmxGetAIStrainGageGageFactor.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIStrainGageGageFactor.__doc__ = \
"""int32 DAQmxGetAIStrainGageGageFactor(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2649"""
DAQmxSetAIStrainGageGageFactor = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIStrainGageGageFactor
DAQmxSetAIStrainGageGageFactor.restype = int32
DAQmxSetAIStrainGageGageFactor.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIStrainGageGageFactor.__doc__ = \
"""int32 DAQmxSetAIStrainGageGageFactor(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2650"""
DAQmxResetAIStrainGageGageFactor = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIStrainGageGageFactor
DAQmxResetAIStrainGageGageFactor.restype = int32
DAQmxResetAIStrainGageGageFactor.argtypes = [TaskHandle, STRING]
DAQmxResetAIStrainGageGageFactor.__doc__ = \
"""int32 DAQmxResetAIStrainGageGageFactor(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2651"""
DAQmxGetAIStrainGagePoissonRatio = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIStrainGagePoissonRatio
DAQmxGetAIStrainGagePoissonRatio.restype = int32
DAQmxGetAIStrainGagePoissonRatio.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIStrainGagePoissonRatio.__doc__ = \
"""int32 DAQmxGetAIStrainGagePoissonRatio(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2653"""
DAQmxSetAIStrainGagePoissonRatio = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIStrainGagePoissonRatio
DAQmxSetAIStrainGagePoissonRatio.restype = int32
DAQmxSetAIStrainGagePoissonRatio.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIStrainGagePoissonRatio.__doc__ = \
"""int32 DAQmxSetAIStrainGagePoissonRatio(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2654"""
DAQmxResetAIStrainGagePoissonRatio = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIStrainGagePoissonRatio
DAQmxResetAIStrainGagePoissonRatio.restype = int32
DAQmxResetAIStrainGagePoissonRatio.argtypes = [TaskHandle, STRING]
DAQmxResetAIStrainGagePoissonRatio.__doc__ = \
"""int32 DAQmxResetAIStrainGagePoissonRatio(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2655"""
DAQmxGetAIStrainGageCfg = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIStrainGageCfg
DAQmxGetAIStrainGageCfg.restype = int32
DAQmxGetAIStrainGageCfg.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIStrainGageCfg.__doc__ = \
"""int32 DAQmxGetAIStrainGageCfg(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2658"""
DAQmxSetAIStrainGageCfg = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIStrainGageCfg
DAQmxSetAIStrainGageCfg.restype = int32
DAQmxSetAIStrainGageCfg.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIStrainGageCfg.__doc__ = \
"""int32 DAQmxSetAIStrainGageCfg(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2659"""
DAQmxResetAIStrainGageCfg = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIStrainGageCfg
DAQmxResetAIStrainGageCfg.restype = int32
DAQmxResetAIStrainGageCfg.argtypes = [TaskHandle, STRING]
DAQmxResetAIStrainGageCfg.__doc__ = \
"""int32 DAQmxResetAIStrainGageCfg(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2660"""
DAQmxGetAIResistanceUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIResistanceUnits
DAQmxGetAIResistanceUnits.restype = int32
DAQmxGetAIResistanceUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIResistanceUnits.__doc__ = \
"""int32 DAQmxGetAIResistanceUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2663"""
DAQmxSetAIResistanceUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIResistanceUnits
DAQmxSetAIResistanceUnits.restype = int32
DAQmxSetAIResistanceUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIResistanceUnits.__doc__ = \
"""int32 DAQmxSetAIResistanceUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2664"""
DAQmxResetAIResistanceUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIResistanceUnits
DAQmxResetAIResistanceUnits.restype = int32
DAQmxResetAIResistanceUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIResistanceUnits.__doc__ = \
"""int32 DAQmxResetAIResistanceUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2665"""
DAQmxGetAIFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIFreqUnits
DAQmxGetAIFreqUnits.restype = int32
DAQmxGetAIFreqUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIFreqUnits.__doc__ = \
"""int32 DAQmxGetAIFreqUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2668"""
DAQmxSetAIFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIFreqUnits
DAQmxSetAIFreqUnits.restype = int32
DAQmxSetAIFreqUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIFreqUnits.__doc__ = \
"""int32 DAQmxSetAIFreqUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2669"""
DAQmxResetAIFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIFreqUnits
DAQmxResetAIFreqUnits.restype = int32
DAQmxResetAIFreqUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIFreqUnits.__doc__ = \
"""int32 DAQmxResetAIFreqUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2670"""
DAQmxGetAIFreqThreshVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIFreqThreshVoltage
DAQmxGetAIFreqThreshVoltage.restype = int32
DAQmxGetAIFreqThreshVoltage.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIFreqThreshVoltage.__doc__ = \
"""int32 DAQmxGetAIFreqThreshVoltage(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2672"""
DAQmxSetAIFreqThreshVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIFreqThreshVoltage
DAQmxSetAIFreqThreshVoltage.restype = int32
DAQmxSetAIFreqThreshVoltage.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIFreqThreshVoltage.__doc__ = \
"""int32 DAQmxSetAIFreqThreshVoltage(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2673"""
DAQmxResetAIFreqThreshVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIFreqThreshVoltage
DAQmxResetAIFreqThreshVoltage.restype = int32
DAQmxResetAIFreqThreshVoltage.argtypes = [TaskHandle, STRING]
DAQmxResetAIFreqThreshVoltage.__doc__ = \
"""int32 DAQmxResetAIFreqThreshVoltage(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2674"""
DAQmxGetAIFreqHyst = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIFreqHyst
DAQmxGetAIFreqHyst.restype = int32
DAQmxGetAIFreqHyst.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIFreqHyst.__doc__ = \
"""int32 DAQmxGetAIFreqHyst(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2676"""
DAQmxSetAIFreqHyst = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIFreqHyst
DAQmxSetAIFreqHyst.restype = int32
DAQmxSetAIFreqHyst.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIFreqHyst.__doc__ = \
"""int32 DAQmxSetAIFreqHyst(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2677"""
DAQmxResetAIFreqHyst = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIFreqHyst
DAQmxResetAIFreqHyst.restype = int32
DAQmxResetAIFreqHyst.argtypes = [TaskHandle, STRING]
DAQmxResetAIFreqHyst.__doc__ = \
"""int32 DAQmxResetAIFreqHyst(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2678"""
DAQmxGetAILVDTUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILVDTUnits
DAQmxGetAILVDTUnits.restype = int32
DAQmxGetAILVDTUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAILVDTUnits.__doc__ = \
"""int32 DAQmxGetAILVDTUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2681"""
DAQmxSetAILVDTUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILVDTUnits
DAQmxSetAILVDTUnits.restype = int32
DAQmxSetAILVDTUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAILVDTUnits.__doc__ = \
"""int32 DAQmxSetAILVDTUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2682"""
DAQmxResetAILVDTUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILVDTUnits
DAQmxResetAILVDTUnits.restype = int32
DAQmxResetAILVDTUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAILVDTUnits.__doc__ = \
"""int32 DAQmxResetAILVDTUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2683"""
DAQmxGetAILVDTSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILVDTSensitivity
DAQmxGetAILVDTSensitivity.restype = int32
DAQmxGetAILVDTSensitivity.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAILVDTSensitivity.__doc__ = \
"""int32 DAQmxGetAILVDTSensitivity(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2685"""
DAQmxSetAILVDTSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILVDTSensitivity
DAQmxSetAILVDTSensitivity.restype = int32
DAQmxSetAILVDTSensitivity.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAILVDTSensitivity.__doc__ = \
"""int32 DAQmxSetAILVDTSensitivity(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2686"""
DAQmxResetAILVDTSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILVDTSensitivity
DAQmxResetAILVDTSensitivity.restype = int32
DAQmxResetAILVDTSensitivity.argtypes = [TaskHandle, STRING]
DAQmxResetAILVDTSensitivity.__doc__ = \
"""int32 DAQmxResetAILVDTSensitivity(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2687"""
DAQmxGetAILVDTSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILVDTSensitivityUnits
DAQmxGetAILVDTSensitivityUnits.restype = int32
DAQmxGetAILVDTSensitivityUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAILVDTSensitivityUnits.__doc__ = \
"""int32 DAQmxGetAILVDTSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2690"""
DAQmxSetAILVDTSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILVDTSensitivityUnits
DAQmxSetAILVDTSensitivityUnits.restype = int32
DAQmxSetAILVDTSensitivityUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAILVDTSensitivityUnits.__doc__ = \
"""int32 DAQmxSetAILVDTSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2691"""
DAQmxResetAILVDTSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILVDTSensitivityUnits
DAQmxResetAILVDTSensitivityUnits.restype = int32
DAQmxResetAILVDTSensitivityUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAILVDTSensitivityUnits.__doc__ = \
"""int32 DAQmxResetAILVDTSensitivityUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2692"""
DAQmxGetAIRVDTUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRVDTUnits
DAQmxGetAIRVDTUnits.restype = int32
DAQmxGetAIRVDTUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIRVDTUnits.__doc__ = \
"""int32 DAQmxGetAIRVDTUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2695"""
DAQmxSetAIRVDTUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRVDTUnits
DAQmxSetAIRVDTUnits.restype = int32
DAQmxSetAIRVDTUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIRVDTUnits.__doc__ = \
"""int32 DAQmxSetAIRVDTUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2696"""
DAQmxResetAIRVDTUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRVDTUnits
DAQmxResetAIRVDTUnits.restype = int32
DAQmxResetAIRVDTUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIRVDTUnits.__doc__ = \
"""int32 DAQmxResetAIRVDTUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2697"""
DAQmxGetAIRVDTSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRVDTSensitivity
DAQmxGetAIRVDTSensitivity.restype = int32
DAQmxGetAIRVDTSensitivity.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRVDTSensitivity.__doc__ = \
"""int32 DAQmxGetAIRVDTSensitivity(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2699"""
DAQmxSetAIRVDTSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRVDTSensitivity
DAQmxSetAIRVDTSensitivity.restype = int32
DAQmxSetAIRVDTSensitivity.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRVDTSensitivity.__doc__ = \
"""int32 DAQmxSetAIRVDTSensitivity(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2700"""
DAQmxResetAIRVDTSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRVDTSensitivity
DAQmxResetAIRVDTSensitivity.restype = int32
DAQmxResetAIRVDTSensitivity.argtypes = [TaskHandle, STRING]
DAQmxResetAIRVDTSensitivity.__doc__ = \
"""int32 DAQmxResetAIRVDTSensitivity(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2701"""
DAQmxGetAIRVDTSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRVDTSensitivityUnits
DAQmxGetAIRVDTSensitivityUnits.restype = int32
DAQmxGetAIRVDTSensitivityUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIRVDTSensitivityUnits.__doc__ = \
"""int32 DAQmxGetAIRVDTSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2704"""
DAQmxSetAIRVDTSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRVDTSensitivityUnits
DAQmxSetAIRVDTSensitivityUnits.restype = int32
DAQmxSetAIRVDTSensitivityUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIRVDTSensitivityUnits.__doc__ = \
"""int32 DAQmxSetAIRVDTSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2705"""
DAQmxResetAIRVDTSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRVDTSensitivityUnits
DAQmxResetAIRVDTSensitivityUnits.restype = int32
DAQmxResetAIRVDTSensitivityUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIRVDTSensitivityUnits.__doc__ = \
"""int32 DAQmxResetAIRVDTSensitivityUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2706"""
DAQmxGetAIEddyCurrentProxProbeUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIEddyCurrentProxProbeUnits
DAQmxGetAIEddyCurrentProxProbeUnits.restype = int32
DAQmxGetAIEddyCurrentProxProbeUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIEddyCurrentProxProbeUnits.__doc__ = \
"""int32 DAQmxGetAIEddyCurrentProxProbeUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2709"""
DAQmxSetAIEddyCurrentProxProbeUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIEddyCurrentProxProbeUnits
DAQmxSetAIEddyCurrentProxProbeUnits.restype = int32
DAQmxSetAIEddyCurrentProxProbeUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIEddyCurrentProxProbeUnits.__doc__ = \
"""int32 DAQmxSetAIEddyCurrentProxProbeUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2710"""
DAQmxResetAIEddyCurrentProxProbeUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIEddyCurrentProxProbeUnits
DAQmxResetAIEddyCurrentProxProbeUnits.restype = int32
DAQmxResetAIEddyCurrentProxProbeUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIEddyCurrentProxProbeUnits.__doc__ = \
"""int32 DAQmxResetAIEddyCurrentProxProbeUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2711"""
DAQmxGetAIEddyCurrentProxProbeSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIEddyCurrentProxProbeSensitivity
DAQmxGetAIEddyCurrentProxProbeSensitivity.restype = int32
DAQmxGetAIEddyCurrentProxProbeSensitivity.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIEddyCurrentProxProbeSensitivity.__doc__ = \
"""int32 DAQmxGetAIEddyCurrentProxProbeSensitivity(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2713"""
DAQmxSetAIEddyCurrentProxProbeSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIEddyCurrentProxProbeSensitivity
DAQmxSetAIEddyCurrentProxProbeSensitivity.restype = int32
DAQmxSetAIEddyCurrentProxProbeSensitivity.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIEddyCurrentProxProbeSensitivity.__doc__ = \
"""int32 DAQmxSetAIEddyCurrentProxProbeSensitivity(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2714"""
DAQmxResetAIEddyCurrentProxProbeSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIEddyCurrentProxProbeSensitivity
DAQmxResetAIEddyCurrentProxProbeSensitivity.restype = int32
DAQmxResetAIEddyCurrentProxProbeSensitivity.argtypes = [TaskHandle, STRING]
DAQmxResetAIEddyCurrentProxProbeSensitivity.__doc__ = \
"""int32 DAQmxResetAIEddyCurrentProxProbeSensitivity(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2715"""
DAQmxGetAIEddyCurrentProxProbeSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIEddyCurrentProxProbeSensitivityUnits
DAQmxGetAIEddyCurrentProxProbeSensitivityUnits.restype = int32
DAQmxGetAIEddyCurrentProxProbeSensitivityUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIEddyCurrentProxProbeSensitivityUnits.__doc__ = \
"""int32 DAQmxGetAIEddyCurrentProxProbeSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2718"""
DAQmxSetAIEddyCurrentProxProbeSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIEddyCurrentProxProbeSensitivityUnits
DAQmxSetAIEddyCurrentProxProbeSensitivityUnits.restype = int32
DAQmxSetAIEddyCurrentProxProbeSensitivityUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIEddyCurrentProxProbeSensitivityUnits.__doc__ = \
"""int32 DAQmxSetAIEddyCurrentProxProbeSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2719"""
DAQmxResetAIEddyCurrentProxProbeSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIEddyCurrentProxProbeSensitivityUnits
DAQmxResetAIEddyCurrentProxProbeSensitivityUnits.restype = int32
DAQmxResetAIEddyCurrentProxProbeSensitivityUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIEddyCurrentProxProbeSensitivityUnits.__doc__ = \
"""int32 DAQmxResetAIEddyCurrentProxProbeSensitivityUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2720"""
DAQmxGetAISoundPressureMaxSoundPressureLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetAISoundPressureMaxSoundPressureLvl
DAQmxGetAISoundPressureMaxSoundPressureLvl.restype = int32
DAQmxGetAISoundPressureMaxSoundPressureLvl.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAISoundPressureMaxSoundPressureLvl.__doc__ = \
"""int32 DAQmxGetAISoundPressureMaxSoundPressureLvl(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2722"""
DAQmxSetAISoundPressureMaxSoundPressureLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetAISoundPressureMaxSoundPressureLvl
DAQmxSetAISoundPressureMaxSoundPressureLvl.restype = int32
DAQmxSetAISoundPressureMaxSoundPressureLvl.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAISoundPressureMaxSoundPressureLvl.__doc__ = \
"""int32 DAQmxSetAISoundPressureMaxSoundPressureLvl(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2723"""
DAQmxResetAISoundPressureMaxSoundPressureLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetAISoundPressureMaxSoundPressureLvl
DAQmxResetAISoundPressureMaxSoundPressureLvl.restype = int32
DAQmxResetAISoundPressureMaxSoundPressureLvl.argtypes = [TaskHandle, STRING]
DAQmxResetAISoundPressureMaxSoundPressureLvl.__doc__ = \
"""int32 DAQmxResetAISoundPressureMaxSoundPressureLvl(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2724"""
DAQmxGetAISoundPressureUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAISoundPressureUnits
DAQmxGetAISoundPressureUnits.restype = int32
DAQmxGetAISoundPressureUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAISoundPressureUnits.__doc__ = \
"""int32 DAQmxGetAISoundPressureUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2727"""
DAQmxSetAISoundPressureUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAISoundPressureUnits
DAQmxSetAISoundPressureUnits.restype = int32
DAQmxSetAISoundPressureUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAISoundPressureUnits.__doc__ = \
"""int32 DAQmxSetAISoundPressureUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2728"""
DAQmxResetAISoundPressureUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAISoundPressureUnits
DAQmxResetAISoundPressureUnits.restype = int32
DAQmxResetAISoundPressureUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAISoundPressureUnits.__doc__ = \
"""int32 DAQmxResetAISoundPressureUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2729"""
DAQmxGetAISoundPressuredBRef = _stdcall_libraries['nicaiu.dll'].DAQmxGetAISoundPressuredBRef
DAQmxGetAISoundPressuredBRef.restype = int32
DAQmxGetAISoundPressuredBRef.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAISoundPressuredBRef.__doc__ = \
"""int32 DAQmxGetAISoundPressuredBRef(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2731"""
DAQmxSetAISoundPressuredBRef = _stdcall_libraries['nicaiu.dll'].DAQmxSetAISoundPressuredBRef
DAQmxSetAISoundPressuredBRef.restype = int32
DAQmxSetAISoundPressuredBRef.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAISoundPressuredBRef.__doc__ = \
"""int32 DAQmxSetAISoundPressuredBRef(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2732"""
DAQmxResetAISoundPressuredBRef = _stdcall_libraries['nicaiu.dll'].DAQmxResetAISoundPressuredBRef
DAQmxResetAISoundPressuredBRef.restype = int32
DAQmxResetAISoundPressuredBRef.argtypes = [TaskHandle, STRING]
DAQmxResetAISoundPressuredBRef.__doc__ = \
"""int32 DAQmxResetAISoundPressuredBRef(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2733"""
DAQmxGetAIMicrophoneSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIMicrophoneSensitivity
DAQmxGetAIMicrophoneSensitivity.restype = int32
DAQmxGetAIMicrophoneSensitivity.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIMicrophoneSensitivity.__doc__ = \
"""int32 DAQmxGetAIMicrophoneSensitivity(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2735"""
DAQmxSetAIMicrophoneSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIMicrophoneSensitivity
DAQmxSetAIMicrophoneSensitivity.restype = int32
DAQmxSetAIMicrophoneSensitivity.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIMicrophoneSensitivity.__doc__ = \
"""int32 DAQmxSetAIMicrophoneSensitivity(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2736"""
DAQmxResetAIMicrophoneSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIMicrophoneSensitivity
DAQmxResetAIMicrophoneSensitivity.restype = int32
DAQmxResetAIMicrophoneSensitivity.argtypes = [TaskHandle, STRING]
DAQmxResetAIMicrophoneSensitivity.__doc__ = \
"""int32 DAQmxResetAIMicrophoneSensitivity(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2737"""
DAQmxGetAIAccelUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIAccelUnits
DAQmxGetAIAccelUnits.restype = int32
DAQmxGetAIAccelUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIAccelUnits.__doc__ = \
"""int32 DAQmxGetAIAccelUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2740"""
DAQmxSetAIAccelUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIAccelUnits
DAQmxSetAIAccelUnits.restype = int32
DAQmxSetAIAccelUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIAccelUnits.__doc__ = \
"""int32 DAQmxSetAIAccelUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2741"""
DAQmxResetAIAccelUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIAccelUnits
DAQmxResetAIAccelUnits.restype = int32
DAQmxResetAIAccelUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIAccelUnits.__doc__ = \
"""int32 DAQmxResetAIAccelUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2742"""
DAQmxGetAIAcceldBRef = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIAcceldBRef
DAQmxGetAIAcceldBRef.restype = int32
DAQmxGetAIAcceldBRef.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIAcceldBRef.__doc__ = \
"""int32 DAQmxGetAIAcceldBRef(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2744"""
DAQmxSetAIAcceldBRef = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIAcceldBRef
DAQmxSetAIAcceldBRef.restype = int32
DAQmxSetAIAcceldBRef.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIAcceldBRef.__doc__ = \
"""int32 DAQmxSetAIAcceldBRef(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2745"""
DAQmxResetAIAcceldBRef = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIAcceldBRef
DAQmxResetAIAcceldBRef.restype = int32
DAQmxResetAIAcceldBRef.argtypes = [TaskHandle, STRING]
DAQmxResetAIAcceldBRef.__doc__ = \
"""int32 DAQmxResetAIAcceldBRef(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2746"""
DAQmxGetAIAccelSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIAccelSensitivity
DAQmxGetAIAccelSensitivity.restype = int32
DAQmxGetAIAccelSensitivity.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIAccelSensitivity.__doc__ = \
"""int32 DAQmxGetAIAccelSensitivity(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2748"""
DAQmxSetAIAccelSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIAccelSensitivity
DAQmxSetAIAccelSensitivity.restype = int32
DAQmxSetAIAccelSensitivity.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIAccelSensitivity.__doc__ = \
"""int32 DAQmxSetAIAccelSensitivity(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2749"""
DAQmxResetAIAccelSensitivity = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIAccelSensitivity
DAQmxResetAIAccelSensitivity.restype = int32
DAQmxResetAIAccelSensitivity.argtypes = [TaskHandle, STRING]
DAQmxResetAIAccelSensitivity.__doc__ = \
"""int32 DAQmxResetAIAccelSensitivity(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2750"""
DAQmxGetAIAccelSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIAccelSensitivityUnits
DAQmxGetAIAccelSensitivityUnits.restype = int32
DAQmxGetAIAccelSensitivityUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIAccelSensitivityUnits.__doc__ = \
"""int32 DAQmxGetAIAccelSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2753"""
DAQmxSetAIAccelSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIAccelSensitivityUnits
DAQmxSetAIAccelSensitivityUnits.restype = int32
DAQmxSetAIAccelSensitivityUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIAccelSensitivityUnits.__doc__ = \
"""int32 DAQmxSetAIAccelSensitivityUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2754"""
DAQmxResetAIAccelSensitivityUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIAccelSensitivityUnits
DAQmxResetAIAccelSensitivityUnits.restype = int32
DAQmxResetAIAccelSensitivityUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAIAccelSensitivityUnits.__doc__ = \
"""int32 DAQmxResetAIAccelSensitivityUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2755"""
DAQmxGetAIIsTEDS = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIIsTEDS
DAQmxGetAIIsTEDS.restype = int32
DAQmxGetAIIsTEDS.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIIsTEDS.__doc__ = \
"""int32 DAQmxGetAIIsTEDS(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2757"""
DAQmxGetAITEDSUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAITEDSUnits
DAQmxGetAITEDSUnits.restype = int32
DAQmxGetAITEDSUnits.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAITEDSUnits.__doc__ = \
"""int32 DAQmxGetAITEDSUnits(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2759"""
DAQmxGetAICoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAICoupling
DAQmxGetAICoupling.restype = int32
DAQmxGetAICoupling.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAICoupling.__doc__ = \
"""int32 DAQmxGetAICoupling(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2762"""
DAQmxSetAICoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAICoupling
DAQmxSetAICoupling.restype = int32
DAQmxSetAICoupling.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAICoupling.__doc__ = \
"""int32 DAQmxSetAICoupling(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2763"""
DAQmxResetAICoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAICoupling
DAQmxResetAICoupling.restype = int32
DAQmxResetAICoupling.argtypes = [TaskHandle, STRING]
DAQmxResetAICoupling.__doc__ = \
"""int32 DAQmxResetAICoupling(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2764"""
DAQmxGetAIImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIImpedance
DAQmxGetAIImpedance.restype = int32
DAQmxGetAIImpedance.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIImpedance.__doc__ = \
"""int32 DAQmxGetAIImpedance(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2767"""
DAQmxSetAIImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIImpedance
DAQmxSetAIImpedance.restype = int32
DAQmxSetAIImpedance.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIImpedance.__doc__ = \
"""int32 DAQmxSetAIImpedance(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2768"""
DAQmxResetAIImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIImpedance
DAQmxResetAIImpedance.restype = int32
DAQmxResetAIImpedance.argtypes = [TaskHandle, STRING]
DAQmxResetAIImpedance.__doc__ = \
"""int32 DAQmxResetAIImpedance(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2769"""
DAQmxGetAITermCfg = _stdcall_libraries['nicaiu.dll'].DAQmxGetAITermCfg
DAQmxGetAITermCfg.restype = int32
DAQmxGetAITermCfg.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAITermCfg.__doc__ = \
"""int32 DAQmxGetAITermCfg(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2772"""
DAQmxSetAITermCfg = _stdcall_libraries['nicaiu.dll'].DAQmxSetAITermCfg
DAQmxSetAITermCfg.restype = int32
DAQmxSetAITermCfg.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAITermCfg.__doc__ = \
"""int32 DAQmxSetAITermCfg(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2773"""
DAQmxResetAITermCfg = _stdcall_libraries['nicaiu.dll'].DAQmxResetAITermCfg
DAQmxResetAITermCfg.restype = int32
DAQmxResetAITermCfg.argtypes = [TaskHandle, STRING]
DAQmxResetAITermCfg.__doc__ = \
"""int32 DAQmxResetAITermCfg(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2774"""
DAQmxGetAIInputSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIInputSrc
DAQmxGetAIInputSrc.restype = int32
DAQmxGetAIInputSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAIInputSrc.__doc__ = \
"""int32 DAQmxGetAIInputSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2776"""
DAQmxSetAIInputSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIInputSrc
DAQmxSetAIInputSrc.restype = int32
DAQmxSetAIInputSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAIInputSrc.__doc__ = \
"""int32 DAQmxSetAIInputSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2777"""
DAQmxResetAIInputSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIInputSrc
DAQmxResetAIInputSrc.restype = int32
DAQmxResetAIInputSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAIInputSrc.__doc__ = \
"""int32 DAQmxResetAIInputSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2778"""
DAQmxGetAIResistanceCfg = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIResistanceCfg
DAQmxGetAIResistanceCfg.restype = int32
DAQmxGetAIResistanceCfg.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIResistanceCfg.__doc__ = \
"""int32 DAQmxGetAIResistanceCfg(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2781"""
DAQmxSetAIResistanceCfg = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIResistanceCfg
DAQmxSetAIResistanceCfg.restype = int32
DAQmxSetAIResistanceCfg.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIResistanceCfg.__doc__ = \
"""int32 DAQmxSetAIResistanceCfg(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2782"""
DAQmxResetAIResistanceCfg = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIResistanceCfg
DAQmxResetAIResistanceCfg.restype = int32
DAQmxResetAIResistanceCfg.argtypes = [TaskHandle, STRING]
DAQmxResetAIResistanceCfg.__doc__ = \
"""int32 DAQmxResetAIResistanceCfg(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2783"""
DAQmxGetAILeadWireResistance = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILeadWireResistance
DAQmxGetAILeadWireResistance.restype = int32
DAQmxGetAILeadWireResistance.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAILeadWireResistance.__doc__ = \
"""int32 DAQmxGetAILeadWireResistance(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2785"""
DAQmxSetAILeadWireResistance = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILeadWireResistance
DAQmxSetAILeadWireResistance.restype = int32
DAQmxSetAILeadWireResistance.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAILeadWireResistance.__doc__ = \
"""int32 DAQmxSetAILeadWireResistance(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2786"""
DAQmxResetAILeadWireResistance = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILeadWireResistance
DAQmxResetAILeadWireResistance.restype = int32
DAQmxResetAILeadWireResistance.argtypes = [TaskHandle, STRING]
DAQmxResetAILeadWireResistance.__doc__ = \
"""int32 DAQmxResetAILeadWireResistance(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2787"""
DAQmxGetAIBridgeCfg = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeCfg
DAQmxGetAIBridgeCfg.restype = int32
DAQmxGetAIBridgeCfg.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIBridgeCfg.__doc__ = \
"""int32 DAQmxGetAIBridgeCfg(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2790"""
DAQmxSetAIBridgeCfg = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeCfg
DAQmxSetAIBridgeCfg.restype = int32
DAQmxSetAIBridgeCfg.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIBridgeCfg.__doc__ = \
"""int32 DAQmxSetAIBridgeCfg(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2791"""
DAQmxResetAIBridgeCfg = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeCfg
DAQmxResetAIBridgeCfg.restype = int32
DAQmxResetAIBridgeCfg.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeCfg.__doc__ = \
"""int32 DAQmxResetAIBridgeCfg(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2792"""
DAQmxGetAIBridgeNomResistance = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeNomResistance
DAQmxGetAIBridgeNomResistance.restype = int32
DAQmxGetAIBridgeNomResistance.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIBridgeNomResistance.__doc__ = \
"""int32 DAQmxGetAIBridgeNomResistance(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2794"""
DAQmxSetAIBridgeNomResistance = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeNomResistance
DAQmxSetAIBridgeNomResistance.restype = int32
DAQmxSetAIBridgeNomResistance.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIBridgeNomResistance.__doc__ = \
"""int32 DAQmxSetAIBridgeNomResistance(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2795"""
DAQmxResetAIBridgeNomResistance = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeNomResistance
DAQmxResetAIBridgeNomResistance.restype = int32
DAQmxResetAIBridgeNomResistance.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeNomResistance.__doc__ = \
"""int32 DAQmxResetAIBridgeNomResistance(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2796"""
DAQmxGetAIBridgeInitialVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeInitialVoltage
DAQmxGetAIBridgeInitialVoltage.restype = int32
DAQmxGetAIBridgeInitialVoltage.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIBridgeInitialVoltage.__doc__ = \
"""int32 DAQmxGetAIBridgeInitialVoltage(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2798"""
DAQmxSetAIBridgeInitialVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeInitialVoltage
DAQmxSetAIBridgeInitialVoltage.restype = int32
DAQmxSetAIBridgeInitialVoltage.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIBridgeInitialVoltage.__doc__ = \
"""int32 DAQmxSetAIBridgeInitialVoltage(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2799"""
DAQmxResetAIBridgeInitialVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeInitialVoltage
DAQmxResetAIBridgeInitialVoltage.restype = int32
DAQmxResetAIBridgeInitialVoltage.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeInitialVoltage.__doc__ = \
"""int32 DAQmxResetAIBridgeInitialVoltage(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2800"""
DAQmxGetAIBridgeShuntCalEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeShuntCalEnable
DAQmxGetAIBridgeShuntCalEnable.restype = int32
DAQmxGetAIBridgeShuntCalEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIBridgeShuntCalEnable.__doc__ = \
"""int32 DAQmxGetAIBridgeShuntCalEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2802"""
DAQmxSetAIBridgeShuntCalEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeShuntCalEnable
DAQmxSetAIBridgeShuntCalEnable.restype = int32
DAQmxSetAIBridgeShuntCalEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIBridgeShuntCalEnable.__doc__ = \
"""int32 DAQmxSetAIBridgeShuntCalEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2803"""
DAQmxResetAIBridgeShuntCalEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeShuntCalEnable
DAQmxResetAIBridgeShuntCalEnable.restype = int32
DAQmxResetAIBridgeShuntCalEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeShuntCalEnable.__doc__ = \
"""int32 DAQmxResetAIBridgeShuntCalEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2804"""
DAQmxGetAIBridgeShuntCalSelect = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeShuntCalSelect
DAQmxGetAIBridgeShuntCalSelect.restype = int32
DAQmxGetAIBridgeShuntCalSelect.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIBridgeShuntCalSelect.__doc__ = \
"""int32 DAQmxGetAIBridgeShuntCalSelect(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2807"""
DAQmxSetAIBridgeShuntCalSelect = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeShuntCalSelect
DAQmxSetAIBridgeShuntCalSelect.restype = int32
DAQmxSetAIBridgeShuntCalSelect.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIBridgeShuntCalSelect.__doc__ = \
"""int32 DAQmxSetAIBridgeShuntCalSelect(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2808"""
DAQmxResetAIBridgeShuntCalSelect = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeShuntCalSelect
DAQmxResetAIBridgeShuntCalSelect.restype = int32
DAQmxResetAIBridgeShuntCalSelect.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeShuntCalSelect.__doc__ = \
"""int32 DAQmxResetAIBridgeShuntCalSelect(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2809"""
DAQmxGetAIBridgeShuntCalGainAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeShuntCalGainAdjust
DAQmxGetAIBridgeShuntCalGainAdjust.restype = int32
DAQmxGetAIBridgeShuntCalGainAdjust.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIBridgeShuntCalGainAdjust.__doc__ = \
"""int32 DAQmxGetAIBridgeShuntCalGainAdjust(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2811"""
DAQmxSetAIBridgeShuntCalGainAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeShuntCalGainAdjust
DAQmxSetAIBridgeShuntCalGainAdjust.restype = int32
DAQmxSetAIBridgeShuntCalGainAdjust.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIBridgeShuntCalGainAdjust.__doc__ = \
"""int32 DAQmxSetAIBridgeShuntCalGainAdjust(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2812"""
DAQmxResetAIBridgeShuntCalGainAdjust = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeShuntCalGainAdjust
DAQmxResetAIBridgeShuntCalGainAdjust.restype = int32
DAQmxResetAIBridgeShuntCalGainAdjust.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeShuntCalGainAdjust.__doc__ = \
"""int32 DAQmxResetAIBridgeShuntCalGainAdjust(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2813"""
DAQmxGetAIBridgeBalanceCoarsePot = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeBalanceCoarsePot
DAQmxGetAIBridgeBalanceCoarsePot.restype = int32
DAQmxGetAIBridgeBalanceCoarsePot.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIBridgeBalanceCoarsePot.__doc__ = \
"""int32 DAQmxGetAIBridgeBalanceCoarsePot(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2815"""
DAQmxSetAIBridgeBalanceCoarsePot = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeBalanceCoarsePot
DAQmxSetAIBridgeBalanceCoarsePot.restype = int32
DAQmxSetAIBridgeBalanceCoarsePot.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIBridgeBalanceCoarsePot.__doc__ = \
"""int32 DAQmxSetAIBridgeBalanceCoarsePot(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2816"""
DAQmxResetAIBridgeBalanceCoarsePot = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeBalanceCoarsePot
DAQmxResetAIBridgeBalanceCoarsePot.restype = int32
DAQmxResetAIBridgeBalanceCoarsePot.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeBalanceCoarsePot.__doc__ = \
"""int32 DAQmxResetAIBridgeBalanceCoarsePot(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2817"""
DAQmxGetAIBridgeBalanceFinePot = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIBridgeBalanceFinePot
DAQmxGetAIBridgeBalanceFinePot.restype = int32
DAQmxGetAIBridgeBalanceFinePot.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIBridgeBalanceFinePot.__doc__ = \
"""int32 DAQmxGetAIBridgeBalanceFinePot(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2819"""
DAQmxSetAIBridgeBalanceFinePot = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIBridgeBalanceFinePot
DAQmxSetAIBridgeBalanceFinePot.restype = int32
DAQmxSetAIBridgeBalanceFinePot.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIBridgeBalanceFinePot.__doc__ = \
"""int32 DAQmxSetAIBridgeBalanceFinePot(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2820"""
DAQmxResetAIBridgeBalanceFinePot = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIBridgeBalanceFinePot
DAQmxResetAIBridgeBalanceFinePot.restype = int32
DAQmxResetAIBridgeBalanceFinePot.argtypes = [TaskHandle, STRING]
DAQmxResetAIBridgeBalanceFinePot.__doc__ = \
"""int32 DAQmxResetAIBridgeBalanceFinePot(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2821"""
DAQmxGetAICurrentShuntLoc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAICurrentShuntLoc
DAQmxGetAICurrentShuntLoc.restype = int32
DAQmxGetAICurrentShuntLoc.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAICurrentShuntLoc.__doc__ = \
"""int32 DAQmxGetAICurrentShuntLoc(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2824"""
DAQmxSetAICurrentShuntLoc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAICurrentShuntLoc
DAQmxSetAICurrentShuntLoc.restype = int32
DAQmxSetAICurrentShuntLoc.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAICurrentShuntLoc.__doc__ = \
"""int32 DAQmxSetAICurrentShuntLoc(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2825"""
DAQmxResetAICurrentShuntLoc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAICurrentShuntLoc
DAQmxResetAICurrentShuntLoc.restype = int32
DAQmxResetAICurrentShuntLoc.argtypes = [TaskHandle, STRING]
DAQmxResetAICurrentShuntLoc.__doc__ = \
"""int32 DAQmxResetAICurrentShuntLoc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2826"""
DAQmxGetAICurrentShuntResistance = _stdcall_libraries['nicaiu.dll'].DAQmxGetAICurrentShuntResistance
DAQmxGetAICurrentShuntResistance.restype = int32
DAQmxGetAICurrentShuntResistance.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAICurrentShuntResistance.__doc__ = \
"""int32 DAQmxGetAICurrentShuntResistance(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2828"""
DAQmxSetAICurrentShuntResistance = _stdcall_libraries['nicaiu.dll'].DAQmxSetAICurrentShuntResistance
DAQmxSetAICurrentShuntResistance.restype = int32
DAQmxSetAICurrentShuntResistance.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAICurrentShuntResistance.__doc__ = \
"""int32 DAQmxSetAICurrentShuntResistance(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2829"""
DAQmxResetAICurrentShuntResistance = _stdcall_libraries['nicaiu.dll'].DAQmxResetAICurrentShuntResistance
DAQmxResetAICurrentShuntResistance.restype = int32
DAQmxResetAICurrentShuntResistance.argtypes = [TaskHandle, STRING]
DAQmxResetAICurrentShuntResistance.__doc__ = \
"""int32 DAQmxResetAICurrentShuntResistance(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2830"""
DAQmxGetAIExcitSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitSrc
DAQmxGetAIExcitSrc.restype = int32
DAQmxGetAIExcitSrc.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIExcitSrc.__doc__ = \
"""int32 DAQmxGetAIExcitSrc(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2833"""
DAQmxSetAIExcitSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitSrc
DAQmxSetAIExcitSrc.restype = int32
DAQmxSetAIExcitSrc.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIExcitSrc.__doc__ = \
"""int32 DAQmxSetAIExcitSrc(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2834"""
DAQmxResetAIExcitSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitSrc
DAQmxResetAIExcitSrc.restype = int32
DAQmxResetAIExcitSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitSrc.__doc__ = \
"""int32 DAQmxResetAIExcitSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2835"""
DAQmxGetAIExcitVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitVal
DAQmxGetAIExcitVal.restype = int32
DAQmxGetAIExcitVal.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIExcitVal.__doc__ = \
"""int32 DAQmxGetAIExcitVal(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2837"""
DAQmxSetAIExcitVal = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitVal
DAQmxSetAIExcitVal.restype = int32
DAQmxSetAIExcitVal.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIExcitVal.__doc__ = \
"""int32 DAQmxSetAIExcitVal(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2838"""
DAQmxResetAIExcitVal = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitVal
DAQmxResetAIExcitVal.restype = int32
DAQmxResetAIExcitVal.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitVal.__doc__ = \
"""int32 DAQmxResetAIExcitVal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2839"""
DAQmxGetAIExcitUseForScaling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitUseForScaling
DAQmxGetAIExcitUseForScaling.restype = int32
DAQmxGetAIExcitUseForScaling.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIExcitUseForScaling.__doc__ = \
"""int32 DAQmxGetAIExcitUseForScaling(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2841"""
DAQmxSetAIExcitUseForScaling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitUseForScaling
DAQmxSetAIExcitUseForScaling.restype = int32
DAQmxSetAIExcitUseForScaling.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIExcitUseForScaling.__doc__ = \
"""int32 DAQmxSetAIExcitUseForScaling(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2842"""
DAQmxResetAIExcitUseForScaling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitUseForScaling
DAQmxResetAIExcitUseForScaling.restype = int32
DAQmxResetAIExcitUseForScaling.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitUseForScaling.__doc__ = \
"""int32 DAQmxResetAIExcitUseForScaling(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2843"""
DAQmxGetAIExcitUseMultiplexed = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitUseMultiplexed
DAQmxGetAIExcitUseMultiplexed.restype = int32
DAQmxGetAIExcitUseMultiplexed.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIExcitUseMultiplexed.__doc__ = \
"""int32 DAQmxGetAIExcitUseMultiplexed(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2845"""
DAQmxSetAIExcitUseMultiplexed = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitUseMultiplexed
DAQmxSetAIExcitUseMultiplexed.restype = int32
DAQmxSetAIExcitUseMultiplexed.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIExcitUseMultiplexed.__doc__ = \
"""int32 DAQmxSetAIExcitUseMultiplexed(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2846"""
DAQmxResetAIExcitUseMultiplexed = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitUseMultiplexed
DAQmxResetAIExcitUseMultiplexed.restype = int32
DAQmxResetAIExcitUseMultiplexed.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitUseMultiplexed.__doc__ = \
"""int32 DAQmxResetAIExcitUseMultiplexed(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2847"""
DAQmxGetAIExcitActualVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitActualVal
DAQmxGetAIExcitActualVal.restype = int32
DAQmxGetAIExcitActualVal.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIExcitActualVal.__doc__ = \
"""int32 DAQmxGetAIExcitActualVal(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2849"""
DAQmxSetAIExcitActualVal = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitActualVal
DAQmxSetAIExcitActualVal.restype = int32
DAQmxSetAIExcitActualVal.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIExcitActualVal.__doc__ = \
"""int32 DAQmxSetAIExcitActualVal(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2850"""
DAQmxResetAIExcitActualVal = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitActualVal
DAQmxResetAIExcitActualVal.restype = int32
DAQmxResetAIExcitActualVal.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitActualVal.__doc__ = \
"""int32 DAQmxResetAIExcitActualVal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2851"""
DAQmxGetAIExcitDCorAC = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitDCorAC
DAQmxGetAIExcitDCorAC.restype = int32
DAQmxGetAIExcitDCorAC.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIExcitDCorAC.__doc__ = \
"""int32 DAQmxGetAIExcitDCorAC(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2854"""
DAQmxSetAIExcitDCorAC = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitDCorAC
DAQmxSetAIExcitDCorAC.restype = int32
DAQmxSetAIExcitDCorAC.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIExcitDCorAC.__doc__ = \
"""int32 DAQmxSetAIExcitDCorAC(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2855"""
DAQmxResetAIExcitDCorAC = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitDCorAC
DAQmxResetAIExcitDCorAC.restype = int32
DAQmxResetAIExcitDCorAC.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitDCorAC.__doc__ = \
"""int32 DAQmxResetAIExcitDCorAC(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2856"""
DAQmxGetAIExcitVoltageOrCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIExcitVoltageOrCurrent
DAQmxGetAIExcitVoltageOrCurrent.restype = int32
DAQmxGetAIExcitVoltageOrCurrent.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIExcitVoltageOrCurrent.__doc__ = \
"""int32 DAQmxGetAIExcitVoltageOrCurrent(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2859"""
DAQmxSetAIExcitVoltageOrCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIExcitVoltageOrCurrent
DAQmxSetAIExcitVoltageOrCurrent.restype = int32
DAQmxSetAIExcitVoltageOrCurrent.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIExcitVoltageOrCurrent.__doc__ = \
"""int32 DAQmxSetAIExcitVoltageOrCurrent(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2860"""
DAQmxResetAIExcitVoltageOrCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIExcitVoltageOrCurrent
DAQmxResetAIExcitVoltageOrCurrent.restype = int32
DAQmxResetAIExcitVoltageOrCurrent.argtypes = [TaskHandle, STRING]
DAQmxResetAIExcitVoltageOrCurrent.__doc__ = \
"""int32 DAQmxResetAIExcitVoltageOrCurrent(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2861"""
DAQmxGetAIACExcitFreq = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIACExcitFreq
DAQmxGetAIACExcitFreq.restype = int32
DAQmxGetAIACExcitFreq.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIACExcitFreq.__doc__ = \
"""int32 DAQmxGetAIACExcitFreq(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2863"""
DAQmxSetAIACExcitFreq = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIACExcitFreq
DAQmxSetAIACExcitFreq.restype = int32
DAQmxSetAIACExcitFreq.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIACExcitFreq.__doc__ = \
"""int32 DAQmxSetAIACExcitFreq(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2864"""
DAQmxResetAIACExcitFreq = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIACExcitFreq
DAQmxResetAIACExcitFreq.restype = int32
DAQmxResetAIACExcitFreq.argtypes = [TaskHandle, STRING]
DAQmxResetAIACExcitFreq.__doc__ = \
"""int32 DAQmxResetAIACExcitFreq(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2865"""
DAQmxGetAIACExcitSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIACExcitSyncEnable
DAQmxGetAIACExcitSyncEnable.restype = int32
DAQmxGetAIACExcitSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIACExcitSyncEnable.__doc__ = \
"""int32 DAQmxGetAIACExcitSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2867"""
DAQmxSetAIACExcitSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIACExcitSyncEnable
DAQmxSetAIACExcitSyncEnable.restype = int32
DAQmxSetAIACExcitSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIACExcitSyncEnable.__doc__ = \
"""int32 DAQmxSetAIACExcitSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2868"""
DAQmxResetAIACExcitSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIACExcitSyncEnable
DAQmxResetAIACExcitSyncEnable.restype = int32
DAQmxResetAIACExcitSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAIACExcitSyncEnable.__doc__ = \
"""int32 DAQmxResetAIACExcitSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2869"""
DAQmxGetAIACExcitWireMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIACExcitWireMode
DAQmxGetAIACExcitWireMode.restype = int32
DAQmxGetAIACExcitWireMode.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIACExcitWireMode.__doc__ = \
"""int32 DAQmxGetAIACExcitWireMode(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2872"""
DAQmxSetAIACExcitWireMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIACExcitWireMode
DAQmxSetAIACExcitWireMode.restype = int32
DAQmxSetAIACExcitWireMode.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIACExcitWireMode.__doc__ = \
"""int32 DAQmxSetAIACExcitWireMode(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2873"""
DAQmxResetAIACExcitWireMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIACExcitWireMode
DAQmxResetAIACExcitWireMode.restype = int32
DAQmxResetAIACExcitWireMode.argtypes = [TaskHandle, STRING]
DAQmxResetAIACExcitWireMode.__doc__ = \
"""int32 DAQmxResetAIACExcitWireMode(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2874"""
DAQmxGetAIAtten = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIAtten
DAQmxGetAIAtten.restype = int32
DAQmxGetAIAtten.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIAtten.__doc__ = \
"""int32 DAQmxGetAIAtten(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2876"""
DAQmxSetAIAtten = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIAtten
DAQmxSetAIAtten.restype = int32
DAQmxSetAIAtten.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIAtten.__doc__ = \
"""int32 DAQmxSetAIAtten(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2877"""
DAQmxResetAIAtten = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIAtten
DAQmxResetAIAtten.restype = int32
DAQmxResetAIAtten.argtypes = [TaskHandle, STRING]
DAQmxResetAIAtten.__doc__ = \
"""int32 DAQmxResetAIAtten(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2878"""
DAQmxGetAIProbeAtten = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIProbeAtten
DAQmxGetAIProbeAtten.restype = int32
DAQmxGetAIProbeAtten.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIProbeAtten.__doc__ = \
"""int32 DAQmxGetAIProbeAtten(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2880"""
DAQmxSetAIProbeAtten = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIProbeAtten
DAQmxSetAIProbeAtten.restype = int32
DAQmxSetAIProbeAtten.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIProbeAtten.__doc__ = \
"""int32 DAQmxSetAIProbeAtten(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2881"""
DAQmxResetAIProbeAtten = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIProbeAtten
DAQmxResetAIProbeAtten.restype = int32
DAQmxResetAIProbeAtten.argtypes = [TaskHandle, STRING]
DAQmxResetAIProbeAtten.__doc__ = \
"""int32 DAQmxResetAIProbeAtten(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2882"""
DAQmxGetAILowpassEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILowpassEnable
DAQmxGetAILowpassEnable.restype = int32
DAQmxGetAILowpassEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAILowpassEnable.__doc__ = \
"""int32 DAQmxGetAILowpassEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2884"""
DAQmxSetAILowpassEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILowpassEnable
DAQmxSetAILowpassEnable.restype = int32
DAQmxSetAILowpassEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAILowpassEnable.__doc__ = \
"""int32 DAQmxSetAILowpassEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2885"""
DAQmxResetAILowpassEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILowpassEnable
DAQmxResetAILowpassEnable.restype = int32
DAQmxResetAILowpassEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAILowpassEnable.__doc__ = \
"""int32 DAQmxResetAILowpassEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2886"""
DAQmxGetAILowpassCutoffFreq = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILowpassCutoffFreq
DAQmxGetAILowpassCutoffFreq.restype = int32
DAQmxGetAILowpassCutoffFreq.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAILowpassCutoffFreq.__doc__ = \
"""int32 DAQmxGetAILowpassCutoffFreq(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2888"""
DAQmxSetAILowpassCutoffFreq = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILowpassCutoffFreq
DAQmxSetAILowpassCutoffFreq.restype = int32
DAQmxSetAILowpassCutoffFreq.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAILowpassCutoffFreq.__doc__ = \
"""int32 DAQmxSetAILowpassCutoffFreq(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2889"""
DAQmxResetAILowpassCutoffFreq = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILowpassCutoffFreq
DAQmxResetAILowpassCutoffFreq.restype = int32
DAQmxResetAILowpassCutoffFreq.argtypes = [TaskHandle, STRING]
DAQmxResetAILowpassCutoffFreq.__doc__ = \
"""int32 DAQmxResetAILowpassCutoffFreq(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2890"""
DAQmxGetAILowpassSwitchCapClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILowpassSwitchCapClkSrc
DAQmxGetAILowpassSwitchCapClkSrc.restype = int32
DAQmxGetAILowpassSwitchCapClkSrc.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAILowpassSwitchCapClkSrc.__doc__ = \
"""int32 DAQmxGetAILowpassSwitchCapClkSrc(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2893"""
DAQmxSetAILowpassSwitchCapClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILowpassSwitchCapClkSrc
DAQmxSetAILowpassSwitchCapClkSrc.restype = int32
DAQmxSetAILowpassSwitchCapClkSrc.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAILowpassSwitchCapClkSrc.__doc__ = \
"""int32 DAQmxSetAILowpassSwitchCapClkSrc(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2894"""
DAQmxResetAILowpassSwitchCapClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILowpassSwitchCapClkSrc
DAQmxResetAILowpassSwitchCapClkSrc.restype = int32
DAQmxResetAILowpassSwitchCapClkSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAILowpassSwitchCapClkSrc.__doc__ = \
"""int32 DAQmxResetAILowpassSwitchCapClkSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2895"""
DAQmxGetAILowpassSwitchCapExtClkFreq = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILowpassSwitchCapExtClkFreq
DAQmxGetAILowpassSwitchCapExtClkFreq.restype = int32
DAQmxGetAILowpassSwitchCapExtClkFreq.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAILowpassSwitchCapExtClkFreq.__doc__ = \
"""int32 DAQmxGetAILowpassSwitchCapExtClkFreq(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2897"""
DAQmxSetAILowpassSwitchCapExtClkFreq = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILowpassSwitchCapExtClkFreq
DAQmxSetAILowpassSwitchCapExtClkFreq.restype = int32
DAQmxSetAILowpassSwitchCapExtClkFreq.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAILowpassSwitchCapExtClkFreq.__doc__ = \
"""int32 DAQmxSetAILowpassSwitchCapExtClkFreq(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2898"""
DAQmxResetAILowpassSwitchCapExtClkFreq = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILowpassSwitchCapExtClkFreq
DAQmxResetAILowpassSwitchCapExtClkFreq.restype = int32
DAQmxResetAILowpassSwitchCapExtClkFreq.argtypes = [TaskHandle, STRING]
DAQmxResetAILowpassSwitchCapExtClkFreq.__doc__ = \
"""int32 DAQmxResetAILowpassSwitchCapExtClkFreq(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2899"""
DAQmxGetAILowpassSwitchCapExtClkDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILowpassSwitchCapExtClkDiv
DAQmxGetAILowpassSwitchCapExtClkDiv.restype = int32
DAQmxGetAILowpassSwitchCapExtClkDiv.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAILowpassSwitchCapExtClkDiv.__doc__ = \
"""int32 DAQmxGetAILowpassSwitchCapExtClkDiv(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2901"""
DAQmxSetAILowpassSwitchCapExtClkDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILowpassSwitchCapExtClkDiv
DAQmxSetAILowpassSwitchCapExtClkDiv.restype = int32
DAQmxSetAILowpassSwitchCapExtClkDiv.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAILowpassSwitchCapExtClkDiv.__doc__ = \
"""int32 DAQmxSetAILowpassSwitchCapExtClkDiv(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2902"""
DAQmxResetAILowpassSwitchCapExtClkDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILowpassSwitchCapExtClkDiv
DAQmxResetAILowpassSwitchCapExtClkDiv.restype = int32
DAQmxResetAILowpassSwitchCapExtClkDiv.argtypes = [TaskHandle, STRING]
DAQmxResetAILowpassSwitchCapExtClkDiv.__doc__ = \
"""int32 DAQmxResetAILowpassSwitchCapExtClkDiv(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2903"""
DAQmxGetAILowpassSwitchCapOutClkDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILowpassSwitchCapOutClkDiv
DAQmxGetAILowpassSwitchCapOutClkDiv.restype = int32
DAQmxGetAILowpassSwitchCapOutClkDiv.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAILowpassSwitchCapOutClkDiv.__doc__ = \
"""int32 DAQmxGetAILowpassSwitchCapOutClkDiv(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2905"""
DAQmxSetAILowpassSwitchCapOutClkDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILowpassSwitchCapOutClkDiv
DAQmxSetAILowpassSwitchCapOutClkDiv.restype = int32
DAQmxSetAILowpassSwitchCapOutClkDiv.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAILowpassSwitchCapOutClkDiv.__doc__ = \
"""int32 DAQmxSetAILowpassSwitchCapOutClkDiv(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2906"""
DAQmxResetAILowpassSwitchCapOutClkDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILowpassSwitchCapOutClkDiv
DAQmxResetAILowpassSwitchCapOutClkDiv.restype = int32
DAQmxResetAILowpassSwitchCapOutClkDiv.argtypes = [TaskHandle, STRING]
DAQmxResetAILowpassSwitchCapOutClkDiv.__doc__ = \
"""int32 DAQmxResetAILowpassSwitchCapOutClkDiv(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2907"""
DAQmxGetAIResolutionUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIResolutionUnits
DAQmxGetAIResolutionUnits.restype = int32
DAQmxGetAIResolutionUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIResolutionUnits.__doc__ = \
"""int32 DAQmxGetAIResolutionUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2910"""
DAQmxGetAIResolution = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIResolution
DAQmxGetAIResolution.restype = int32
DAQmxGetAIResolution.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIResolution.__doc__ = \
"""int32 DAQmxGetAIResolution(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2912"""
DAQmxGetAIRawSampSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRawSampSize
DAQmxGetAIRawSampSize.restype = int32
DAQmxGetAIRawSampSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAIRawSampSize.__doc__ = \
"""int32 DAQmxGetAIRawSampSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2914"""
DAQmxGetAIRawSampJustification = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRawSampJustification
DAQmxGetAIRawSampJustification.restype = int32
DAQmxGetAIRawSampJustification.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIRawSampJustification.__doc__ = \
"""int32 DAQmxGetAIRawSampJustification(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2917"""
DAQmxGetAIADCTimingMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIADCTimingMode
DAQmxGetAIADCTimingMode.restype = int32
DAQmxGetAIADCTimingMode.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIADCTimingMode.__doc__ = \
"""int32 DAQmxGetAIADCTimingMode(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2920"""
DAQmxSetAIADCTimingMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIADCTimingMode
DAQmxSetAIADCTimingMode.restype = int32
DAQmxSetAIADCTimingMode.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIADCTimingMode.__doc__ = \
"""int32 DAQmxSetAIADCTimingMode(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2921"""
DAQmxResetAIADCTimingMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIADCTimingMode
DAQmxResetAIADCTimingMode.restype = int32
DAQmxResetAIADCTimingMode.argtypes = [TaskHandle, STRING]
DAQmxResetAIADCTimingMode.__doc__ = \
"""int32 DAQmxResetAIADCTimingMode(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2922"""
DAQmxGetAIDitherEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIDitherEnable
DAQmxGetAIDitherEnable.restype = int32
DAQmxGetAIDitherEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIDitherEnable.__doc__ = \
"""int32 DAQmxGetAIDitherEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2924"""
DAQmxSetAIDitherEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIDitherEnable
DAQmxSetAIDitherEnable.restype = int32
DAQmxSetAIDitherEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIDitherEnable.__doc__ = \
"""int32 DAQmxSetAIDitherEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2925"""
DAQmxResetAIDitherEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIDitherEnable
DAQmxResetAIDitherEnable.restype = int32
DAQmxResetAIDitherEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAIDitherEnable.__doc__ = \
"""int32 DAQmxResetAIDitherEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2926"""
DAQmxGetAIChanCalHasValidCalInfo = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalHasValidCalInfo
DAQmxGetAIChanCalHasValidCalInfo.restype = int32
DAQmxGetAIChanCalHasValidCalInfo.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIChanCalHasValidCalInfo.__doc__ = \
"""int32 DAQmxGetAIChanCalHasValidCalInfo(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2928"""
DAQmxGetAIChanCalEnableCal = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalEnableCal
DAQmxGetAIChanCalEnableCal.restype = int32
DAQmxGetAIChanCalEnableCal.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIChanCalEnableCal.__doc__ = \
"""int32 DAQmxGetAIChanCalEnableCal(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2930"""
DAQmxSetAIChanCalEnableCal = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalEnableCal
DAQmxSetAIChanCalEnableCal.restype = int32
DAQmxSetAIChanCalEnableCal.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIChanCalEnableCal.__doc__ = \
"""int32 DAQmxSetAIChanCalEnableCal(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2931"""
DAQmxResetAIChanCalEnableCal = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalEnableCal
DAQmxResetAIChanCalEnableCal.restype = int32
DAQmxResetAIChanCalEnableCal.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalEnableCal.__doc__ = \
"""int32 DAQmxResetAIChanCalEnableCal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2932"""
DAQmxGetAIChanCalApplyCalIfExp = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalApplyCalIfExp
DAQmxGetAIChanCalApplyCalIfExp.restype = int32
DAQmxGetAIChanCalApplyCalIfExp.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIChanCalApplyCalIfExp.__doc__ = \
"""int32 DAQmxGetAIChanCalApplyCalIfExp(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2934"""
DAQmxSetAIChanCalApplyCalIfExp = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalApplyCalIfExp
DAQmxSetAIChanCalApplyCalIfExp.restype = int32
DAQmxSetAIChanCalApplyCalIfExp.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIChanCalApplyCalIfExp.__doc__ = \
"""int32 DAQmxSetAIChanCalApplyCalIfExp(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2935"""
DAQmxResetAIChanCalApplyCalIfExp = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalApplyCalIfExp
DAQmxResetAIChanCalApplyCalIfExp.restype = int32
DAQmxResetAIChanCalApplyCalIfExp.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalApplyCalIfExp.__doc__ = \
"""int32 DAQmxResetAIChanCalApplyCalIfExp(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2936"""
DAQmxGetAIChanCalScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalScaleType
DAQmxGetAIChanCalScaleType.restype = int32
DAQmxGetAIChanCalScaleType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIChanCalScaleType.__doc__ = \
"""int32 DAQmxGetAIChanCalScaleType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2939"""
DAQmxSetAIChanCalScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalScaleType
DAQmxSetAIChanCalScaleType.restype = int32
DAQmxSetAIChanCalScaleType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIChanCalScaleType.__doc__ = \
"""int32 DAQmxSetAIChanCalScaleType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2940"""
DAQmxResetAIChanCalScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalScaleType
DAQmxResetAIChanCalScaleType.restype = int32
DAQmxResetAIChanCalScaleType.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalScaleType.__doc__ = \
"""int32 DAQmxResetAIChanCalScaleType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2941"""
DAQmxGetAIChanCalTablePreScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalTablePreScaledVals
DAQmxGetAIChanCalTablePreScaledVals.restype = int32
DAQmxGetAIChanCalTablePreScaledVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIChanCalTablePreScaledVals.__doc__ = \
"""int32 DAQmxGetAIChanCalTablePreScaledVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2943"""
DAQmxSetAIChanCalTablePreScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalTablePreScaledVals
DAQmxSetAIChanCalTablePreScaledVals.restype = int32
DAQmxSetAIChanCalTablePreScaledVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxSetAIChanCalTablePreScaledVals.__doc__ = \
"""int32 DAQmxSetAIChanCalTablePreScaledVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2944"""
DAQmxResetAIChanCalTablePreScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalTablePreScaledVals
DAQmxResetAIChanCalTablePreScaledVals.restype = int32
DAQmxResetAIChanCalTablePreScaledVals.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalTablePreScaledVals.__doc__ = \
"""int32 DAQmxResetAIChanCalTablePreScaledVals(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2945"""
DAQmxGetAIChanCalTableScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalTableScaledVals
DAQmxGetAIChanCalTableScaledVals.restype = int32
DAQmxGetAIChanCalTableScaledVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIChanCalTableScaledVals.__doc__ = \
"""int32 DAQmxGetAIChanCalTableScaledVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2947"""
DAQmxSetAIChanCalTableScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalTableScaledVals
DAQmxSetAIChanCalTableScaledVals.restype = int32
DAQmxSetAIChanCalTableScaledVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxSetAIChanCalTableScaledVals.__doc__ = \
"""int32 DAQmxSetAIChanCalTableScaledVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2948"""
DAQmxResetAIChanCalTableScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalTableScaledVals
DAQmxResetAIChanCalTableScaledVals.restype = int32
DAQmxResetAIChanCalTableScaledVals.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalTableScaledVals.__doc__ = \
"""int32 DAQmxResetAIChanCalTableScaledVals(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2949"""
DAQmxGetAIChanCalPolyForwardCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalPolyForwardCoeff
DAQmxGetAIChanCalPolyForwardCoeff.restype = int32
DAQmxGetAIChanCalPolyForwardCoeff.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIChanCalPolyForwardCoeff.__doc__ = \
"""int32 DAQmxGetAIChanCalPolyForwardCoeff(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2951"""
DAQmxSetAIChanCalPolyForwardCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalPolyForwardCoeff
DAQmxSetAIChanCalPolyForwardCoeff.restype = int32
DAQmxSetAIChanCalPolyForwardCoeff.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxSetAIChanCalPolyForwardCoeff.__doc__ = \
"""int32 DAQmxSetAIChanCalPolyForwardCoeff(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2952"""
DAQmxResetAIChanCalPolyForwardCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalPolyForwardCoeff
DAQmxResetAIChanCalPolyForwardCoeff.restype = int32
DAQmxResetAIChanCalPolyForwardCoeff.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalPolyForwardCoeff.__doc__ = \
"""int32 DAQmxResetAIChanCalPolyForwardCoeff(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2953"""
DAQmxGetAIChanCalPolyReverseCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalPolyReverseCoeff
DAQmxGetAIChanCalPolyReverseCoeff.restype = int32
DAQmxGetAIChanCalPolyReverseCoeff.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIChanCalPolyReverseCoeff.__doc__ = \
"""int32 DAQmxGetAIChanCalPolyReverseCoeff(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2955"""
DAQmxSetAIChanCalPolyReverseCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalPolyReverseCoeff
DAQmxSetAIChanCalPolyReverseCoeff.restype = int32
DAQmxSetAIChanCalPolyReverseCoeff.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxSetAIChanCalPolyReverseCoeff.__doc__ = \
"""int32 DAQmxSetAIChanCalPolyReverseCoeff(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2956"""
DAQmxResetAIChanCalPolyReverseCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalPolyReverseCoeff
DAQmxResetAIChanCalPolyReverseCoeff.restype = int32
DAQmxResetAIChanCalPolyReverseCoeff.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalPolyReverseCoeff.__doc__ = \
"""int32 DAQmxResetAIChanCalPolyReverseCoeff(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2957"""
DAQmxGetAIChanCalOperatorName = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalOperatorName
DAQmxGetAIChanCalOperatorName.restype = int32
DAQmxGetAIChanCalOperatorName.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAIChanCalOperatorName.__doc__ = \
"""int32 DAQmxGetAIChanCalOperatorName(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2959"""
DAQmxSetAIChanCalOperatorName = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalOperatorName
DAQmxSetAIChanCalOperatorName.restype = int32
DAQmxSetAIChanCalOperatorName.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAIChanCalOperatorName.__doc__ = \
"""int32 DAQmxSetAIChanCalOperatorName(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2960"""
DAQmxResetAIChanCalOperatorName = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalOperatorName
DAQmxResetAIChanCalOperatorName.restype = int32
DAQmxResetAIChanCalOperatorName.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalOperatorName.__doc__ = \
"""int32 DAQmxResetAIChanCalOperatorName(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2961"""
DAQmxGetAIChanCalDesc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalDesc
DAQmxGetAIChanCalDesc.restype = int32
DAQmxGetAIChanCalDesc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAIChanCalDesc.__doc__ = \
"""int32 DAQmxGetAIChanCalDesc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2963"""
DAQmxSetAIChanCalDesc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalDesc
DAQmxSetAIChanCalDesc.restype = int32
DAQmxSetAIChanCalDesc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAIChanCalDesc.__doc__ = \
"""int32 DAQmxSetAIChanCalDesc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2964"""
DAQmxResetAIChanCalDesc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalDesc
DAQmxResetAIChanCalDesc.restype = int32
DAQmxResetAIChanCalDesc.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalDesc.__doc__ = \
"""int32 DAQmxResetAIChanCalDesc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2965"""
DAQmxGetAIChanCalVerifRefVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalVerifRefVals
DAQmxGetAIChanCalVerifRefVals.restype = int32
DAQmxGetAIChanCalVerifRefVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIChanCalVerifRefVals.__doc__ = \
"""int32 DAQmxGetAIChanCalVerifRefVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2967"""
DAQmxSetAIChanCalVerifRefVals = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalVerifRefVals
DAQmxSetAIChanCalVerifRefVals.restype = int32
DAQmxSetAIChanCalVerifRefVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxSetAIChanCalVerifRefVals.__doc__ = \
"""int32 DAQmxSetAIChanCalVerifRefVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2968"""
DAQmxResetAIChanCalVerifRefVals = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalVerifRefVals
DAQmxResetAIChanCalVerifRefVals.restype = int32
DAQmxResetAIChanCalVerifRefVals.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalVerifRefVals.__doc__ = \
"""int32 DAQmxResetAIChanCalVerifRefVals(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2969"""
DAQmxGetAIChanCalVerifAcqVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIChanCalVerifAcqVals
DAQmxGetAIChanCalVerifAcqVals.restype = int32
DAQmxGetAIChanCalVerifAcqVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIChanCalVerifAcqVals.__doc__ = \
"""int32 DAQmxGetAIChanCalVerifAcqVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2971"""
DAQmxSetAIChanCalVerifAcqVals = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIChanCalVerifAcqVals
DAQmxSetAIChanCalVerifAcqVals.restype = int32
DAQmxSetAIChanCalVerifAcqVals.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxSetAIChanCalVerifAcqVals.__doc__ = \
"""int32 DAQmxSetAIChanCalVerifAcqVals(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2972"""
DAQmxResetAIChanCalVerifAcqVals = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIChanCalVerifAcqVals
DAQmxResetAIChanCalVerifAcqVals.restype = int32
DAQmxResetAIChanCalVerifAcqVals.argtypes = [TaskHandle, STRING]
DAQmxResetAIChanCalVerifAcqVals.__doc__ = \
"""int32 DAQmxResetAIChanCalVerifAcqVals(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2973"""
DAQmxGetAIRngHigh = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRngHigh
DAQmxGetAIRngHigh.restype = int32
DAQmxGetAIRngHigh.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRngHigh.__doc__ = \
"""int32 DAQmxGetAIRngHigh(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2975"""
DAQmxSetAIRngHigh = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRngHigh
DAQmxSetAIRngHigh.restype = int32
DAQmxSetAIRngHigh.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRngHigh.__doc__ = \
"""int32 DAQmxSetAIRngHigh(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2976"""
DAQmxResetAIRngHigh = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRngHigh
DAQmxResetAIRngHigh.restype = int32
DAQmxResetAIRngHigh.argtypes = [TaskHandle, STRING]
DAQmxResetAIRngHigh.__doc__ = \
"""int32 DAQmxResetAIRngHigh(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2977"""
DAQmxGetAIRngLow = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRngLow
DAQmxGetAIRngLow.restype = int32
DAQmxGetAIRngLow.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIRngLow.__doc__ = \
"""int32 DAQmxGetAIRngLow(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2979"""
DAQmxSetAIRngLow = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRngLow
DAQmxSetAIRngLow.restype = int32
DAQmxSetAIRngLow.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIRngLow.__doc__ = \
"""int32 DAQmxSetAIRngLow(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2980"""
DAQmxResetAIRngLow = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRngLow
DAQmxResetAIRngLow.restype = int32
DAQmxResetAIRngLow.argtypes = [TaskHandle, STRING]
DAQmxResetAIRngLow.__doc__ = \
"""int32 DAQmxResetAIRngLow(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2981"""
DAQmxGetAIDCOffset = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIDCOffset
DAQmxGetAIDCOffset.restype = int32
DAQmxGetAIDCOffset.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIDCOffset.__doc__ = \
"""int32 DAQmxGetAIDCOffset(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2983"""
DAQmxSetAIDCOffset = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIDCOffset
DAQmxSetAIDCOffset.restype = int32
DAQmxSetAIDCOffset.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIDCOffset.__doc__ = \
"""int32 DAQmxSetAIDCOffset(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2984"""
DAQmxResetAIDCOffset = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIDCOffset
DAQmxResetAIDCOffset.restype = int32
DAQmxResetAIDCOffset.argtypes = [TaskHandle, STRING]
DAQmxResetAIDCOffset.__doc__ = \
"""int32 DAQmxResetAIDCOffset(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2985"""
DAQmxGetAIGain = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIGain
DAQmxGetAIGain.restype = int32
DAQmxGetAIGain.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIGain.__doc__ = \
"""int32 DAQmxGetAIGain(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2987"""
DAQmxSetAIGain = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIGain
DAQmxSetAIGain.restype = int32
DAQmxSetAIGain.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIGain.__doc__ = \
"""int32 DAQmxSetAIGain(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2988"""
DAQmxResetAIGain = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIGain
DAQmxResetAIGain.restype = int32
DAQmxResetAIGain.argtypes = [TaskHandle, STRING]
DAQmxResetAIGain.__doc__ = \
"""int32 DAQmxResetAIGain(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2989"""
DAQmxGetAISampAndHoldEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAISampAndHoldEnable
DAQmxGetAISampAndHoldEnable.restype = int32
DAQmxGetAISampAndHoldEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAISampAndHoldEnable.__doc__ = \
"""int32 DAQmxGetAISampAndHoldEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2991"""
DAQmxSetAISampAndHoldEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAISampAndHoldEnable
DAQmxSetAISampAndHoldEnable.restype = int32
DAQmxSetAISampAndHoldEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAISampAndHoldEnable.__doc__ = \
"""int32 DAQmxSetAISampAndHoldEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2992"""
DAQmxResetAISampAndHoldEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAISampAndHoldEnable
DAQmxResetAISampAndHoldEnable.restype = int32
DAQmxResetAISampAndHoldEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAISampAndHoldEnable.__doc__ = \
"""int32 DAQmxResetAISampAndHoldEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2993"""
DAQmxGetAIAutoZeroMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIAutoZeroMode
DAQmxGetAIAutoZeroMode.restype = int32
DAQmxGetAIAutoZeroMode.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIAutoZeroMode.__doc__ = \
"""int32 DAQmxGetAIAutoZeroMode(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2996"""
DAQmxSetAIAutoZeroMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIAutoZeroMode
DAQmxSetAIAutoZeroMode.restype = int32
DAQmxSetAIAutoZeroMode.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIAutoZeroMode.__doc__ = \
"""int32 DAQmxSetAIAutoZeroMode(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2997"""
DAQmxResetAIAutoZeroMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIAutoZeroMode
DAQmxResetAIAutoZeroMode.restype = int32
DAQmxResetAIAutoZeroMode.argtypes = [TaskHandle, STRING]
DAQmxResetAIAutoZeroMode.__doc__ = \
"""int32 DAQmxResetAIAutoZeroMode(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:2998"""
DAQmxGetAIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIDataXferMech
DAQmxGetAIDataXferMech.restype = int32
DAQmxGetAIDataXferMech.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIDataXferMech.__doc__ = \
"""int32 DAQmxGetAIDataXferMech(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3001"""
DAQmxSetAIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIDataXferMech
DAQmxSetAIDataXferMech.restype = int32
DAQmxSetAIDataXferMech.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIDataXferMech.__doc__ = \
"""int32 DAQmxSetAIDataXferMech(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3002"""
DAQmxResetAIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIDataXferMech
DAQmxResetAIDataXferMech.restype = int32
DAQmxResetAIDataXferMech.argtypes = [TaskHandle, STRING]
DAQmxResetAIDataXferMech.__doc__ = \
"""int32 DAQmxResetAIDataXferMech(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3003"""
DAQmxGetAIDataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIDataXferReqCond
DAQmxGetAIDataXferReqCond.restype = int32
DAQmxGetAIDataXferReqCond.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIDataXferReqCond.__doc__ = \
"""int32 DAQmxGetAIDataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3006"""
DAQmxSetAIDataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIDataXferReqCond
DAQmxSetAIDataXferReqCond.restype = int32
DAQmxSetAIDataXferReqCond.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIDataXferReqCond.__doc__ = \
"""int32 DAQmxSetAIDataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3007"""
DAQmxResetAIDataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIDataXferReqCond
DAQmxResetAIDataXferReqCond.restype = int32
DAQmxResetAIDataXferReqCond.argtypes = [TaskHandle, STRING]
DAQmxResetAIDataXferReqCond.__doc__ = \
"""int32 DAQmxResetAIDataXferReqCond(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3008"""
DAQmxGetAIDataXferCustomThreshold = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIDataXferCustomThreshold
DAQmxGetAIDataXferCustomThreshold.restype = int32
DAQmxGetAIDataXferCustomThreshold.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAIDataXferCustomThreshold.__doc__ = \
"""int32 DAQmxGetAIDataXferCustomThreshold(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3010"""
DAQmxSetAIDataXferCustomThreshold = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIDataXferCustomThreshold
DAQmxSetAIDataXferCustomThreshold.restype = int32
DAQmxSetAIDataXferCustomThreshold.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAIDataXferCustomThreshold.__doc__ = \
"""int32 DAQmxSetAIDataXferCustomThreshold(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3011"""
DAQmxResetAIDataXferCustomThreshold = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIDataXferCustomThreshold
DAQmxResetAIDataXferCustomThreshold.restype = int32
DAQmxResetAIDataXferCustomThreshold.argtypes = [TaskHandle, STRING]
DAQmxResetAIDataXferCustomThreshold.__doc__ = \
"""int32 DAQmxResetAIDataXferCustomThreshold(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3012"""
DAQmxGetAIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIUsbXferReqSize
DAQmxGetAIUsbXferReqSize.restype = int32
DAQmxGetAIUsbXferReqSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAIUsbXferReqSize.__doc__ = \
"""int32 DAQmxGetAIUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3014"""
DAQmxSetAIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIUsbXferReqSize
DAQmxSetAIUsbXferReqSize.restype = int32
DAQmxSetAIUsbXferReqSize.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAIUsbXferReqSize.__doc__ = \
"""int32 DAQmxSetAIUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3015"""
DAQmxResetAIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIUsbXferReqSize
DAQmxResetAIUsbXferReqSize.restype = int32
DAQmxResetAIUsbXferReqSize.argtypes = [TaskHandle, STRING]
DAQmxResetAIUsbXferReqSize.__doc__ = \
"""int32 DAQmxResetAIUsbXferReqSize(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3016"""
DAQmxGetAIMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIMemMapEnable
DAQmxGetAIMemMapEnable.restype = int32
DAQmxGetAIMemMapEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIMemMapEnable.__doc__ = \
"""int32 DAQmxGetAIMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3018"""
DAQmxSetAIMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIMemMapEnable
DAQmxSetAIMemMapEnable.restype = int32
DAQmxSetAIMemMapEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIMemMapEnable.__doc__ = \
"""int32 DAQmxSetAIMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3019"""
DAQmxResetAIMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIMemMapEnable
DAQmxResetAIMemMapEnable.restype = int32
DAQmxResetAIMemMapEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAIMemMapEnable.__doc__ = \
"""int32 DAQmxResetAIMemMapEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3020"""
DAQmxGetAIRawDataCompressionType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIRawDataCompressionType
DAQmxGetAIRawDataCompressionType.restype = int32
DAQmxGetAIRawDataCompressionType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIRawDataCompressionType.__doc__ = \
"""int32 DAQmxGetAIRawDataCompressionType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3023"""
DAQmxSetAIRawDataCompressionType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIRawDataCompressionType
DAQmxSetAIRawDataCompressionType.restype = int32
DAQmxSetAIRawDataCompressionType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIRawDataCompressionType.__doc__ = \
"""int32 DAQmxSetAIRawDataCompressionType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3024"""
DAQmxResetAIRawDataCompressionType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIRawDataCompressionType
DAQmxResetAIRawDataCompressionType.restype = int32
DAQmxResetAIRawDataCompressionType.argtypes = [TaskHandle, STRING]
DAQmxResetAIRawDataCompressionType.__doc__ = \
"""int32 DAQmxResetAIRawDataCompressionType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3025"""
DAQmxGetAILossyLSBRemovalCompressedSampSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetAILossyLSBRemovalCompressedSampSize
DAQmxGetAILossyLSBRemovalCompressedSampSize.restype = int32
DAQmxGetAILossyLSBRemovalCompressedSampSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAILossyLSBRemovalCompressedSampSize.__doc__ = \
"""int32 DAQmxGetAILossyLSBRemovalCompressedSampSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3027"""
DAQmxSetAILossyLSBRemovalCompressedSampSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetAILossyLSBRemovalCompressedSampSize
DAQmxSetAILossyLSBRemovalCompressedSampSize.restype = int32
DAQmxSetAILossyLSBRemovalCompressedSampSize.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAILossyLSBRemovalCompressedSampSize.__doc__ = \
"""int32 DAQmxSetAILossyLSBRemovalCompressedSampSize(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3028"""
DAQmxResetAILossyLSBRemovalCompressedSampSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetAILossyLSBRemovalCompressedSampSize
DAQmxResetAILossyLSBRemovalCompressedSampSize.restype = int32
DAQmxResetAILossyLSBRemovalCompressedSampSize.argtypes = [TaskHandle, STRING]
DAQmxResetAILossyLSBRemovalCompressedSampSize.__doc__ = \
"""int32 DAQmxResetAILossyLSBRemovalCompressedSampSize(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3029"""
DAQmxGetAIDevScalingCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIDevScalingCoeff
DAQmxGetAIDevScalingCoeff.restype = int32
DAQmxGetAIDevScalingCoeff.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAIDevScalingCoeff.__doc__ = \
"""int32 DAQmxGetAIDevScalingCoeff(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3031"""
DAQmxGetAIEnhancedAliasRejectionEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIEnhancedAliasRejectionEnable
DAQmxGetAIEnhancedAliasRejectionEnable.restype = int32
DAQmxGetAIEnhancedAliasRejectionEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAIEnhancedAliasRejectionEnable.__doc__ = \
"""int32 DAQmxGetAIEnhancedAliasRejectionEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3033"""
DAQmxSetAIEnhancedAliasRejectionEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIEnhancedAliasRejectionEnable
DAQmxSetAIEnhancedAliasRejectionEnable.restype = int32
DAQmxSetAIEnhancedAliasRejectionEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAIEnhancedAliasRejectionEnable.__doc__ = \
"""int32 DAQmxSetAIEnhancedAliasRejectionEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3034"""
DAQmxResetAIEnhancedAliasRejectionEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIEnhancedAliasRejectionEnable
DAQmxResetAIEnhancedAliasRejectionEnable.restype = int32
DAQmxResetAIEnhancedAliasRejectionEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAIEnhancedAliasRejectionEnable.__doc__ = \
"""int32 DAQmxResetAIEnhancedAliasRejectionEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3035"""
DAQmxGetAOMax = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOMax
DAQmxGetAOMax.restype = int32
DAQmxGetAOMax.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOMax.__doc__ = \
"""int32 DAQmxGetAOMax(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3037"""
DAQmxSetAOMax = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOMax
DAQmxSetAOMax.restype = int32
DAQmxSetAOMax.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOMax.__doc__ = \
"""int32 DAQmxSetAOMax(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3038"""
DAQmxResetAOMax = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOMax
DAQmxResetAOMax.restype = int32
DAQmxResetAOMax.argtypes = [TaskHandle, STRING]
DAQmxResetAOMax.__doc__ = \
"""int32 DAQmxResetAOMax(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3039"""
DAQmxGetAOMin = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOMin
DAQmxGetAOMin.restype = int32
DAQmxGetAOMin.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOMin.__doc__ = \
"""int32 DAQmxGetAOMin(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3041"""
DAQmxSetAOMin = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOMin
DAQmxSetAOMin.restype = int32
DAQmxSetAOMin.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOMin.__doc__ = \
"""int32 DAQmxSetAOMin(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3042"""
DAQmxResetAOMin = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOMin
DAQmxResetAOMin.restype = int32
DAQmxResetAOMin.argtypes = [TaskHandle, STRING]
DAQmxResetAOMin.__doc__ = \
"""int32 DAQmxResetAOMin(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3043"""
DAQmxGetAOCustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOCustomScaleName
DAQmxGetAOCustomScaleName.restype = int32
DAQmxGetAOCustomScaleName.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAOCustomScaleName.__doc__ = \
"""int32 DAQmxGetAOCustomScaleName(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3045"""
DAQmxSetAOCustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOCustomScaleName
DAQmxSetAOCustomScaleName.restype = int32
DAQmxSetAOCustomScaleName.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAOCustomScaleName.__doc__ = \
"""int32 DAQmxSetAOCustomScaleName(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3046"""
DAQmxResetAOCustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOCustomScaleName
DAQmxResetAOCustomScaleName.restype = int32
DAQmxResetAOCustomScaleName.argtypes = [TaskHandle, STRING]
DAQmxResetAOCustomScaleName.__doc__ = \
"""int32 DAQmxResetAOCustomScaleName(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3047"""
DAQmxGetAOOutputType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOOutputType
DAQmxGetAOOutputType.restype = int32
DAQmxGetAOOutputType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOOutputType.__doc__ = \
"""int32 DAQmxGetAOOutputType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3050"""
DAQmxGetAOVoltageUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOVoltageUnits
DAQmxGetAOVoltageUnits.restype = int32
DAQmxGetAOVoltageUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOVoltageUnits.__doc__ = \
"""int32 DAQmxGetAOVoltageUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3053"""
DAQmxSetAOVoltageUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOVoltageUnits
DAQmxSetAOVoltageUnits.restype = int32
DAQmxSetAOVoltageUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOVoltageUnits.__doc__ = \
"""int32 DAQmxSetAOVoltageUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3054"""
DAQmxResetAOVoltageUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOVoltageUnits
DAQmxResetAOVoltageUnits.restype = int32
DAQmxResetAOVoltageUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAOVoltageUnits.__doc__ = \
"""int32 DAQmxResetAOVoltageUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3055"""
DAQmxGetAOVoltageCurrentLimit = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOVoltageCurrentLimit
DAQmxGetAOVoltageCurrentLimit.restype = int32
DAQmxGetAOVoltageCurrentLimit.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOVoltageCurrentLimit.__doc__ = \
"""int32 DAQmxGetAOVoltageCurrentLimit(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3057"""
DAQmxSetAOVoltageCurrentLimit = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOVoltageCurrentLimit
DAQmxSetAOVoltageCurrentLimit.restype = int32
DAQmxSetAOVoltageCurrentLimit.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOVoltageCurrentLimit.__doc__ = \
"""int32 DAQmxSetAOVoltageCurrentLimit(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3058"""
DAQmxResetAOVoltageCurrentLimit = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOVoltageCurrentLimit
DAQmxResetAOVoltageCurrentLimit.restype = int32
DAQmxResetAOVoltageCurrentLimit.argtypes = [TaskHandle, STRING]
DAQmxResetAOVoltageCurrentLimit.__doc__ = \
"""int32 DAQmxResetAOVoltageCurrentLimit(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3059"""
DAQmxGetAOCurrentUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOCurrentUnits
DAQmxGetAOCurrentUnits.restype = int32
DAQmxGetAOCurrentUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOCurrentUnits.__doc__ = \
"""int32 DAQmxGetAOCurrentUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3062"""
DAQmxSetAOCurrentUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOCurrentUnits
DAQmxSetAOCurrentUnits.restype = int32
DAQmxSetAOCurrentUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOCurrentUnits.__doc__ = \
"""int32 DAQmxSetAOCurrentUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3063"""
DAQmxResetAOCurrentUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOCurrentUnits
DAQmxResetAOCurrentUnits.restype = int32
DAQmxResetAOCurrentUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAOCurrentUnits.__doc__ = \
"""int32 DAQmxResetAOCurrentUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3064"""
DAQmxGetAOFuncGenType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenType
DAQmxGetAOFuncGenType.restype = int32
DAQmxGetAOFuncGenType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOFuncGenType.__doc__ = \
"""int32 DAQmxGetAOFuncGenType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3067"""
DAQmxSetAOFuncGenType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenType
DAQmxSetAOFuncGenType.restype = int32
DAQmxSetAOFuncGenType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOFuncGenType.__doc__ = \
"""int32 DAQmxSetAOFuncGenType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3068"""
DAQmxResetAOFuncGenType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenType
DAQmxResetAOFuncGenType.restype = int32
DAQmxResetAOFuncGenType.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenType.__doc__ = \
"""int32 DAQmxResetAOFuncGenType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3069"""
DAQmxGetAOFuncGenFreq = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenFreq
DAQmxGetAOFuncGenFreq.restype = int32
DAQmxGetAOFuncGenFreq.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOFuncGenFreq.__doc__ = \
"""int32 DAQmxGetAOFuncGenFreq(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3071"""
DAQmxSetAOFuncGenFreq = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenFreq
DAQmxSetAOFuncGenFreq.restype = int32
DAQmxSetAOFuncGenFreq.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOFuncGenFreq.__doc__ = \
"""int32 DAQmxSetAOFuncGenFreq(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3072"""
DAQmxResetAOFuncGenFreq = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenFreq
DAQmxResetAOFuncGenFreq.restype = int32
DAQmxResetAOFuncGenFreq.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenFreq.__doc__ = \
"""int32 DAQmxResetAOFuncGenFreq(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3073"""
DAQmxGetAOFuncGenAmplitude = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenAmplitude
DAQmxGetAOFuncGenAmplitude.restype = int32
DAQmxGetAOFuncGenAmplitude.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOFuncGenAmplitude.__doc__ = \
"""int32 DAQmxGetAOFuncGenAmplitude(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3075"""
DAQmxSetAOFuncGenAmplitude = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenAmplitude
DAQmxSetAOFuncGenAmplitude.restype = int32
DAQmxSetAOFuncGenAmplitude.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOFuncGenAmplitude.__doc__ = \
"""int32 DAQmxSetAOFuncGenAmplitude(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3076"""
DAQmxResetAOFuncGenAmplitude = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenAmplitude
DAQmxResetAOFuncGenAmplitude.restype = int32
DAQmxResetAOFuncGenAmplitude.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenAmplitude.__doc__ = \
"""int32 DAQmxResetAOFuncGenAmplitude(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3077"""
DAQmxGetAOFuncGenOffset = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenOffset
DAQmxGetAOFuncGenOffset.restype = int32
DAQmxGetAOFuncGenOffset.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOFuncGenOffset.__doc__ = \
"""int32 DAQmxGetAOFuncGenOffset(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3079"""
DAQmxSetAOFuncGenOffset = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenOffset
DAQmxSetAOFuncGenOffset.restype = int32
DAQmxSetAOFuncGenOffset.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOFuncGenOffset.__doc__ = \
"""int32 DAQmxSetAOFuncGenOffset(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3080"""
DAQmxResetAOFuncGenOffset = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenOffset
DAQmxResetAOFuncGenOffset.restype = int32
DAQmxResetAOFuncGenOffset.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenOffset.__doc__ = \
"""int32 DAQmxResetAOFuncGenOffset(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3081"""
DAQmxGetAOFuncGenSquareDutyCycle = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenSquareDutyCycle
DAQmxGetAOFuncGenSquareDutyCycle.restype = int32
DAQmxGetAOFuncGenSquareDutyCycle.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOFuncGenSquareDutyCycle.__doc__ = \
"""int32 DAQmxGetAOFuncGenSquareDutyCycle(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3083"""
DAQmxSetAOFuncGenSquareDutyCycle = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenSquareDutyCycle
DAQmxSetAOFuncGenSquareDutyCycle.restype = int32
DAQmxSetAOFuncGenSquareDutyCycle.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOFuncGenSquareDutyCycle.__doc__ = \
"""int32 DAQmxSetAOFuncGenSquareDutyCycle(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3084"""
DAQmxResetAOFuncGenSquareDutyCycle = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenSquareDutyCycle
DAQmxResetAOFuncGenSquareDutyCycle.restype = int32
DAQmxResetAOFuncGenSquareDutyCycle.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenSquareDutyCycle.__doc__ = \
"""int32 DAQmxResetAOFuncGenSquareDutyCycle(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3085"""
DAQmxGetAOFuncGenModulationType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenModulationType
DAQmxGetAOFuncGenModulationType.restype = int32
DAQmxGetAOFuncGenModulationType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOFuncGenModulationType.__doc__ = \
"""int32 DAQmxGetAOFuncGenModulationType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3088"""
DAQmxSetAOFuncGenModulationType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenModulationType
DAQmxSetAOFuncGenModulationType.restype = int32
DAQmxSetAOFuncGenModulationType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOFuncGenModulationType.__doc__ = \
"""int32 DAQmxSetAOFuncGenModulationType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3089"""
DAQmxResetAOFuncGenModulationType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenModulationType
DAQmxResetAOFuncGenModulationType.restype = int32
DAQmxResetAOFuncGenModulationType.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenModulationType.__doc__ = \
"""int32 DAQmxResetAOFuncGenModulationType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3090"""
DAQmxGetAOFuncGenFMDeviation = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOFuncGenFMDeviation
DAQmxGetAOFuncGenFMDeviation.restype = int32
DAQmxGetAOFuncGenFMDeviation.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOFuncGenFMDeviation.__doc__ = \
"""int32 DAQmxGetAOFuncGenFMDeviation(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3092"""
DAQmxSetAOFuncGenFMDeviation = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOFuncGenFMDeviation
DAQmxSetAOFuncGenFMDeviation.restype = int32
DAQmxSetAOFuncGenFMDeviation.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOFuncGenFMDeviation.__doc__ = \
"""int32 DAQmxSetAOFuncGenFMDeviation(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3093"""
DAQmxResetAOFuncGenFMDeviation = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOFuncGenFMDeviation
DAQmxResetAOFuncGenFMDeviation.restype = int32
DAQmxResetAOFuncGenFMDeviation.argtypes = [TaskHandle, STRING]
DAQmxResetAOFuncGenFMDeviation.__doc__ = \
"""int32 DAQmxResetAOFuncGenFMDeviation(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3094"""
DAQmxGetAOOutputImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOOutputImpedance
DAQmxGetAOOutputImpedance.restype = int32
DAQmxGetAOOutputImpedance.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOOutputImpedance.__doc__ = \
"""int32 DAQmxGetAOOutputImpedance(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3096"""
DAQmxSetAOOutputImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOOutputImpedance
DAQmxSetAOOutputImpedance.restype = int32
DAQmxSetAOOutputImpedance.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOOutputImpedance.__doc__ = \
"""int32 DAQmxSetAOOutputImpedance(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3097"""
DAQmxResetAOOutputImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOOutputImpedance
DAQmxResetAOOutputImpedance.restype = int32
DAQmxResetAOOutputImpedance.argtypes = [TaskHandle, STRING]
DAQmxResetAOOutputImpedance.__doc__ = \
"""int32 DAQmxResetAOOutputImpedance(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3098"""
DAQmxGetAOLoadImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOLoadImpedance
DAQmxGetAOLoadImpedance.restype = int32
DAQmxGetAOLoadImpedance.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOLoadImpedance.__doc__ = \
"""int32 DAQmxGetAOLoadImpedance(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3100"""
DAQmxSetAOLoadImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOLoadImpedance
DAQmxSetAOLoadImpedance.restype = int32
DAQmxSetAOLoadImpedance.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOLoadImpedance.__doc__ = \
"""int32 DAQmxSetAOLoadImpedance(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3101"""
DAQmxResetAOLoadImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOLoadImpedance
DAQmxResetAOLoadImpedance.restype = int32
DAQmxResetAOLoadImpedance.argtypes = [TaskHandle, STRING]
DAQmxResetAOLoadImpedance.__doc__ = \
"""int32 DAQmxResetAOLoadImpedance(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3102"""
DAQmxGetAOIdleOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOIdleOutputBehavior
DAQmxGetAOIdleOutputBehavior.restype = int32
DAQmxGetAOIdleOutputBehavior.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOIdleOutputBehavior.__doc__ = \
"""int32 DAQmxGetAOIdleOutputBehavior(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3105"""
DAQmxSetAOIdleOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOIdleOutputBehavior
DAQmxSetAOIdleOutputBehavior.restype = int32
DAQmxSetAOIdleOutputBehavior.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOIdleOutputBehavior.__doc__ = \
"""int32 DAQmxSetAOIdleOutputBehavior(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3106"""
DAQmxResetAOIdleOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOIdleOutputBehavior
DAQmxResetAOIdleOutputBehavior.restype = int32
DAQmxResetAOIdleOutputBehavior.argtypes = [TaskHandle, STRING]
DAQmxResetAOIdleOutputBehavior.__doc__ = \
"""int32 DAQmxResetAOIdleOutputBehavior(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3107"""
DAQmxGetAOTermCfg = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOTermCfg
DAQmxGetAOTermCfg.restype = int32
DAQmxGetAOTermCfg.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOTermCfg.__doc__ = \
"""int32 DAQmxGetAOTermCfg(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3110"""
DAQmxSetAOTermCfg = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOTermCfg
DAQmxSetAOTermCfg.restype = int32
DAQmxSetAOTermCfg.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOTermCfg.__doc__ = \
"""int32 DAQmxSetAOTermCfg(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3111"""
DAQmxResetAOTermCfg = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOTermCfg
DAQmxResetAOTermCfg.restype = int32
DAQmxResetAOTermCfg.argtypes = [TaskHandle, STRING]
DAQmxResetAOTermCfg.__doc__ = \
"""int32 DAQmxResetAOTermCfg(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3112"""
DAQmxGetAOResolutionUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOResolutionUnits
DAQmxGetAOResolutionUnits.restype = int32
DAQmxGetAOResolutionUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAOResolutionUnits.__doc__ = \
"""int32 DAQmxGetAOResolutionUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3115"""
DAQmxSetAOResolutionUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOResolutionUnits
DAQmxSetAOResolutionUnits.restype = int32
DAQmxSetAOResolutionUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAOResolutionUnits.__doc__ = \
"""int32 DAQmxSetAOResolutionUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3116"""
DAQmxResetAOResolutionUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOResolutionUnits
DAQmxResetAOResolutionUnits.restype = int32
DAQmxResetAOResolutionUnits.argtypes = [TaskHandle, STRING]
DAQmxResetAOResolutionUnits.__doc__ = \
"""int32 DAQmxResetAOResolutionUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3117"""
DAQmxGetAOResolution = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOResolution
DAQmxGetAOResolution.restype = int32
DAQmxGetAOResolution.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOResolution.__doc__ = \
"""int32 DAQmxGetAOResolution(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3119"""
DAQmxGetAODACRngHigh = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRngHigh
DAQmxGetAODACRngHigh.restype = int32
DAQmxGetAODACRngHigh.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAODACRngHigh.__doc__ = \
"""int32 DAQmxGetAODACRngHigh(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3121"""
DAQmxSetAODACRngHigh = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRngHigh
DAQmxSetAODACRngHigh.restype = int32
DAQmxSetAODACRngHigh.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAODACRngHigh.__doc__ = \
"""int32 DAQmxSetAODACRngHigh(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3122"""
DAQmxResetAODACRngHigh = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRngHigh
DAQmxResetAODACRngHigh.restype = int32
DAQmxResetAODACRngHigh.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRngHigh.__doc__ = \
"""int32 DAQmxResetAODACRngHigh(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3123"""
DAQmxGetAODACRngLow = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRngLow
DAQmxGetAODACRngLow.restype = int32
DAQmxGetAODACRngLow.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAODACRngLow.__doc__ = \
"""int32 DAQmxGetAODACRngLow(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3125"""
DAQmxSetAODACRngLow = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRngLow
DAQmxSetAODACRngLow.restype = int32
DAQmxSetAODACRngLow.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAODACRngLow.__doc__ = \
"""int32 DAQmxSetAODACRngLow(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3126"""
DAQmxResetAODACRngLow = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRngLow
DAQmxResetAODACRngLow.restype = int32
DAQmxResetAODACRngLow.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRngLow.__doc__ = \
"""int32 DAQmxResetAODACRngLow(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3127"""
DAQmxGetAODACRefConnToGnd = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRefConnToGnd
DAQmxGetAODACRefConnToGnd.restype = int32
DAQmxGetAODACRefConnToGnd.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAODACRefConnToGnd.__doc__ = \
"""int32 DAQmxGetAODACRefConnToGnd(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3129"""
DAQmxSetAODACRefConnToGnd = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRefConnToGnd
DAQmxSetAODACRefConnToGnd.restype = int32
DAQmxSetAODACRefConnToGnd.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAODACRefConnToGnd.__doc__ = \
"""int32 DAQmxSetAODACRefConnToGnd(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3130"""
DAQmxResetAODACRefConnToGnd = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRefConnToGnd
DAQmxResetAODACRefConnToGnd.restype = int32
DAQmxResetAODACRefConnToGnd.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRefConnToGnd.__doc__ = \
"""int32 DAQmxResetAODACRefConnToGnd(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3131"""
DAQmxGetAODACRefAllowConnToGnd = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRefAllowConnToGnd
DAQmxGetAODACRefAllowConnToGnd.restype = int32
DAQmxGetAODACRefAllowConnToGnd.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAODACRefAllowConnToGnd.__doc__ = \
"""int32 DAQmxGetAODACRefAllowConnToGnd(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3133"""
DAQmxSetAODACRefAllowConnToGnd = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRefAllowConnToGnd
DAQmxSetAODACRefAllowConnToGnd.restype = int32
DAQmxSetAODACRefAllowConnToGnd.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAODACRefAllowConnToGnd.__doc__ = \
"""int32 DAQmxSetAODACRefAllowConnToGnd(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3134"""
DAQmxResetAODACRefAllowConnToGnd = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRefAllowConnToGnd
DAQmxResetAODACRefAllowConnToGnd.restype = int32
DAQmxResetAODACRefAllowConnToGnd.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRefAllowConnToGnd.__doc__ = \
"""int32 DAQmxResetAODACRefAllowConnToGnd(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3135"""
DAQmxGetAODACRefSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRefSrc
DAQmxGetAODACRefSrc.restype = int32
DAQmxGetAODACRefSrc.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAODACRefSrc.__doc__ = \
"""int32 DAQmxGetAODACRefSrc(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3138"""
DAQmxSetAODACRefSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRefSrc
DAQmxSetAODACRefSrc.restype = int32
DAQmxSetAODACRefSrc.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAODACRefSrc.__doc__ = \
"""int32 DAQmxSetAODACRefSrc(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3139"""
DAQmxResetAODACRefSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRefSrc
DAQmxResetAODACRefSrc.restype = int32
DAQmxResetAODACRefSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRefSrc.__doc__ = \
"""int32 DAQmxResetAODACRefSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3140"""
DAQmxGetAODACRefExtSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRefExtSrc
DAQmxGetAODACRefExtSrc.restype = int32
DAQmxGetAODACRefExtSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAODACRefExtSrc.__doc__ = \
"""int32 DAQmxGetAODACRefExtSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3142"""
DAQmxSetAODACRefExtSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRefExtSrc
DAQmxSetAODACRefExtSrc.restype = int32
DAQmxSetAODACRefExtSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAODACRefExtSrc.__doc__ = \
"""int32 DAQmxSetAODACRefExtSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3143"""
DAQmxResetAODACRefExtSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRefExtSrc
DAQmxResetAODACRefExtSrc.restype = int32
DAQmxResetAODACRefExtSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRefExtSrc.__doc__ = \
"""int32 DAQmxResetAODACRefExtSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3144"""
DAQmxGetAODACRefVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACRefVal
DAQmxGetAODACRefVal.restype = int32
DAQmxGetAODACRefVal.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAODACRefVal.__doc__ = \
"""int32 DAQmxGetAODACRefVal(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3146"""
DAQmxSetAODACRefVal = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACRefVal
DAQmxSetAODACRefVal.restype = int32
DAQmxSetAODACRefVal.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAODACRefVal.__doc__ = \
"""int32 DAQmxSetAODACRefVal(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3147"""
DAQmxResetAODACRefVal = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACRefVal
DAQmxResetAODACRefVal.restype = int32
DAQmxResetAODACRefVal.argtypes = [TaskHandle, STRING]
DAQmxResetAODACRefVal.__doc__ = \
"""int32 DAQmxResetAODACRefVal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3148"""
DAQmxGetAODACOffsetSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACOffsetSrc
DAQmxGetAODACOffsetSrc.restype = int32
DAQmxGetAODACOffsetSrc.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAODACOffsetSrc.__doc__ = \
"""int32 DAQmxGetAODACOffsetSrc(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3151"""
DAQmxSetAODACOffsetSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACOffsetSrc
DAQmxSetAODACOffsetSrc.restype = int32
DAQmxSetAODACOffsetSrc.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAODACOffsetSrc.__doc__ = \
"""int32 DAQmxSetAODACOffsetSrc(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3152"""
DAQmxResetAODACOffsetSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACOffsetSrc
DAQmxResetAODACOffsetSrc.restype = int32
DAQmxResetAODACOffsetSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAODACOffsetSrc.__doc__ = \
"""int32 DAQmxResetAODACOffsetSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3153"""
DAQmxGetAODACOffsetExtSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACOffsetExtSrc
DAQmxGetAODACOffsetExtSrc.restype = int32
DAQmxGetAODACOffsetExtSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAODACOffsetExtSrc.__doc__ = \
"""int32 DAQmxGetAODACOffsetExtSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3155"""
DAQmxSetAODACOffsetExtSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACOffsetExtSrc
DAQmxSetAODACOffsetExtSrc.restype = int32
DAQmxSetAODACOffsetExtSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAODACOffsetExtSrc.__doc__ = \
"""int32 DAQmxSetAODACOffsetExtSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3156"""
DAQmxResetAODACOffsetExtSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACOffsetExtSrc
DAQmxResetAODACOffsetExtSrc.restype = int32
DAQmxResetAODACOffsetExtSrc.argtypes = [TaskHandle, STRING]
DAQmxResetAODACOffsetExtSrc.__doc__ = \
"""int32 DAQmxResetAODACOffsetExtSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3157"""
DAQmxGetAODACOffsetVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODACOffsetVal
DAQmxGetAODACOffsetVal.restype = int32
DAQmxGetAODACOffsetVal.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAODACOffsetVal.__doc__ = \
"""int32 DAQmxGetAODACOffsetVal(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3159"""
DAQmxSetAODACOffsetVal = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODACOffsetVal
DAQmxSetAODACOffsetVal.restype = int32
DAQmxSetAODACOffsetVal.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAODACOffsetVal.__doc__ = \
"""int32 DAQmxSetAODACOffsetVal(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3160"""
DAQmxResetAODACOffsetVal = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODACOffsetVal
DAQmxResetAODACOffsetVal.restype = int32
DAQmxResetAODACOffsetVal.argtypes = [TaskHandle, STRING]
DAQmxResetAODACOffsetVal.__doc__ = \
"""int32 DAQmxResetAODACOffsetVal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3161"""
DAQmxGetAOReglitchEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOReglitchEnable
DAQmxGetAOReglitchEnable.restype = int32
DAQmxGetAOReglitchEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAOReglitchEnable.__doc__ = \
"""int32 DAQmxGetAOReglitchEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3163"""
DAQmxSetAOReglitchEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOReglitchEnable
DAQmxSetAOReglitchEnable.restype = int32
DAQmxSetAOReglitchEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAOReglitchEnable.__doc__ = \
"""int32 DAQmxSetAOReglitchEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3164"""
DAQmxResetAOReglitchEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOReglitchEnable
DAQmxResetAOReglitchEnable.restype = int32
DAQmxResetAOReglitchEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAOReglitchEnable.__doc__ = \
"""int32 DAQmxResetAOReglitchEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3165"""
DAQmxGetAOGain = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOGain
DAQmxGetAOGain.restype = int32
DAQmxGetAOGain.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAOGain.__doc__ = \
"""int32 DAQmxGetAOGain(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3167"""
DAQmxSetAOGain = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOGain
DAQmxSetAOGain.restype = int32
DAQmxSetAOGain.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAOGain.__doc__ = \
"""int32 DAQmxSetAOGain(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3168"""
DAQmxResetAOGain = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOGain
DAQmxResetAOGain.restype = int32
DAQmxResetAOGain.argtypes = [TaskHandle, STRING]
DAQmxResetAOGain.__doc__ = \
"""int32 DAQmxResetAOGain(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3169"""
DAQmxGetAOUseOnlyOnBrdMem = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOUseOnlyOnBrdMem
DAQmxGetAOUseOnlyOnBrdMem.restype = int32
DAQmxGetAOUseOnlyOnBrdMem.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAOUseOnlyOnBrdMem.__doc__ = \
"""int32 DAQmxGetAOUseOnlyOnBrdMem(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3171"""
DAQmxSetAOUseOnlyOnBrdMem = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOUseOnlyOnBrdMem
DAQmxSetAOUseOnlyOnBrdMem.restype = int32
DAQmxSetAOUseOnlyOnBrdMem.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAOUseOnlyOnBrdMem.__doc__ = \
"""int32 DAQmxSetAOUseOnlyOnBrdMem(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3172"""
DAQmxResetAOUseOnlyOnBrdMem = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOUseOnlyOnBrdMem
DAQmxResetAOUseOnlyOnBrdMem.restype = int32
DAQmxResetAOUseOnlyOnBrdMem.argtypes = [TaskHandle, STRING]
DAQmxResetAOUseOnlyOnBrdMem.__doc__ = \
"""int32 DAQmxResetAOUseOnlyOnBrdMem(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3173"""
DAQmxGetAODataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODataXferMech
DAQmxGetAODataXferMech.restype = int32
DAQmxGetAODataXferMech.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAODataXferMech.__doc__ = \
"""int32 DAQmxGetAODataXferMech(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3176"""
DAQmxSetAODataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODataXferMech
DAQmxSetAODataXferMech.restype = int32
DAQmxSetAODataXferMech.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAODataXferMech.__doc__ = \
"""int32 DAQmxSetAODataXferMech(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3177"""
DAQmxResetAODataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODataXferMech
DAQmxResetAODataXferMech.restype = int32
DAQmxResetAODataXferMech.argtypes = [TaskHandle, STRING]
DAQmxResetAODataXferMech.__doc__ = \
"""int32 DAQmxResetAODataXferMech(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3178"""
DAQmxGetAODataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODataXferReqCond
DAQmxGetAODataXferReqCond.restype = int32
DAQmxGetAODataXferReqCond.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAODataXferReqCond.__doc__ = \
"""int32 DAQmxGetAODataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3181"""
DAQmxSetAODataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxSetAODataXferReqCond
DAQmxSetAODataXferReqCond.restype = int32
DAQmxSetAODataXferReqCond.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAODataXferReqCond.__doc__ = \
"""int32 DAQmxSetAODataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3182"""
DAQmxResetAODataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxResetAODataXferReqCond
DAQmxResetAODataXferReqCond.restype = int32
DAQmxResetAODataXferReqCond.argtypes = [TaskHandle, STRING]
DAQmxResetAODataXferReqCond.__doc__ = \
"""int32 DAQmxResetAODataXferReqCond(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3183"""
DAQmxGetAOUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOUsbXferReqSize
DAQmxGetAOUsbXferReqSize.restype = int32
DAQmxGetAOUsbXferReqSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAOUsbXferReqSize.__doc__ = \
"""int32 DAQmxGetAOUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3185"""
DAQmxSetAOUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOUsbXferReqSize
DAQmxSetAOUsbXferReqSize.restype = int32
DAQmxSetAOUsbXferReqSize.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAOUsbXferReqSize.__doc__ = \
"""int32 DAQmxSetAOUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3186"""
DAQmxResetAOUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOUsbXferReqSize
DAQmxResetAOUsbXferReqSize.restype = int32
DAQmxResetAOUsbXferReqSize.argtypes = [TaskHandle, STRING]
DAQmxResetAOUsbXferReqSize.__doc__ = \
"""int32 DAQmxResetAOUsbXferReqSize(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3187"""
DAQmxGetAOMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOMemMapEnable
DAQmxGetAOMemMapEnable.restype = int32
DAQmxGetAOMemMapEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAOMemMapEnable.__doc__ = \
"""int32 DAQmxGetAOMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3189"""
DAQmxSetAOMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOMemMapEnable
DAQmxSetAOMemMapEnable.restype = int32
DAQmxSetAOMemMapEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAOMemMapEnable.__doc__ = \
"""int32 DAQmxSetAOMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3190"""
DAQmxResetAOMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOMemMapEnable
DAQmxResetAOMemMapEnable.restype = int32
DAQmxResetAOMemMapEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAOMemMapEnable.__doc__ = \
"""int32 DAQmxResetAOMemMapEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3191"""
DAQmxGetAODevScalingCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxGetAODevScalingCoeff
DAQmxGetAODevScalingCoeff.restype = int32
DAQmxGetAODevScalingCoeff.argtypes = [TaskHandle, STRING, POINTER(float64), uInt32]
DAQmxGetAODevScalingCoeff.__doc__ = \
"""int32 DAQmxGetAODevScalingCoeff(TaskHandle taskHandle, unknown * channel, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3193"""
DAQmxGetAOEnhancedImageRejectionEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetAOEnhancedImageRejectionEnable
DAQmxGetAOEnhancedImageRejectionEnable.restype = int32
DAQmxGetAOEnhancedImageRejectionEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetAOEnhancedImageRejectionEnable.__doc__ = \
"""int32 DAQmxGetAOEnhancedImageRejectionEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3195"""
DAQmxSetAOEnhancedImageRejectionEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetAOEnhancedImageRejectionEnable
DAQmxSetAOEnhancedImageRejectionEnable.restype = int32
DAQmxSetAOEnhancedImageRejectionEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetAOEnhancedImageRejectionEnable.__doc__ = \
"""int32 DAQmxSetAOEnhancedImageRejectionEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3196"""
DAQmxResetAOEnhancedImageRejectionEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetAOEnhancedImageRejectionEnable
DAQmxResetAOEnhancedImageRejectionEnable.restype = int32
DAQmxResetAOEnhancedImageRejectionEnable.argtypes = [TaskHandle, STRING]
DAQmxResetAOEnhancedImageRejectionEnable.__doc__ = \
"""int32 DAQmxResetAOEnhancedImageRejectionEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3197"""
DAQmxGetDIInvertLines = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIInvertLines
DAQmxGetDIInvertLines.restype = int32
DAQmxGetDIInvertLines.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDIInvertLines.__doc__ = \
"""int32 DAQmxGetDIInvertLines(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3199"""
DAQmxSetDIInvertLines = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIInvertLines
DAQmxSetDIInvertLines.restype = int32
DAQmxSetDIInvertLines.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDIInvertLines.__doc__ = \
"""int32 DAQmxSetDIInvertLines(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3200"""
DAQmxResetDIInvertLines = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIInvertLines
DAQmxResetDIInvertLines.restype = int32
DAQmxResetDIInvertLines.argtypes = [TaskHandle, STRING]
DAQmxResetDIInvertLines.__doc__ = \
"""int32 DAQmxResetDIInvertLines(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3201"""
DAQmxGetDINumLines = _stdcall_libraries['nicaiu.dll'].DAQmxGetDINumLines
DAQmxGetDINumLines.restype = int32
DAQmxGetDINumLines.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetDINumLines.__doc__ = \
"""int32 DAQmxGetDINumLines(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3203"""
DAQmxGetDIDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIDigFltrEnable
DAQmxGetDIDigFltrEnable.restype = int32
DAQmxGetDIDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDIDigFltrEnable.__doc__ = \
"""int32 DAQmxGetDIDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3205"""
DAQmxSetDIDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIDigFltrEnable
DAQmxSetDIDigFltrEnable.restype = int32
DAQmxSetDIDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDIDigFltrEnable.__doc__ = \
"""int32 DAQmxSetDIDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3206"""
DAQmxResetDIDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIDigFltrEnable
DAQmxResetDIDigFltrEnable.restype = int32
DAQmxResetDIDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetDIDigFltrEnable.__doc__ = \
"""int32 DAQmxResetDIDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3207"""
DAQmxGetDIDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIDigFltrMinPulseWidth
DAQmxGetDIDigFltrMinPulseWidth.restype = int32
DAQmxGetDIDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetDIDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetDIDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3209"""
DAQmxSetDIDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIDigFltrMinPulseWidth
DAQmxSetDIDigFltrMinPulseWidth.restype = int32
DAQmxSetDIDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetDIDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetDIDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3210"""
DAQmxResetDIDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIDigFltrMinPulseWidth
DAQmxResetDIDigFltrMinPulseWidth.restype = int32
DAQmxResetDIDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetDIDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetDIDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3211"""
DAQmxGetDITristate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDITristate
DAQmxGetDITristate.restype = int32
DAQmxGetDITristate.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDITristate.__doc__ = \
"""int32 DAQmxGetDITristate(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3213"""
DAQmxSetDITristate = _stdcall_libraries['nicaiu.dll'].DAQmxSetDITristate
DAQmxSetDITristate.restype = int32
DAQmxSetDITristate.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDITristate.__doc__ = \
"""int32 DAQmxSetDITristate(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3214"""
DAQmxResetDITristate = _stdcall_libraries['nicaiu.dll'].DAQmxResetDITristate
DAQmxResetDITristate.restype = int32
DAQmxResetDITristate.argtypes = [TaskHandle, STRING]
DAQmxResetDITristate.__doc__ = \
"""int32 DAQmxResetDITristate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3215"""
DAQmxGetDILogicFamily = _stdcall_libraries['nicaiu.dll'].DAQmxGetDILogicFamily
DAQmxGetDILogicFamily.restype = int32
DAQmxGetDILogicFamily.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDILogicFamily.__doc__ = \
"""int32 DAQmxGetDILogicFamily(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3218"""
DAQmxSetDILogicFamily = _stdcall_libraries['nicaiu.dll'].DAQmxSetDILogicFamily
DAQmxSetDILogicFamily.restype = int32
DAQmxSetDILogicFamily.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDILogicFamily.__doc__ = \
"""int32 DAQmxSetDILogicFamily(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3219"""
DAQmxResetDILogicFamily = _stdcall_libraries['nicaiu.dll'].DAQmxResetDILogicFamily
DAQmxResetDILogicFamily.restype = int32
DAQmxResetDILogicFamily.argtypes = [TaskHandle, STRING]
DAQmxResetDILogicFamily.__doc__ = \
"""int32 DAQmxResetDILogicFamily(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3220"""
DAQmxGetDIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIDataXferMech
DAQmxGetDIDataXferMech.restype = int32
DAQmxGetDIDataXferMech.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDIDataXferMech.__doc__ = \
"""int32 DAQmxGetDIDataXferMech(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3223"""
DAQmxSetDIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIDataXferMech
DAQmxSetDIDataXferMech.restype = int32
DAQmxSetDIDataXferMech.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDIDataXferMech.__doc__ = \
"""int32 DAQmxSetDIDataXferMech(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3224"""
DAQmxResetDIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIDataXferMech
DAQmxResetDIDataXferMech.restype = int32
DAQmxResetDIDataXferMech.argtypes = [TaskHandle, STRING]
DAQmxResetDIDataXferMech.__doc__ = \
"""int32 DAQmxResetDIDataXferMech(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3225"""
DAQmxGetDIDataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIDataXferReqCond
DAQmxGetDIDataXferReqCond.restype = int32
DAQmxGetDIDataXferReqCond.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDIDataXferReqCond.__doc__ = \
"""int32 DAQmxGetDIDataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3228"""
DAQmxSetDIDataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIDataXferReqCond
DAQmxSetDIDataXferReqCond.restype = int32
DAQmxSetDIDataXferReqCond.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDIDataXferReqCond.__doc__ = \
"""int32 DAQmxSetDIDataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3229"""
DAQmxResetDIDataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIDataXferReqCond
DAQmxResetDIDataXferReqCond.restype = int32
DAQmxResetDIDataXferReqCond.argtypes = [TaskHandle, STRING]
DAQmxResetDIDataXferReqCond.__doc__ = \
"""int32 DAQmxResetDIDataXferReqCond(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3230"""
DAQmxGetDIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIUsbXferReqSize
DAQmxGetDIUsbXferReqSize.restype = int32
DAQmxGetDIUsbXferReqSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetDIUsbXferReqSize.__doc__ = \
"""int32 DAQmxGetDIUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3232"""
DAQmxSetDIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIUsbXferReqSize
DAQmxSetDIUsbXferReqSize.restype = int32
DAQmxSetDIUsbXferReqSize.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetDIUsbXferReqSize.__doc__ = \
"""int32 DAQmxSetDIUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3233"""
DAQmxResetDIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIUsbXferReqSize
DAQmxResetDIUsbXferReqSize.restype = int32
DAQmxResetDIUsbXferReqSize.argtypes = [TaskHandle, STRING]
DAQmxResetDIUsbXferReqSize.__doc__ = \
"""int32 DAQmxResetDIUsbXferReqSize(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3234"""
DAQmxGetDIMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIMemMapEnable
DAQmxGetDIMemMapEnable.restype = int32
DAQmxGetDIMemMapEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDIMemMapEnable.__doc__ = \
"""int32 DAQmxGetDIMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3236"""
DAQmxSetDIMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIMemMapEnable
DAQmxSetDIMemMapEnable.restype = int32
DAQmxSetDIMemMapEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDIMemMapEnable.__doc__ = \
"""int32 DAQmxSetDIMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3237"""
DAQmxResetDIMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIMemMapEnable
DAQmxResetDIMemMapEnable.restype = int32
DAQmxResetDIMemMapEnable.argtypes = [TaskHandle, STRING]
DAQmxResetDIMemMapEnable.__doc__ = \
"""int32 DAQmxResetDIMemMapEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3238"""
DAQmxGetDIAcquireOn = _stdcall_libraries['nicaiu.dll'].DAQmxGetDIAcquireOn
DAQmxGetDIAcquireOn.restype = int32
DAQmxGetDIAcquireOn.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDIAcquireOn.__doc__ = \
"""int32 DAQmxGetDIAcquireOn(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3241"""
DAQmxSetDIAcquireOn = _stdcall_libraries['nicaiu.dll'].DAQmxSetDIAcquireOn
DAQmxSetDIAcquireOn.restype = int32
DAQmxSetDIAcquireOn.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDIAcquireOn.__doc__ = \
"""int32 DAQmxSetDIAcquireOn(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3242"""
DAQmxResetDIAcquireOn = _stdcall_libraries['nicaiu.dll'].DAQmxResetDIAcquireOn
DAQmxResetDIAcquireOn.restype = int32
DAQmxResetDIAcquireOn.argtypes = [TaskHandle, STRING]
DAQmxResetDIAcquireOn.__doc__ = \
"""int32 DAQmxResetDIAcquireOn(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3243"""
DAQmxGetDOOutputDriveType = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOOutputDriveType
DAQmxGetDOOutputDriveType.restype = int32
DAQmxGetDOOutputDriveType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDOOutputDriveType.__doc__ = \
"""int32 DAQmxGetDOOutputDriveType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3246"""
DAQmxSetDOOutputDriveType = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOOutputDriveType
DAQmxSetDOOutputDriveType.restype = int32
DAQmxSetDOOutputDriveType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDOOutputDriveType.__doc__ = \
"""int32 DAQmxSetDOOutputDriveType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3247"""
DAQmxResetDOOutputDriveType = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOOutputDriveType
DAQmxResetDOOutputDriveType.restype = int32
DAQmxResetDOOutputDriveType.argtypes = [TaskHandle, STRING]
DAQmxResetDOOutputDriveType.__doc__ = \
"""int32 DAQmxResetDOOutputDriveType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3248"""
DAQmxGetDOInvertLines = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOInvertLines
DAQmxGetDOInvertLines.restype = int32
DAQmxGetDOInvertLines.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDOInvertLines.__doc__ = \
"""int32 DAQmxGetDOInvertLines(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3250"""
DAQmxSetDOInvertLines = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOInvertLines
DAQmxSetDOInvertLines.restype = int32
DAQmxSetDOInvertLines.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDOInvertLines.__doc__ = \
"""int32 DAQmxSetDOInvertLines(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3251"""
DAQmxResetDOInvertLines = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOInvertLines
DAQmxResetDOInvertLines.restype = int32
DAQmxResetDOInvertLines.argtypes = [TaskHandle, STRING]
DAQmxResetDOInvertLines.__doc__ = \
"""int32 DAQmxResetDOInvertLines(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3252"""
DAQmxGetDONumLines = _stdcall_libraries['nicaiu.dll'].DAQmxGetDONumLines
DAQmxGetDONumLines.restype = int32
DAQmxGetDONumLines.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetDONumLines.__doc__ = \
"""int32 DAQmxGetDONumLines(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3254"""
DAQmxGetDOTristate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOTristate
DAQmxGetDOTristate.restype = int32
DAQmxGetDOTristate.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDOTristate.__doc__ = \
"""int32 DAQmxGetDOTristate(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3256"""
DAQmxSetDOTristate = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOTristate
DAQmxSetDOTristate.restype = int32
DAQmxSetDOTristate.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDOTristate.__doc__ = \
"""int32 DAQmxSetDOTristate(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3257"""
DAQmxResetDOTristate = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOTristate
DAQmxResetDOTristate.restype = int32
DAQmxResetDOTristate.argtypes = [TaskHandle, STRING]
DAQmxResetDOTristate.__doc__ = \
"""int32 DAQmxResetDOTristate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3258"""
DAQmxGetDOLineStatesStartState = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOLineStatesStartState
DAQmxGetDOLineStatesStartState.restype = int32
DAQmxGetDOLineStatesStartState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDOLineStatesStartState.__doc__ = \
"""int32 DAQmxGetDOLineStatesStartState(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3261"""
DAQmxSetDOLineStatesStartState = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOLineStatesStartState
DAQmxSetDOLineStatesStartState.restype = int32
DAQmxSetDOLineStatesStartState.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDOLineStatesStartState.__doc__ = \
"""int32 DAQmxSetDOLineStatesStartState(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3262"""
DAQmxResetDOLineStatesStartState = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOLineStatesStartState
DAQmxResetDOLineStatesStartState.restype = int32
DAQmxResetDOLineStatesStartState.argtypes = [TaskHandle, STRING]
DAQmxResetDOLineStatesStartState.__doc__ = \
"""int32 DAQmxResetDOLineStatesStartState(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3263"""
DAQmxGetDOLineStatesPausedState = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOLineStatesPausedState
DAQmxGetDOLineStatesPausedState.restype = int32
DAQmxGetDOLineStatesPausedState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDOLineStatesPausedState.__doc__ = \
"""int32 DAQmxGetDOLineStatesPausedState(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3266"""
DAQmxSetDOLineStatesPausedState = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOLineStatesPausedState
DAQmxSetDOLineStatesPausedState.restype = int32
DAQmxSetDOLineStatesPausedState.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDOLineStatesPausedState.__doc__ = \
"""int32 DAQmxSetDOLineStatesPausedState(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3267"""
DAQmxResetDOLineStatesPausedState = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOLineStatesPausedState
DAQmxResetDOLineStatesPausedState.restype = int32
DAQmxResetDOLineStatesPausedState.argtypes = [TaskHandle, STRING]
DAQmxResetDOLineStatesPausedState.__doc__ = \
"""int32 DAQmxResetDOLineStatesPausedState(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3268"""
DAQmxGetDOLineStatesDoneState = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOLineStatesDoneState
DAQmxGetDOLineStatesDoneState.restype = int32
DAQmxGetDOLineStatesDoneState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDOLineStatesDoneState.__doc__ = \
"""int32 DAQmxGetDOLineStatesDoneState(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3271"""
DAQmxSetDOLineStatesDoneState = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOLineStatesDoneState
DAQmxSetDOLineStatesDoneState.restype = int32
DAQmxSetDOLineStatesDoneState.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDOLineStatesDoneState.__doc__ = \
"""int32 DAQmxSetDOLineStatesDoneState(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3272"""
DAQmxResetDOLineStatesDoneState = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOLineStatesDoneState
DAQmxResetDOLineStatesDoneState.restype = int32
DAQmxResetDOLineStatesDoneState.argtypes = [TaskHandle, STRING]
DAQmxResetDOLineStatesDoneState.__doc__ = \
"""int32 DAQmxResetDOLineStatesDoneState(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3273"""
DAQmxGetDOLogicFamily = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOLogicFamily
DAQmxGetDOLogicFamily.restype = int32
DAQmxGetDOLogicFamily.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDOLogicFamily.__doc__ = \
"""int32 DAQmxGetDOLogicFamily(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3276"""
DAQmxSetDOLogicFamily = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOLogicFamily
DAQmxSetDOLogicFamily.restype = int32
DAQmxSetDOLogicFamily.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDOLogicFamily.__doc__ = \
"""int32 DAQmxSetDOLogicFamily(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3277"""
DAQmxResetDOLogicFamily = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOLogicFamily
DAQmxResetDOLogicFamily.restype = int32
DAQmxResetDOLogicFamily.argtypes = [TaskHandle, STRING]
DAQmxResetDOLogicFamily.__doc__ = \
"""int32 DAQmxResetDOLogicFamily(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3278"""
DAQmxGetDOOvercurrentLimit = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOOvercurrentLimit
DAQmxGetDOOvercurrentLimit.restype = int32
DAQmxGetDOOvercurrentLimit.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetDOOvercurrentLimit.__doc__ = \
"""int32 DAQmxGetDOOvercurrentLimit(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3280"""
DAQmxSetDOOvercurrentLimit = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOOvercurrentLimit
DAQmxSetDOOvercurrentLimit.restype = int32
DAQmxSetDOOvercurrentLimit.argtypes = [TaskHandle, STRING, float64]
DAQmxSetDOOvercurrentLimit.__doc__ = \
"""int32 DAQmxSetDOOvercurrentLimit(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3281"""
DAQmxResetDOOvercurrentLimit = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOOvercurrentLimit
DAQmxResetDOOvercurrentLimit.restype = int32
DAQmxResetDOOvercurrentLimit.argtypes = [TaskHandle, STRING]
DAQmxResetDOOvercurrentLimit.__doc__ = \
"""int32 DAQmxResetDOOvercurrentLimit(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3282"""
DAQmxGetDOOvercurrentAutoReenable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOOvercurrentAutoReenable
DAQmxGetDOOvercurrentAutoReenable.restype = int32
DAQmxGetDOOvercurrentAutoReenable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDOOvercurrentAutoReenable.__doc__ = \
"""int32 DAQmxGetDOOvercurrentAutoReenable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3284"""
DAQmxSetDOOvercurrentAutoReenable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOOvercurrentAutoReenable
DAQmxSetDOOvercurrentAutoReenable.restype = int32
DAQmxSetDOOvercurrentAutoReenable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDOOvercurrentAutoReenable.__doc__ = \
"""int32 DAQmxSetDOOvercurrentAutoReenable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3285"""
DAQmxResetDOOvercurrentAutoReenable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOOvercurrentAutoReenable
DAQmxResetDOOvercurrentAutoReenable.restype = int32
DAQmxResetDOOvercurrentAutoReenable.argtypes = [TaskHandle, STRING]
DAQmxResetDOOvercurrentAutoReenable.__doc__ = \
"""int32 DAQmxResetDOOvercurrentAutoReenable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3286"""
DAQmxGetDOOvercurrentReenablePeriod = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOOvercurrentReenablePeriod
DAQmxGetDOOvercurrentReenablePeriod.restype = int32
DAQmxGetDOOvercurrentReenablePeriod.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetDOOvercurrentReenablePeriod.__doc__ = \
"""int32 DAQmxGetDOOvercurrentReenablePeriod(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3288"""
DAQmxSetDOOvercurrentReenablePeriod = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOOvercurrentReenablePeriod
DAQmxSetDOOvercurrentReenablePeriod.restype = int32
DAQmxSetDOOvercurrentReenablePeriod.argtypes = [TaskHandle, STRING, float64]
DAQmxSetDOOvercurrentReenablePeriod.__doc__ = \
"""int32 DAQmxSetDOOvercurrentReenablePeriod(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3289"""
DAQmxResetDOOvercurrentReenablePeriod = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOOvercurrentReenablePeriod
DAQmxResetDOOvercurrentReenablePeriod.restype = int32
DAQmxResetDOOvercurrentReenablePeriod.argtypes = [TaskHandle, STRING]
DAQmxResetDOOvercurrentReenablePeriod.__doc__ = \
"""int32 DAQmxResetDOOvercurrentReenablePeriod(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3290"""
DAQmxGetDOUseOnlyOnBrdMem = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOUseOnlyOnBrdMem
DAQmxGetDOUseOnlyOnBrdMem.restype = int32
DAQmxGetDOUseOnlyOnBrdMem.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDOUseOnlyOnBrdMem.__doc__ = \
"""int32 DAQmxGetDOUseOnlyOnBrdMem(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3292"""
DAQmxSetDOUseOnlyOnBrdMem = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOUseOnlyOnBrdMem
DAQmxSetDOUseOnlyOnBrdMem.restype = int32
DAQmxSetDOUseOnlyOnBrdMem.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDOUseOnlyOnBrdMem.__doc__ = \
"""int32 DAQmxSetDOUseOnlyOnBrdMem(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3293"""
DAQmxResetDOUseOnlyOnBrdMem = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOUseOnlyOnBrdMem
DAQmxResetDOUseOnlyOnBrdMem.restype = int32
DAQmxResetDOUseOnlyOnBrdMem.argtypes = [TaskHandle, STRING]
DAQmxResetDOUseOnlyOnBrdMem.__doc__ = \
"""int32 DAQmxResetDOUseOnlyOnBrdMem(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3294"""
DAQmxGetDODataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxGetDODataXferMech
DAQmxGetDODataXferMech.restype = int32
DAQmxGetDODataXferMech.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDODataXferMech.__doc__ = \
"""int32 DAQmxGetDODataXferMech(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3297"""
DAQmxSetDODataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxSetDODataXferMech
DAQmxSetDODataXferMech.restype = int32
DAQmxSetDODataXferMech.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDODataXferMech.__doc__ = \
"""int32 DAQmxSetDODataXferMech(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3298"""
DAQmxResetDODataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxResetDODataXferMech
DAQmxResetDODataXferMech.restype = int32
DAQmxResetDODataXferMech.argtypes = [TaskHandle, STRING]
DAQmxResetDODataXferMech.__doc__ = \
"""int32 DAQmxResetDODataXferMech(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3299"""
DAQmxGetDODataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxGetDODataXferReqCond
DAQmxGetDODataXferReqCond.restype = int32
DAQmxGetDODataXferReqCond.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDODataXferReqCond.__doc__ = \
"""int32 DAQmxGetDODataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3302"""
DAQmxSetDODataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxSetDODataXferReqCond
DAQmxSetDODataXferReqCond.restype = int32
DAQmxSetDODataXferReqCond.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDODataXferReqCond.__doc__ = \
"""int32 DAQmxSetDODataXferReqCond(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3303"""
DAQmxResetDODataXferReqCond = _stdcall_libraries['nicaiu.dll'].DAQmxResetDODataXferReqCond
DAQmxResetDODataXferReqCond.restype = int32
DAQmxResetDODataXferReqCond.argtypes = [TaskHandle, STRING]
DAQmxResetDODataXferReqCond.__doc__ = \
"""int32 DAQmxResetDODataXferReqCond(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3304"""
DAQmxGetDOUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOUsbXferReqSize
DAQmxGetDOUsbXferReqSize.restype = int32
DAQmxGetDOUsbXferReqSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetDOUsbXferReqSize.__doc__ = \
"""int32 DAQmxGetDOUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3306"""
DAQmxSetDOUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOUsbXferReqSize
DAQmxSetDOUsbXferReqSize.restype = int32
DAQmxSetDOUsbXferReqSize.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetDOUsbXferReqSize.__doc__ = \
"""int32 DAQmxSetDOUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3307"""
DAQmxResetDOUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOUsbXferReqSize
DAQmxResetDOUsbXferReqSize.restype = int32
DAQmxResetDOUsbXferReqSize.argtypes = [TaskHandle, STRING]
DAQmxResetDOUsbXferReqSize.__doc__ = \
"""int32 DAQmxResetDOUsbXferReqSize(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3308"""
DAQmxGetDOMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOMemMapEnable
DAQmxGetDOMemMapEnable.restype = int32
DAQmxGetDOMemMapEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetDOMemMapEnable.__doc__ = \
"""int32 DAQmxGetDOMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3310"""
DAQmxSetDOMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOMemMapEnable
DAQmxSetDOMemMapEnable.restype = int32
DAQmxSetDOMemMapEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetDOMemMapEnable.__doc__ = \
"""int32 DAQmxSetDOMemMapEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3311"""
DAQmxResetDOMemMapEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOMemMapEnable
DAQmxResetDOMemMapEnable.restype = int32
DAQmxResetDOMemMapEnable.argtypes = [TaskHandle, STRING]
DAQmxResetDOMemMapEnable.__doc__ = \
"""int32 DAQmxResetDOMemMapEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3312"""
DAQmxGetDOGenerateOn = _stdcall_libraries['nicaiu.dll'].DAQmxGetDOGenerateOn
DAQmxGetDOGenerateOn.restype = int32
DAQmxGetDOGenerateOn.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDOGenerateOn.__doc__ = \
"""int32 DAQmxGetDOGenerateOn(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3315"""
DAQmxSetDOGenerateOn = _stdcall_libraries['nicaiu.dll'].DAQmxSetDOGenerateOn
DAQmxSetDOGenerateOn.restype = int32
DAQmxSetDOGenerateOn.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDOGenerateOn.__doc__ = \
"""int32 DAQmxSetDOGenerateOn(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3316"""
DAQmxResetDOGenerateOn = _stdcall_libraries['nicaiu.dll'].DAQmxResetDOGenerateOn
DAQmxResetDOGenerateOn.restype = int32
DAQmxResetDOGenerateOn.argtypes = [TaskHandle, STRING]
DAQmxResetDOGenerateOn.__doc__ = \
"""int32 DAQmxResetDOGenerateOn(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3317"""
DAQmxGetCIMax = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIMax
DAQmxGetCIMax.restype = int32
DAQmxGetCIMax.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIMax.__doc__ = \
"""int32 DAQmxGetCIMax(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3319"""
DAQmxSetCIMax = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIMax
DAQmxSetCIMax.restype = int32
DAQmxSetCIMax.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIMax.__doc__ = \
"""int32 DAQmxSetCIMax(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3320"""
DAQmxResetCIMax = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIMax
DAQmxResetCIMax.restype = int32
DAQmxResetCIMax.argtypes = [TaskHandle, STRING]
DAQmxResetCIMax.__doc__ = \
"""int32 DAQmxResetCIMax(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3321"""
DAQmxGetCIMin = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIMin
DAQmxGetCIMin.restype = int32
DAQmxGetCIMin.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIMin.__doc__ = \
"""int32 DAQmxGetCIMin(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3323"""
DAQmxSetCIMin = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIMin
DAQmxSetCIMin.restype = int32
DAQmxSetCIMin.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIMin.__doc__ = \
"""int32 DAQmxSetCIMin(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3324"""
DAQmxResetCIMin = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIMin
DAQmxResetCIMin.restype = int32
DAQmxResetCIMin.argtypes = [TaskHandle, STRING]
DAQmxResetCIMin.__doc__ = \
"""int32 DAQmxResetCIMin(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3325"""
DAQmxGetCICustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICustomScaleName
DAQmxGetCICustomScaleName.restype = int32
DAQmxGetCICustomScaleName.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICustomScaleName.__doc__ = \
"""int32 DAQmxGetCICustomScaleName(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3327"""
DAQmxSetCICustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICustomScaleName
DAQmxSetCICustomScaleName.restype = int32
DAQmxSetCICustomScaleName.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICustomScaleName.__doc__ = \
"""int32 DAQmxSetCICustomScaleName(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3328"""
DAQmxResetCICustomScaleName = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICustomScaleName
DAQmxResetCICustomScaleName.restype = int32
DAQmxResetCICustomScaleName.argtypes = [TaskHandle, STRING]
DAQmxResetCICustomScaleName.__doc__ = \
"""int32 DAQmxResetCICustomScaleName(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3329"""
DAQmxGetCIMeasType = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIMeasType
DAQmxGetCIMeasType.restype = int32
DAQmxGetCIMeasType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIMeasType.__doc__ = \
"""int32 DAQmxGetCIMeasType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3332"""
DAQmxGetCIFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqUnits
DAQmxGetCIFreqUnits.restype = int32
DAQmxGetCIFreqUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIFreqUnits.__doc__ = \
"""int32 DAQmxGetCIFreqUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3335"""
DAQmxSetCIFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqUnits
DAQmxSetCIFreqUnits.restype = int32
DAQmxSetCIFreqUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIFreqUnits.__doc__ = \
"""int32 DAQmxSetCIFreqUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3336"""
DAQmxResetCIFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqUnits
DAQmxResetCIFreqUnits.restype = int32
DAQmxResetCIFreqUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqUnits.__doc__ = \
"""int32 DAQmxResetCIFreqUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3337"""
DAQmxGetCIFreqTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqTerm
DAQmxGetCIFreqTerm.restype = int32
DAQmxGetCIFreqTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIFreqTerm.__doc__ = \
"""int32 DAQmxGetCIFreqTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3339"""
DAQmxSetCIFreqTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqTerm
DAQmxSetCIFreqTerm.restype = int32
DAQmxSetCIFreqTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIFreqTerm.__doc__ = \
"""int32 DAQmxSetCIFreqTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3340"""
DAQmxResetCIFreqTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqTerm
DAQmxResetCIFreqTerm.restype = int32
DAQmxResetCIFreqTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqTerm.__doc__ = \
"""int32 DAQmxResetCIFreqTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3341"""
DAQmxGetCIFreqStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqStartingEdge
DAQmxGetCIFreqStartingEdge.restype = int32
DAQmxGetCIFreqStartingEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIFreqStartingEdge.__doc__ = \
"""int32 DAQmxGetCIFreqStartingEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3344"""
DAQmxSetCIFreqStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqStartingEdge
DAQmxSetCIFreqStartingEdge.restype = int32
DAQmxSetCIFreqStartingEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIFreqStartingEdge.__doc__ = \
"""int32 DAQmxSetCIFreqStartingEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3345"""
DAQmxResetCIFreqStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqStartingEdge
DAQmxResetCIFreqStartingEdge.restype = int32
DAQmxResetCIFreqStartingEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqStartingEdge.__doc__ = \
"""int32 DAQmxResetCIFreqStartingEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3346"""
DAQmxGetCIFreqMeasMeth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqMeasMeth
DAQmxGetCIFreqMeasMeth.restype = int32
DAQmxGetCIFreqMeasMeth.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIFreqMeasMeth.__doc__ = \
"""int32 DAQmxGetCIFreqMeasMeth(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3349"""
DAQmxSetCIFreqMeasMeth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqMeasMeth
DAQmxSetCIFreqMeasMeth.restype = int32
DAQmxSetCIFreqMeasMeth.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIFreqMeasMeth.__doc__ = \
"""int32 DAQmxSetCIFreqMeasMeth(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3350"""
DAQmxResetCIFreqMeasMeth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqMeasMeth
DAQmxResetCIFreqMeasMeth.restype = int32
DAQmxResetCIFreqMeasMeth.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqMeasMeth.__doc__ = \
"""int32 DAQmxResetCIFreqMeasMeth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3351"""
DAQmxGetCIFreqMeasTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqMeasTime
DAQmxGetCIFreqMeasTime.restype = int32
DAQmxGetCIFreqMeasTime.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIFreqMeasTime.__doc__ = \
"""int32 DAQmxGetCIFreqMeasTime(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3353"""
DAQmxSetCIFreqMeasTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqMeasTime
DAQmxSetCIFreqMeasTime.restype = int32
DAQmxSetCIFreqMeasTime.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIFreqMeasTime.__doc__ = \
"""int32 DAQmxSetCIFreqMeasTime(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3354"""
DAQmxResetCIFreqMeasTime = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqMeasTime
DAQmxResetCIFreqMeasTime.restype = int32
DAQmxResetCIFreqMeasTime.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqMeasTime.__doc__ = \
"""int32 DAQmxResetCIFreqMeasTime(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3355"""
DAQmxGetCIFreqDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqDiv
DAQmxGetCIFreqDiv.restype = int32
DAQmxGetCIFreqDiv.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCIFreqDiv.__doc__ = \
"""int32 DAQmxGetCIFreqDiv(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3357"""
DAQmxSetCIFreqDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqDiv
DAQmxSetCIFreqDiv.restype = int32
DAQmxSetCIFreqDiv.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCIFreqDiv.__doc__ = \
"""int32 DAQmxSetCIFreqDiv(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3358"""
DAQmxResetCIFreqDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqDiv
DAQmxResetCIFreqDiv.restype = int32
DAQmxResetCIFreqDiv.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqDiv.__doc__ = \
"""int32 DAQmxResetCIFreqDiv(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3359"""
DAQmxGetCIFreqDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqDigFltrEnable
DAQmxGetCIFreqDigFltrEnable.restype = int32
DAQmxGetCIFreqDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIFreqDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCIFreqDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3361"""
DAQmxSetCIFreqDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqDigFltrEnable
DAQmxSetCIFreqDigFltrEnable.restype = int32
DAQmxSetCIFreqDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIFreqDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCIFreqDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3362"""
DAQmxResetCIFreqDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqDigFltrEnable
DAQmxResetCIFreqDigFltrEnable.restype = int32
DAQmxResetCIFreqDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCIFreqDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3363"""
DAQmxGetCIFreqDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqDigFltrMinPulseWidth
DAQmxGetCIFreqDigFltrMinPulseWidth.restype = int32
DAQmxGetCIFreqDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIFreqDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCIFreqDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3365"""
DAQmxSetCIFreqDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqDigFltrMinPulseWidth
DAQmxSetCIFreqDigFltrMinPulseWidth.restype = int32
DAQmxSetCIFreqDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIFreqDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCIFreqDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3366"""
DAQmxResetCIFreqDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqDigFltrMinPulseWidth
DAQmxResetCIFreqDigFltrMinPulseWidth.restype = int32
DAQmxResetCIFreqDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCIFreqDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3367"""
DAQmxGetCIFreqDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqDigFltrTimebaseSrc
DAQmxGetCIFreqDigFltrTimebaseSrc.restype = int32
DAQmxGetCIFreqDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIFreqDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCIFreqDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3369"""
DAQmxSetCIFreqDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqDigFltrTimebaseSrc
DAQmxSetCIFreqDigFltrTimebaseSrc.restype = int32
DAQmxSetCIFreqDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIFreqDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCIFreqDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3370"""
DAQmxResetCIFreqDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqDigFltrTimebaseSrc
DAQmxResetCIFreqDigFltrTimebaseSrc.restype = int32
DAQmxResetCIFreqDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCIFreqDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3371"""
DAQmxGetCIFreqDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqDigFltrTimebaseRate
DAQmxGetCIFreqDigFltrTimebaseRate.restype = int32
DAQmxGetCIFreqDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIFreqDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCIFreqDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3373"""
DAQmxSetCIFreqDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqDigFltrTimebaseRate
DAQmxSetCIFreqDigFltrTimebaseRate.restype = int32
DAQmxSetCIFreqDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIFreqDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCIFreqDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3374"""
DAQmxResetCIFreqDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqDigFltrTimebaseRate
DAQmxResetCIFreqDigFltrTimebaseRate.restype = int32
DAQmxResetCIFreqDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCIFreqDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3375"""
DAQmxGetCIFreqDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIFreqDigSyncEnable
DAQmxGetCIFreqDigSyncEnable.restype = int32
DAQmxGetCIFreqDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIFreqDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCIFreqDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3377"""
DAQmxSetCIFreqDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIFreqDigSyncEnable
DAQmxSetCIFreqDigSyncEnable.restype = int32
DAQmxSetCIFreqDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIFreqDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCIFreqDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3378"""
DAQmxResetCIFreqDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIFreqDigSyncEnable
DAQmxResetCIFreqDigSyncEnable.restype = int32
DAQmxResetCIFreqDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIFreqDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCIFreqDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3379"""
DAQmxGetCIPeriodUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodUnits
DAQmxGetCIPeriodUnits.restype = int32
DAQmxGetCIPeriodUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIPeriodUnits.__doc__ = \
"""int32 DAQmxGetCIPeriodUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3382"""
DAQmxSetCIPeriodUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodUnits
DAQmxSetCIPeriodUnits.restype = int32
DAQmxSetCIPeriodUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIPeriodUnits.__doc__ = \
"""int32 DAQmxSetCIPeriodUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3383"""
DAQmxResetCIPeriodUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodUnits
DAQmxResetCIPeriodUnits.restype = int32
DAQmxResetCIPeriodUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodUnits.__doc__ = \
"""int32 DAQmxResetCIPeriodUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3384"""
DAQmxGetCIPeriodTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodTerm
DAQmxGetCIPeriodTerm.restype = int32
DAQmxGetCIPeriodTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIPeriodTerm.__doc__ = \
"""int32 DAQmxGetCIPeriodTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3386"""
DAQmxSetCIPeriodTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodTerm
DAQmxSetCIPeriodTerm.restype = int32
DAQmxSetCIPeriodTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIPeriodTerm.__doc__ = \
"""int32 DAQmxSetCIPeriodTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3387"""
DAQmxResetCIPeriodTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodTerm
DAQmxResetCIPeriodTerm.restype = int32
DAQmxResetCIPeriodTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodTerm.__doc__ = \
"""int32 DAQmxResetCIPeriodTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3388"""
DAQmxGetCIPeriodStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodStartingEdge
DAQmxGetCIPeriodStartingEdge.restype = int32
DAQmxGetCIPeriodStartingEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIPeriodStartingEdge.__doc__ = \
"""int32 DAQmxGetCIPeriodStartingEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3391"""
DAQmxSetCIPeriodStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodStartingEdge
DAQmxSetCIPeriodStartingEdge.restype = int32
DAQmxSetCIPeriodStartingEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIPeriodStartingEdge.__doc__ = \
"""int32 DAQmxSetCIPeriodStartingEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3392"""
DAQmxResetCIPeriodStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodStartingEdge
DAQmxResetCIPeriodStartingEdge.restype = int32
DAQmxResetCIPeriodStartingEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodStartingEdge.__doc__ = \
"""int32 DAQmxResetCIPeriodStartingEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3393"""
DAQmxGetCIPeriodMeasMeth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodMeasMeth
DAQmxGetCIPeriodMeasMeth.restype = int32
DAQmxGetCIPeriodMeasMeth.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIPeriodMeasMeth.__doc__ = \
"""int32 DAQmxGetCIPeriodMeasMeth(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3396"""
DAQmxSetCIPeriodMeasMeth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodMeasMeth
DAQmxSetCIPeriodMeasMeth.restype = int32
DAQmxSetCIPeriodMeasMeth.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIPeriodMeasMeth.__doc__ = \
"""int32 DAQmxSetCIPeriodMeasMeth(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3397"""
DAQmxResetCIPeriodMeasMeth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodMeasMeth
DAQmxResetCIPeriodMeasMeth.restype = int32
DAQmxResetCIPeriodMeasMeth.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodMeasMeth.__doc__ = \
"""int32 DAQmxResetCIPeriodMeasMeth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3398"""
DAQmxGetCIPeriodMeasTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodMeasTime
DAQmxGetCIPeriodMeasTime.restype = int32
DAQmxGetCIPeriodMeasTime.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIPeriodMeasTime.__doc__ = \
"""int32 DAQmxGetCIPeriodMeasTime(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3400"""
DAQmxSetCIPeriodMeasTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodMeasTime
DAQmxSetCIPeriodMeasTime.restype = int32
DAQmxSetCIPeriodMeasTime.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIPeriodMeasTime.__doc__ = \
"""int32 DAQmxSetCIPeriodMeasTime(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3401"""
DAQmxResetCIPeriodMeasTime = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodMeasTime
DAQmxResetCIPeriodMeasTime.restype = int32
DAQmxResetCIPeriodMeasTime.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodMeasTime.__doc__ = \
"""int32 DAQmxResetCIPeriodMeasTime(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3402"""
DAQmxGetCIPeriodDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodDiv
DAQmxGetCIPeriodDiv.restype = int32
DAQmxGetCIPeriodDiv.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCIPeriodDiv.__doc__ = \
"""int32 DAQmxGetCIPeriodDiv(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3404"""
DAQmxSetCIPeriodDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodDiv
DAQmxSetCIPeriodDiv.restype = int32
DAQmxSetCIPeriodDiv.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCIPeriodDiv.__doc__ = \
"""int32 DAQmxSetCIPeriodDiv(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3405"""
DAQmxResetCIPeriodDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodDiv
DAQmxResetCIPeriodDiv.restype = int32
DAQmxResetCIPeriodDiv.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodDiv.__doc__ = \
"""int32 DAQmxResetCIPeriodDiv(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3406"""
DAQmxGetCIPeriodDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodDigFltrEnable
DAQmxGetCIPeriodDigFltrEnable.restype = int32
DAQmxGetCIPeriodDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIPeriodDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCIPeriodDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3408"""
DAQmxSetCIPeriodDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodDigFltrEnable
DAQmxSetCIPeriodDigFltrEnable.restype = int32
DAQmxSetCIPeriodDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIPeriodDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCIPeriodDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3409"""
DAQmxResetCIPeriodDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodDigFltrEnable
DAQmxResetCIPeriodDigFltrEnable.restype = int32
DAQmxResetCIPeriodDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCIPeriodDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3410"""
DAQmxGetCIPeriodDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodDigFltrMinPulseWidth
DAQmxGetCIPeriodDigFltrMinPulseWidth.restype = int32
DAQmxGetCIPeriodDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIPeriodDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCIPeriodDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3412"""
DAQmxSetCIPeriodDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodDigFltrMinPulseWidth
DAQmxSetCIPeriodDigFltrMinPulseWidth.restype = int32
DAQmxSetCIPeriodDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIPeriodDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCIPeriodDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3413"""
DAQmxResetCIPeriodDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodDigFltrMinPulseWidth
DAQmxResetCIPeriodDigFltrMinPulseWidth.restype = int32
DAQmxResetCIPeriodDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCIPeriodDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3414"""
DAQmxGetCIPeriodDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodDigFltrTimebaseSrc
DAQmxGetCIPeriodDigFltrTimebaseSrc.restype = int32
DAQmxGetCIPeriodDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIPeriodDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCIPeriodDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3416"""
DAQmxSetCIPeriodDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodDigFltrTimebaseSrc
DAQmxSetCIPeriodDigFltrTimebaseSrc.restype = int32
DAQmxSetCIPeriodDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIPeriodDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCIPeriodDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3417"""
DAQmxResetCIPeriodDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodDigFltrTimebaseSrc
DAQmxResetCIPeriodDigFltrTimebaseSrc.restype = int32
DAQmxResetCIPeriodDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCIPeriodDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3418"""
DAQmxGetCIPeriodDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodDigFltrTimebaseRate
DAQmxGetCIPeriodDigFltrTimebaseRate.restype = int32
DAQmxGetCIPeriodDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIPeriodDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCIPeriodDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3420"""
DAQmxSetCIPeriodDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodDigFltrTimebaseRate
DAQmxSetCIPeriodDigFltrTimebaseRate.restype = int32
DAQmxSetCIPeriodDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIPeriodDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCIPeriodDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3421"""
DAQmxResetCIPeriodDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodDigFltrTimebaseRate
DAQmxResetCIPeriodDigFltrTimebaseRate.restype = int32
DAQmxResetCIPeriodDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCIPeriodDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3422"""
DAQmxGetCIPeriodDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPeriodDigSyncEnable
DAQmxGetCIPeriodDigSyncEnable.restype = int32
DAQmxGetCIPeriodDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIPeriodDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCIPeriodDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3424"""
DAQmxSetCIPeriodDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPeriodDigSyncEnable
DAQmxSetCIPeriodDigSyncEnable.restype = int32
DAQmxSetCIPeriodDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIPeriodDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCIPeriodDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3425"""
DAQmxResetCIPeriodDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPeriodDigSyncEnable
DAQmxResetCIPeriodDigSyncEnable.restype = int32
DAQmxResetCIPeriodDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIPeriodDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCIPeriodDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3426"""
DAQmxGetCICountEdgesTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesTerm
DAQmxGetCICountEdgesTerm.restype = int32
DAQmxGetCICountEdgesTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICountEdgesTerm.__doc__ = \
"""int32 DAQmxGetCICountEdgesTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3428"""
DAQmxSetCICountEdgesTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesTerm
DAQmxSetCICountEdgesTerm.restype = int32
DAQmxSetCICountEdgesTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICountEdgesTerm.__doc__ = \
"""int32 DAQmxSetCICountEdgesTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3429"""
DAQmxResetCICountEdgesTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesTerm
DAQmxResetCICountEdgesTerm.restype = int32
DAQmxResetCICountEdgesTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesTerm.__doc__ = \
"""int32 DAQmxResetCICountEdgesTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3430"""
DAQmxGetCICountEdgesDir = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDir
DAQmxGetCICountEdgesDir.restype = int32
DAQmxGetCICountEdgesDir.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCICountEdgesDir.__doc__ = \
"""int32 DAQmxGetCICountEdgesDir(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3433"""
DAQmxSetCICountEdgesDir = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDir
DAQmxSetCICountEdgesDir.restype = int32
DAQmxSetCICountEdgesDir.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCICountEdgesDir.__doc__ = \
"""int32 DAQmxSetCICountEdgesDir(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3434"""
DAQmxResetCICountEdgesDir = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDir
DAQmxResetCICountEdgesDir.restype = int32
DAQmxResetCICountEdgesDir.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDir.__doc__ = \
"""int32 DAQmxResetCICountEdgesDir(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3435"""
DAQmxGetCICountEdgesDirTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDirTerm
DAQmxGetCICountEdgesDirTerm.restype = int32
DAQmxGetCICountEdgesDirTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICountEdgesDirTerm.__doc__ = \
"""int32 DAQmxGetCICountEdgesDirTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3437"""
DAQmxSetCICountEdgesDirTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDirTerm
DAQmxSetCICountEdgesDirTerm.restype = int32
DAQmxSetCICountEdgesDirTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICountEdgesDirTerm.__doc__ = \
"""int32 DAQmxSetCICountEdgesDirTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3438"""
DAQmxResetCICountEdgesDirTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDirTerm
DAQmxResetCICountEdgesDirTerm.restype = int32
DAQmxResetCICountEdgesDirTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDirTerm.__doc__ = \
"""int32 DAQmxResetCICountEdgesDirTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3439"""
DAQmxGetCICountEdgesCountDirDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesCountDirDigFltrEnable
DAQmxGetCICountEdgesCountDirDigFltrEnable.restype = int32
DAQmxGetCICountEdgesCountDirDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCICountEdgesCountDirDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCICountEdgesCountDirDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3441"""
DAQmxSetCICountEdgesCountDirDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesCountDirDigFltrEnable
DAQmxSetCICountEdgesCountDirDigFltrEnable.restype = int32
DAQmxSetCICountEdgesCountDirDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCICountEdgesCountDirDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCICountEdgesCountDirDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3442"""
DAQmxResetCICountEdgesCountDirDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesCountDirDigFltrEnable
DAQmxResetCICountEdgesCountDirDigFltrEnable.restype = int32
DAQmxResetCICountEdgesCountDirDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesCountDirDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCICountEdgesCountDirDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3443"""
DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth
DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth.restype = int32
DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3445"""
DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth
DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth.restype = int32
DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3446"""
DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth
DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth.restype = int32
DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3447"""
DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc
DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc.restype = int32
DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3449"""
DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc
DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc.restype = int32
DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3450"""
DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc
DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc.restype = int32
DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3451"""
DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate
DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate.restype = int32
DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3453"""
DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate
DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate.restype = int32
DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3454"""
DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate
DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate.restype = int32
DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3455"""
DAQmxGetCICountEdgesCountDirDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesCountDirDigSyncEnable
DAQmxGetCICountEdgesCountDirDigSyncEnable.restype = int32
DAQmxGetCICountEdgesCountDirDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCICountEdgesCountDirDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCICountEdgesCountDirDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3457"""
DAQmxSetCICountEdgesCountDirDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesCountDirDigSyncEnable
DAQmxSetCICountEdgesCountDirDigSyncEnable.restype = int32
DAQmxSetCICountEdgesCountDirDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCICountEdgesCountDirDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCICountEdgesCountDirDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3458"""
DAQmxResetCICountEdgesCountDirDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesCountDirDigSyncEnable
DAQmxResetCICountEdgesCountDirDigSyncEnable.restype = int32
DAQmxResetCICountEdgesCountDirDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesCountDirDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCICountEdgesCountDirDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3459"""
DAQmxGetCICountEdgesInitialCnt = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesInitialCnt
DAQmxGetCICountEdgesInitialCnt.restype = int32
DAQmxGetCICountEdgesInitialCnt.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCICountEdgesInitialCnt.__doc__ = \
"""int32 DAQmxGetCICountEdgesInitialCnt(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3461"""
DAQmxSetCICountEdgesInitialCnt = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesInitialCnt
DAQmxSetCICountEdgesInitialCnt.restype = int32
DAQmxSetCICountEdgesInitialCnt.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCICountEdgesInitialCnt.__doc__ = \
"""int32 DAQmxSetCICountEdgesInitialCnt(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3462"""
DAQmxResetCICountEdgesInitialCnt = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesInitialCnt
DAQmxResetCICountEdgesInitialCnt.restype = int32
DAQmxResetCICountEdgesInitialCnt.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesInitialCnt.__doc__ = \
"""int32 DAQmxResetCICountEdgesInitialCnt(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3463"""
DAQmxGetCICountEdgesActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesActiveEdge
DAQmxGetCICountEdgesActiveEdge.restype = int32
DAQmxGetCICountEdgesActiveEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCICountEdgesActiveEdge.__doc__ = \
"""int32 DAQmxGetCICountEdgesActiveEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3466"""
DAQmxSetCICountEdgesActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesActiveEdge
DAQmxSetCICountEdgesActiveEdge.restype = int32
DAQmxSetCICountEdgesActiveEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCICountEdgesActiveEdge.__doc__ = \
"""int32 DAQmxSetCICountEdgesActiveEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3467"""
DAQmxResetCICountEdgesActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesActiveEdge
DAQmxResetCICountEdgesActiveEdge.restype = int32
DAQmxResetCICountEdgesActiveEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesActiveEdge.__doc__ = \
"""int32 DAQmxResetCICountEdgesActiveEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3468"""
DAQmxGetCICountEdgesDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDigFltrEnable
DAQmxGetCICountEdgesDigFltrEnable.restype = int32
DAQmxGetCICountEdgesDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCICountEdgesDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCICountEdgesDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3470"""
DAQmxSetCICountEdgesDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDigFltrEnable
DAQmxSetCICountEdgesDigFltrEnable.restype = int32
DAQmxSetCICountEdgesDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCICountEdgesDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCICountEdgesDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3471"""
DAQmxResetCICountEdgesDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDigFltrEnable
DAQmxResetCICountEdgesDigFltrEnable.restype = int32
DAQmxResetCICountEdgesDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCICountEdgesDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3472"""
DAQmxGetCICountEdgesDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDigFltrMinPulseWidth
DAQmxGetCICountEdgesDigFltrMinPulseWidth.restype = int32
DAQmxGetCICountEdgesDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICountEdgesDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCICountEdgesDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3474"""
DAQmxSetCICountEdgesDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDigFltrMinPulseWidth
DAQmxSetCICountEdgesDigFltrMinPulseWidth.restype = int32
DAQmxSetCICountEdgesDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICountEdgesDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCICountEdgesDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3475"""
DAQmxResetCICountEdgesDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDigFltrMinPulseWidth
DAQmxResetCICountEdgesDigFltrMinPulseWidth.restype = int32
DAQmxResetCICountEdgesDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCICountEdgesDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3476"""
DAQmxGetCICountEdgesDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDigFltrTimebaseSrc
DAQmxGetCICountEdgesDigFltrTimebaseSrc.restype = int32
DAQmxGetCICountEdgesDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICountEdgesDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCICountEdgesDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3478"""
DAQmxSetCICountEdgesDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDigFltrTimebaseSrc
DAQmxSetCICountEdgesDigFltrTimebaseSrc.restype = int32
DAQmxSetCICountEdgesDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICountEdgesDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCICountEdgesDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3479"""
DAQmxResetCICountEdgesDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDigFltrTimebaseSrc
DAQmxResetCICountEdgesDigFltrTimebaseSrc.restype = int32
DAQmxResetCICountEdgesDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCICountEdgesDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3480"""
DAQmxGetCICountEdgesDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDigFltrTimebaseRate
DAQmxGetCICountEdgesDigFltrTimebaseRate.restype = int32
DAQmxGetCICountEdgesDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICountEdgesDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCICountEdgesDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3482"""
DAQmxSetCICountEdgesDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDigFltrTimebaseRate
DAQmxSetCICountEdgesDigFltrTimebaseRate.restype = int32
DAQmxSetCICountEdgesDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICountEdgesDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCICountEdgesDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3483"""
DAQmxResetCICountEdgesDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDigFltrTimebaseRate
DAQmxResetCICountEdgesDigFltrTimebaseRate.restype = int32
DAQmxResetCICountEdgesDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCICountEdgesDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3484"""
DAQmxGetCICountEdgesDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICountEdgesDigSyncEnable
DAQmxGetCICountEdgesDigSyncEnable.restype = int32
DAQmxGetCICountEdgesDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCICountEdgesDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCICountEdgesDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3486"""
DAQmxSetCICountEdgesDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICountEdgesDigSyncEnable
DAQmxSetCICountEdgesDigSyncEnable.restype = int32
DAQmxSetCICountEdgesDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCICountEdgesDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCICountEdgesDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3487"""
DAQmxResetCICountEdgesDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICountEdgesDigSyncEnable
DAQmxResetCICountEdgesDigSyncEnable.restype = int32
DAQmxResetCICountEdgesDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCICountEdgesDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCICountEdgesDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3488"""
DAQmxGetCIAngEncoderUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIAngEncoderUnits
DAQmxGetCIAngEncoderUnits.restype = int32
DAQmxGetCIAngEncoderUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIAngEncoderUnits.__doc__ = \
"""int32 DAQmxGetCIAngEncoderUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3491"""
DAQmxSetCIAngEncoderUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIAngEncoderUnits
DAQmxSetCIAngEncoderUnits.restype = int32
DAQmxSetCIAngEncoderUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIAngEncoderUnits.__doc__ = \
"""int32 DAQmxSetCIAngEncoderUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3492"""
DAQmxResetCIAngEncoderUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIAngEncoderUnits
DAQmxResetCIAngEncoderUnits.restype = int32
DAQmxResetCIAngEncoderUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCIAngEncoderUnits.__doc__ = \
"""int32 DAQmxResetCIAngEncoderUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3493"""
DAQmxGetCIAngEncoderPulsesPerRev = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIAngEncoderPulsesPerRev
DAQmxGetCIAngEncoderPulsesPerRev.restype = int32
DAQmxGetCIAngEncoderPulsesPerRev.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCIAngEncoderPulsesPerRev.__doc__ = \
"""int32 DAQmxGetCIAngEncoderPulsesPerRev(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3495"""
DAQmxSetCIAngEncoderPulsesPerRev = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIAngEncoderPulsesPerRev
DAQmxSetCIAngEncoderPulsesPerRev.restype = int32
DAQmxSetCIAngEncoderPulsesPerRev.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCIAngEncoderPulsesPerRev.__doc__ = \
"""int32 DAQmxSetCIAngEncoderPulsesPerRev(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3496"""
DAQmxResetCIAngEncoderPulsesPerRev = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIAngEncoderPulsesPerRev
DAQmxResetCIAngEncoderPulsesPerRev.restype = int32
DAQmxResetCIAngEncoderPulsesPerRev.argtypes = [TaskHandle, STRING]
DAQmxResetCIAngEncoderPulsesPerRev.__doc__ = \
"""int32 DAQmxResetCIAngEncoderPulsesPerRev(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3497"""
DAQmxGetCIAngEncoderInitialAngle = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIAngEncoderInitialAngle
DAQmxGetCIAngEncoderInitialAngle.restype = int32
DAQmxGetCIAngEncoderInitialAngle.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIAngEncoderInitialAngle.__doc__ = \
"""int32 DAQmxGetCIAngEncoderInitialAngle(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3499"""
DAQmxSetCIAngEncoderInitialAngle = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIAngEncoderInitialAngle
DAQmxSetCIAngEncoderInitialAngle.restype = int32
DAQmxSetCIAngEncoderInitialAngle.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIAngEncoderInitialAngle.__doc__ = \
"""int32 DAQmxSetCIAngEncoderInitialAngle(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3500"""
DAQmxResetCIAngEncoderInitialAngle = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIAngEncoderInitialAngle
DAQmxResetCIAngEncoderInitialAngle.restype = int32
DAQmxResetCIAngEncoderInitialAngle.argtypes = [TaskHandle, STRING]
DAQmxResetCIAngEncoderInitialAngle.__doc__ = \
"""int32 DAQmxResetCIAngEncoderInitialAngle(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3501"""
DAQmxGetCILinEncoderUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCILinEncoderUnits
DAQmxGetCILinEncoderUnits.restype = int32
DAQmxGetCILinEncoderUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCILinEncoderUnits.__doc__ = \
"""int32 DAQmxGetCILinEncoderUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3504"""
DAQmxSetCILinEncoderUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCILinEncoderUnits
DAQmxSetCILinEncoderUnits.restype = int32
DAQmxSetCILinEncoderUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCILinEncoderUnits.__doc__ = \
"""int32 DAQmxSetCILinEncoderUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3505"""
DAQmxResetCILinEncoderUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCILinEncoderUnits
DAQmxResetCILinEncoderUnits.restype = int32
DAQmxResetCILinEncoderUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCILinEncoderUnits.__doc__ = \
"""int32 DAQmxResetCILinEncoderUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3506"""
DAQmxGetCILinEncoderDistPerPulse = _stdcall_libraries['nicaiu.dll'].DAQmxGetCILinEncoderDistPerPulse
DAQmxGetCILinEncoderDistPerPulse.restype = int32
DAQmxGetCILinEncoderDistPerPulse.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCILinEncoderDistPerPulse.__doc__ = \
"""int32 DAQmxGetCILinEncoderDistPerPulse(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3508"""
DAQmxSetCILinEncoderDistPerPulse = _stdcall_libraries['nicaiu.dll'].DAQmxSetCILinEncoderDistPerPulse
DAQmxSetCILinEncoderDistPerPulse.restype = int32
DAQmxSetCILinEncoderDistPerPulse.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCILinEncoderDistPerPulse.__doc__ = \
"""int32 DAQmxSetCILinEncoderDistPerPulse(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3509"""
DAQmxResetCILinEncoderDistPerPulse = _stdcall_libraries['nicaiu.dll'].DAQmxResetCILinEncoderDistPerPulse
DAQmxResetCILinEncoderDistPerPulse.restype = int32
DAQmxResetCILinEncoderDistPerPulse.argtypes = [TaskHandle, STRING]
DAQmxResetCILinEncoderDistPerPulse.__doc__ = \
"""int32 DAQmxResetCILinEncoderDistPerPulse(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3510"""
DAQmxGetCILinEncoderInitialPos = _stdcall_libraries['nicaiu.dll'].DAQmxGetCILinEncoderInitialPos
DAQmxGetCILinEncoderInitialPos.restype = int32
DAQmxGetCILinEncoderInitialPos.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCILinEncoderInitialPos.__doc__ = \
"""int32 DAQmxGetCILinEncoderInitialPos(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3512"""
DAQmxSetCILinEncoderInitialPos = _stdcall_libraries['nicaiu.dll'].DAQmxSetCILinEncoderInitialPos
DAQmxSetCILinEncoderInitialPos.restype = int32
DAQmxSetCILinEncoderInitialPos.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCILinEncoderInitialPos.__doc__ = \
"""int32 DAQmxSetCILinEncoderInitialPos(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3513"""
DAQmxResetCILinEncoderInitialPos = _stdcall_libraries['nicaiu.dll'].DAQmxResetCILinEncoderInitialPos
DAQmxResetCILinEncoderInitialPos.restype = int32
DAQmxResetCILinEncoderInitialPos.argtypes = [TaskHandle, STRING]
DAQmxResetCILinEncoderInitialPos.__doc__ = \
"""int32 DAQmxResetCILinEncoderInitialPos(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3514"""
DAQmxGetCIEncoderDecodingType = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderDecodingType
DAQmxGetCIEncoderDecodingType.restype = int32
DAQmxGetCIEncoderDecodingType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIEncoderDecodingType.__doc__ = \
"""int32 DAQmxGetCIEncoderDecodingType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3517"""
DAQmxSetCIEncoderDecodingType = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderDecodingType
DAQmxSetCIEncoderDecodingType.restype = int32
DAQmxSetCIEncoderDecodingType.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIEncoderDecodingType.__doc__ = \
"""int32 DAQmxSetCIEncoderDecodingType(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3518"""
DAQmxResetCIEncoderDecodingType = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderDecodingType
DAQmxResetCIEncoderDecodingType.restype = int32
DAQmxResetCIEncoderDecodingType.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderDecodingType.__doc__ = \
"""int32 DAQmxResetCIEncoderDecodingType(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3519"""
DAQmxGetCIEncoderAInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderAInputTerm
DAQmxGetCIEncoderAInputTerm.restype = int32
DAQmxGetCIEncoderAInputTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIEncoderAInputTerm.__doc__ = \
"""int32 DAQmxGetCIEncoderAInputTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3521"""
DAQmxSetCIEncoderAInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderAInputTerm
DAQmxSetCIEncoderAInputTerm.restype = int32
DAQmxSetCIEncoderAInputTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIEncoderAInputTerm.__doc__ = \
"""int32 DAQmxSetCIEncoderAInputTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3522"""
DAQmxResetCIEncoderAInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderAInputTerm
DAQmxResetCIEncoderAInputTerm.restype = int32
DAQmxResetCIEncoderAInputTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderAInputTerm.__doc__ = \
"""int32 DAQmxResetCIEncoderAInputTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3523"""
DAQmxGetCIEncoderAInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderAInputDigFltrEnable
DAQmxGetCIEncoderAInputDigFltrEnable.restype = int32
DAQmxGetCIEncoderAInputDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderAInputDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderAInputDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3525"""
DAQmxSetCIEncoderAInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderAInputDigFltrEnable
DAQmxSetCIEncoderAInputDigFltrEnable.restype = int32
DAQmxSetCIEncoderAInputDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderAInputDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderAInputDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3526"""
DAQmxResetCIEncoderAInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderAInputDigFltrEnable
DAQmxResetCIEncoderAInputDigFltrEnable.restype = int32
DAQmxResetCIEncoderAInputDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderAInputDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderAInputDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3527"""
DAQmxGetCIEncoderAInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderAInputDigFltrMinPulseWidth
DAQmxGetCIEncoderAInputDigFltrMinPulseWidth.restype = int32
DAQmxGetCIEncoderAInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderAInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCIEncoderAInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3529"""
DAQmxSetCIEncoderAInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderAInputDigFltrMinPulseWidth
DAQmxSetCIEncoderAInputDigFltrMinPulseWidth.restype = int32
DAQmxSetCIEncoderAInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderAInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCIEncoderAInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3530"""
DAQmxResetCIEncoderAInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderAInputDigFltrMinPulseWidth
DAQmxResetCIEncoderAInputDigFltrMinPulseWidth.restype = int32
DAQmxResetCIEncoderAInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderAInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCIEncoderAInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3531"""
DAQmxGetCIEncoderAInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderAInputDigFltrTimebaseSrc
DAQmxGetCIEncoderAInputDigFltrTimebaseSrc.restype = int32
DAQmxGetCIEncoderAInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIEncoderAInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCIEncoderAInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3533"""
DAQmxSetCIEncoderAInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderAInputDigFltrTimebaseSrc
DAQmxSetCIEncoderAInputDigFltrTimebaseSrc.restype = int32
DAQmxSetCIEncoderAInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIEncoderAInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCIEncoderAInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3534"""
DAQmxResetCIEncoderAInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderAInputDigFltrTimebaseSrc
DAQmxResetCIEncoderAInputDigFltrTimebaseSrc.restype = int32
DAQmxResetCIEncoderAInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderAInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCIEncoderAInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3535"""
DAQmxGetCIEncoderAInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderAInputDigFltrTimebaseRate
DAQmxGetCIEncoderAInputDigFltrTimebaseRate.restype = int32
DAQmxGetCIEncoderAInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderAInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCIEncoderAInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3537"""
DAQmxSetCIEncoderAInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderAInputDigFltrTimebaseRate
DAQmxSetCIEncoderAInputDigFltrTimebaseRate.restype = int32
DAQmxSetCIEncoderAInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderAInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCIEncoderAInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3538"""
DAQmxResetCIEncoderAInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderAInputDigFltrTimebaseRate
DAQmxResetCIEncoderAInputDigFltrTimebaseRate.restype = int32
DAQmxResetCIEncoderAInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderAInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCIEncoderAInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3539"""
DAQmxGetCIEncoderAInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderAInputDigSyncEnable
DAQmxGetCIEncoderAInputDigSyncEnable.restype = int32
DAQmxGetCIEncoderAInputDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderAInputDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderAInputDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3541"""
DAQmxSetCIEncoderAInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderAInputDigSyncEnable
DAQmxSetCIEncoderAInputDigSyncEnable.restype = int32
DAQmxSetCIEncoderAInputDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderAInputDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderAInputDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3542"""
DAQmxResetCIEncoderAInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderAInputDigSyncEnable
DAQmxResetCIEncoderAInputDigSyncEnable.restype = int32
DAQmxResetCIEncoderAInputDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderAInputDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderAInputDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3543"""
DAQmxGetCIEncoderBInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderBInputTerm
DAQmxGetCIEncoderBInputTerm.restype = int32
DAQmxGetCIEncoderBInputTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIEncoderBInputTerm.__doc__ = \
"""int32 DAQmxGetCIEncoderBInputTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3545"""
DAQmxSetCIEncoderBInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderBInputTerm
DAQmxSetCIEncoderBInputTerm.restype = int32
DAQmxSetCIEncoderBInputTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIEncoderBInputTerm.__doc__ = \
"""int32 DAQmxSetCIEncoderBInputTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3546"""
DAQmxResetCIEncoderBInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderBInputTerm
DAQmxResetCIEncoderBInputTerm.restype = int32
DAQmxResetCIEncoderBInputTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderBInputTerm.__doc__ = \
"""int32 DAQmxResetCIEncoderBInputTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3547"""
DAQmxGetCIEncoderBInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderBInputDigFltrEnable
DAQmxGetCIEncoderBInputDigFltrEnable.restype = int32
DAQmxGetCIEncoderBInputDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderBInputDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderBInputDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3549"""
DAQmxSetCIEncoderBInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderBInputDigFltrEnable
DAQmxSetCIEncoderBInputDigFltrEnable.restype = int32
DAQmxSetCIEncoderBInputDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderBInputDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderBInputDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3550"""
DAQmxResetCIEncoderBInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderBInputDigFltrEnable
DAQmxResetCIEncoderBInputDigFltrEnable.restype = int32
DAQmxResetCIEncoderBInputDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderBInputDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderBInputDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3551"""
DAQmxGetCIEncoderBInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderBInputDigFltrMinPulseWidth
DAQmxGetCIEncoderBInputDigFltrMinPulseWidth.restype = int32
DAQmxGetCIEncoderBInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderBInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCIEncoderBInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3553"""
DAQmxSetCIEncoderBInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderBInputDigFltrMinPulseWidth
DAQmxSetCIEncoderBInputDigFltrMinPulseWidth.restype = int32
DAQmxSetCIEncoderBInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderBInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCIEncoderBInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3554"""
DAQmxResetCIEncoderBInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderBInputDigFltrMinPulseWidth
DAQmxResetCIEncoderBInputDigFltrMinPulseWidth.restype = int32
DAQmxResetCIEncoderBInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderBInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCIEncoderBInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3555"""
DAQmxGetCIEncoderBInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderBInputDigFltrTimebaseSrc
DAQmxGetCIEncoderBInputDigFltrTimebaseSrc.restype = int32
DAQmxGetCIEncoderBInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIEncoderBInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCIEncoderBInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3557"""
DAQmxSetCIEncoderBInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderBInputDigFltrTimebaseSrc
DAQmxSetCIEncoderBInputDigFltrTimebaseSrc.restype = int32
DAQmxSetCIEncoderBInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIEncoderBInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCIEncoderBInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3558"""
DAQmxResetCIEncoderBInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderBInputDigFltrTimebaseSrc
DAQmxResetCIEncoderBInputDigFltrTimebaseSrc.restype = int32
DAQmxResetCIEncoderBInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderBInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCIEncoderBInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3559"""
DAQmxGetCIEncoderBInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderBInputDigFltrTimebaseRate
DAQmxGetCIEncoderBInputDigFltrTimebaseRate.restype = int32
DAQmxGetCIEncoderBInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderBInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCIEncoderBInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3561"""
DAQmxSetCIEncoderBInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderBInputDigFltrTimebaseRate
DAQmxSetCIEncoderBInputDigFltrTimebaseRate.restype = int32
DAQmxSetCIEncoderBInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderBInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCIEncoderBInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3562"""
DAQmxResetCIEncoderBInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderBInputDigFltrTimebaseRate
DAQmxResetCIEncoderBInputDigFltrTimebaseRate.restype = int32
DAQmxResetCIEncoderBInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderBInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCIEncoderBInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3563"""
DAQmxGetCIEncoderBInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderBInputDigSyncEnable
DAQmxGetCIEncoderBInputDigSyncEnable.restype = int32
DAQmxGetCIEncoderBInputDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderBInputDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderBInputDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3565"""
DAQmxSetCIEncoderBInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderBInputDigSyncEnable
DAQmxSetCIEncoderBInputDigSyncEnable.restype = int32
DAQmxSetCIEncoderBInputDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderBInputDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderBInputDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3566"""
DAQmxResetCIEncoderBInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderBInputDigSyncEnable
DAQmxResetCIEncoderBInputDigSyncEnable.restype = int32
DAQmxResetCIEncoderBInputDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderBInputDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderBInputDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3567"""
DAQmxGetCIEncoderZInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZInputTerm
DAQmxGetCIEncoderZInputTerm.restype = int32
DAQmxGetCIEncoderZInputTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIEncoderZInputTerm.__doc__ = \
"""int32 DAQmxGetCIEncoderZInputTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3569"""
DAQmxSetCIEncoderZInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZInputTerm
DAQmxSetCIEncoderZInputTerm.restype = int32
DAQmxSetCIEncoderZInputTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIEncoderZInputTerm.__doc__ = \
"""int32 DAQmxSetCIEncoderZInputTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3570"""
DAQmxResetCIEncoderZInputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZInputTerm
DAQmxResetCIEncoderZInputTerm.restype = int32
DAQmxResetCIEncoderZInputTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZInputTerm.__doc__ = \
"""int32 DAQmxResetCIEncoderZInputTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3571"""
DAQmxGetCIEncoderZInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZInputDigFltrEnable
DAQmxGetCIEncoderZInputDigFltrEnable.restype = int32
DAQmxGetCIEncoderZInputDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderZInputDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderZInputDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3573"""
DAQmxSetCIEncoderZInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZInputDigFltrEnable
DAQmxSetCIEncoderZInputDigFltrEnable.restype = int32
DAQmxSetCIEncoderZInputDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderZInputDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderZInputDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3574"""
DAQmxResetCIEncoderZInputDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZInputDigFltrEnable
DAQmxResetCIEncoderZInputDigFltrEnable.restype = int32
DAQmxResetCIEncoderZInputDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZInputDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderZInputDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3575"""
DAQmxGetCIEncoderZInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZInputDigFltrMinPulseWidth
DAQmxGetCIEncoderZInputDigFltrMinPulseWidth.restype = int32
DAQmxGetCIEncoderZInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderZInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCIEncoderZInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3577"""
DAQmxSetCIEncoderZInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZInputDigFltrMinPulseWidth
DAQmxSetCIEncoderZInputDigFltrMinPulseWidth.restype = int32
DAQmxSetCIEncoderZInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderZInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCIEncoderZInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3578"""
DAQmxResetCIEncoderZInputDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZInputDigFltrMinPulseWidth
DAQmxResetCIEncoderZInputDigFltrMinPulseWidth.restype = int32
DAQmxResetCIEncoderZInputDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZInputDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCIEncoderZInputDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3579"""
DAQmxGetCIEncoderZInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZInputDigFltrTimebaseSrc
DAQmxGetCIEncoderZInputDigFltrTimebaseSrc.restype = int32
DAQmxGetCIEncoderZInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIEncoderZInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCIEncoderZInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3581"""
DAQmxSetCIEncoderZInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZInputDigFltrTimebaseSrc
DAQmxSetCIEncoderZInputDigFltrTimebaseSrc.restype = int32
DAQmxSetCIEncoderZInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIEncoderZInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCIEncoderZInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3582"""
DAQmxResetCIEncoderZInputDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZInputDigFltrTimebaseSrc
DAQmxResetCIEncoderZInputDigFltrTimebaseSrc.restype = int32
DAQmxResetCIEncoderZInputDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZInputDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCIEncoderZInputDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3583"""
DAQmxGetCIEncoderZInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZInputDigFltrTimebaseRate
DAQmxGetCIEncoderZInputDigFltrTimebaseRate.restype = int32
DAQmxGetCIEncoderZInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderZInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCIEncoderZInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3585"""
DAQmxSetCIEncoderZInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZInputDigFltrTimebaseRate
DAQmxSetCIEncoderZInputDigFltrTimebaseRate.restype = int32
DAQmxSetCIEncoderZInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderZInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCIEncoderZInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3586"""
DAQmxResetCIEncoderZInputDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZInputDigFltrTimebaseRate
DAQmxResetCIEncoderZInputDigFltrTimebaseRate.restype = int32
DAQmxResetCIEncoderZInputDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZInputDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCIEncoderZInputDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3587"""
DAQmxGetCIEncoderZInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZInputDigSyncEnable
DAQmxGetCIEncoderZInputDigSyncEnable.restype = int32
DAQmxGetCIEncoderZInputDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderZInputDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderZInputDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3589"""
DAQmxSetCIEncoderZInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZInputDigSyncEnable
DAQmxSetCIEncoderZInputDigSyncEnable.restype = int32
DAQmxSetCIEncoderZInputDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderZInputDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderZInputDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3590"""
DAQmxResetCIEncoderZInputDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZInputDigSyncEnable
DAQmxResetCIEncoderZInputDigSyncEnable.restype = int32
DAQmxResetCIEncoderZInputDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZInputDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderZInputDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3591"""
DAQmxGetCIEncoderZIndexEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZIndexEnable
DAQmxGetCIEncoderZIndexEnable.restype = int32
DAQmxGetCIEncoderZIndexEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIEncoderZIndexEnable.__doc__ = \
"""int32 DAQmxGetCIEncoderZIndexEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3593"""
DAQmxSetCIEncoderZIndexEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZIndexEnable
DAQmxSetCIEncoderZIndexEnable.restype = int32
DAQmxSetCIEncoderZIndexEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIEncoderZIndexEnable.__doc__ = \
"""int32 DAQmxSetCIEncoderZIndexEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3594"""
DAQmxResetCIEncoderZIndexEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZIndexEnable
DAQmxResetCIEncoderZIndexEnable.restype = int32
DAQmxResetCIEncoderZIndexEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZIndexEnable.__doc__ = \
"""int32 DAQmxResetCIEncoderZIndexEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3595"""
DAQmxGetCIEncoderZIndexVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZIndexVal
DAQmxGetCIEncoderZIndexVal.restype = int32
DAQmxGetCIEncoderZIndexVal.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIEncoderZIndexVal.__doc__ = \
"""int32 DAQmxGetCIEncoderZIndexVal(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3597"""
DAQmxSetCIEncoderZIndexVal = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZIndexVal
DAQmxSetCIEncoderZIndexVal.restype = int32
DAQmxSetCIEncoderZIndexVal.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIEncoderZIndexVal.__doc__ = \
"""int32 DAQmxSetCIEncoderZIndexVal(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3598"""
DAQmxResetCIEncoderZIndexVal = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZIndexVal
DAQmxResetCIEncoderZIndexVal.restype = int32
DAQmxResetCIEncoderZIndexVal.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZIndexVal.__doc__ = \
"""int32 DAQmxResetCIEncoderZIndexVal(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3599"""
DAQmxGetCIEncoderZIndexPhase = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIEncoderZIndexPhase
DAQmxGetCIEncoderZIndexPhase.restype = int32
DAQmxGetCIEncoderZIndexPhase.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIEncoderZIndexPhase.__doc__ = \
"""int32 DAQmxGetCIEncoderZIndexPhase(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3602"""
DAQmxSetCIEncoderZIndexPhase = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIEncoderZIndexPhase
DAQmxSetCIEncoderZIndexPhase.restype = int32
DAQmxSetCIEncoderZIndexPhase.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIEncoderZIndexPhase.__doc__ = \
"""int32 DAQmxSetCIEncoderZIndexPhase(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3603"""
DAQmxResetCIEncoderZIndexPhase = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIEncoderZIndexPhase
DAQmxResetCIEncoderZIndexPhase.restype = int32
DAQmxResetCIEncoderZIndexPhase.argtypes = [TaskHandle, STRING]
DAQmxResetCIEncoderZIndexPhase.__doc__ = \
"""int32 DAQmxResetCIEncoderZIndexPhase(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3604"""
DAQmxGetCIPulseWidthUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthUnits
DAQmxGetCIPulseWidthUnits.restype = int32
DAQmxGetCIPulseWidthUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIPulseWidthUnits.__doc__ = \
"""int32 DAQmxGetCIPulseWidthUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3607"""
DAQmxSetCIPulseWidthUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthUnits
DAQmxSetCIPulseWidthUnits.restype = int32
DAQmxSetCIPulseWidthUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIPulseWidthUnits.__doc__ = \
"""int32 DAQmxSetCIPulseWidthUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3608"""
DAQmxResetCIPulseWidthUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthUnits
DAQmxResetCIPulseWidthUnits.restype = int32
DAQmxResetCIPulseWidthUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthUnits.__doc__ = \
"""int32 DAQmxResetCIPulseWidthUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3609"""
DAQmxGetCIPulseWidthTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthTerm
DAQmxGetCIPulseWidthTerm.restype = int32
DAQmxGetCIPulseWidthTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIPulseWidthTerm.__doc__ = \
"""int32 DAQmxGetCIPulseWidthTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3611"""
DAQmxSetCIPulseWidthTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthTerm
DAQmxSetCIPulseWidthTerm.restype = int32
DAQmxSetCIPulseWidthTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIPulseWidthTerm.__doc__ = \
"""int32 DAQmxSetCIPulseWidthTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3612"""
DAQmxResetCIPulseWidthTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthTerm
DAQmxResetCIPulseWidthTerm.restype = int32
DAQmxResetCIPulseWidthTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthTerm.__doc__ = \
"""int32 DAQmxResetCIPulseWidthTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3613"""
DAQmxGetCIPulseWidthStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthStartingEdge
DAQmxGetCIPulseWidthStartingEdge.restype = int32
DAQmxGetCIPulseWidthStartingEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIPulseWidthStartingEdge.__doc__ = \
"""int32 DAQmxGetCIPulseWidthStartingEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3616"""
DAQmxSetCIPulseWidthStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthStartingEdge
DAQmxSetCIPulseWidthStartingEdge.restype = int32
DAQmxSetCIPulseWidthStartingEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIPulseWidthStartingEdge.__doc__ = \
"""int32 DAQmxSetCIPulseWidthStartingEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3617"""
DAQmxResetCIPulseWidthStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthStartingEdge
DAQmxResetCIPulseWidthStartingEdge.restype = int32
DAQmxResetCIPulseWidthStartingEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthStartingEdge.__doc__ = \
"""int32 DAQmxResetCIPulseWidthStartingEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3618"""
DAQmxGetCIPulseWidthDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthDigFltrEnable
DAQmxGetCIPulseWidthDigFltrEnable.restype = int32
DAQmxGetCIPulseWidthDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIPulseWidthDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCIPulseWidthDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3620"""
DAQmxSetCIPulseWidthDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthDigFltrEnable
DAQmxSetCIPulseWidthDigFltrEnable.restype = int32
DAQmxSetCIPulseWidthDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIPulseWidthDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCIPulseWidthDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3621"""
DAQmxResetCIPulseWidthDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthDigFltrEnable
DAQmxResetCIPulseWidthDigFltrEnable.restype = int32
DAQmxResetCIPulseWidthDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCIPulseWidthDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3622"""
DAQmxGetCIPulseWidthDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthDigFltrMinPulseWidth
DAQmxGetCIPulseWidthDigFltrMinPulseWidth.restype = int32
DAQmxGetCIPulseWidthDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIPulseWidthDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCIPulseWidthDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3624"""
DAQmxSetCIPulseWidthDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthDigFltrMinPulseWidth
DAQmxSetCIPulseWidthDigFltrMinPulseWidth.restype = int32
DAQmxSetCIPulseWidthDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIPulseWidthDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCIPulseWidthDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3625"""
DAQmxResetCIPulseWidthDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthDigFltrMinPulseWidth
DAQmxResetCIPulseWidthDigFltrMinPulseWidth.restype = int32
DAQmxResetCIPulseWidthDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCIPulseWidthDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3626"""
DAQmxGetCIPulseWidthDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthDigFltrTimebaseSrc
DAQmxGetCIPulseWidthDigFltrTimebaseSrc.restype = int32
DAQmxGetCIPulseWidthDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIPulseWidthDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCIPulseWidthDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3628"""
DAQmxSetCIPulseWidthDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthDigFltrTimebaseSrc
DAQmxSetCIPulseWidthDigFltrTimebaseSrc.restype = int32
DAQmxSetCIPulseWidthDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIPulseWidthDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCIPulseWidthDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3629"""
DAQmxResetCIPulseWidthDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthDigFltrTimebaseSrc
DAQmxResetCIPulseWidthDigFltrTimebaseSrc.restype = int32
DAQmxResetCIPulseWidthDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCIPulseWidthDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3630"""
DAQmxGetCIPulseWidthDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthDigFltrTimebaseRate
DAQmxGetCIPulseWidthDigFltrTimebaseRate.restype = int32
DAQmxGetCIPulseWidthDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCIPulseWidthDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCIPulseWidthDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3632"""
DAQmxSetCIPulseWidthDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthDigFltrTimebaseRate
DAQmxSetCIPulseWidthDigFltrTimebaseRate.restype = int32
DAQmxSetCIPulseWidthDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCIPulseWidthDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCIPulseWidthDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3633"""
DAQmxResetCIPulseWidthDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthDigFltrTimebaseRate
DAQmxResetCIPulseWidthDigFltrTimebaseRate.restype = int32
DAQmxResetCIPulseWidthDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCIPulseWidthDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3634"""
DAQmxGetCIPulseWidthDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPulseWidthDigSyncEnable
DAQmxGetCIPulseWidthDigSyncEnable.restype = int32
DAQmxGetCIPulseWidthDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIPulseWidthDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCIPulseWidthDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3636"""
DAQmxSetCIPulseWidthDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPulseWidthDigSyncEnable
DAQmxSetCIPulseWidthDigSyncEnable.restype = int32
DAQmxSetCIPulseWidthDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIPulseWidthDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCIPulseWidthDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3637"""
DAQmxResetCIPulseWidthDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPulseWidthDigSyncEnable
DAQmxResetCIPulseWidthDigSyncEnable.restype = int32
DAQmxResetCIPulseWidthDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCIPulseWidthDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCIPulseWidthDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3638"""
DAQmxGetCITwoEdgeSepUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepUnits
DAQmxGetCITwoEdgeSepUnits.restype = int32
DAQmxGetCITwoEdgeSepUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCITwoEdgeSepUnits.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3641"""
DAQmxSetCITwoEdgeSepUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepUnits
DAQmxSetCITwoEdgeSepUnits.restype = int32
DAQmxSetCITwoEdgeSepUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCITwoEdgeSepUnits.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3642"""
DAQmxResetCITwoEdgeSepUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepUnits
DAQmxResetCITwoEdgeSepUnits.restype = int32
DAQmxResetCITwoEdgeSepUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepUnits.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3643"""
DAQmxGetCITwoEdgeSepFirstTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstTerm
DAQmxGetCITwoEdgeSepFirstTerm.restype = int32
DAQmxGetCITwoEdgeSepFirstTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCITwoEdgeSepFirstTerm.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3645"""
DAQmxSetCITwoEdgeSepFirstTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstTerm
DAQmxSetCITwoEdgeSepFirstTerm.restype = int32
DAQmxSetCITwoEdgeSepFirstTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCITwoEdgeSepFirstTerm.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3646"""
DAQmxResetCITwoEdgeSepFirstTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstTerm
DAQmxResetCITwoEdgeSepFirstTerm.restype = int32
DAQmxResetCITwoEdgeSepFirstTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstTerm.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3647"""
DAQmxGetCITwoEdgeSepFirstEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstEdge
DAQmxGetCITwoEdgeSepFirstEdge.restype = int32
DAQmxGetCITwoEdgeSepFirstEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCITwoEdgeSepFirstEdge.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3650"""
DAQmxSetCITwoEdgeSepFirstEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstEdge
DAQmxSetCITwoEdgeSepFirstEdge.restype = int32
DAQmxSetCITwoEdgeSepFirstEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCITwoEdgeSepFirstEdge.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3651"""
DAQmxResetCITwoEdgeSepFirstEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstEdge
DAQmxResetCITwoEdgeSepFirstEdge.restype = int32
DAQmxResetCITwoEdgeSepFirstEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstEdge.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3652"""
DAQmxGetCITwoEdgeSepFirstDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstDigFltrEnable
DAQmxGetCITwoEdgeSepFirstDigFltrEnable.restype = int32
DAQmxGetCITwoEdgeSepFirstDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCITwoEdgeSepFirstDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3654"""
DAQmxSetCITwoEdgeSepFirstDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstDigFltrEnable
DAQmxSetCITwoEdgeSepFirstDigFltrEnable.restype = int32
DAQmxSetCITwoEdgeSepFirstDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCITwoEdgeSepFirstDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3655"""
DAQmxResetCITwoEdgeSepFirstDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstDigFltrEnable
DAQmxResetCITwoEdgeSepFirstDigFltrEnable.restype = int32
DAQmxResetCITwoEdgeSepFirstDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3656"""
DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth
DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth.restype = int32
DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3658"""
DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth
DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth.restype = int32
DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3659"""
DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth
DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth.restype = int32
DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3660"""
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc.restype = int32
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3662"""
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc.restype = int32
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3663"""
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc.restype = int32
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3664"""
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate.restype = int32
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3666"""
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate.restype = int32
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3667"""
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate.restype = int32
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3668"""
DAQmxGetCITwoEdgeSepFirstDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepFirstDigSyncEnable
DAQmxGetCITwoEdgeSepFirstDigSyncEnable.restype = int32
DAQmxGetCITwoEdgeSepFirstDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCITwoEdgeSepFirstDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepFirstDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3670"""
DAQmxSetCITwoEdgeSepFirstDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepFirstDigSyncEnable
DAQmxSetCITwoEdgeSepFirstDigSyncEnable.restype = int32
DAQmxSetCITwoEdgeSepFirstDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCITwoEdgeSepFirstDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepFirstDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3671"""
DAQmxResetCITwoEdgeSepFirstDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepFirstDigSyncEnable
DAQmxResetCITwoEdgeSepFirstDigSyncEnable.restype = int32
DAQmxResetCITwoEdgeSepFirstDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepFirstDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepFirstDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3672"""
DAQmxGetCITwoEdgeSepSecondTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondTerm
DAQmxGetCITwoEdgeSepSecondTerm.restype = int32
DAQmxGetCITwoEdgeSepSecondTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCITwoEdgeSepSecondTerm.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3674"""
DAQmxSetCITwoEdgeSepSecondTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondTerm
DAQmxSetCITwoEdgeSepSecondTerm.restype = int32
DAQmxSetCITwoEdgeSepSecondTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCITwoEdgeSepSecondTerm.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3675"""
DAQmxResetCITwoEdgeSepSecondTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondTerm
DAQmxResetCITwoEdgeSepSecondTerm.restype = int32
DAQmxResetCITwoEdgeSepSecondTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondTerm.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3676"""
DAQmxGetCITwoEdgeSepSecondEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondEdge
DAQmxGetCITwoEdgeSepSecondEdge.restype = int32
DAQmxGetCITwoEdgeSepSecondEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCITwoEdgeSepSecondEdge.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3679"""
DAQmxSetCITwoEdgeSepSecondEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondEdge
DAQmxSetCITwoEdgeSepSecondEdge.restype = int32
DAQmxSetCITwoEdgeSepSecondEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCITwoEdgeSepSecondEdge.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3680"""
DAQmxResetCITwoEdgeSepSecondEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondEdge
DAQmxResetCITwoEdgeSepSecondEdge.restype = int32
DAQmxResetCITwoEdgeSepSecondEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondEdge.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3681"""
DAQmxGetCITwoEdgeSepSecondDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondDigFltrEnable
DAQmxGetCITwoEdgeSepSecondDigFltrEnable.restype = int32
DAQmxGetCITwoEdgeSepSecondDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCITwoEdgeSepSecondDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3683"""
DAQmxSetCITwoEdgeSepSecondDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondDigFltrEnable
DAQmxSetCITwoEdgeSepSecondDigFltrEnable.restype = int32
DAQmxSetCITwoEdgeSepSecondDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCITwoEdgeSepSecondDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3684"""
DAQmxResetCITwoEdgeSepSecondDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondDigFltrEnable
DAQmxResetCITwoEdgeSepSecondDigFltrEnable.restype = int32
DAQmxResetCITwoEdgeSepSecondDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3685"""
DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth
DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth.restype = int32
DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3687"""
DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth
DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth.restype = int32
DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3688"""
DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth
DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth.restype = int32
DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3689"""
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc.restype = int32
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3691"""
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc.restype = int32
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3692"""
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc.restype = int32
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3693"""
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate.restype = int32
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3695"""
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate.restype = int32
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3696"""
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate.restype = int32
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3697"""
DAQmxGetCITwoEdgeSepSecondDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITwoEdgeSepSecondDigSyncEnable
DAQmxGetCITwoEdgeSepSecondDigSyncEnable.restype = int32
DAQmxGetCITwoEdgeSepSecondDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCITwoEdgeSepSecondDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCITwoEdgeSepSecondDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3699"""
DAQmxSetCITwoEdgeSepSecondDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITwoEdgeSepSecondDigSyncEnable
DAQmxSetCITwoEdgeSepSecondDigSyncEnable.restype = int32
DAQmxSetCITwoEdgeSepSecondDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCITwoEdgeSepSecondDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCITwoEdgeSepSecondDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3700"""
DAQmxResetCITwoEdgeSepSecondDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITwoEdgeSepSecondDigSyncEnable
DAQmxResetCITwoEdgeSepSecondDigSyncEnable.restype = int32
DAQmxResetCITwoEdgeSepSecondDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCITwoEdgeSepSecondDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCITwoEdgeSepSecondDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3701"""
DAQmxGetCISemiPeriodUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodUnits
DAQmxGetCISemiPeriodUnits.restype = int32
DAQmxGetCISemiPeriodUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCISemiPeriodUnits.__doc__ = \
"""int32 DAQmxGetCISemiPeriodUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3704"""
DAQmxSetCISemiPeriodUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodUnits
DAQmxSetCISemiPeriodUnits.restype = int32
DAQmxSetCISemiPeriodUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCISemiPeriodUnits.__doc__ = \
"""int32 DAQmxSetCISemiPeriodUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3705"""
DAQmxResetCISemiPeriodUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodUnits
DAQmxResetCISemiPeriodUnits.restype = int32
DAQmxResetCISemiPeriodUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodUnits.__doc__ = \
"""int32 DAQmxResetCISemiPeriodUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3706"""
DAQmxGetCISemiPeriodTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodTerm
DAQmxGetCISemiPeriodTerm.restype = int32
DAQmxGetCISemiPeriodTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCISemiPeriodTerm.__doc__ = \
"""int32 DAQmxGetCISemiPeriodTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3708"""
DAQmxSetCISemiPeriodTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodTerm
DAQmxSetCISemiPeriodTerm.restype = int32
DAQmxSetCISemiPeriodTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCISemiPeriodTerm.__doc__ = \
"""int32 DAQmxSetCISemiPeriodTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3709"""
DAQmxResetCISemiPeriodTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodTerm
DAQmxResetCISemiPeriodTerm.restype = int32
DAQmxResetCISemiPeriodTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodTerm.__doc__ = \
"""int32 DAQmxResetCISemiPeriodTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3710"""
DAQmxGetCISemiPeriodStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodStartingEdge
DAQmxGetCISemiPeriodStartingEdge.restype = int32
DAQmxGetCISemiPeriodStartingEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCISemiPeriodStartingEdge.__doc__ = \
"""int32 DAQmxGetCISemiPeriodStartingEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3713"""
DAQmxSetCISemiPeriodStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodStartingEdge
DAQmxSetCISemiPeriodStartingEdge.restype = int32
DAQmxSetCISemiPeriodStartingEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCISemiPeriodStartingEdge.__doc__ = \
"""int32 DAQmxSetCISemiPeriodStartingEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3714"""
DAQmxResetCISemiPeriodStartingEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodStartingEdge
DAQmxResetCISemiPeriodStartingEdge.restype = int32
DAQmxResetCISemiPeriodStartingEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodStartingEdge.__doc__ = \
"""int32 DAQmxResetCISemiPeriodStartingEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3715"""
DAQmxGetCISemiPeriodDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodDigFltrEnable
DAQmxGetCISemiPeriodDigFltrEnable.restype = int32
DAQmxGetCISemiPeriodDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCISemiPeriodDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCISemiPeriodDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3717"""
DAQmxSetCISemiPeriodDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodDigFltrEnable
DAQmxSetCISemiPeriodDigFltrEnable.restype = int32
DAQmxSetCISemiPeriodDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCISemiPeriodDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCISemiPeriodDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3718"""
DAQmxResetCISemiPeriodDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodDigFltrEnable
DAQmxResetCISemiPeriodDigFltrEnable.restype = int32
DAQmxResetCISemiPeriodDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCISemiPeriodDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3719"""
DAQmxGetCISemiPeriodDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodDigFltrMinPulseWidth
DAQmxGetCISemiPeriodDigFltrMinPulseWidth.restype = int32
DAQmxGetCISemiPeriodDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCISemiPeriodDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCISemiPeriodDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3721"""
DAQmxSetCISemiPeriodDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodDigFltrMinPulseWidth
DAQmxSetCISemiPeriodDigFltrMinPulseWidth.restype = int32
DAQmxSetCISemiPeriodDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCISemiPeriodDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCISemiPeriodDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3722"""
DAQmxResetCISemiPeriodDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodDigFltrMinPulseWidth
DAQmxResetCISemiPeriodDigFltrMinPulseWidth.restype = int32
DAQmxResetCISemiPeriodDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCISemiPeriodDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3723"""
DAQmxGetCISemiPeriodDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodDigFltrTimebaseSrc
DAQmxGetCISemiPeriodDigFltrTimebaseSrc.restype = int32
DAQmxGetCISemiPeriodDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCISemiPeriodDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCISemiPeriodDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3725"""
DAQmxSetCISemiPeriodDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodDigFltrTimebaseSrc
DAQmxSetCISemiPeriodDigFltrTimebaseSrc.restype = int32
DAQmxSetCISemiPeriodDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCISemiPeriodDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCISemiPeriodDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3726"""
DAQmxResetCISemiPeriodDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodDigFltrTimebaseSrc
DAQmxResetCISemiPeriodDigFltrTimebaseSrc.restype = int32
DAQmxResetCISemiPeriodDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCISemiPeriodDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3727"""
DAQmxGetCISemiPeriodDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodDigFltrTimebaseRate
DAQmxGetCISemiPeriodDigFltrTimebaseRate.restype = int32
DAQmxGetCISemiPeriodDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCISemiPeriodDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCISemiPeriodDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3729"""
DAQmxSetCISemiPeriodDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodDigFltrTimebaseRate
DAQmxSetCISemiPeriodDigFltrTimebaseRate.restype = int32
DAQmxSetCISemiPeriodDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCISemiPeriodDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCISemiPeriodDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3730"""
DAQmxResetCISemiPeriodDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodDigFltrTimebaseRate
DAQmxResetCISemiPeriodDigFltrTimebaseRate.restype = int32
DAQmxResetCISemiPeriodDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCISemiPeriodDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3731"""
DAQmxGetCISemiPeriodDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCISemiPeriodDigSyncEnable
DAQmxGetCISemiPeriodDigSyncEnable.restype = int32
DAQmxGetCISemiPeriodDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCISemiPeriodDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCISemiPeriodDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3733"""
DAQmxSetCISemiPeriodDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCISemiPeriodDigSyncEnable
DAQmxSetCISemiPeriodDigSyncEnable.restype = int32
DAQmxSetCISemiPeriodDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCISemiPeriodDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCISemiPeriodDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3734"""
DAQmxResetCISemiPeriodDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCISemiPeriodDigSyncEnable
DAQmxResetCISemiPeriodDigSyncEnable.restype = int32
DAQmxResetCISemiPeriodDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCISemiPeriodDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCISemiPeriodDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3735"""
DAQmxGetCITimestampUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITimestampUnits
DAQmxGetCITimestampUnits.restype = int32
DAQmxGetCITimestampUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCITimestampUnits.__doc__ = \
"""int32 DAQmxGetCITimestampUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3738"""
DAQmxSetCITimestampUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITimestampUnits
DAQmxSetCITimestampUnits.restype = int32
DAQmxSetCITimestampUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCITimestampUnits.__doc__ = \
"""int32 DAQmxSetCITimestampUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3739"""
DAQmxResetCITimestampUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITimestampUnits
DAQmxResetCITimestampUnits.restype = int32
DAQmxResetCITimestampUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCITimestampUnits.__doc__ = \
"""int32 DAQmxResetCITimestampUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3740"""
DAQmxGetCITimestampInitialSeconds = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITimestampInitialSeconds
DAQmxGetCITimestampInitialSeconds.restype = int32
DAQmxGetCITimestampInitialSeconds.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCITimestampInitialSeconds.__doc__ = \
"""int32 DAQmxGetCITimestampInitialSeconds(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3742"""
DAQmxSetCITimestampInitialSeconds = _stdcall_libraries['nicaiu.dll'].DAQmxSetCITimestampInitialSeconds
DAQmxSetCITimestampInitialSeconds.restype = int32
DAQmxSetCITimestampInitialSeconds.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCITimestampInitialSeconds.__doc__ = \
"""int32 DAQmxSetCITimestampInitialSeconds(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3743"""
DAQmxResetCITimestampInitialSeconds = _stdcall_libraries['nicaiu.dll'].DAQmxResetCITimestampInitialSeconds
DAQmxResetCITimestampInitialSeconds.restype = int32
DAQmxResetCITimestampInitialSeconds.argtypes = [TaskHandle, STRING]
DAQmxResetCITimestampInitialSeconds.__doc__ = \
"""int32 DAQmxResetCITimestampInitialSeconds(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3744"""
DAQmxGetCIGPSSyncMethod = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIGPSSyncMethod
DAQmxGetCIGPSSyncMethod.restype = int32
DAQmxGetCIGPSSyncMethod.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIGPSSyncMethod.__doc__ = \
"""int32 DAQmxGetCIGPSSyncMethod(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3747"""
DAQmxSetCIGPSSyncMethod = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIGPSSyncMethod
DAQmxSetCIGPSSyncMethod.restype = int32
DAQmxSetCIGPSSyncMethod.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIGPSSyncMethod.__doc__ = \
"""int32 DAQmxSetCIGPSSyncMethod(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3748"""
DAQmxResetCIGPSSyncMethod = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIGPSSyncMethod
DAQmxResetCIGPSSyncMethod.restype = int32
DAQmxResetCIGPSSyncMethod.argtypes = [TaskHandle, STRING]
DAQmxResetCIGPSSyncMethod.__doc__ = \
"""int32 DAQmxResetCIGPSSyncMethod(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3749"""
DAQmxGetCIGPSSyncSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIGPSSyncSrc
DAQmxGetCIGPSSyncSrc.restype = int32
DAQmxGetCIGPSSyncSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCIGPSSyncSrc.__doc__ = \
"""int32 DAQmxGetCIGPSSyncSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3751"""
DAQmxSetCIGPSSyncSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIGPSSyncSrc
DAQmxSetCIGPSSyncSrc.restype = int32
DAQmxSetCIGPSSyncSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCIGPSSyncSrc.__doc__ = \
"""int32 DAQmxSetCIGPSSyncSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3752"""
DAQmxResetCIGPSSyncSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIGPSSyncSrc
DAQmxResetCIGPSSyncSrc.restype = int32
DAQmxResetCIGPSSyncSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCIGPSSyncSrc.__doc__ = \
"""int32 DAQmxResetCIGPSSyncSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3753"""
DAQmxGetCICtrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseSrc
DAQmxGetCICtrTimebaseSrc.restype = int32
DAQmxGetCICtrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICtrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3755"""
DAQmxSetCICtrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseSrc
DAQmxSetCICtrTimebaseSrc.restype = int32
DAQmxSetCICtrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICtrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3756"""
DAQmxResetCICtrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseSrc
DAQmxResetCICtrTimebaseSrc.restype = int32
DAQmxResetCICtrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3757"""
DAQmxGetCICtrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseRate
DAQmxGetCICtrTimebaseRate.restype = int32
DAQmxGetCICtrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICtrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3759"""
DAQmxSetCICtrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseRate
DAQmxSetCICtrTimebaseRate.restype = int32
DAQmxSetCICtrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICtrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3760"""
DAQmxResetCICtrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseRate
DAQmxResetCICtrTimebaseRate.restype = int32
DAQmxResetCICtrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3761"""
DAQmxGetCICtrTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseActiveEdge
DAQmxGetCICtrTimebaseActiveEdge.restype = int32
DAQmxGetCICtrTimebaseActiveEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCICtrTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseActiveEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3764"""
DAQmxSetCICtrTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseActiveEdge
DAQmxSetCICtrTimebaseActiveEdge.restype = int32
DAQmxSetCICtrTimebaseActiveEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCICtrTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseActiveEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3765"""
DAQmxResetCICtrTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseActiveEdge
DAQmxResetCICtrTimebaseActiveEdge.restype = int32
DAQmxResetCICtrTimebaseActiveEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseActiveEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3766"""
DAQmxGetCICtrTimebaseDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseDigFltrEnable
DAQmxGetCICtrTimebaseDigFltrEnable.restype = int32
DAQmxGetCICtrTimebaseDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCICtrTimebaseDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3768"""
DAQmxSetCICtrTimebaseDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseDigFltrEnable
DAQmxSetCICtrTimebaseDigFltrEnable.restype = int32
DAQmxSetCICtrTimebaseDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCICtrTimebaseDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3769"""
DAQmxResetCICtrTimebaseDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseDigFltrEnable
DAQmxResetCICtrTimebaseDigFltrEnable.restype = int32
DAQmxResetCICtrTimebaseDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3770"""
DAQmxGetCICtrTimebaseDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseDigFltrMinPulseWidth
DAQmxGetCICtrTimebaseDigFltrMinPulseWidth.restype = int32
DAQmxGetCICtrTimebaseDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICtrTimebaseDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3772"""
DAQmxSetCICtrTimebaseDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseDigFltrMinPulseWidth
DAQmxSetCICtrTimebaseDigFltrMinPulseWidth.restype = int32
DAQmxSetCICtrTimebaseDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICtrTimebaseDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3773"""
DAQmxResetCICtrTimebaseDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseDigFltrMinPulseWidth
DAQmxResetCICtrTimebaseDigFltrMinPulseWidth.restype = int32
DAQmxResetCICtrTimebaseDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3774"""
DAQmxGetCICtrTimebaseDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseDigFltrTimebaseSrc
DAQmxGetCICtrTimebaseDigFltrTimebaseSrc.restype = int32
DAQmxGetCICtrTimebaseDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCICtrTimebaseDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3776"""
DAQmxSetCICtrTimebaseDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseDigFltrTimebaseSrc
DAQmxSetCICtrTimebaseDigFltrTimebaseSrc.restype = int32
DAQmxSetCICtrTimebaseDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCICtrTimebaseDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3777"""
DAQmxResetCICtrTimebaseDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseDigFltrTimebaseSrc
DAQmxResetCICtrTimebaseDigFltrTimebaseSrc.restype = int32
DAQmxResetCICtrTimebaseDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3778"""
DAQmxGetCICtrTimebaseDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseDigFltrTimebaseRate
DAQmxGetCICtrTimebaseDigFltrTimebaseRate.restype = int32
DAQmxGetCICtrTimebaseDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCICtrTimebaseDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3780"""
DAQmxSetCICtrTimebaseDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseDigFltrTimebaseRate
DAQmxSetCICtrTimebaseDigFltrTimebaseRate.restype = int32
DAQmxSetCICtrTimebaseDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCICtrTimebaseDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3781"""
DAQmxResetCICtrTimebaseDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseDigFltrTimebaseRate
DAQmxResetCICtrTimebaseDigFltrTimebaseRate.restype = int32
DAQmxResetCICtrTimebaseDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3782"""
DAQmxGetCICtrTimebaseDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseDigSyncEnable
DAQmxGetCICtrTimebaseDigSyncEnable.restype = int32
DAQmxGetCICtrTimebaseDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCICtrTimebaseDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3784"""
DAQmxSetCICtrTimebaseDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseDigSyncEnable
DAQmxSetCICtrTimebaseDigSyncEnable.restype = int32
DAQmxSetCICtrTimebaseDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCICtrTimebaseDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3785"""
DAQmxResetCICtrTimebaseDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseDigSyncEnable
DAQmxResetCICtrTimebaseDigSyncEnable.restype = int32
DAQmxResetCICtrTimebaseDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3786"""
DAQmxGetCICount = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICount
DAQmxGetCICount.restype = int32
DAQmxGetCICount.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCICount.__doc__ = \
"""int32 DAQmxGetCICount(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3788"""
DAQmxGetCIOutputState = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIOutputState
DAQmxGetCIOutputState.restype = int32
DAQmxGetCIOutputState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIOutputState.__doc__ = \
"""int32 DAQmxGetCIOutputState(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3791"""
DAQmxGetCITCReached = _stdcall_libraries['nicaiu.dll'].DAQmxGetCITCReached
DAQmxGetCITCReached.restype = int32
DAQmxGetCITCReached.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCITCReached.__doc__ = \
"""int32 DAQmxGetCITCReached(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3793"""
DAQmxGetCICtrTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetCICtrTimebaseMasterTimebaseDiv
DAQmxGetCICtrTimebaseMasterTimebaseDiv.restype = int32
DAQmxGetCICtrTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCICtrTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxGetCICtrTimebaseMasterTimebaseDiv(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3795"""
DAQmxSetCICtrTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetCICtrTimebaseMasterTimebaseDiv
DAQmxSetCICtrTimebaseMasterTimebaseDiv.restype = int32
DAQmxSetCICtrTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCICtrTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxSetCICtrTimebaseMasterTimebaseDiv(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3796"""
DAQmxResetCICtrTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetCICtrTimebaseMasterTimebaseDiv
DAQmxResetCICtrTimebaseMasterTimebaseDiv.restype = int32
DAQmxResetCICtrTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, STRING]
DAQmxResetCICtrTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxResetCICtrTimebaseMasterTimebaseDiv(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3797"""
DAQmxGetCIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIDataXferMech
DAQmxGetCIDataXferMech.restype = int32
DAQmxGetCIDataXferMech.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCIDataXferMech.__doc__ = \
"""int32 DAQmxGetCIDataXferMech(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3800"""
DAQmxSetCIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIDataXferMech
DAQmxSetCIDataXferMech.restype = int32
DAQmxSetCIDataXferMech.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCIDataXferMech.__doc__ = \
"""int32 DAQmxSetCIDataXferMech(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3801"""
DAQmxResetCIDataXferMech = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIDataXferMech
DAQmxResetCIDataXferMech.restype = int32
DAQmxResetCIDataXferMech.argtypes = [TaskHandle, STRING]
DAQmxResetCIDataXferMech.__doc__ = \
"""int32 DAQmxResetCIDataXferMech(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3802"""
DAQmxGetCIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIUsbXferReqSize
DAQmxGetCIUsbXferReqSize.restype = int32
DAQmxGetCIUsbXferReqSize.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCIUsbXferReqSize.__doc__ = \
"""int32 DAQmxGetCIUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3804"""
DAQmxSetCIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIUsbXferReqSize
DAQmxSetCIUsbXferReqSize.restype = int32
DAQmxSetCIUsbXferReqSize.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCIUsbXferReqSize.__doc__ = \
"""int32 DAQmxSetCIUsbXferReqSize(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3805"""
DAQmxResetCIUsbXferReqSize = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIUsbXferReqSize
DAQmxResetCIUsbXferReqSize.restype = int32
DAQmxResetCIUsbXferReqSize.argtypes = [TaskHandle, STRING]
DAQmxResetCIUsbXferReqSize.__doc__ = \
"""int32 DAQmxResetCIUsbXferReqSize(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3806"""
DAQmxGetCINumPossiblyInvalidSamps = _stdcall_libraries['nicaiu.dll'].DAQmxGetCINumPossiblyInvalidSamps
DAQmxGetCINumPossiblyInvalidSamps.restype = int32
DAQmxGetCINumPossiblyInvalidSamps.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCINumPossiblyInvalidSamps.__doc__ = \
"""int32 DAQmxGetCINumPossiblyInvalidSamps(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3808"""
DAQmxGetCIDupCountPrevent = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIDupCountPrevent
DAQmxGetCIDupCountPrevent.restype = int32
DAQmxGetCIDupCountPrevent.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCIDupCountPrevent.__doc__ = \
"""int32 DAQmxGetCIDupCountPrevent(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3810"""
DAQmxSetCIDupCountPrevent = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIDupCountPrevent
DAQmxSetCIDupCountPrevent.restype = int32
DAQmxSetCIDupCountPrevent.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCIDupCountPrevent.__doc__ = \
"""int32 DAQmxSetCIDupCountPrevent(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3811"""
DAQmxResetCIDupCountPrevent = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIDupCountPrevent
DAQmxResetCIDupCountPrevent.restype = int32
DAQmxResetCIDupCountPrevent.argtypes = [TaskHandle, STRING]
DAQmxResetCIDupCountPrevent.__doc__ = \
"""int32 DAQmxResetCIDupCountPrevent(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3812"""
DAQmxGetCIPrescaler = _stdcall_libraries['nicaiu.dll'].DAQmxGetCIPrescaler
DAQmxGetCIPrescaler.restype = int32
DAQmxGetCIPrescaler.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCIPrescaler.__doc__ = \
"""int32 DAQmxGetCIPrescaler(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3814"""
DAQmxSetCIPrescaler = _stdcall_libraries['nicaiu.dll'].DAQmxSetCIPrescaler
DAQmxSetCIPrescaler.restype = int32
DAQmxSetCIPrescaler.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCIPrescaler.__doc__ = \
"""int32 DAQmxSetCIPrescaler(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3815"""
DAQmxResetCIPrescaler = _stdcall_libraries['nicaiu.dll'].DAQmxResetCIPrescaler
DAQmxResetCIPrescaler.restype = int32
DAQmxResetCIPrescaler.argtypes = [TaskHandle, STRING]
DAQmxResetCIPrescaler.__doc__ = \
"""int32 DAQmxResetCIPrescaler(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3816"""
DAQmxGetCOOutputType = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOOutputType
DAQmxGetCOOutputType.restype = int32
DAQmxGetCOOutputType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOOutputType.__doc__ = \
"""int32 DAQmxGetCOOutputType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3819"""
DAQmxGetCOPulseIdleState = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseIdleState
DAQmxGetCOPulseIdleState.restype = int32
DAQmxGetCOPulseIdleState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOPulseIdleState.__doc__ = \
"""int32 DAQmxGetCOPulseIdleState(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3822"""
DAQmxSetCOPulseIdleState = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseIdleState
DAQmxSetCOPulseIdleState.restype = int32
DAQmxSetCOPulseIdleState.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCOPulseIdleState.__doc__ = \
"""int32 DAQmxSetCOPulseIdleState(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3823"""
DAQmxResetCOPulseIdleState = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseIdleState
DAQmxResetCOPulseIdleState.restype = int32
DAQmxResetCOPulseIdleState.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseIdleState.__doc__ = \
"""int32 DAQmxResetCOPulseIdleState(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3824"""
DAQmxGetCOPulseTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseTerm
DAQmxGetCOPulseTerm.restype = int32
DAQmxGetCOPulseTerm.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCOPulseTerm.__doc__ = \
"""int32 DAQmxGetCOPulseTerm(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3826"""
DAQmxSetCOPulseTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseTerm
DAQmxSetCOPulseTerm.restype = int32
DAQmxSetCOPulseTerm.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCOPulseTerm.__doc__ = \
"""int32 DAQmxSetCOPulseTerm(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3827"""
DAQmxResetCOPulseTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseTerm
DAQmxResetCOPulseTerm.restype = int32
DAQmxResetCOPulseTerm.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseTerm.__doc__ = \
"""int32 DAQmxResetCOPulseTerm(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3828"""
DAQmxGetCOPulseTimeUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseTimeUnits
DAQmxGetCOPulseTimeUnits.restype = int32
DAQmxGetCOPulseTimeUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOPulseTimeUnits.__doc__ = \
"""int32 DAQmxGetCOPulseTimeUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3831"""
DAQmxSetCOPulseTimeUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseTimeUnits
DAQmxSetCOPulseTimeUnits.restype = int32
DAQmxSetCOPulseTimeUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCOPulseTimeUnits.__doc__ = \
"""int32 DAQmxSetCOPulseTimeUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3832"""
DAQmxResetCOPulseTimeUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseTimeUnits
DAQmxResetCOPulseTimeUnits.restype = int32
DAQmxResetCOPulseTimeUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseTimeUnits.__doc__ = \
"""int32 DAQmxResetCOPulseTimeUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3833"""
DAQmxGetCOPulseHighTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseHighTime
DAQmxGetCOPulseHighTime.restype = int32
DAQmxGetCOPulseHighTime.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOPulseHighTime.__doc__ = \
"""int32 DAQmxGetCOPulseHighTime(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3835"""
DAQmxSetCOPulseHighTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseHighTime
DAQmxSetCOPulseHighTime.restype = int32
DAQmxSetCOPulseHighTime.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOPulseHighTime.__doc__ = \
"""int32 DAQmxSetCOPulseHighTime(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3836"""
DAQmxResetCOPulseHighTime = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseHighTime
DAQmxResetCOPulseHighTime.restype = int32
DAQmxResetCOPulseHighTime.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseHighTime.__doc__ = \
"""int32 DAQmxResetCOPulseHighTime(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3837"""
DAQmxGetCOPulseLowTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseLowTime
DAQmxGetCOPulseLowTime.restype = int32
DAQmxGetCOPulseLowTime.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOPulseLowTime.__doc__ = \
"""int32 DAQmxGetCOPulseLowTime(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3839"""
DAQmxSetCOPulseLowTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseLowTime
DAQmxSetCOPulseLowTime.restype = int32
DAQmxSetCOPulseLowTime.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOPulseLowTime.__doc__ = \
"""int32 DAQmxSetCOPulseLowTime(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3840"""
DAQmxResetCOPulseLowTime = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseLowTime
DAQmxResetCOPulseLowTime.restype = int32
DAQmxResetCOPulseLowTime.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseLowTime.__doc__ = \
"""int32 DAQmxResetCOPulseLowTime(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3841"""
DAQmxGetCOPulseTimeInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseTimeInitialDelay
DAQmxGetCOPulseTimeInitialDelay.restype = int32
DAQmxGetCOPulseTimeInitialDelay.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOPulseTimeInitialDelay.__doc__ = \
"""int32 DAQmxGetCOPulseTimeInitialDelay(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3843"""
DAQmxSetCOPulseTimeInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseTimeInitialDelay
DAQmxSetCOPulseTimeInitialDelay.restype = int32
DAQmxSetCOPulseTimeInitialDelay.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOPulseTimeInitialDelay.__doc__ = \
"""int32 DAQmxSetCOPulseTimeInitialDelay(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3844"""
DAQmxResetCOPulseTimeInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseTimeInitialDelay
DAQmxResetCOPulseTimeInitialDelay.restype = int32
DAQmxResetCOPulseTimeInitialDelay.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseTimeInitialDelay.__doc__ = \
"""int32 DAQmxResetCOPulseTimeInitialDelay(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3845"""
DAQmxGetCOPulseDutyCyc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseDutyCyc
DAQmxGetCOPulseDutyCyc.restype = int32
DAQmxGetCOPulseDutyCyc.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOPulseDutyCyc.__doc__ = \
"""int32 DAQmxGetCOPulseDutyCyc(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3847"""
DAQmxSetCOPulseDutyCyc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseDutyCyc
DAQmxSetCOPulseDutyCyc.restype = int32
DAQmxSetCOPulseDutyCyc.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOPulseDutyCyc.__doc__ = \
"""int32 DAQmxSetCOPulseDutyCyc(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3848"""
DAQmxResetCOPulseDutyCyc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseDutyCyc
DAQmxResetCOPulseDutyCyc.restype = int32
DAQmxResetCOPulseDutyCyc.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseDutyCyc.__doc__ = \
"""int32 DAQmxResetCOPulseDutyCyc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3849"""
DAQmxGetCOPulseFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseFreqUnits
DAQmxGetCOPulseFreqUnits.restype = int32
DAQmxGetCOPulseFreqUnits.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOPulseFreqUnits.__doc__ = \
"""int32 DAQmxGetCOPulseFreqUnits(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3852"""
DAQmxSetCOPulseFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseFreqUnits
DAQmxSetCOPulseFreqUnits.restype = int32
DAQmxSetCOPulseFreqUnits.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCOPulseFreqUnits.__doc__ = \
"""int32 DAQmxSetCOPulseFreqUnits(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3853"""
DAQmxResetCOPulseFreqUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseFreqUnits
DAQmxResetCOPulseFreqUnits.restype = int32
DAQmxResetCOPulseFreqUnits.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseFreqUnits.__doc__ = \
"""int32 DAQmxResetCOPulseFreqUnits(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3854"""
DAQmxGetCOPulseFreq = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseFreq
DAQmxGetCOPulseFreq.restype = int32
DAQmxGetCOPulseFreq.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOPulseFreq.__doc__ = \
"""int32 DAQmxGetCOPulseFreq(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3856"""
DAQmxSetCOPulseFreq = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseFreq
DAQmxSetCOPulseFreq.restype = int32
DAQmxSetCOPulseFreq.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOPulseFreq.__doc__ = \
"""int32 DAQmxSetCOPulseFreq(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3857"""
DAQmxResetCOPulseFreq = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseFreq
DAQmxResetCOPulseFreq.restype = int32
DAQmxResetCOPulseFreq.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseFreq.__doc__ = \
"""int32 DAQmxResetCOPulseFreq(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3858"""
DAQmxGetCOPulseFreqInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseFreqInitialDelay
DAQmxGetCOPulseFreqInitialDelay.restype = int32
DAQmxGetCOPulseFreqInitialDelay.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOPulseFreqInitialDelay.__doc__ = \
"""int32 DAQmxGetCOPulseFreqInitialDelay(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3860"""
DAQmxSetCOPulseFreqInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseFreqInitialDelay
DAQmxSetCOPulseFreqInitialDelay.restype = int32
DAQmxSetCOPulseFreqInitialDelay.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOPulseFreqInitialDelay.__doc__ = \
"""int32 DAQmxSetCOPulseFreqInitialDelay(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3861"""
DAQmxResetCOPulseFreqInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseFreqInitialDelay
DAQmxResetCOPulseFreqInitialDelay.restype = int32
DAQmxResetCOPulseFreqInitialDelay.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseFreqInitialDelay.__doc__ = \
"""int32 DAQmxResetCOPulseFreqInitialDelay(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3862"""
DAQmxGetCOPulseHighTicks = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseHighTicks
DAQmxGetCOPulseHighTicks.restype = int32
DAQmxGetCOPulseHighTicks.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOPulseHighTicks.__doc__ = \
"""int32 DAQmxGetCOPulseHighTicks(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3864"""
DAQmxSetCOPulseHighTicks = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseHighTicks
DAQmxSetCOPulseHighTicks.restype = int32
DAQmxSetCOPulseHighTicks.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCOPulseHighTicks.__doc__ = \
"""int32 DAQmxSetCOPulseHighTicks(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3865"""
DAQmxResetCOPulseHighTicks = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseHighTicks
DAQmxResetCOPulseHighTicks.restype = int32
DAQmxResetCOPulseHighTicks.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseHighTicks.__doc__ = \
"""int32 DAQmxResetCOPulseHighTicks(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3866"""
DAQmxGetCOPulseLowTicks = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseLowTicks
DAQmxGetCOPulseLowTicks.restype = int32
DAQmxGetCOPulseLowTicks.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOPulseLowTicks.__doc__ = \
"""int32 DAQmxGetCOPulseLowTicks(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3868"""
DAQmxSetCOPulseLowTicks = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseLowTicks
DAQmxSetCOPulseLowTicks.restype = int32
DAQmxSetCOPulseLowTicks.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCOPulseLowTicks.__doc__ = \
"""int32 DAQmxSetCOPulseLowTicks(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3869"""
DAQmxResetCOPulseLowTicks = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseLowTicks
DAQmxResetCOPulseLowTicks.restype = int32
DAQmxResetCOPulseLowTicks.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseLowTicks.__doc__ = \
"""int32 DAQmxResetCOPulseLowTicks(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3870"""
DAQmxGetCOPulseTicksInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseTicksInitialDelay
DAQmxGetCOPulseTicksInitialDelay.restype = int32
DAQmxGetCOPulseTicksInitialDelay.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOPulseTicksInitialDelay.__doc__ = \
"""int32 DAQmxGetCOPulseTicksInitialDelay(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3872"""
DAQmxSetCOPulseTicksInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPulseTicksInitialDelay
DAQmxSetCOPulseTicksInitialDelay.restype = int32
DAQmxSetCOPulseTicksInitialDelay.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCOPulseTicksInitialDelay.__doc__ = \
"""int32 DAQmxSetCOPulseTicksInitialDelay(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3873"""
DAQmxResetCOPulseTicksInitialDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPulseTicksInitialDelay
DAQmxResetCOPulseTicksInitialDelay.restype = int32
DAQmxResetCOPulseTicksInitialDelay.argtypes = [TaskHandle, STRING]
DAQmxResetCOPulseTicksInitialDelay.__doc__ = \
"""int32 DAQmxResetCOPulseTicksInitialDelay(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3874"""
DAQmxGetCOCtrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseSrc
DAQmxGetCOCtrTimebaseSrc.restype = int32
DAQmxGetCOCtrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCOCtrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3876"""
DAQmxSetCOCtrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseSrc
DAQmxSetCOCtrTimebaseSrc.restype = int32
DAQmxSetCOCtrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCOCtrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3877"""
DAQmxResetCOCtrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseSrc
DAQmxResetCOCtrTimebaseSrc.restype = int32
DAQmxResetCOCtrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3878"""
DAQmxGetCOCtrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseRate
DAQmxGetCOCtrTimebaseRate.restype = int32
DAQmxGetCOCtrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOCtrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3880"""
DAQmxSetCOCtrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseRate
DAQmxSetCOCtrTimebaseRate.restype = int32
DAQmxSetCOCtrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOCtrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3881"""
DAQmxResetCOCtrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseRate
DAQmxResetCOCtrTimebaseRate.restype = int32
DAQmxResetCOCtrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3882"""
DAQmxGetCOCtrTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseActiveEdge
DAQmxGetCOCtrTimebaseActiveEdge.restype = int32
DAQmxGetCOCtrTimebaseActiveEdge.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOCtrTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseActiveEdge(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3885"""
DAQmxSetCOCtrTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseActiveEdge
DAQmxSetCOCtrTimebaseActiveEdge.restype = int32
DAQmxSetCOCtrTimebaseActiveEdge.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCOCtrTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseActiveEdge(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3886"""
DAQmxResetCOCtrTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseActiveEdge
DAQmxResetCOCtrTimebaseActiveEdge.restype = int32
DAQmxResetCOCtrTimebaseActiveEdge.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseActiveEdge(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3887"""
DAQmxGetCOCtrTimebaseDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseDigFltrEnable
DAQmxGetCOCtrTimebaseDigFltrEnable.restype = int32
DAQmxGetCOCtrTimebaseDigFltrEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCOCtrTimebaseDigFltrEnable.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3889"""
DAQmxSetCOCtrTimebaseDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseDigFltrEnable
DAQmxSetCOCtrTimebaseDigFltrEnable.restype = int32
DAQmxSetCOCtrTimebaseDigFltrEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCOCtrTimebaseDigFltrEnable.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseDigFltrEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3890"""
DAQmxResetCOCtrTimebaseDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseDigFltrEnable
DAQmxResetCOCtrTimebaseDigFltrEnable.restype = int32
DAQmxResetCOCtrTimebaseDigFltrEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseDigFltrEnable.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseDigFltrEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3891"""
DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth
DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth.restype = int32
DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3893"""
DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth
DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth.restype = int32
DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3894"""
DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth
DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth.restype = int32
DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseDigFltrMinPulseWidth(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3895"""
DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc
DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc.restype = int32
DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3897"""
DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc
DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc.restype = int32
DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3898"""
DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc
DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc.restype = int32
DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3899"""
DAQmxGetCOCtrTimebaseDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseDigFltrTimebaseRate
DAQmxGetCOCtrTimebaseDigFltrTimebaseRate.restype = int32
DAQmxGetCOCtrTimebaseDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetCOCtrTimebaseDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3901"""
DAQmxSetCOCtrTimebaseDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseDigFltrTimebaseRate
DAQmxSetCOCtrTimebaseDigFltrTimebaseRate.restype = int32
DAQmxSetCOCtrTimebaseDigFltrTimebaseRate.argtypes = [TaskHandle, STRING, float64]
DAQmxSetCOCtrTimebaseDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3902"""
DAQmxResetCOCtrTimebaseDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseDigFltrTimebaseRate
DAQmxResetCOCtrTimebaseDigFltrTimebaseRate.restype = int32
DAQmxResetCOCtrTimebaseDigFltrTimebaseRate.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3903"""
DAQmxGetCOCtrTimebaseDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseDigSyncEnable
DAQmxGetCOCtrTimebaseDigSyncEnable.restype = int32
DAQmxGetCOCtrTimebaseDigSyncEnable.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCOCtrTimebaseDigSyncEnable.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3905"""
DAQmxSetCOCtrTimebaseDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseDigSyncEnable
DAQmxSetCOCtrTimebaseDigSyncEnable.restype = int32
DAQmxSetCOCtrTimebaseDigSyncEnable.argtypes = [TaskHandle, STRING, bool32]
DAQmxSetCOCtrTimebaseDigSyncEnable.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseDigSyncEnable(TaskHandle taskHandle, unknown * channel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3906"""
DAQmxResetCOCtrTimebaseDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseDigSyncEnable
DAQmxResetCOCtrTimebaseDigSyncEnable.restype = int32
DAQmxResetCOCtrTimebaseDigSyncEnable.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseDigSyncEnable.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseDigSyncEnable(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3907"""
DAQmxGetCOCount = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCount
DAQmxGetCOCount.restype = int32
DAQmxGetCOCount.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOCount.__doc__ = \
"""int32 DAQmxGetCOCount(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3909"""
DAQmxGetCOOutputState = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOOutputState
DAQmxGetCOOutputState.restype = int32
DAQmxGetCOOutputState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOOutputState.__doc__ = \
"""int32 DAQmxGetCOOutputState(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3912"""
DAQmxGetCOAutoIncrCnt = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOAutoIncrCnt
DAQmxGetCOAutoIncrCnt.restype = int32
DAQmxGetCOAutoIncrCnt.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOAutoIncrCnt.__doc__ = \
"""int32 DAQmxGetCOAutoIncrCnt(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3914"""
DAQmxSetCOAutoIncrCnt = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOAutoIncrCnt
DAQmxSetCOAutoIncrCnt.restype = int32
DAQmxSetCOAutoIncrCnt.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCOAutoIncrCnt.__doc__ = \
"""int32 DAQmxSetCOAutoIncrCnt(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3915"""
DAQmxResetCOAutoIncrCnt = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOAutoIncrCnt
DAQmxResetCOAutoIncrCnt.restype = int32
DAQmxResetCOAutoIncrCnt.argtypes = [TaskHandle, STRING]
DAQmxResetCOAutoIncrCnt.__doc__ = \
"""int32 DAQmxResetCOAutoIncrCnt(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3916"""
DAQmxGetCOCtrTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOCtrTimebaseMasterTimebaseDiv
DAQmxGetCOCtrTimebaseMasterTimebaseDiv.restype = int32
DAQmxGetCOCtrTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOCtrTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxGetCOCtrTimebaseMasterTimebaseDiv(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3918"""
DAQmxSetCOCtrTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOCtrTimebaseMasterTimebaseDiv
DAQmxSetCOCtrTimebaseMasterTimebaseDiv.restype = int32
DAQmxSetCOCtrTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCOCtrTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxSetCOCtrTimebaseMasterTimebaseDiv(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3919"""
DAQmxResetCOCtrTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOCtrTimebaseMasterTimebaseDiv
DAQmxResetCOCtrTimebaseMasterTimebaseDiv.restype = int32
DAQmxResetCOCtrTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, STRING]
DAQmxResetCOCtrTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxResetCOCtrTimebaseMasterTimebaseDiv(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3920"""
DAQmxGetCOPulseDone = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPulseDone
DAQmxGetCOPulseDone.restype = int32
DAQmxGetCOPulseDone.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCOPulseDone.__doc__ = \
"""int32 DAQmxGetCOPulseDone(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3922"""
DAQmxGetCOConstrainedGenMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOConstrainedGenMode
DAQmxGetCOConstrainedGenMode.restype = int32
DAQmxGetCOConstrainedGenMode.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetCOConstrainedGenMode.__doc__ = \
"""int32 DAQmxGetCOConstrainedGenMode(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3925"""
DAQmxSetCOConstrainedGenMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOConstrainedGenMode
DAQmxSetCOConstrainedGenMode.restype = int32
DAQmxSetCOConstrainedGenMode.argtypes = [TaskHandle, STRING, int32]
DAQmxSetCOConstrainedGenMode.__doc__ = \
"""int32 DAQmxSetCOConstrainedGenMode(TaskHandle taskHandle, unknown * channel, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3926"""
DAQmxResetCOConstrainedGenMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOConstrainedGenMode
DAQmxResetCOConstrainedGenMode.restype = int32
DAQmxResetCOConstrainedGenMode.argtypes = [TaskHandle, STRING]
DAQmxResetCOConstrainedGenMode.__doc__ = \
"""int32 DAQmxResetCOConstrainedGenMode(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3927"""
DAQmxGetCOPrescaler = _stdcall_libraries['nicaiu.dll'].DAQmxGetCOPrescaler
DAQmxGetCOPrescaler.restype = int32
DAQmxGetCOPrescaler.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetCOPrescaler.__doc__ = \
"""int32 DAQmxGetCOPrescaler(TaskHandle taskHandle, unknown * channel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3929"""
DAQmxSetCOPrescaler = _stdcall_libraries['nicaiu.dll'].DAQmxSetCOPrescaler
DAQmxSetCOPrescaler.restype = int32
DAQmxSetCOPrescaler.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetCOPrescaler.__doc__ = \
"""int32 DAQmxSetCOPrescaler(TaskHandle taskHandle, unknown * channel, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3930"""
DAQmxResetCOPrescaler = _stdcall_libraries['nicaiu.dll'].DAQmxResetCOPrescaler
DAQmxResetCOPrescaler.restype = int32
DAQmxResetCOPrescaler.argtypes = [TaskHandle, STRING]
DAQmxResetCOPrescaler.__doc__ = \
"""int32 DAQmxResetCOPrescaler(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3931"""
DAQmxGetCORdyForNewVal = _stdcall_libraries['nicaiu.dll'].DAQmxGetCORdyForNewVal
DAQmxGetCORdyForNewVal.restype = int32
DAQmxGetCORdyForNewVal.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetCORdyForNewVal.__doc__ = \
"""int32 DAQmxGetCORdyForNewVal(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3933"""
DAQmxGetChanType = _stdcall_libraries['nicaiu.dll'].DAQmxGetChanType
DAQmxGetChanType.restype = int32
DAQmxGetChanType.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetChanType.__doc__ = \
"""int32 DAQmxGetChanType(TaskHandle taskHandle, unknown * channel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3936"""
DAQmxGetPhysicalChanName = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanName
DAQmxGetPhysicalChanName.restype = int32
DAQmxGetPhysicalChanName.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetPhysicalChanName.__doc__ = \
"""int32 DAQmxGetPhysicalChanName(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3938"""
DAQmxSetPhysicalChanName = _stdcall_libraries['nicaiu.dll'].DAQmxSetPhysicalChanName
DAQmxSetPhysicalChanName.restype = int32
DAQmxSetPhysicalChanName.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetPhysicalChanName.__doc__ = \
"""int32 DAQmxSetPhysicalChanName(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3939"""
DAQmxGetChanDescr = _stdcall_libraries['nicaiu.dll'].DAQmxGetChanDescr
DAQmxGetChanDescr.restype = int32
DAQmxGetChanDescr.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetChanDescr.__doc__ = \
"""int32 DAQmxGetChanDescr(TaskHandle taskHandle, unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3941"""
DAQmxSetChanDescr = _stdcall_libraries['nicaiu.dll'].DAQmxSetChanDescr
DAQmxSetChanDescr.restype = int32
DAQmxSetChanDescr.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetChanDescr.__doc__ = \
"""int32 DAQmxSetChanDescr(TaskHandle taskHandle, unknown * channel, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3942"""
DAQmxResetChanDescr = _stdcall_libraries['nicaiu.dll'].DAQmxResetChanDescr
DAQmxResetChanDescr.restype = int32
DAQmxResetChanDescr.argtypes = [TaskHandle, STRING]
DAQmxResetChanDescr.__doc__ = \
"""int32 DAQmxResetChanDescr(TaskHandle taskHandle, unknown * channel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3943"""
DAQmxGetChanIsGlobal = _stdcall_libraries['nicaiu.dll'].DAQmxGetChanIsGlobal
DAQmxGetChanIsGlobal.restype = int32
DAQmxGetChanIsGlobal.argtypes = [TaskHandle, STRING, POINTER(bool32)]
DAQmxGetChanIsGlobal.__doc__ = \
"""int32 DAQmxGetChanIsGlobal(TaskHandle taskHandle, unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3945"""
DAQmxGetExportedAIConvClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAIConvClkOutputTerm
DAQmxGetExportedAIConvClkOutputTerm.restype = int32
DAQmxGetExportedAIConvClkOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedAIConvClkOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedAIConvClkOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3949"""
DAQmxSetExportedAIConvClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAIConvClkOutputTerm
DAQmxSetExportedAIConvClkOutputTerm.restype = int32
DAQmxSetExportedAIConvClkOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedAIConvClkOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedAIConvClkOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3950"""
DAQmxResetExportedAIConvClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAIConvClkOutputTerm
DAQmxResetExportedAIConvClkOutputTerm.restype = int32
DAQmxResetExportedAIConvClkOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedAIConvClkOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedAIConvClkOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3951"""
DAQmxGetExportedAIConvClkPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAIConvClkPulsePolarity
DAQmxGetExportedAIConvClkPulsePolarity.restype = int32
DAQmxGetExportedAIConvClkPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedAIConvClkPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedAIConvClkPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3954"""
DAQmxGetExported10MHzRefClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExported10MHzRefClkOutputTerm
DAQmxGetExported10MHzRefClkOutputTerm.restype = int32
DAQmxGetExported10MHzRefClkOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExported10MHzRefClkOutputTerm.__doc__ = \
"""int32 DAQmxGetExported10MHzRefClkOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3956"""
DAQmxSetExported10MHzRefClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExported10MHzRefClkOutputTerm
DAQmxSetExported10MHzRefClkOutputTerm.restype = int32
DAQmxSetExported10MHzRefClkOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExported10MHzRefClkOutputTerm.__doc__ = \
"""int32 DAQmxSetExported10MHzRefClkOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3957"""
DAQmxResetExported10MHzRefClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExported10MHzRefClkOutputTerm
DAQmxResetExported10MHzRefClkOutputTerm.restype = int32
DAQmxResetExported10MHzRefClkOutputTerm.argtypes = [TaskHandle]
DAQmxResetExported10MHzRefClkOutputTerm.__doc__ = \
"""int32 DAQmxResetExported10MHzRefClkOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3958"""
DAQmxGetExported20MHzTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExported20MHzTimebaseOutputTerm
DAQmxGetExported20MHzTimebaseOutputTerm.restype = int32
DAQmxGetExported20MHzTimebaseOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExported20MHzTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxGetExported20MHzTimebaseOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3960"""
DAQmxSetExported20MHzTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExported20MHzTimebaseOutputTerm
DAQmxSetExported20MHzTimebaseOutputTerm.restype = int32
DAQmxSetExported20MHzTimebaseOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExported20MHzTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxSetExported20MHzTimebaseOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3961"""
DAQmxResetExported20MHzTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExported20MHzTimebaseOutputTerm
DAQmxResetExported20MHzTimebaseOutputTerm.restype = int32
DAQmxResetExported20MHzTimebaseOutputTerm.argtypes = [TaskHandle]
DAQmxResetExported20MHzTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxResetExported20MHzTimebaseOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3962"""
DAQmxGetExportedSampClkOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedSampClkOutputBehavior
DAQmxGetExportedSampClkOutputBehavior.restype = int32
DAQmxGetExportedSampClkOutputBehavior.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedSampClkOutputBehavior.__doc__ = \
"""int32 DAQmxGetExportedSampClkOutputBehavior(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3965"""
DAQmxSetExportedSampClkOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedSampClkOutputBehavior
DAQmxSetExportedSampClkOutputBehavior.restype = int32
DAQmxSetExportedSampClkOutputBehavior.argtypes = [TaskHandle, int32]
DAQmxSetExportedSampClkOutputBehavior.__doc__ = \
"""int32 DAQmxSetExportedSampClkOutputBehavior(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3966"""
DAQmxResetExportedSampClkOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSampClkOutputBehavior
DAQmxResetExportedSampClkOutputBehavior.restype = int32
DAQmxResetExportedSampClkOutputBehavior.argtypes = [TaskHandle]
DAQmxResetExportedSampClkOutputBehavior.__doc__ = \
"""int32 DAQmxResetExportedSampClkOutputBehavior(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3967"""
DAQmxGetExportedSampClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedSampClkOutputTerm
DAQmxGetExportedSampClkOutputTerm.restype = int32
DAQmxGetExportedSampClkOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedSampClkOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedSampClkOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3969"""
DAQmxSetExportedSampClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedSampClkOutputTerm
DAQmxSetExportedSampClkOutputTerm.restype = int32
DAQmxSetExportedSampClkOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedSampClkOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedSampClkOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3970"""
DAQmxResetExportedSampClkOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSampClkOutputTerm
DAQmxResetExportedSampClkOutputTerm.restype = int32
DAQmxResetExportedSampClkOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedSampClkOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedSampClkOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3971"""
DAQmxGetExportedSampClkDelayOffset = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedSampClkDelayOffset
DAQmxGetExportedSampClkDelayOffset.restype = int32
DAQmxGetExportedSampClkDelayOffset.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedSampClkDelayOffset.__doc__ = \
"""int32 DAQmxGetExportedSampClkDelayOffset(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3973"""
DAQmxSetExportedSampClkDelayOffset = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedSampClkDelayOffset
DAQmxSetExportedSampClkDelayOffset.restype = int32
DAQmxSetExportedSampClkDelayOffset.argtypes = [TaskHandle, float64]
DAQmxSetExportedSampClkDelayOffset.__doc__ = \
"""int32 DAQmxSetExportedSampClkDelayOffset(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3974"""
DAQmxResetExportedSampClkDelayOffset = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSampClkDelayOffset
DAQmxResetExportedSampClkDelayOffset.restype = int32
DAQmxResetExportedSampClkDelayOffset.argtypes = [TaskHandle]
DAQmxResetExportedSampClkDelayOffset.__doc__ = \
"""int32 DAQmxResetExportedSampClkDelayOffset(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3975"""
DAQmxGetExportedSampClkPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedSampClkPulsePolarity
DAQmxGetExportedSampClkPulsePolarity.restype = int32
DAQmxGetExportedSampClkPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedSampClkPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedSampClkPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3978"""
DAQmxSetExportedSampClkPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedSampClkPulsePolarity
DAQmxSetExportedSampClkPulsePolarity.restype = int32
DAQmxSetExportedSampClkPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedSampClkPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedSampClkPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3979"""
DAQmxResetExportedSampClkPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSampClkPulsePolarity
DAQmxResetExportedSampClkPulsePolarity.restype = int32
DAQmxResetExportedSampClkPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedSampClkPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedSampClkPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3980"""
DAQmxGetExportedSampClkTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedSampClkTimebaseOutputTerm
DAQmxGetExportedSampClkTimebaseOutputTerm.restype = int32
DAQmxGetExportedSampClkTimebaseOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedSampClkTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedSampClkTimebaseOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3982"""
DAQmxSetExportedSampClkTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedSampClkTimebaseOutputTerm
DAQmxSetExportedSampClkTimebaseOutputTerm.restype = int32
DAQmxSetExportedSampClkTimebaseOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedSampClkTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedSampClkTimebaseOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3983"""
DAQmxResetExportedSampClkTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSampClkTimebaseOutputTerm
DAQmxResetExportedSampClkTimebaseOutputTerm.restype = int32
DAQmxResetExportedSampClkTimebaseOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedSampClkTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedSampClkTimebaseOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3984"""
DAQmxGetExportedDividedSampClkTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedDividedSampClkTimebaseOutputTerm
DAQmxGetExportedDividedSampClkTimebaseOutputTerm.restype = int32
DAQmxGetExportedDividedSampClkTimebaseOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedDividedSampClkTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedDividedSampClkTimebaseOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3986"""
DAQmxSetExportedDividedSampClkTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedDividedSampClkTimebaseOutputTerm
DAQmxSetExportedDividedSampClkTimebaseOutputTerm.restype = int32
DAQmxSetExportedDividedSampClkTimebaseOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedDividedSampClkTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedDividedSampClkTimebaseOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3987"""
DAQmxResetExportedDividedSampClkTimebaseOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedDividedSampClkTimebaseOutputTerm
DAQmxResetExportedDividedSampClkTimebaseOutputTerm.restype = int32
DAQmxResetExportedDividedSampClkTimebaseOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedDividedSampClkTimebaseOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedDividedSampClkTimebaseOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3988"""
DAQmxGetExportedAdvTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvTrigOutputTerm
DAQmxGetExportedAdvTrigOutputTerm.restype = int32
DAQmxGetExportedAdvTrigOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedAdvTrigOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedAdvTrigOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3990"""
DAQmxSetExportedAdvTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvTrigOutputTerm
DAQmxSetExportedAdvTrigOutputTerm.restype = int32
DAQmxSetExportedAdvTrigOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedAdvTrigOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedAdvTrigOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3991"""
DAQmxResetExportedAdvTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvTrigOutputTerm
DAQmxResetExportedAdvTrigOutputTerm.restype = int32
DAQmxResetExportedAdvTrigOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedAdvTrigOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedAdvTrigOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3992"""
DAQmxGetExportedAdvTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvTrigPulsePolarity
DAQmxGetExportedAdvTrigPulsePolarity.restype = int32
DAQmxGetExportedAdvTrigPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedAdvTrigPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedAdvTrigPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3995"""
DAQmxGetExportedAdvTrigPulseWidthUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvTrigPulseWidthUnits
DAQmxGetExportedAdvTrigPulseWidthUnits.restype = int32
DAQmxGetExportedAdvTrigPulseWidthUnits.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedAdvTrigPulseWidthUnits.__doc__ = \
"""int32 DAQmxGetExportedAdvTrigPulseWidthUnits(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3998"""
DAQmxSetExportedAdvTrigPulseWidthUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvTrigPulseWidthUnits
DAQmxSetExportedAdvTrigPulseWidthUnits.restype = int32
DAQmxSetExportedAdvTrigPulseWidthUnits.argtypes = [TaskHandle, int32]
DAQmxSetExportedAdvTrigPulseWidthUnits.__doc__ = \
"""int32 DAQmxSetExportedAdvTrigPulseWidthUnits(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:3999"""
DAQmxResetExportedAdvTrigPulseWidthUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvTrigPulseWidthUnits
DAQmxResetExportedAdvTrigPulseWidthUnits.restype = int32
DAQmxResetExportedAdvTrigPulseWidthUnits.argtypes = [TaskHandle]
DAQmxResetExportedAdvTrigPulseWidthUnits.__doc__ = \
"""int32 DAQmxResetExportedAdvTrigPulseWidthUnits(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4000"""
DAQmxGetExportedAdvTrigPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvTrigPulseWidth
DAQmxGetExportedAdvTrigPulseWidth.restype = int32
DAQmxGetExportedAdvTrigPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedAdvTrigPulseWidth.__doc__ = \
"""int32 DAQmxGetExportedAdvTrigPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4002"""
DAQmxSetExportedAdvTrigPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvTrigPulseWidth
DAQmxSetExportedAdvTrigPulseWidth.restype = int32
DAQmxSetExportedAdvTrigPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetExportedAdvTrigPulseWidth.__doc__ = \
"""int32 DAQmxSetExportedAdvTrigPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4003"""
DAQmxResetExportedAdvTrigPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvTrigPulseWidth
DAQmxResetExportedAdvTrigPulseWidth.restype = int32
DAQmxResetExportedAdvTrigPulseWidth.argtypes = [TaskHandle]
DAQmxResetExportedAdvTrigPulseWidth.__doc__ = \
"""int32 DAQmxResetExportedAdvTrigPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4004"""
DAQmxGetExportedPauseTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedPauseTrigOutputTerm
DAQmxGetExportedPauseTrigOutputTerm.restype = int32
DAQmxGetExportedPauseTrigOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedPauseTrigOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedPauseTrigOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4006"""
DAQmxSetExportedPauseTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedPauseTrigOutputTerm
DAQmxSetExportedPauseTrigOutputTerm.restype = int32
DAQmxSetExportedPauseTrigOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedPauseTrigOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedPauseTrigOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4007"""
DAQmxResetExportedPauseTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedPauseTrigOutputTerm
DAQmxResetExportedPauseTrigOutputTerm.restype = int32
DAQmxResetExportedPauseTrigOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedPauseTrigOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedPauseTrigOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4008"""
DAQmxGetExportedPauseTrigLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedPauseTrigLvlActiveLvl
DAQmxGetExportedPauseTrigLvlActiveLvl.restype = int32
DAQmxGetExportedPauseTrigLvlActiveLvl.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedPauseTrigLvlActiveLvl.__doc__ = \
"""int32 DAQmxGetExportedPauseTrigLvlActiveLvl(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4011"""
DAQmxSetExportedPauseTrigLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedPauseTrigLvlActiveLvl
DAQmxSetExportedPauseTrigLvlActiveLvl.restype = int32
DAQmxSetExportedPauseTrigLvlActiveLvl.argtypes = [TaskHandle, int32]
DAQmxSetExportedPauseTrigLvlActiveLvl.__doc__ = \
"""int32 DAQmxSetExportedPauseTrigLvlActiveLvl(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4012"""
DAQmxResetExportedPauseTrigLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedPauseTrigLvlActiveLvl
DAQmxResetExportedPauseTrigLvlActiveLvl.restype = int32
DAQmxResetExportedPauseTrigLvlActiveLvl.argtypes = [TaskHandle]
DAQmxResetExportedPauseTrigLvlActiveLvl.__doc__ = \
"""int32 DAQmxResetExportedPauseTrigLvlActiveLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4013"""
DAQmxGetExportedRefTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRefTrigOutputTerm
DAQmxGetExportedRefTrigOutputTerm.restype = int32
DAQmxGetExportedRefTrigOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedRefTrigOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedRefTrigOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4015"""
DAQmxSetExportedRefTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRefTrigOutputTerm
DAQmxSetExportedRefTrigOutputTerm.restype = int32
DAQmxSetExportedRefTrigOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedRefTrigOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedRefTrigOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4016"""
DAQmxResetExportedRefTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRefTrigOutputTerm
DAQmxResetExportedRefTrigOutputTerm.restype = int32
DAQmxResetExportedRefTrigOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedRefTrigOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedRefTrigOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4017"""
DAQmxGetExportedRefTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRefTrigPulsePolarity
DAQmxGetExportedRefTrigPulsePolarity.restype = int32
DAQmxGetExportedRefTrigPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedRefTrigPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedRefTrigPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4020"""
DAQmxSetExportedRefTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRefTrigPulsePolarity
DAQmxSetExportedRefTrigPulsePolarity.restype = int32
DAQmxSetExportedRefTrigPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedRefTrigPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedRefTrigPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4021"""
DAQmxResetExportedRefTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRefTrigPulsePolarity
DAQmxResetExportedRefTrigPulsePolarity.restype = int32
DAQmxResetExportedRefTrigPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedRefTrigPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedRefTrigPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4022"""
DAQmxGetExportedStartTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedStartTrigOutputTerm
DAQmxGetExportedStartTrigOutputTerm.restype = int32
DAQmxGetExportedStartTrigOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedStartTrigOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedStartTrigOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4024"""
DAQmxSetExportedStartTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedStartTrigOutputTerm
DAQmxSetExportedStartTrigOutputTerm.restype = int32
DAQmxSetExportedStartTrigOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedStartTrigOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedStartTrigOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4025"""
DAQmxResetExportedStartTrigOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedStartTrigOutputTerm
DAQmxResetExportedStartTrigOutputTerm.restype = int32
DAQmxResetExportedStartTrigOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedStartTrigOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedStartTrigOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4026"""
DAQmxGetExportedStartTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedStartTrigPulsePolarity
DAQmxGetExportedStartTrigPulsePolarity.restype = int32
DAQmxGetExportedStartTrigPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedStartTrigPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedStartTrigPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4029"""
DAQmxSetExportedStartTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedStartTrigPulsePolarity
DAQmxSetExportedStartTrigPulsePolarity.restype = int32
DAQmxSetExportedStartTrigPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedStartTrigPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedStartTrigPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4030"""
DAQmxResetExportedStartTrigPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedStartTrigPulsePolarity
DAQmxResetExportedStartTrigPulsePolarity.restype = int32
DAQmxResetExportedStartTrigPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedStartTrigPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedStartTrigPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4031"""
DAQmxGetExportedAdvCmpltEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvCmpltEventOutputTerm
DAQmxGetExportedAdvCmpltEventOutputTerm.restype = int32
DAQmxGetExportedAdvCmpltEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedAdvCmpltEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedAdvCmpltEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4033"""
DAQmxSetExportedAdvCmpltEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvCmpltEventOutputTerm
DAQmxSetExportedAdvCmpltEventOutputTerm.restype = int32
DAQmxSetExportedAdvCmpltEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedAdvCmpltEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedAdvCmpltEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4034"""
DAQmxResetExportedAdvCmpltEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvCmpltEventOutputTerm
DAQmxResetExportedAdvCmpltEventOutputTerm.restype = int32
DAQmxResetExportedAdvCmpltEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedAdvCmpltEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedAdvCmpltEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4035"""
DAQmxGetExportedAdvCmpltEventDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvCmpltEventDelay
DAQmxGetExportedAdvCmpltEventDelay.restype = int32
DAQmxGetExportedAdvCmpltEventDelay.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedAdvCmpltEventDelay.__doc__ = \
"""int32 DAQmxGetExportedAdvCmpltEventDelay(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4037"""
DAQmxSetExportedAdvCmpltEventDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvCmpltEventDelay
DAQmxSetExportedAdvCmpltEventDelay.restype = int32
DAQmxSetExportedAdvCmpltEventDelay.argtypes = [TaskHandle, float64]
DAQmxSetExportedAdvCmpltEventDelay.__doc__ = \
"""int32 DAQmxSetExportedAdvCmpltEventDelay(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4038"""
DAQmxResetExportedAdvCmpltEventDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvCmpltEventDelay
DAQmxResetExportedAdvCmpltEventDelay.restype = int32
DAQmxResetExportedAdvCmpltEventDelay.argtypes = [TaskHandle]
DAQmxResetExportedAdvCmpltEventDelay.__doc__ = \
"""int32 DAQmxResetExportedAdvCmpltEventDelay(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4039"""
DAQmxGetExportedAdvCmpltEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvCmpltEventPulsePolarity
DAQmxGetExportedAdvCmpltEventPulsePolarity.restype = int32
DAQmxGetExportedAdvCmpltEventPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedAdvCmpltEventPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedAdvCmpltEventPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4042"""
DAQmxSetExportedAdvCmpltEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvCmpltEventPulsePolarity
DAQmxSetExportedAdvCmpltEventPulsePolarity.restype = int32
DAQmxSetExportedAdvCmpltEventPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedAdvCmpltEventPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedAdvCmpltEventPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4043"""
DAQmxResetExportedAdvCmpltEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvCmpltEventPulsePolarity
DAQmxResetExportedAdvCmpltEventPulsePolarity.restype = int32
DAQmxResetExportedAdvCmpltEventPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedAdvCmpltEventPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedAdvCmpltEventPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4044"""
DAQmxGetExportedAdvCmpltEventPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAdvCmpltEventPulseWidth
DAQmxGetExportedAdvCmpltEventPulseWidth.restype = int32
DAQmxGetExportedAdvCmpltEventPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedAdvCmpltEventPulseWidth.__doc__ = \
"""int32 DAQmxGetExportedAdvCmpltEventPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4046"""
DAQmxSetExportedAdvCmpltEventPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAdvCmpltEventPulseWidth
DAQmxSetExportedAdvCmpltEventPulseWidth.restype = int32
DAQmxSetExportedAdvCmpltEventPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetExportedAdvCmpltEventPulseWidth.__doc__ = \
"""int32 DAQmxSetExportedAdvCmpltEventPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4047"""
DAQmxResetExportedAdvCmpltEventPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAdvCmpltEventPulseWidth
DAQmxResetExportedAdvCmpltEventPulseWidth.restype = int32
DAQmxResetExportedAdvCmpltEventPulseWidth.argtypes = [TaskHandle]
DAQmxResetExportedAdvCmpltEventPulseWidth.__doc__ = \
"""int32 DAQmxResetExportedAdvCmpltEventPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4048"""
DAQmxGetExportedAIHoldCmpltEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAIHoldCmpltEventOutputTerm
DAQmxGetExportedAIHoldCmpltEventOutputTerm.restype = int32
DAQmxGetExportedAIHoldCmpltEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedAIHoldCmpltEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedAIHoldCmpltEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4050"""
DAQmxSetExportedAIHoldCmpltEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAIHoldCmpltEventOutputTerm
DAQmxSetExportedAIHoldCmpltEventOutputTerm.restype = int32
DAQmxSetExportedAIHoldCmpltEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedAIHoldCmpltEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedAIHoldCmpltEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4051"""
DAQmxResetExportedAIHoldCmpltEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAIHoldCmpltEventOutputTerm
DAQmxResetExportedAIHoldCmpltEventOutputTerm.restype = int32
DAQmxResetExportedAIHoldCmpltEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedAIHoldCmpltEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedAIHoldCmpltEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4052"""
DAQmxGetExportedAIHoldCmpltEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedAIHoldCmpltEventPulsePolarity
DAQmxGetExportedAIHoldCmpltEventPulsePolarity.restype = int32
DAQmxGetExportedAIHoldCmpltEventPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedAIHoldCmpltEventPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedAIHoldCmpltEventPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4055"""
DAQmxSetExportedAIHoldCmpltEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedAIHoldCmpltEventPulsePolarity
DAQmxSetExportedAIHoldCmpltEventPulsePolarity.restype = int32
DAQmxSetExportedAIHoldCmpltEventPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedAIHoldCmpltEventPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedAIHoldCmpltEventPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4056"""
DAQmxResetExportedAIHoldCmpltEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedAIHoldCmpltEventPulsePolarity
DAQmxResetExportedAIHoldCmpltEventPulsePolarity.restype = int32
DAQmxResetExportedAIHoldCmpltEventPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedAIHoldCmpltEventPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedAIHoldCmpltEventPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4057"""
DAQmxGetExportedChangeDetectEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedChangeDetectEventOutputTerm
DAQmxGetExportedChangeDetectEventOutputTerm.restype = int32
DAQmxGetExportedChangeDetectEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedChangeDetectEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedChangeDetectEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4059"""
DAQmxSetExportedChangeDetectEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedChangeDetectEventOutputTerm
DAQmxSetExportedChangeDetectEventOutputTerm.restype = int32
DAQmxSetExportedChangeDetectEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedChangeDetectEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedChangeDetectEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4060"""
DAQmxResetExportedChangeDetectEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedChangeDetectEventOutputTerm
DAQmxResetExportedChangeDetectEventOutputTerm.restype = int32
DAQmxResetExportedChangeDetectEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedChangeDetectEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedChangeDetectEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4061"""
DAQmxGetExportedChangeDetectEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedChangeDetectEventPulsePolarity
DAQmxGetExportedChangeDetectEventPulsePolarity.restype = int32
DAQmxGetExportedChangeDetectEventPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedChangeDetectEventPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedChangeDetectEventPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4064"""
DAQmxSetExportedChangeDetectEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedChangeDetectEventPulsePolarity
DAQmxSetExportedChangeDetectEventPulsePolarity.restype = int32
DAQmxSetExportedChangeDetectEventPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedChangeDetectEventPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedChangeDetectEventPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4065"""
DAQmxResetExportedChangeDetectEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedChangeDetectEventPulsePolarity
DAQmxResetExportedChangeDetectEventPulsePolarity.restype = int32
DAQmxResetExportedChangeDetectEventPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedChangeDetectEventPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedChangeDetectEventPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4066"""
DAQmxGetExportedCtrOutEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedCtrOutEventOutputTerm
DAQmxGetExportedCtrOutEventOutputTerm.restype = int32
DAQmxGetExportedCtrOutEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedCtrOutEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedCtrOutEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4068"""
DAQmxSetExportedCtrOutEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedCtrOutEventOutputTerm
DAQmxSetExportedCtrOutEventOutputTerm.restype = int32
DAQmxSetExportedCtrOutEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedCtrOutEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedCtrOutEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4069"""
DAQmxResetExportedCtrOutEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedCtrOutEventOutputTerm
DAQmxResetExportedCtrOutEventOutputTerm.restype = int32
DAQmxResetExportedCtrOutEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedCtrOutEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedCtrOutEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4070"""
DAQmxGetExportedCtrOutEventOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedCtrOutEventOutputBehavior
DAQmxGetExportedCtrOutEventOutputBehavior.restype = int32
DAQmxGetExportedCtrOutEventOutputBehavior.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedCtrOutEventOutputBehavior.__doc__ = \
"""int32 DAQmxGetExportedCtrOutEventOutputBehavior(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4073"""
DAQmxSetExportedCtrOutEventOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedCtrOutEventOutputBehavior
DAQmxSetExportedCtrOutEventOutputBehavior.restype = int32
DAQmxSetExportedCtrOutEventOutputBehavior.argtypes = [TaskHandle, int32]
DAQmxSetExportedCtrOutEventOutputBehavior.__doc__ = \
"""int32 DAQmxSetExportedCtrOutEventOutputBehavior(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4074"""
DAQmxResetExportedCtrOutEventOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedCtrOutEventOutputBehavior
DAQmxResetExportedCtrOutEventOutputBehavior.restype = int32
DAQmxResetExportedCtrOutEventOutputBehavior.argtypes = [TaskHandle]
DAQmxResetExportedCtrOutEventOutputBehavior.__doc__ = \
"""int32 DAQmxResetExportedCtrOutEventOutputBehavior(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4075"""
DAQmxGetExportedCtrOutEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedCtrOutEventPulsePolarity
DAQmxGetExportedCtrOutEventPulsePolarity.restype = int32
DAQmxGetExportedCtrOutEventPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedCtrOutEventPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedCtrOutEventPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4078"""
DAQmxSetExportedCtrOutEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedCtrOutEventPulsePolarity
DAQmxSetExportedCtrOutEventPulsePolarity.restype = int32
DAQmxSetExportedCtrOutEventPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedCtrOutEventPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedCtrOutEventPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4079"""
DAQmxResetExportedCtrOutEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedCtrOutEventPulsePolarity
DAQmxResetExportedCtrOutEventPulsePolarity.restype = int32
DAQmxResetExportedCtrOutEventPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedCtrOutEventPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedCtrOutEventPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4080"""
DAQmxGetExportedCtrOutEventToggleIdleState = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedCtrOutEventToggleIdleState
DAQmxGetExportedCtrOutEventToggleIdleState.restype = int32
DAQmxGetExportedCtrOutEventToggleIdleState.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedCtrOutEventToggleIdleState.__doc__ = \
"""int32 DAQmxGetExportedCtrOutEventToggleIdleState(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4083"""
DAQmxSetExportedCtrOutEventToggleIdleState = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedCtrOutEventToggleIdleState
DAQmxSetExportedCtrOutEventToggleIdleState.restype = int32
DAQmxSetExportedCtrOutEventToggleIdleState.argtypes = [TaskHandle, int32]
DAQmxSetExportedCtrOutEventToggleIdleState.__doc__ = \
"""int32 DAQmxSetExportedCtrOutEventToggleIdleState(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4084"""
DAQmxResetExportedCtrOutEventToggleIdleState = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedCtrOutEventToggleIdleState
DAQmxResetExportedCtrOutEventToggleIdleState.restype = int32
DAQmxResetExportedCtrOutEventToggleIdleState.argtypes = [TaskHandle]
DAQmxResetExportedCtrOutEventToggleIdleState.__doc__ = \
"""int32 DAQmxResetExportedCtrOutEventToggleIdleState(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4085"""
DAQmxGetExportedHshkEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventOutputTerm
DAQmxGetExportedHshkEventOutputTerm.restype = int32
DAQmxGetExportedHshkEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedHshkEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedHshkEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4087"""
DAQmxSetExportedHshkEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventOutputTerm
DAQmxSetExportedHshkEventOutputTerm.restype = int32
DAQmxSetExportedHshkEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedHshkEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedHshkEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4088"""
DAQmxResetExportedHshkEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventOutputTerm
DAQmxResetExportedHshkEventOutputTerm.restype = int32
DAQmxResetExportedHshkEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedHshkEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4089"""
DAQmxGetExportedHshkEventOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventOutputBehavior
DAQmxGetExportedHshkEventOutputBehavior.restype = int32
DAQmxGetExportedHshkEventOutputBehavior.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedHshkEventOutputBehavior.__doc__ = \
"""int32 DAQmxGetExportedHshkEventOutputBehavior(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4092"""
DAQmxSetExportedHshkEventOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventOutputBehavior
DAQmxSetExportedHshkEventOutputBehavior.restype = int32
DAQmxSetExportedHshkEventOutputBehavior.argtypes = [TaskHandle, int32]
DAQmxSetExportedHshkEventOutputBehavior.__doc__ = \
"""int32 DAQmxSetExportedHshkEventOutputBehavior(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4093"""
DAQmxResetExportedHshkEventOutputBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventOutputBehavior
DAQmxResetExportedHshkEventOutputBehavior.restype = int32
DAQmxResetExportedHshkEventOutputBehavior.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventOutputBehavior.__doc__ = \
"""int32 DAQmxResetExportedHshkEventOutputBehavior(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4094"""
DAQmxGetExportedHshkEventDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventDelay
DAQmxGetExportedHshkEventDelay.restype = int32
DAQmxGetExportedHshkEventDelay.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedHshkEventDelay.__doc__ = \
"""int32 DAQmxGetExportedHshkEventDelay(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4096"""
DAQmxSetExportedHshkEventDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventDelay
DAQmxSetExportedHshkEventDelay.restype = int32
DAQmxSetExportedHshkEventDelay.argtypes = [TaskHandle, float64]
DAQmxSetExportedHshkEventDelay.__doc__ = \
"""int32 DAQmxSetExportedHshkEventDelay(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4097"""
DAQmxResetExportedHshkEventDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventDelay
DAQmxResetExportedHshkEventDelay.restype = int32
DAQmxResetExportedHshkEventDelay.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventDelay.__doc__ = \
"""int32 DAQmxResetExportedHshkEventDelay(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4098"""
DAQmxGetExportedHshkEventInterlockedAssertedLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventInterlockedAssertedLvl
DAQmxGetExportedHshkEventInterlockedAssertedLvl.restype = int32
DAQmxGetExportedHshkEventInterlockedAssertedLvl.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedHshkEventInterlockedAssertedLvl.__doc__ = \
"""int32 DAQmxGetExportedHshkEventInterlockedAssertedLvl(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4101"""
DAQmxSetExportedHshkEventInterlockedAssertedLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventInterlockedAssertedLvl
DAQmxSetExportedHshkEventInterlockedAssertedLvl.restype = int32
DAQmxSetExportedHshkEventInterlockedAssertedLvl.argtypes = [TaskHandle, int32]
DAQmxSetExportedHshkEventInterlockedAssertedLvl.__doc__ = \
"""int32 DAQmxSetExportedHshkEventInterlockedAssertedLvl(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4102"""
DAQmxResetExportedHshkEventInterlockedAssertedLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventInterlockedAssertedLvl
DAQmxResetExportedHshkEventInterlockedAssertedLvl.restype = int32
DAQmxResetExportedHshkEventInterlockedAssertedLvl.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventInterlockedAssertedLvl.__doc__ = \
"""int32 DAQmxResetExportedHshkEventInterlockedAssertedLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4103"""
DAQmxGetExportedHshkEventInterlockedAssertOnStart = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventInterlockedAssertOnStart
DAQmxGetExportedHshkEventInterlockedAssertOnStart.restype = int32
DAQmxGetExportedHshkEventInterlockedAssertOnStart.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetExportedHshkEventInterlockedAssertOnStart.__doc__ = \
"""int32 DAQmxGetExportedHshkEventInterlockedAssertOnStart(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4105"""
DAQmxSetExportedHshkEventInterlockedAssertOnStart = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventInterlockedAssertOnStart
DAQmxSetExportedHshkEventInterlockedAssertOnStart.restype = int32
DAQmxSetExportedHshkEventInterlockedAssertOnStart.argtypes = [TaskHandle, bool32]
DAQmxSetExportedHshkEventInterlockedAssertOnStart.__doc__ = \
"""int32 DAQmxSetExportedHshkEventInterlockedAssertOnStart(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4106"""
DAQmxResetExportedHshkEventInterlockedAssertOnStart = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventInterlockedAssertOnStart
DAQmxResetExportedHshkEventInterlockedAssertOnStart.restype = int32
DAQmxResetExportedHshkEventInterlockedAssertOnStart.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventInterlockedAssertOnStart.__doc__ = \
"""int32 DAQmxResetExportedHshkEventInterlockedAssertOnStart(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4107"""
DAQmxGetExportedHshkEventInterlockedDeassertDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventInterlockedDeassertDelay
DAQmxGetExportedHshkEventInterlockedDeassertDelay.restype = int32
DAQmxGetExportedHshkEventInterlockedDeassertDelay.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedHshkEventInterlockedDeassertDelay.__doc__ = \
"""int32 DAQmxGetExportedHshkEventInterlockedDeassertDelay(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4109"""
DAQmxSetExportedHshkEventInterlockedDeassertDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventInterlockedDeassertDelay
DAQmxSetExportedHshkEventInterlockedDeassertDelay.restype = int32
DAQmxSetExportedHshkEventInterlockedDeassertDelay.argtypes = [TaskHandle, float64]
DAQmxSetExportedHshkEventInterlockedDeassertDelay.__doc__ = \
"""int32 DAQmxSetExportedHshkEventInterlockedDeassertDelay(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4110"""
DAQmxResetExportedHshkEventInterlockedDeassertDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventInterlockedDeassertDelay
DAQmxResetExportedHshkEventInterlockedDeassertDelay.restype = int32
DAQmxResetExportedHshkEventInterlockedDeassertDelay.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventInterlockedDeassertDelay.__doc__ = \
"""int32 DAQmxResetExportedHshkEventInterlockedDeassertDelay(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4111"""
DAQmxGetExportedHshkEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventPulsePolarity
DAQmxGetExportedHshkEventPulsePolarity.restype = int32
DAQmxGetExportedHshkEventPulsePolarity.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedHshkEventPulsePolarity.__doc__ = \
"""int32 DAQmxGetExportedHshkEventPulsePolarity(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4114"""
DAQmxSetExportedHshkEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventPulsePolarity
DAQmxSetExportedHshkEventPulsePolarity.restype = int32
DAQmxSetExportedHshkEventPulsePolarity.argtypes = [TaskHandle, int32]
DAQmxSetExportedHshkEventPulsePolarity.__doc__ = \
"""int32 DAQmxSetExportedHshkEventPulsePolarity(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4115"""
DAQmxResetExportedHshkEventPulsePolarity = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventPulsePolarity
DAQmxResetExportedHshkEventPulsePolarity.restype = int32
DAQmxResetExportedHshkEventPulsePolarity.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventPulsePolarity.__doc__ = \
"""int32 DAQmxResetExportedHshkEventPulsePolarity(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4116"""
DAQmxGetExportedHshkEventPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedHshkEventPulseWidth
DAQmxGetExportedHshkEventPulseWidth.restype = int32
DAQmxGetExportedHshkEventPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetExportedHshkEventPulseWidth.__doc__ = \
"""int32 DAQmxGetExportedHshkEventPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4118"""
DAQmxSetExportedHshkEventPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedHshkEventPulseWidth
DAQmxSetExportedHshkEventPulseWidth.restype = int32
DAQmxSetExportedHshkEventPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetExportedHshkEventPulseWidth.__doc__ = \
"""int32 DAQmxSetExportedHshkEventPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4119"""
DAQmxResetExportedHshkEventPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedHshkEventPulseWidth
DAQmxResetExportedHshkEventPulseWidth.restype = int32
DAQmxResetExportedHshkEventPulseWidth.argtypes = [TaskHandle]
DAQmxResetExportedHshkEventPulseWidth.__doc__ = \
"""int32 DAQmxResetExportedHshkEventPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4120"""
DAQmxGetExportedRdyForXferEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRdyForXferEventOutputTerm
DAQmxGetExportedRdyForXferEventOutputTerm.restype = int32
DAQmxGetExportedRdyForXferEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedRdyForXferEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedRdyForXferEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4122"""
DAQmxSetExportedRdyForXferEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRdyForXferEventOutputTerm
DAQmxSetExportedRdyForXferEventOutputTerm.restype = int32
DAQmxSetExportedRdyForXferEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedRdyForXferEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedRdyForXferEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4123"""
DAQmxResetExportedRdyForXferEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRdyForXferEventOutputTerm
DAQmxResetExportedRdyForXferEventOutputTerm.restype = int32
DAQmxResetExportedRdyForXferEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedRdyForXferEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedRdyForXferEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4124"""
DAQmxGetExportedRdyForXferEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRdyForXferEventLvlActiveLvl
DAQmxGetExportedRdyForXferEventLvlActiveLvl.restype = int32
DAQmxGetExportedRdyForXferEventLvlActiveLvl.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedRdyForXferEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxGetExportedRdyForXferEventLvlActiveLvl(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4127"""
DAQmxSetExportedRdyForXferEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRdyForXferEventLvlActiveLvl
DAQmxSetExportedRdyForXferEventLvlActiveLvl.restype = int32
DAQmxSetExportedRdyForXferEventLvlActiveLvl.argtypes = [TaskHandle, int32]
DAQmxSetExportedRdyForXferEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxSetExportedRdyForXferEventLvlActiveLvl(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4128"""
DAQmxResetExportedRdyForXferEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRdyForXferEventLvlActiveLvl
DAQmxResetExportedRdyForXferEventLvlActiveLvl.restype = int32
DAQmxResetExportedRdyForXferEventLvlActiveLvl.argtypes = [TaskHandle]
DAQmxResetExportedRdyForXferEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxResetExportedRdyForXferEventLvlActiveLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4129"""
DAQmxGetExportedRdyForXferEventDeassertCond = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRdyForXferEventDeassertCond
DAQmxGetExportedRdyForXferEventDeassertCond.restype = int32
DAQmxGetExportedRdyForXferEventDeassertCond.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedRdyForXferEventDeassertCond.__doc__ = \
"""int32 DAQmxGetExportedRdyForXferEventDeassertCond(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4132"""
DAQmxSetExportedRdyForXferEventDeassertCond = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRdyForXferEventDeassertCond
DAQmxSetExportedRdyForXferEventDeassertCond.restype = int32
DAQmxSetExportedRdyForXferEventDeassertCond.argtypes = [TaskHandle, int32]
DAQmxSetExportedRdyForXferEventDeassertCond.__doc__ = \
"""int32 DAQmxSetExportedRdyForXferEventDeassertCond(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4133"""
DAQmxResetExportedRdyForXferEventDeassertCond = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRdyForXferEventDeassertCond
DAQmxResetExportedRdyForXferEventDeassertCond.restype = int32
DAQmxResetExportedRdyForXferEventDeassertCond.argtypes = [TaskHandle]
DAQmxResetExportedRdyForXferEventDeassertCond.__doc__ = \
"""int32 DAQmxResetExportedRdyForXferEventDeassertCond(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4134"""
DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold
DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold.restype = int32
DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold.__doc__ = \
"""int32 DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4136"""
DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold
DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold.restype = int32
DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold.argtypes = [TaskHandle, uInt32]
DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold.__doc__ = \
"""int32 DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4137"""
DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold
DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold.restype = int32
DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold.argtypes = [TaskHandle]
DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold.__doc__ = \
"""int32 DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4138"""
DAQmxGetExportedDataActiveEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedDataActiveEventOutputTerm
DAQmxGetExportedDataActiveEventOutputTerm.restype = int32
DAQmxGetExportedDataActiveEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedDataActiveEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedDataActiveEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4140"""
DAQmxSetExportedDataActiveEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedDataActiveEventOutputTerm
DAQmxSetExportedDataActiveEventOutputTerm.restype = int32
DAQmxSetExportedDataActiveEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedDataActiveEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedDataActiveEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4141"""
DAQmxResetExportedDataActiveEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedDataActiveEventOutputTerm
DAQmxResetExportedDataActiveEventOutputTerm.restype = int32
DAQmxResetExportedDataActiveEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedDataActiveEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedDataActiveEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4142"""
DAQmxGetExportedDataActiveEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedDataActiveEventLvlActiveLvl
DAQmxGetExportedDataActiveEventLvlActiveLvl.restype = int32
DAQmxGetExportedDataActiveEventLvlActiveLvl.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedDataActiveEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxGetExportedDataActiveEventLvlActiveLvl(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4145"""
DAQmxSetExportedDataActiveEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedDataActiveEventLvlActiveLvl
DAQmxSetExportedDataActiveEventLvlActiveLvl.restype = int32
DAQmxSetExportedDataActiveEventLvlActiveLvl.argtypes = [TaskHandle, int32]
DAQmxSetExportedDataActiveEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxSetExportedDataActiveEventLvlActiveLvl(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4146"""
DAQmxResetExportedDataActiveEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedDataActiveEventLvlActiveLvl
DAQmxResetExportedDataActiveEventLvlActiveLvl.restype = int32
DAQmxResetExportedDataActiveEventLvlActiveLvl.argtypes = [TaskHandle]
DAQmxResetExportedDataActiveEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxResetExportedDataActiveEventLvlActiveLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4147"""
DAQmxGetExportedRdyForStartEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRdyForStartEventOutputTerm
DAQmxGetExportedRdyForStartEventOutputTerm.restype = int32
DAQmxGetExportedRdyForStartEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedRdyForStartEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedRdyForStartEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4149"""
DAQmxSetExportedRdyForStartEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRdyForStartEventOutputTerm
DAQmxSetExportedRdyForStartEventOutputTerm.restype = int32
DAQmxSetExportedRdyForStartEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedRdyForStartEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedRdyForStartEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4150"""
DAQmxResetExportedRdyForStartEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRdyForStartEventOutputTerm
DAQmxResetExportedRdyForStartEventOutputTerm.restype = int32
DAQmxResetExportedRdyForStartEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedRdyForStartEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedRdyForStartEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4151"""
DAQmxGetExportedRdyForStartEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedRdyForStartEventLvlActiveLvl
DAQmxGetExportedRdyForStartEventLvlActiveLvl.restype = int32
DAQmxGetExportedRdyForStartEventLvlActiveLvl.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetExportedRdyForStartEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxGetExportedRdyForStartEventLvlActiveLvl(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4154"""
DAQmxSetExportedRdyForStartEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedRdyForStartEventLvlActiveLvl
DAQmxSetExportedRdyForStartEventLvlActiveLvl.restype = int32
DAQmxSetExportedRdyForStartEventLvlActiveLvl.argtypes = [TaskHandle, int32]
DAQmxSetExportedRdyForStartEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxSetExportedRdyForStartEventLvlActiveLvl(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4155"""
DAQmxResetExportedRdyForStartEventLvlActiveLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedRdyForStartEventLvlActiveLvl
DAQmxResetExportedRdyForStartEventLvlActiveLvl.restype = int32
DAQmxResetExportedRdyForStartEventLvlActiveLvl.argtypes = [TaskHandle]
DAQmxResetExportedRdyForStartEventLvlActiveLvl.__doc__ = \
"""int32 DAQmxResetExportedRdyForStartEventLvlActiveLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4156"""
DAQmxGetExportedSyncPulseEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedSyncPulseEventOutputTerm
DAQmxGetExportedSyncPulseEventOutputTerm.restype = int32
DAQmxGetExportedSyncPulseEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedSyncPulseEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedSyncPulseEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4158"""
DAQmxSetExportedSyncPulseEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedSyncPulseEventOutputTerm
DAQmxSetExportedSyncPulseEventOutputTerm.restype = int32
DAQmxSetExportedSyncPulseEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedSyncPulseEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedSyncPulseEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4159"""
DAQmxResetExportedSyncPulseEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedSyncPulseEventOutputTerm
DAQmxResetExportedSyncPulseEventOutputTerm.restype = int32
DAQmxResetExportedSyncPulseEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedSyncPulseEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedSyncPulseEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4160"""
DAQmxGetExportedWatchdogExpiredEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxGetExportedWatchdogExpiredEventOutputTerm
DAQmxGetExportedWatchdogExpiredEventOutputTerm.restype = int32
DAQmxGetExportedWatchdogExpiredEventOutputTerm.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetExportedWatchdogExpiredEventOutputTerm.__doc__ = \
"""int32 DAQmxGetExportedWatchdogExpiredEventOutputTerm(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4162"""
DAQmxSetExportedWatchdogExpiredEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxSetExportedWatchdogExpiredEventOutputTerm
DAQmxSetExportedWatchdogExpiredEventOutputTerm.restype = int32
DAQmxSetExportedWatchdogExpiredEventOutputTerm.argtypes = [TaskHandle, STRING]
DAQmxSetExportedWatchdogExpiredEventOutputTerm.__doc__ = \
"""int32 DAQmxSetExportedWatchdogExpiredEventOutputTerm(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4163"""
DAQmxResetExportedWatchdogExpiredEventOutputTerm = _stdcall_libraries['nicaiu.dll'].DAQmxResetExportedWatchdogExpiredEventOutputTerm
DAQmxResetExportedWatchdogExpiredEventOutputTerm.restype = int32
DAQmxResetExportedWatchdogExpiredEventOutputTerm.argtypes = [TaskHandle]
DAQmxResetExportedWatchdogExpiredEventOutputTerm.__doc__ = \
"""int32 DAQmxResetExportedWatchdogExpiredEventOutputTerm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4164"""
DAQmxGetDevIsSimulated = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevIsSimulated
DAQmxGetDevIsSimulated.restype = int32
DAQmxGetDevIsSimulated.argtypes = [STRING, POINTER(bool32)]
DAQmxGetDevIsSimulated.__doc__ = \
"""int32 DAQmxGetDevIsSimulated(unknown * device, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4168"""
DAQmxGetDevProductCategory = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevProductCategory
DAQmxGetDevProductCategory.restype = int32
DAQmxGetDevProductCategory.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevProductCategory.__doc__ = \
"""int32 DAQmxGetDevProductCategory(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4171"""
DAQmxGetDevProductType = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevProductType
DAQmxGetDevProductType.restype = int32
DAQmxGetDevProductType.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevProductType.__doc__ = \
"""int32 DAQmxGetDevProductType(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4173"""
DAQmxGetDevProductNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevProductNum
DAQmxGetDevProductNum.restype = int32
DAQmxGetDevProductNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevProductNum.__doc__ = \
"""int32 DAQmxGetDevProductNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4175"""
DAQmxGetDevSerialNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevSerialNum
DAQmxGetDevSerialNum.restype = int32
DAQmxGetDevSerialNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevSerialNum.__doc__ = \
"""int32 DAQmxGetDevSerialNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4177"""
DAQmxGetCarrierSerialNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetCarrierSerialNum
DAQmxGetCarrierSerialNum.restype = int32
DAQmxGetCarrierSerialNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetCarrierSerialNum.__doc__ = \
"""int32 DAQmxGetCarrierSerialNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4179"""
DAQmxGetDevChassisModuleDevNames = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevChassisModuleDevNames
DAQmxGetDevChassisModuleDevNames.restype = int32
DAQmxGetDevChassisModuleDevNames.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevChassisModuleDevNames.__doc__ = \
"""int32 DAQmxGetDevChassisModuleDevNames(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4181"""
DAQmxGetDevAnlgTrigSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAnlgTrigSupported
DAQmxGetDevAnlgTrigSupported.restype = int32
DAQmxGetDevAnlgTrigSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetDevAnlgTrigSupported.__doc__ = \
"""int32 DAQmxGetDevAnlgTrigSupported(unknown * device, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4183"""
DAQmxGetDevDigTrigSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDigTrigSupported
DAQmxGetDevDigTrigSupported.restype = int32
DAQmxGetDevDigTrigSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetDevDigTrigSupported.__doc__ = \
"""int32 DAQmxGetDevDigTrigSupported(unknown * device, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4185"""
DAQmxGetDevAIPhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIPhysicalChans
DAQmxGetDevAIPhysicalChans.restype = int32
DAQmxGetDevAIPhysicalChans.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevAIPhysicalChans.__doc__ = \
"""int32 DAQmxGetDevAIPhysicalChans(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4187"""
DAQmxGetDevAIMaxSingleChanRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIMaxSingleChanRate
DAQmxGetDevAIMaxSingleChanRate.restype = int32
DAQmxGetDevAIMaxSingleChanRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevAIMaxSingleChanRate.__doc__ = \
"""int32 DAQmxGetDevAIMaxSingleChanRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4189"""
DAQmxGetDevAIMaxMultiChanRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIMaxMultiChanRate
DAQmxGetDevAIMaxMultiChanRate.restype = int32
DAQmxGetDevAIMaxMultiChanRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevAIMaxMultiChanRate.__doc__ = \
"""int32 DAQmxGetDevAIMaxMultiChanRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4191"""
DAQmxGetDevAIMinRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIMinRate
DAQmxGetDevAIMinRate.restype = int32
DAQmxGetDevAIMinRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevAIMinRate.__doc__ = \
"""int32 DAQmxGetDevAIMinRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4193"""
DAQmxGetDevAISimultaneousSamplingSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAISimultaneousSamplingSupported
DAQmxGetDevAISimultaneousSamplingSupported.restype = int32
DAQmxGetDevAISimultaneousSamplingSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetDevAISimultaneousSamplingSupported.__doc__ = \
"""int32 DAQmxGetDevAISimultaneousSamplingSupported(unknown * device, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4195"""
DAQmxGetDevAITrigUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAITrigUsage
DAQmxGetDevAITrigUsage.restype = int32
DAQmxGetDevAITrigUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevAITrigUsage.__doc__ = \
"""int32 DAQmxGetDevAITrigUsage(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4198"""
DAQmxGetDevAIVoltageRngs = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIVoltageRngs
DAQmxGetDevAIVoltageRngs.restype = int32
DAQmxGetDevAIVoltageRngs.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAIVoltageRngs.__doc__ = \
"""int32 DAQmxGetDevAIVoltageRngs(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4200"""
DAQmxGetDevAIVoltageIntExcitDiscreteVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIVoltageIntExcitDiscreteVals
DAQmxGetDevAIVoltageIntExcitDiscreteVals.restype = int32
DAQmxGetDevAIVoltageIntExcitDiscreteVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAIVoltageIntExcitDiscreteVals.__doc__ = \
"""int32 DAQmxGetDevAIVoltageIntExcitDiscreteVals(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4202"""
DAQmxGetDevAIVoltageIntExcitRangeVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIVoltageIntExcitRangeVals
DAQmxGetDevAIVoltageIntExcitRangeVals.restype = int32
DAQmxGetDevAIVoltageIntExcitRangeVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAIVoltageIntExcitRangeVals.__doc__ = \
"""int32 DAQmxGetDevAIVoltageIntExcitRangeVals(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4204"""
DAQmxGetDevAICurrentRngs = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAICurrentRngs
DAQmxGetDevAICurrentRngs.restype = int32
DAQmxGetDevAICurrentRngs.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAICurrentRngs.__doc__ = \
"""int32 DAQmxGetDevAICurrentRngs(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4206"""
DAQmxGetDevAICurrentIntExcitDiscreteVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAICurrentIntExcitDiscreteVals
DAQmxGetDevAICurrentIntExcitDiscreteVals.restype = int32
DAQmxGetDevAICurrentIntExcitDiscreteVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAICurrentIntExcitDiscreteVals.__doc__ = \
"""int32 DAQmxGetDevAICurrentIntExcitDiscreteVals(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4208"""
DAQmxGetDevAIFreqRngs = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIFreqRngs
DAQmxGetDevAIFreqRngs.restype = int32
DAQmxGetDevAIFreqRngs.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAIFreqRngs.__doc__ = \
"""int32 DAQmxGetDevAIFreqRngs(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4210"""
DAQmxGetDevAIGains = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAIGains
DAQmxGetDevAIGains.restype = int32
DAQmxGetDevAIGains.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAIGains.__doc__ = \
"""int32 DAQmxGetDevAIGains(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4212"""
DAQmxGetDevAICouplings = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAICouplings
DAQmxGetDevAICouplings.restype = int32
DAQmxGetDevAICouplings.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevAICouplings.__doc__ = \
"""int32 DAQmxGetDevAICouplings(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4215"""
DAQmxGetDevAILowpassCutoffFreqDiscreteVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAILowpassCutoffFreqDiscreteVals
DAQmxGetDevAILowpassCutoffFreqDiscreteVals.restype = int32
DAQmxGetDevAILowpassCutoffFreqDiscreteVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAILowpassCutoffFreqDiscreteVals.__doc__ = \
"""int32 DAQmxGetDevAILowpassCutoffFreqDiscreteVals(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4217"""
DAQmxGetDevAILowpassCutoffFreqRangeVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAILowpassCutoffFreqRangeVals
DAQmxGetDevAILowpassCutoffFreqRangeVals.restype = int32
DAQmxGetDevAILowpassCutoffFreqRangeVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAILowpassCutoffFreqRangeVals.__doc__ = \
"""int32 DAQmxGetDevAILowpassCutoffFreqRangeVals(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4219"""
DAQmxGetDevAOPhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOPhysicalChans
DAQmxGetDevAOPhysicalChans.restype = int32
DAQmxGetDevAOPhysicalChans.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevAOPhysicalChans.__doc__ = \
"""int32 DAQmxGetDevAOPhysicalChans(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4221"""
DAQmxGetDevAOSampClkSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOSampClkSupported
DAQmxGetDevAOSampClkSupported.restype = int32
DAQmxGetDevAOSampClkSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetDevAOSampClkSupported.__doc__ = \
"""int32 DAQmxGetDevAOSampClkSupported(unknown * device, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4223"""
DAQmxGetDevAOMaxRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOMaxRate
DAQmxGetDevAOMaxRate.restype = int32
DAQmxGetDevAOMaxRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevAOMaxRate.__doc__ = \
"""int32 DAQmxGetDevAOMaxRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4225"""
DAQmxGetDevAOMinRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOMinRate
DAQmxGetDevAOMinRate.restype = int32
DAQmxGetDevAOMinRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevAOMinRate.__doc__ = \
"""int32 DAQmxGetDevAOMinRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4227"""
DAQmxGetDevAOTrigUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOTrigUsage
DAQmxGetDevAOTrigUsage.restype = int32
DAQmxGetDevAOTrigUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevAOTrigUsage.__doc__ = \
"""int32 DAQmxGetDevAOTrigUsage(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4230"""
DAQmxGetDevAOVoltageRngs = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOVoltageRngs
DAQmxGetDevAOVoltageRngs.restype = int32
DAQmxGetDevAOVoltageRngs.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAOVoltageRngs.__doc__ = \
"""int32 DAQmxGetDevAOVoltageRngs(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4232"""
DAQmxGetDevAOCurrentRngs = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOCurrentRngs
DAQmxGetDevAOCurrentRngs.restype = int32
DAQmxGetDevAOCurrentRngs.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAOCurrentRngs.__doc__ = \
"""int32 DAQmxGetDevAOCurrentRngs(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4234"""
DAQmxGetDevAOGains = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevAOGains
DAQmxGetDevAOGains.restype = int32
DAQmxGetDevAOGains.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetDevAOGains.__doc__ = \
"""int32 DAQmxGetDevAOGains(unknown * device, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4236"""
DAQmxGetDevDILines = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDILines
DAQmxGetDevDILines.restype = int32
DAQmxGetDevDILines.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevDILines.__doc__ = \
"""int32 DAQmxGetDevDILines(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4238"""
DAQmxGetDevDIPorts = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDIPorts
DAQmxGetDevDIPorts.restype = int32
DAQmxGetDevDIPorts.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevDIPorts.__doc__ = \
"""int32 DAQmxGetDevDIPorts(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4240"""
DAQmxGetDevDIMaxRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDIMaxRate
DAQmxGetDevDIMaxRate.restype = int32
DAQmxGetDevDIMaxRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevDIMaxRate.__doc__ = \
"""int32 DAQmxGetDevDIMaxRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4242"""
DAQmxGetDevDITrigUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDITrigUsage
DAQmxGetDevDITrigUsage.restype = int32
DAQmxGetDevDITrigUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevDITrigUsage.__doc__ = \
"""int32 DAQmxGetDevDITrigUsage(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4245"""
DAQmxGetDevDOLines = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDOLines
DAQmxGetDevDOLines.restype = int32
DAQmxGetDevDOLines.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevDOLines.__doc__ = \
"""int32 DAQmxGetDevDOLines(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4247"""
DAQmxGetDevDOPorts = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDOPorts
DAQmxGetDevDOPorts.restype = int32
DAQmxGetDevDOPorts.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevDOPorts.__doc__ = \
"""int32 DAQmxGetDevDOPorts(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4249"""
DAQmxGetDevDOMaxRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDOMaxRate
DAQmxGetDevDOMaxRate.restype = int32
DAQmxGetDevDOMaxRate.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevDOMaxRate.__doc__ = \
"""int32 DAQmxGetDevDOMaxRate(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4251"""
DAQmxGetDevDOTrigUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevDOTrigUsage
DAQmxGetDevDOTrigUsage.restype = int32
DAQmxGetDevDOTrigUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevDOTrigUsage.__doc__ = \
"""int32 DAQmxGetDevDOTrigUsage(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4254"""
DAQmxGetDevCIPhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCIPhysicalChans
DAQmxGetDevCIPhysicalChans.restype = int32
DAQmxGetDevCIPhysicalChans.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevCIPhysicalChans.__doc__ = \
"""int32 DAQmxGetDevCIPhysicalChans(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4256"""
DAQmxGetDevCITrigUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCITrigUsage
DAQmxGetDevCITrigUsage.restype = int32
DAQmxGetDevCITrigUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevCITrigUsage.__doc__ = \
"""int32 DAQmxGetDevCITrigUsage(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4259"""
DAQmxGetDevCISampClkSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCISampClkSupported
DAQmxGetDevCISampClkSupported.restype = int32
DAQmxGetDevCISampClkSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetDevCISampClkSupported.__doc__ = \
"""int32 DAQmxGetDevCISampClkSupported(unknown * device, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4261"""
DAQmxGetDevCIMaxSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCIMaxSize
DAQmxGetDevCIMaxSize.restype = int32
DAQmxGetDevCIMaxSize.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevCIMaxSize.__doc__ = \
"""int32 DAQmxGetDevCIMaxSize(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4263"""
DAQmxGetDevCIMaxTimebase = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCIMaxTimebase
DAQmxGetDevCIMaxTimebase.restype = int32
DAQmxGetDevCIMaxTimebase.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevCIMaxTimebase.__doc__ = \
"""int32 DAQmxGetDevCIMaxTimebase(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4265"""
DAQmxGetDevCOPhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCOPhysicalChans
DAQmxGetDevCOPhysicalChans.restype = int32
DAQmxGetDevCOPhysicalChans.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevCOPhysicalChans.__doc__ = \
"""int32 DAQmxGetDevCOPhysicalChans(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4267"""
DAQmxGetDevCOTrigUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCOTrigUsage
DAQmxGetDevCOTrigUsage.restype = int32
DAQmxGetDevCOTrigUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevCOTrigUsage.__doc__ = \
"""int32 DAQmxGetDevCOTrigUsage(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4270"""
DAQmxGetDevCOMaxSize = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCOMaxSize
DAQmxGetDevCOMaxSize.restype = int32
DAQmxGetDevCOMaxSize.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevCOMaxSize.__doc__ = \
"""int32 DAQmxGetDevCOMaxSize(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4272"""
DAQmxGetDevCOMaxTimebase = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCOMaxTimebase
DAQmxGetDevCOMaxTimebase.restype = int32
DAQmxGetDevCOMaxTimebase.argtypes = [STRING, POINTER(float64)]
DAQmxGetDevCOMaxTimebase.__doc__ = \
"""int32 DAQmxGetDevCOMaxTimebase(unknown * device, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4274"""
DAQmxGetDevNumDMAChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevNumDMAChans
DAQmxGetDevNumDMAChans.restype = int32
DAQmxGetDevNumDMAChans.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevNumDMAChans.__doc__ = \
"""int32 DAQmxGetDevNumDMAChans(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4276"""
DAQmxGetDevBusType = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevBusType
DAQmxGetDevBusType.restype = int32
DAQmxGetDevBusType.argtypes = [STRING, POINTER(int32)]
DAQmxGetDevBusType.__doc__ = \
"""int32 DAQmxGetDevBusType(unknown * device, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4279"""
DAQmxGetDevPCIBusNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevPCIBusNum
DAQmxGetDevPCIBusNum.restype = int32
DAQmxGetDevPCIBusNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevPCIBusNum.__doc__ = \
"""int32 DAQmxGetDevPCIBusNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4281"""
DAQmxGetDevPCIDevNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevPCIDevNum
DAQmxGetDevPCIDevNum.restype = int32
DAQmxGetDevPCIDevNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevPCIDevNum.__doc__ = \
"""int32 DAQmxGetDevPCIDevNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4283"""
DAQmxGetDevPXIChassisNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevPXIChassisNum
DAQmxGetDevPXIChassisNum.restype = int32
DAQmxGetDevPXIChassisNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevPXIChassisNum.__doc__ = \
"""int32 DAQmxGetDevPXIChassisNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4285"""
DAQmxGetDevPXISlotNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevPXISlotNum
DAQmxGetDevPXISlotNum.restype = int32
DAQmxGetDevPXISlotNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevPXISlotNum.__doc__ = \
"""int32 DAQmxGetDevPXISlotNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4287"""
DAQmxGetDevCompactDAQChassisDevName = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCompactDAQChassisDevName
DAQmxGetDevCompactDAQChassisDevName.restype = int32
DAQmxGetDevCompactDAQChassisDevName.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevCompactDAQChassisDevName.__doc__ = \
"""int32 DAQmxGetDevCompactDAQChassisDevName(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4289"""
DAQmxGetDevCompactDAQSlotNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevCompactDAQSlotNum
DAQmxGetDevCompactDAQSlotNum.restype = int32
DAQmxGetDevCompactDAQSlotNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetDevCompactDAQSlotNum.__doc__ = \
"""int32 DAQmxGetDevCompactDAQSlotNum(unknown * device, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4291"""
DAQmxGetDevTCPIPHostname = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevTCPIPHostname
DAQmxGetDevTCPIPHostname.restype = int32
DAQmxGetDevTCPIPHostname.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevTCPIPHostname.__doc__ = \
"""int32 DAQmxGetDevTCPIPHostname(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4293"""
DAQmxGetDevTCPIPEthernetIP = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevTCPIPEthernetIP
DAQmxGetDevTCPIPEthernetIP.restype = int32
DAQmxGetDevTCPIPEthernetIP.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevTCPIPEthernetIP.__doc__ = \
"""int32 DAQmxGetDevTCPIPEthernetIP(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4295"""
DAQmxGetDevTCPIPWirelessIP = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevTCPIPWirelessIP
DAQmxGetDevTCPIPWirelessIP.restype = int32
DAQmxGetDevTCPIPWirelessIP.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevTCPIPWirelessIP.__doc__ = \
"""int32 DAQmxGetDevTCPIPWirelessIP(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4297"""
DAQmxGetDevTerminals = _stdcall_libraries['nicaiu.dll'].DAQmxGetDevTerminals
DAQmxGetDevTerminals.restype = int32
DAQmxGetDevTerminals.argtypes = [STRING, STRING, uInt32]
DAQmxGetDevTerminals.__doc__ = \
"""int32 DAQmxGetDevTerminals(unknown * device, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4299"""
DAQmxGetReadRelativeTo = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadRelativeTo
DAQmxGetReadRelativeTo.restype = int32
DAQmxGetReadRelativeTo.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetReadRelativeTo.__doc__ = \
"""int32 DAQmxGetReadRelativeTo(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4304"""
DAQmxSetReadRelativeTo = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadRelativeTo
DAQmxSetReadRelativeTo.restype = int32
DAQmxSetReadRelativeTo.argtypes = [TaskHandle, int32]
DAQmxSetReadRelativeTo.__doc__ = \
"""int32 DAQmxSetReadRelativeTo(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4305"""
DAQmxResetReadRelativeTo = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadRelativeTo
DAQmxResetReadRelativeTo.restype = int32
DAQmxResetReadRelativeTo.argtypes = [TaskHandle]
DAQmxResetReadRelativeTo.__doc__ = \
"""int32 DAQmxResetReadRelativeTo(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4306"""
DAQmxGetReadOffset = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOffset
DAQmxGetReadOffset.restype = int32
DAQmxGetReadOffset.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetReadOffset.__doc__ = \
"""int32 DAQmxGetReadOffset(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4308"""
DAQmxSetReadOffset = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadOffset
DAQmxSetReadOffset.restype = int32
DAQmxSetReadOffset.argtypes = [TaskHandle, int32]
DAQmxSetReadOffset.__doc__ = \
"""int32 DAQmxSetReadOffset(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4309"""
DAQmxResetReadOffset = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadOffset
DAQmxResetReadOffset.restype = int32
DAQmxResetReadOffset.argtypes = [TaskHandle]
DAQmxResetReadOffset.__doc__ = \
"""int32 DAQmxResetReadOffset(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4310"""
DAQmxGetReadChannelsToRead = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadChannelsToRead
DAQmxGetReadChannelsToRead.restype = int32
DAQmxGetReadChannelsToRead.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetReadChannelsToRead.__doc__ = \
"""int32 DAQmxGetReadChannelsToRead(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4312"""
DAQmxSetReadChannelsToRead = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadChannelsToRead
DAQmxSetReadChannelsToRead.restype = int32
DAQmxSetReadChannelsToRead.argtypes = [TaskHandle, STRING]
DAQmxSetReadChannelsToRead.__doc__ = \
"""int32 DAQmxSetReadChannelsToRead(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4313"""
DAQmxResetReadChannelsToRead = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadChannelsToRead
DAQmxResetReadChannelsToRead.restype = int32
DAQmxResetReadChannelsToRead.argtypes = [TaskHandle]
DAQmxResetReadChannelsToRead.__doc__ = \
"""int32 DAQmxResetReadChannelsToRead(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4314"""
DAQmxGetReadReadAllAvailSamp = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadReadAllAvailSamp
DAQmxGetReadReadAllAvailSamp.restype = int32
DAQmxGetReadReadAllAvailSamp.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadReadAllAvailSamp.__doc__ = \
"""int32 DAQmxGetReadReadAllAvailSamp(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4316"""
DAQmxSetReadReadAllAvailSamp = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadReadAllAvailSamp
DAQmxSetReadReadAllAvailSamp.restype = int32
DAQmxSetReadReadAllAvailSamp.argtypes = [TaskHandle, bool32]
DAQmxSetReadReadAllAvailSamp.__doc__ = \
"""int32 DAQmxSetReadReadAllAvailSamp(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4317"""
DAQmxResetReadReadAllAvailSamp = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadReadAllAvailSamp
DAQmxResetReadReadAllAvailSamp.restype = int32
DAQmxResetReadReadAllAvailSamp.argtypes = [TaskHandle]
DAQmxResetReadReadAllAvailSamp.__doc__ = \
"""int32 DAQmxResetReadReadAllAvailSamp(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4318"""
DAQmxGetReadAutoStart = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadAutoStart
DAQmxGetReadAutoStart.restype = int32
DAQmxGetReadAutoStart.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadAutoStart.__doc__ = \
"""int32 DAQmxGetReadAutoStart(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4320"""
DAQmxSetReadAutoStart = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadAutoStart
DAQmxSetReadAutoStart.restype = int32
DAQmxSetReadAutoStart.argtypes = [TaskHandle, bool32]
DAQmxSetReadAutoStart.__doc__ = \
"""int32 DAQmxSetReadAutoStart(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4321"""
DAQmxResetReadAutoStart = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadAutoStart
DAQmxResetReadAutoStart.restype = int32
DAQmxResetReadAutoStart.argtypes = [TaskHandle]
DAQmxResetReadAutoStart.__doc__ = \
"""int32 DAQmxResetReadAutoStart(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4322"""
DAQmxGetReadOverWrite = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOverWrite
DAQmxGetReadOverWrite.restype = int32
DAQmxGetReadOverWrite.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetReadOverWrite.__doc__ = \
"""int32 DAQmxGetReadOverWrite(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4325"""
DAQmxSetReadOverWrite = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadOverWrite
DAQmxSetReadOverWrite.restype = int32
DAQmxSetReadOverWrite.argtypes = [TaskHandle, int32]
DAQmxSetReadOverWrite.__doc__ = \
"""int32 DAQmxSetReadOverWrite(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4326"""
DAQmxResetReadOverWrite = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadOverWrite
DAQmxResetReadOverWrite.restype = int32
DAQmxResetReadOverWrite.argtypes = [TaskHandle]
DAQmxResetReadOverWrite.__doc__ = \
"""int32 DAQmxResetReadOverWrite(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4327"""
DAQmxGetReadCurrReadPos = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadCurrReadPos
DAQmxGetReadCurrReadPos.restype = int32
DAQmxGetReadCurrReadPos.argtypes = [TaskHandle, POINTER(uInt64)]
DAQmxGetReadCurrReadPos.__doc__ = \
"""int32 DAQmxGetReadCurrReadPos(TaskHandle taskHandle, uInt64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4329"""
DAQmxGetReadAvailSampPerChan = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadAvailSampPerChan
DAQmxGetReadAvailSampPerChan.restype = int32
DAQmxGetReadAvailSampPerChan.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetReadAvailSampPerChan.__doc__ = \
"""int32 DAQmxGetReadAvailSampPerChan(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4331"""
DAQmxGetReadTotalSampPerChanAcquired = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadTotalSampPerChanAcquired
DAQmxGetReadTotalSampPerChanAcquired.restype = int32
DAQmxGetReadTotalSampPerChanAcquired.argtypes = [TaskHandle, POINTER(uInt64)]
DAQmxGetReadTotalSampPerChanAcquired.__doc__ = \
"""int32 DAQmxGetReadTotalSampPerChanAcquired(TaskHandle taskHandle, uInt64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4333"""
DAQmxGetReadCommonModeRangeErrorChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadCommonModeRangeErrorChansExist
DAQmxGetReadCommonModeRangeErrorChansExist.restype = int32
DAQmxGetReadCommonModeRangeErrorChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadCommonModeRangeErrorChansExist.__doc__ = \
"""int32 DAQmxGetReadCommonModeRangeErrorChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4335"""
DAQmxGetReadCommonModeRangeErrorChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadCommonModeRangeErrorChans
DAQmxGetReadCommonModeRangeErrorChans.restype = int32
DAQmxGetReadCommonModeRangeErrorChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetReadCommonModeRangeErrorChans.__doc__ = \
"""int32 DAQmxGetReadCommonModeRangeErrorChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4337"""
DAQmxGetReadOvercurrentChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOvercurrentChansExist
DAQmxGetReadOvercurrentChansExist.restype = int32
DAQmxGetReadOvercurrentChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadOvercurrentChansExist.__doc__ = \
"""int32 DAQmxGetReadOvercurrentChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4339"""
DAQmxGetReadOvercurrentChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOvercurrentChans
DAQmxGetReadOvercurrentChans.restype = int32
DAQmxGetReadOvercurrentChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetReadOvercurrentChans.__doc__ = \
"""int32 DAQmxGetReadOvercurrentChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4341"""
DAQmxGetReadOpenCurrentLoopChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOpenCurrentLoopChansExist
DAQmxGetReadOpenCurrentLoopChansExist.restype = int32
DAQmxGetReadOpenCurrentLoopChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadOpenCurrentLoopChansExist.__doc__ = \
"""int32 DAQmxGetReadOpenCurrentLoopChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4343"""
DAQmxGetReadOpenCurrentLoopChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOpenCurrentLoopChans
DAQmxGetReadOpenCurrentLoopChans.restype = int32
DAQmxGetReadOpenCurrentLoopChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetReadOpenCurrentLoopChans.__doc__ = \
"""int32 DAQmxGetReadOpenCurrentLoopChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4345"""
DAQmxGetReadOpenThrmcplChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOpenThrmcplChansExist
DAQmxGetReadOpenThrmcplChansExist.restype = int32
DAQmxGetReadOpenThrmcplChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadOpenThrmcplChansExist.__doc__ = \
"""int32 DAQmxGetReadOpenThrmcplChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4347"""
DAQmxGetReadOpenThrmcplChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOpenThrmcplChans
DAQmxGetReadOpenThrmcplChans.restype = int32
DAQmxGetReadOpenThrmcplChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetReadOpenThrmcplChans.__doc__ = \
"""int32 DAQmxGetReadOpenThrmcplChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4349"""
DAQmxGetReadOverloadedChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOverloadedChansExist
DAQmxGetReadOverloadedChansExist.restype = int32
DAQmxGetReadOverloadedChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadOverloadedChansExist.__doc__ = \
"""int32 DAQmxGetReadOverloadedChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4351"""
DAQmxGetReadOverloadedChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadOverloadedChans
DAQmxGetReadOverloadedChans.restype = int32
DAQmxGetReadOverloadedChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetReadOverloadedChans.__doc__ = \
"""int32 DAQmxGetReadOverloadedChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4353"""
DAQmxGetReadChangeDetectHasOverflowed = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadChangeDetectHasOverflowed
DAQmxGetReadChangeDetectHasOverflowed.restype = int32
DAQmxGetReadChangeDetectHasOverflowed.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetReadChangeDetectHasOverflowed.__doc__ = \
"""int32 DAQmxGetReadChangeDetectHasOverflowed(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4355"""
DAQmxGetReadRawDataWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadRawDataWidth
DAQmxGetReadRawDataWidth.restype = int32
DAQmxGetReadRawDataWidth.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetReadRawDataWidth.__doc__ = \
"""int32 DAQmxGetReadRawDataWidth(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4357"""
DAQmxGetReadNumChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadNumChans
DAQmxGetReadNumChans.restype = int32
DAQmxGetReadNumChans.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetReadNumChans.__doc__ = \
"""int32 DAQmxGetReadNumChans(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4359"""
DAQmxGetReadDigitalLinesBytesPerChan = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadDigitalLinesBytesPerChan
DAQmxGetReadDigitalLinesBytesPerChan.restype = int32
DAQmxGetReadDigitalLinesBytesPerChan.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetReadDigitalLinesBytesPerChan.__doc__ = \
"""int32 DAQmxGetReadDigitalLinesBytesPerChan(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4361"""
DAQmxGetReadWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadWaitMode
DAQmxGetReadWaitMode.restype = int32
DAQmxGetReadWaitMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetReadWaitMode.__doc__ = \
"""int32 DAQmxGetReadWaitMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4364"""
DAQmxSetReadWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadWaitMode
DAQmxSetReadWaitMode.restype = int32
DAQmxSetReadWaitMode.argtypes = [TaskHandle, int32]
DAQmxSetReadWaitMode.__doc__ = \
"""int32 DAQmxSetReadWaitMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4365"""
DAQmxResetReadWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadWaitMode
DAQmxResetReadWaitMode.restype = int32
DAQmxResetReadWaitMode.argtypes = [TaskHandle]
DAQmxResetReadWaitMode.__doc__ = \
"""int32 DAQmxResetReadWaitMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4366"""
DAQmxGetReadSleepTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetReadSleepTime
DAQmxGetReadSleepTime.restype = int32
DAQmxGetReadSleepTime.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetReadSleepTime.__doc__ = \
"""int32 DAQmxGetReadSleepTime(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4368"""
DAQmxSetReadSleepTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetReadSleepTime
DAQmxSetReadSleepTime.restype = int32
DAQmxSetReadSleepTime.argtypes = [TaskHandle, float64]
DAQmxSetReadSleepTime.__doc__ = \
"""int32 DAQmxSetReadSleepTime(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4369"""
DAQmxResetReadSleepTime = _stdcall_libraries['nicaiu.dll'].DAQmxResetReadSleepTime
DAQmxResetReadSleepTime.restype = int32
DAQmxResetReadSleepTime.argtypes = [TaskHandle]
DAQmxResetReadSleepTime.__doc__ = \
"""int32 DAQmxResetReadSleepTime(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4370"""
DAQmxGetRealTimeConvLateErrorsToWarnings = _stdcall_libraries['nicaiu.dll'].DAQmxGetRealTimeConvLateErrorsToWarnings
DAQmxGetRealTimeConvLateErrorsToWarnings.restype = int32
DAQmxGetRealTimeConvLateErrorsToWarnings.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetRealTimeConvLateErrorsToWarnings.__doc__ = \
"""int32 DAQmxGetRealTimeConvLateErrorsToWarnings(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4374"""
DAQmxSetRealTimeConvLateErrorsToWarnings = _stdcall_libraries['nicaiu.dll'].DAQmxSetRealTimeConvLateErrorsToWarnings
DAQmxSetRealTimeConvLateErrorsToWarnings.restype = int32
DAQmxSetRealTimeConvLateErrorsToWarnings.argtypes = [TaskHandle, bool32]
DAQmxSetRealTimeConvLateErrorsToWarnings.__doc__ = \
"""int32 DAQmxSetRealTimeConvLateErrorsToWarnings(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4375"""
DAQmxResetRealTimeConvLateErrorsToWarnings = _stdcall_libraries['nicaiu.dll'].DAQmxResetRealTimeConvLateErrorsToWarnings
DAQmxResetRealTimeConvLateErrorsToWarnings.restype = int32
DAQmxResetRealTimeConvLateErrorsToWarnings.argtypes = [TaskHandle]
DAQmxResetRealTimeConvLateErrorsToWarnings.__doc__ = \
"""int32 DAQmxResetRealTimeConvLateErrorsToWarnings(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4376"""
DAQmxGetRealTimeNumOfWarmupIters = _stdcall_libraries['nicaiu.dll'].DAQmxGetRealTimeNumOfWarmupIters
DAQmxGetRealTimeNumOfWarmupIters.restype = int32
DAQmxGetRealTimeNumOfWarmupIters.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetRealTimeNumOfWarmupIters.__doc__ = \
"""int32 DAQmxGetRealTimeNumOfWarmupIters(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4378"""
DAQmxSetRealTimeNumOfWarmupIters = _stdcall_libraries['nicaiu.dll'].DAQmxSetRealTimeNumOfWarmupIters
DAQmxSetRealTimeNumOfWarmupIters.restype = int32
DAQmxSetRealTimeNumOfWarmupIters.argtypes = [TaskHandle, uInt32]
DAQmxSetRealTimeNumOfWarmupIters.__doc__ = \
"""int32 DAQmxSetRealTimeNumOfWarmupIters(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4379"""
DAQmxResetRealTimeNumOfWarmupIters = _stdcall_libraries['nicaiu.dll'].DAQmxResetRealTimeNumOfWarmupIters
DAQmxResetRealTimeNumOfWarmupIters.restype = int32
DAQmxResetRealTimeNumOfWarmupIters.argtypes = [TaskHandle]
DAQmxResetRealTimeNumOfWarmupIters.__doc__ = \
"""int32 DAQmxResetRealTimeNumOfWarmupIters(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4380"""
DAQmxGetRealTimeWaitForNextSampClkWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetRealTimeWaitForNextSampClkWaitMode
DAQmxGetRealTimeWaitForNextSampClkWaitMode.restype = int32
DAQmxGetRealTimeWaitForNextSampClkWaitMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetRealTimeWaitForNextSampClkWaitMode.__doc__ = \
"""int32 DAQmxGetRealTimeWaitForNextSampClkWaitMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4383"""
DAQmxSetRealTimeWaitForNextSampClkWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetRealTimeWaitForNextSampClkWaitMode
DAQmxSetRealTimeWaitForNextSampClkWaitMode.restype = int32
DAQmxSetRealTimeWaitForNextSampClkWaitMode.argtypes = [TaskHandle, int32]
DAQmxSetRealTimeWaitForNextSampClkWaitMode.__doc__ = \
"""int32 DAQmxSetRealTimeWaitForNextSampClkWaitMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4384"""
DAQmxResetRealTimeWaitForNextSampClkWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetRealTimeWaitForNextSampClkWaitMode
DAQmxResetRealTimeWaitForNextSampClkWaitMode.restype = int32
DAQmxResetRealTimeWaitForNextSampClkWaitMode.argtypes = [TaskHandle]
DAQmxResetRealTimeWaitForNextSampClkWaitMode.__doc__ = \
"""int32 DAQmxResetRealTimeWaitForNextSampClkWaitMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4385"""
DAQmxGetRealTimeReportMissedSamp = _stdcall_libraries['nicaiu.dll'].DAQmxGetRealTimeReportMissedSamp
DAQmxGetRealTimeReportMissedSamp.restype = int32
DAQmxGetRealTimeReportMissedSamp.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetRealTimeReportMissedSamp.__doc__ = \
"""int32 DAQmxGetRealTimeReportMissedSamp(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4387"""
DAQmxSetRealTimeReportMissedSamp = _stdcall_libraries['nicaiu.dll'].DAQmxSetRealTimeReportMissedSamp
DAQmxSetRealTimeReportMissedSamp.restype = int32
DAQmxSetRealTimeReportMissedSamp.argtypes = [TaskHandle, bool32]
DAQmxSetRealTimeReportMissedSamp.__doc__ = \
"""int32 DAQmxSetRealTimeReportMissedSamp(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4388"""
DAQmxResetRealTimeReportMissedSamp = _stdcall_libraries['nicaiu.dll'].DAQmxResetRealTimeReportMissedSamp
DAQmxResetRealTimeReportMissedSamp.restype = int32
DAQmxResetRealTimeReportMissedSamp.argtypes = [TaskHandle]
DAQmxResetRealTimeReportMissedSamp.__doc__ = \
"""int32 DAQmxResetRealTimeReportMissedSamp(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4389"""
DAQmxGetRealTimeWriteRecoveryMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetRealTimeWriteRecoveryMode
DAQmxGetRealTimeWriteRecoveryMode.restype = int32
DAQmxGetRealTimeWriteRecoveryMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetRealTimeWriteRecoveryMode.__doc__ = \
"""int32 DAQmxGetRealTimeWriteRecoveryMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4392"""
DAQmxSetRealTimeWriteRecoveryMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetRealTimeWriteRecoveryMode
DAQmxSetRealTimeWriteRecoveryMode.restype = int32
DAQmxSetRealTimeWriteRecoveryMode.argtypes = [TaskHandle, int32]
DAQmxSetRealTimeWriteRecoveryMode.__doc__ = \
"""int32 DAQmxSetRealTimeWriteRecoveryMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4393"""
DAQmxResetRealTimeWriteRecoveryMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetRealTimeWriteRecoveryMode
DAQmxResetRealTimeWriteRecoveryMode.restype = int32
DAQmxResetRealTimeWriteRecoveryMode.argtypes = [TaskHandle]
DAQmxResetRealTimeWriteRecoveryMode.__doc__ = \
"""int32 DAQmxResetRealTimeWriteRecoveryMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4394"""
DAQmxGetSwitchChanUsage = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanUsage
DAQmxGetSwitchChanUsage.restype = int32
DAQmxGetSwitchChanUsage.argtypes = [STRING, POINTER(int32)]
DAQmxGetSwitchChanUsage.__doc__ = \
"""int32 DAQmxGetSwitchChanUsage(unknown * switchChannelName, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4399"""
DAQmxSetSwitchChanUsage = _stdcall_libraries['nicaiu.dll'].DAQmxSetSwitchChanUsage
DAQmxSetSwitchChanUsage.restype = int32
DAQmxSetSwitchChanUsage.argtypes = [STRING, int32]
DAQmxSetSwitchChanUsage.__doc__ = \
"""int32 DAQmxSetSwitchChanUsage(unknown * switchChannelName, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4400"""
DAQmxGetSwitchChanMaxACCarryCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxACCarryCurrent
DAQmxGetSwitchChanMaxACCarryCurrent.restype = int32
DAQmxGetSwitchChanMaxACCarryCurrent.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxACCarryCurrent.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxACCarryCurrent(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4402"""
DAQmxGetSwitchChanMaxACSwitchCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxACSwitchCurrent
DAQmxGetSwitchChanMaxACSwitchCurrent.restype = int32
DAQmxGetSwitchChanMaxACSwitchCurrent.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxACSwitchCurrent.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxACSwitchCurrent(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4404"""
DAQmxGetSwitchChanMaxACCarryPwr = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxACCarryPwr
DAQmxGetSwitchChanMaxACCarryPwr.restype = int32
DAQmxGetSwitchChanMaxACCarryPwr.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxACCarryPwr.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxACCarryPwr(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4406"""
DAQmxGetSwitchChanMaxACSwitchPwr = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxACSwitchPwr
DAQmxGetSwitchChanMaxACSwitchPwr.restype = int32
DAQmxGetSwitchChanMaxACSwitchPwr.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxACSwitchPwr.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxACSwitchPwr(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4408"""
DAQmxGetSwitchChanMaxDCCarryCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxDCCarryCurrent
DAQmxGetSwitchChanMaxDCCarryCurrent.restype = int32
DAQmxGetSwitchChanMaxDCCarryCurrent.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxDCCarryCurrent.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxDCCarryCurrent(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4410"""
DAQmxGetSwitchChanMaxDCSwitchCurrent = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxDCSwitchCurrent
DAQmxGetSwitchChanMaxDCSwitchCurrent.restype = int32
DAQmxGetSwitchChanMaxDCSwitchCurrent.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxDCSwitchCurrent.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxDCSwitchCurrent(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4412"""
DAQmxGetSwitchChanMaxDCCarryPwr = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxDCCarryPwr
DAQmxGetSwitchChanMaxDCCarryPwr.restype = int32
DAQmxGetSwitchChanMaxDCCarryPwr.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxDCCarryPwr.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxDCCarryPwr(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4414"""
DAQmxGetSwitchChanMaxDCSwitchPwr = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxDCSwitchPwr
DAQmxGetSwitchChanMaxDCSwitchPwr.restype = int32
DAQmxGetSwitchChanMaxDCSwitchPwr.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxDCSwitchPwr.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxDCSwitchPwr(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4416"""
DAQmxGetSwitchChanMaxACVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxACVoltage
DAQmxGetSwitchChanMaxACVoltage.restype = int32
DAQmxGetSwitchChanMaxACVoltage.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxACVoltage.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxACVoltage(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4418"""
DAQmxGetSwitchChanMaxDCVoltage = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanMaxDCVoltage
DAQmxGetSwitchChanMaxDCVoltage.restype = int32
DAQmxGetSwitchChanMaxDCVoltage.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanMaxDCVoltage.__doc__ = \
"""int32 DAQmxGetSwitchChanMaxDCVoltage(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4420"""
DAQmxGetSwitchChanWireMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanWireMode
DAQmxGetSwitchChanWireMode.restype = int32
DAQmxGetSwitchChanWireMode.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetSwitchChanWireMode.__doc__ = \
"""int32 DAQmxGetSwitchChanWireMode(unknown * switchChannelName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4422"""
DAQmxGetSwitchChanBandwidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanBandwidth
DAQmxGetSwitchChanBandwidth.restype = int32
DAQmxGetSwitchChanBandwidth.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanBandwidth.__doc__ = \
"""int32 DAQmxGetSwitchChanBandwidth(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4424"""
DAQmxGetSwitchChanImpedance = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchChanImpedance
DAQmxGetSwitchChanImpedance.restype = int32
DAQmxGetSwitchChanImpedance.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchChanImpedance.__doc__ = \
"""int32 DAQmxGetSwitchChanImpedance(unknown * switchChannelName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4426"""
DAQmxGetSwitchDevSettlingTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevSettlingTime
DAQmxGetSwitchDevSettlingTime.restype = int32
DAQmxGetSwitchDevSettlingTime.argtypes = [STRING, POINTER(float64)]
DAQmxGetSwitchDevSettlingTime.__doc__ = \
"""int32 DAQmxGetSwitchDevSettlingTime(unknown * deviceName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4430"""
DAQmxSetSwitchDevSettlingTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetSwitchDevSettlingTime
DAQmxSetSwitchDevSettlingTime.restype = int32
DAQmxSetSwitchDevSettlingTime.argtypes = [STRING, float64]
DAQmxSetSwitchDevSettlingTime.__doc__ = \
"""int32 DAQmxSetSwitchDevSettlingTime(unknown * deviceName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4431"""
DAQmxGetSwitchDevAutoConnAnlgBus = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevAutoConnAnlgBus
DAQmxGetSwitchDevAutoConnAnlgBus.restype = int32
DAQmxGetSwitchDevAutoConnAnlgBus.argtypes = [STRING, POINTER(bool32)]
DAQmxGetSwitchDevAutoConnAnlgBus.__doc__ = \
"""int32 DAQmxGetSwitchDevAutoConnAnlgBus(unknown * deviceName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4433"""
DAQmxSetSwitchDevAutoConnAnlgBus = _stdcall_libraries['nicaiu.dll'].DAQmxSetSwitchDevAutoConnAnlgBus
DAQmxSetSwitchDevAutoConnAnlgBus.restype = int32
DAQmxSetSwitchDevAutoConnAnlgBus.argtypes = [STRING, bool32]
DAQmxSetSwitchDevAutoConnAnlgBus.__doc__ = \
"""int32 DAQmxSetSwitchDevAutoConnAnlgBus(unknown * deviceName, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4434"""
DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling
DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling.restype = int32
DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling.argtypes = [STRING, POINTER(bool32)]
DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling.__doc__ = \
"""int32 DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling(unknown * deviceName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4436"""
DAQmxSetSwitchDevPwrDownLatchRelaysAfterSettling = _stdcall_libraries['nicaiu.dll'].DAQmxSetSwitchDevPwrDownLatchRelaysAfterSettling
DAQmxSetSwitchDevPwrDownLatchRelaysAfterSettling.restype = int32
DAQmxSetSwitchDevPwrDownLatchRelaysAfterSettling.argtypes = [STRING, bool32]
DAQmxSetSwitchDevPwrDownLatchRelaysAfterSettling.__doc__ = \
"""int32 DAQmxSetSwitchDevPwrDownLatchRelaysAfterSettling(unknown * deviceName, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4437"""
DAQmxGetSwitchDevSettled = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevSettled
DAQmxGetSwitchDevSettled.restype = int32
DAQmxGetSwitchDevSettled.argtypes = [STRING, POINTER(bool32)]
DAQmxGetSwitchDevSettled.__doc__ = \
"""int32 DAQmxGetSwitchDevSettled(unknown * deviceName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4439"""
DAQmxGetSwitchDevRelayList = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevRelayList
DAQmxGetSwitchDevRelayList.restype = int32
DAQmxGetSwitchDevRelayList.argtypes = [STRING, STRING, uInt32]
DAQmxGetSwitchDevRelayList.__doc__ = \
"""int32 DAQmxGetSwitchDevRelayList(unknown * deviceName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4441"""
DAQmxGetSwitchDevNumRelays = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevNumRelays
DAQmxGetSwitchDevNumRelays.restype = int32
DAQmxGetSwitchDevNumRelays.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetSwitchDevNumRelays.__doc__ = \
"""int32 DAQmxGetSwitchDevNumRelays(unknown * deviceName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4443"""
DAQmxGetSwitchDevSwitchChanList = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevSwitchChanList
DAQmxGetSwitchDevSwitchChanList.restype = int32
DAQmxGetSwitchDevSwitchChanList.argtypes = [STRING, STRING, uInt32]
DAQmxGetSwitchDevSwitchChanList.__doc__ = \
"""int32 DAQmxGetSwitchDevSwitchChanList(unknown * deviceName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4445"""
DAQmxGetSwitchDevNumSwitchChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevNumSwitchChans
DAQmxGetSwitchDevNumSwitchChans.restype = int32
DAQmxGetSwitchDevNumSwitchChans.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetSwitchDevNumSwitchChans.__doc__ = \
"""int32 DAQmxGetSwitchDevNumSwitchChans(unknown * deviceName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4447"""
DAQmxGetSwitchDevNumRows = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevNumRows
DAQmxGetSwitchDevNumRows.restype = int32
DAQmxGetSwitchDevNumRows.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetSwitchDevNumRows.__doc__ = \
"""int32 DAQmxGetSwitchDevNumRows(unknown * deviceName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4449"""
DAQmxGetSwitchDevNumColumns = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevNumColumns
DAQmxGetSwitchDevNumColumns.restype = int32
DAQmxGetSwitchDevNumColumns.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetSwitchDevNumColumns.__doc__ = \
"""int32 DAQmxGetSwitchDevNumColumns(unknown * deviceName, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4451"""
DAQmxGetSwitchDevTopology = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchDevTopology
DAQmxGetSwitchDevTopology.restype = int32
DAQmxGetSwitchDevTopology.argtypes = [STRING, STRING, uInt32]
DAQmxGetSwitchDevTopology.__doc__ = \
"""int32 DAQmxGetSwitchDevTopology(unknown * deviceName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4453"""
DAQmxGetSwitchScanBreakMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchScanBreakMode
DAQmxGetSwitchScanBreakMode.restype = int32
DAQmxGetSwitchScanBreakMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSwitchScanBreakMode.__doc__ = \
"""int32 DAQmxGetSwitchScanBreakMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4458"""
DAQmxSetSwitchScanBreakMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetSwitchScanBreakMode
DAQmxSetSwitchScanBreakMode.restype = int32
DAQmxSetSwitchScanBreakMode.argtypes = [TaskHandle, int32]
DAQmxSetSwitchScanBreakMode.__doc__ = \
"""int32 DAQmxSetSwitchScanBreakMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4459"""
DAQmxResetSwitchScanBreakMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetSwitchScanBreakMode
DAQmxResetSwitchScanBreakMode.restype = int32
DAQmxResetSwitchScanBreakMode.argtypes = [TaskHandle]
DAQmxResetSwitchScanBreakMode.__doc__ = \
"""int32 DAQmxResetSwitchScanBreakMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4460"""
DAQmxGetSwitchScanRepeatMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchScanRepeatMode
DAQmxGetSwitchScanRepeatMode.restype = int32
DAQmxGetSwitchScanRepeatMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSwitchScanRepeatMode.__doc__ = \
"""int32 DAQmxGetSwitchScanRepeatMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4463"""
DAQmxSetSwitchScanRepeatMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetSwitchScanRepeatMode
DAQmxSetSwitchScanRepeatMode.restype = int32
DAQmxSetSwitchScanRepeatMode.argtypes = [TaskHandle, int32]
DAQmxSetSwitchScanRepeatMode.__doc__ = \
"""int32 DAQmxSetSwitchScanRepeatMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4464"""
DAQmxResetSwitchScanRepeatMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetSwitchScanRepeatMode
DAQmxResetSwitchScanRepeatMode.restype = int32
DAQmxResetSwitchScanRepeatMode.argtypes = [TaskHandle]
DAQmxResetSwitchScanRepeatMode.__doc__ = \
"""int32 DAQmxResetSwitchScanRepeatMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4465"""
DAQmxGetSwitchScanWaitingForAdv = _stdcall_libraries['nicaiu.dll'].DAQmxGetSwitchScanWaitingForAdv
DAQmxGetSwitchScanWaitingForAdv.restype = int32
DAQmxGetSwitchScanWaitingForAdv.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetSwitchScanWaitingForAdv.__doc__ = \
"""int32 DAQmxGetSwitchScanWaitingForAdv(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4467"""
DAQmxGetScaleDescr = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleDescr
DAQmxGetScaleDescr.restype = int32
DAQmxGetScaleDescr.argtypes = [STRING, STRING, uInt32]
DAQmxGetScaleDescr.__doc__ = \
"""int32 DAQmxGetScaleDescr(unknown * scaleName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4471"""
DAQmxSetScaleDescr = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleDescr
DAQmxSetScaleDescr.restype = int32
DAQmxSetScaleDescr.argtypes = [STRING, STRING]
DAQmxSetScaleDescr.__doc__ = \
"""int32 DAQmxSetScaleDescr(unknown * scaleName, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4472"""
DAQmxGetScaleScaledUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleScaledUnits
DAQmxGetScaleScaledUnits.restype = int32
DAQmxGetScaleScaledUnits.argtypes = [STRING, STRING, uInt32]
DAQmxGetScaleScaledUnits.__doc__ = \
"""int32 DAQmxGetScaleScaledUnits(unknown * scaleName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4474"""
DAQmxSetScaleScaledUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleScaledUnits
DAQmxSetScaleScaledUnits.restype = int32
DAQmxSetScaleScaledUnits.argtypes = [STRING, STRING]
DAQmxSetScaleScaledUnits.__doc__ = \
"""int32 DAQmxSetScaleScaledUnits(unknown * scaleName, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4475"""
DAQmxGetScalePreScaledUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetScalePreScaledUnits
DAQmxGetScalePreScaledUnits.restype = int32
DAQmxGetScalePreScaledUnits.argtypes = [STRING, POINTER(int32)]
DAQmxGetScalePreScaledUnits.__doc__ = \
"""int32 DAQmxGetScalePreScaledUnits(unknown * scaleName, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4478"""
DAQmxSetScalePreScaledUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetScalePreScaledUnits
DAQmxSetScalePreScaledUnits.restype = int32
DAQmxSetScalePreScaledUnits.argtypes = [STRING, int32]
DAQmxSetScalePreScaledUnits.__doc__ = \
"""int32 DAQmxSetScalePreScaledUnits(unknown * scaleName, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4479"""
DAQmxGetScaleType = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleType
DAQmxGetScaleType.restype = int32
DAQmxGetScaleType.argtypes = [STRING, POINTER(int32)]
DAQmxGetScaleType.__doc__ = \
"""int32 DAQmxGetScaleType(unknown * scaleName, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4482"""
DAQmxGetScaleLinSlope = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleLinSlope
DAQmxGetScaleLinSlope.restype = int32
DAQmxGetScaleLinSlope.argtypes = [STRING, POINTER(float64)]
DAQmxGetScaleLinSlope.__doc__ = \
"""int32 DAQmxGetScaleLinSlope(unknown * scaleName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4484"""
DAQmxSetScaleLinSlope = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleLinSlope
DAQmxSetScaleLinSlope.restype = int32
DAQmxSetScaleLinSlope.argtypes = [STRING, float64]
DAQmxSetScaleLinSlope.__doc__ = \
"""int32 DAQmxSetScaleLinSlope(unknown * scaleName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4485"""
DAQmxGetScaleLinYIntercept = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleLinYIntercept
DAQmxGetScaleLinYIntercept.restype = int32
DAQmxGetScaleLinYIntercept.argtypes = [STRING, POINTER(float64)]
DAQmxGetScaleLinYIntercept.__doc__ = \
"""int32 DAQmxGetScaleLinYIntercept(unknown * scaleName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4487"""
DAQmxSetScaleLinYIntercept = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleLinYIntercept
DAQmxSetScaleLinYIntercept.restype = int32
DAQmxSetScaleLinYIntercept.argtypes = [STRING, float64]
DAQmxSetScaleLinYIntercept.__doc__ = \
"""int32 DAQmxSetScaleLinYIntercept(unknown * scaleName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4488"""
DAQmxGetScaleMapScaledMax = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleMapScaledMax
DAQmxGetScaleMapScaledMax.restype = int32
DAQmxGetScaleMapScaledMax.argtypes = [STRING, POINTER(float64)]
DAQmxGetScaleMapScaledMax.__doc__ = \
"""int32 DAQmxGetScaleMapScaledMax(unknown * scaleName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4490"""
DAQmxSetScaleMapScaledMax = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleMapScaledMax
DAQmxSetScaleMapScaledMax.restype = int32
DAQmxSetScaleMapScaledMax.argtypes = [STRING, float64]
DAQmxSetScaleMapScaledMax.__doc__ = \
"""int32 DAQmxSetScaleMapScaledMax(unknown * scaleName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4491"""
DAQmxGetScaleMapPreScaledMax = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleMapPreScaledMax
DAQmxGetScaleMapPreScaledMax.restype = int32
DAQmxGetScaleMapPreScaledMax.argtypes = [STRING, POINTER(float64)]
DAQmxGetScaleMapPreScaledMax.__doc__ = \
"""int32 DAQmxGetScaleMapPreScaledMax(unknown * scaleName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4493"""
DAQmxSetScaleMapPreScaledMax = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleMapPreScaledMax
DAQmxSetScaleMapPreScaledMax.restype = int32
DAQmxSetScaleMapPreScaledMax.argtypes = [STRING, float64]
DAQmxSetScaleMapPreScaledMax.__doc__ = \
"""int32 DAQmxSetScaleMapPreScaledMax(unknown * scaleName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4494"""
DAQmxGetScaleMapScaledMin = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleMapScaledMin
DAQmxGetScaleMapScaledMin.restype = int32
DAQmxGetScaleMapScaledMin.argtypes = [STRING, POINTER(float64)]
DAQmxGetScaleMapScaledMin.__doc__ = \
"""int32 DAQmxGetScaleMapScaledMin(unknown * scaleName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4496"""
DAQmxSetScaleMapScaledMin = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleMapScaledMin
DAQmxSetScaleMapScaledMin.restype = int32
DAQmxSetScaleMapScaledMin.argtypes = [STRING, float64]
DAQmxSetScaleMapScaledMin.__doc__ = \
"""int32 DAQmxSetScaleMapScaledMin(unknown * scaleName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4497"""
DAQmxGetScaleMapPreScaledMin = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleMapPreScaledMin
DAQmxGetScaleMapPreScaledMin.restype = int32
DAQmxGetScaleMapPreScaledMin.argtypes = [STRING, POINTER(float64)]
DAQmxGetScaleMapPreScaledMin.__doc__ = \
"""int32 DAQmxGetScaleMapPreScaledMin(unknown * scaleName, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4499"""
DAQmxSetScaleMapPreScaledMin = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleMapPreScaledMin
DAQmxSetScaleMapPreScaledMin.restype = int32
DAQmxSetScaleMapPreScaledMin.argtypes = [STRING, float64]
DAQmxSetScaleMapPreScaledMin.__doc__ = \
"""int32 DAQmxSetScaleMapPreScaledMin(unknown * scaleName, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4500"""
DAQmxGetScalePolyForwardCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxGetScalePolyForwardCoeff
DAQmxGetScalePolyForwardCoeff.restype = int32
DAQmxGetScalePolyForwardCoeff.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetScalePolyForwardCoeff.__doc__ = \
"""int32 DAQmxGetScalePolyForwardCoeff(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4502"""
DAQmxSetScalePolyForwardCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxSetScalePolyForwardCoeff
DAQmxSetScalePolyForwardCoeff.restype = int32
DAQmxSetScalePolyForwardCoeff.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxSetScalePolyForwardCoeff.__doc__ = \
"""int32 DAQmxSetScalePolyForwardCoeff(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4503"""
DAQmxGetScalePolyReverseCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxGetScalePolyReverseCoeff
DAQmxGetScalePolyReverseCoeff.restype = int32
DAQmxGetScalePolyReverseCoeff.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetScalePolyReverseCoeff.__doc__ = \
"""int32 DAQmxGetScalePolyReverseCoeff(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4505"""
DAQmxSetScalePolyReverseCoeff = _stdcall_libraries['nicaiu.dll'].DAQmxSetScalePolyReverseCoeff
DAQmxSetScalePolyReverseCoeff.restype = int32
DAQmxSetScalePolyReverseCoeff.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxSetScalePolyReverseCoeff.__doc__ = \
"""int32 DAQmxSetScalePolyReverseCoeff(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4506"""
DAQmxGetScaleTableScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleTableScaledVals
DAQmxGetScaleTableScaledVals.restype = int32
DAQmxGetScaleTableScaledVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetScaleTableScaledVals.__doc__ = \
"""int32 DAQmxGetScaleTableScaledVals(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4508"""
DAQmxSetScaleTableScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleTableScaledVals
DAQmxSetScaleTableScaledVals.restype = int32
DAQmxSetScaleTableScaledVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxSetScaleTableScaledVals.__doc__ = \
"""int32 DAQmxSetScaleTableScaledVals(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4509"""
DAQmxGetScaleTablePreScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxGetScaleTablePreScaledVals
DAQmxGetScaleTablePreScaledVals.restype = int32
DAQmxGetScaleTablePreScaledVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxGetScaleTablePreScaledVals.__doc__ = \
"""int32 DAQmxGetScaleTablePreScaledVals(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4511"""
DAQmxSetScaleTablePreScaledVals = _stdcall_libraries['nicaiu.dll'].DAQmxSetScaleTablePreScaledVals
DAQmxSetScaleTablePreScaledVals.restype = int32
DAQmxSetScaleTablePreScaledVals.argtypes = [STRING, POINTER(float64), uInt32]
DAQmxSetScaleTablePreScaledVals.__doc__ = \
"""int32 DAQmxSetScaleTablePreScaledVals(unknown * scaleName, float64 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4512"""
DAQmxGetSysGlobalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetSysGlobalChans
DAQmxGetSysGlobalChans.restype = int32
DAQmxGetSysGlobalChans.argtypes = [STRING, uInt32]
DAQmxGetSysGlobalChans.__doc__ = \
"""int32 DAQmxGetSysGlobalChans(char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4516"""
DAQmxGetSysScales = _stdcall_libraries['nicaiu.dll'].DAQmxGetSysScales
DAQmxGetSysScales.restype = int32
DAQmxGetSysScales.argtypes = [STRING, uInt32]
DAQmxGetSysScales.__doc__ = \
"""int32 DAQmxGetSysScales(char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4518"""
DAQmxGetSysTasks = _stdcall_libraries['nicaiu.dll'].DAQmxGetSysTasks
DAQmxGetSysTasks.restype = int32
DAQmxGetSysTasks.argtypes = [STRING, uInt32]
DAQmxGetSysTasks.__doc__ = \
"""int32 DAQmxGetSysTasks(char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4520"""
DAQmxGetSysDevNames = _stdcall_libraries['nicaiu.dll'].DAQmxGetSysDevNames
DAQmxGetSysDevNames.restype = int32
DAQmxGetSysDevNames.argtypes = [STRING, uInt32]
DAQmxGetSysDevNames.__doc__ = \
"""int32 DAQmxGetSysDevNames(char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4522"""
DAQmxGetSysNIDAQMajorVersion = _stdcall_libraries['nicaiu.dll'].DAQmxGetSysNIDAQMajorVersion
DAQmxGetSysNIDAQMajorVersion.restype = int32
DAQmxGetSysNIDAQMajorVersion.argtypes = [POINTER(uInt32)]
DAQmxGetSysNIDAQMajorVersion.__doc__ = \
"""int32 DAQmxGetSysNIDAQMajorVersion(uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4524"""
DAQmxGetSysNIDAQMinorVersion = _stdcall_libraries['nicaiu.dll'].DAQmxGetSysNIDAQMinorVersion
DAQmxGetSysNIDAQMinorVersion.restype = int32
DAQmxGetSysNIDAQMinorVersion.argtypes = [POINTER(uInt32)]
DAQmxGetSysNIDAQMinorVersion.__doc__ = \
"""int32 DAQmxGetSysNIDAQMinorVersion(uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4526"""
DAQmxGetTaskName = _stdcall_libraries['nicaiu.dll'].DAQmxGetTaskName
DAQmxGetTaskName.restype = int32
DAQmxGetTaskName.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetTaskName.__doc__ = \
"""int32 DAQmxGetTaskName(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4530"""
DAQmxGetTaskChannels = _stdcall_libraries['nicaiu.dll'].DAQmxGetTaskChannels
DAQmxGetTaskChannels.restype = int32
DAQmxGetTaskChannels.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetTaskChannels.__doc__ = \
"""int32 DAQmxGetTaskChannels(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4532"""
DAQmxGetTaskNumChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetTaskNumChans
DAQmxGetTaskNumChans.restype = int32
DAQmxGetTaskNumChans.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetTaskNumChans.__doc__ = \
"""int32 DAQmxGetTaskNumChans(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4534"""
DAQmxGetTaskDevices = _stdcall_libraries['nicaiu.dll'].DAQmxGetTaskDevices
DAQmxGetTaskDevices.restype = int32
DAQmxGetTaskDevices.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetTaskDevices.__doc__ = \
"""int32 DAQmxGetTaskDevices(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4536"""
DAQmxGetTaskNumDevices = _stdcall_libraries['nicaiu.dll'].DAQmxGetTaskNumDevices
DAQmxGetTaskNumDevices.restype = int32
DAQmxGetTaskNumDevices.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetTaskNumDevices.__doc__ = \
"""int32 DAQmxGetTaskNumDevices(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4538"""
DAQmxGetTaskComplete = _stdcall_libraries['nicaiu.dll'].DAQmxGetTaskComplete
DAQmxGetTaskComplete.restype = int32
DAQmxGetTaskComplete.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetTaskComplete.__doc__ = \
"""int32 DAQmxGetTaskComplete(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4540"""
DAQmxGetSampQuantSampMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampQuantSampMode
DAQmxGetSampQuantSampMode.restype = int32
DAQmxGetSampQuantSampMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSampQuantSampMode.__doc__ = \
"""int32 DAQmxGetSampQuantSampMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4545"""
DAQmxSetSampQuantSampMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampQuantSampMode
DAQmxSetSampQuantSampMode.restype = int32
DAQmxSetSampQuantSampMode.argtypes = [TaskHandle, int32]
DAQmxSetSampQuantSampMode.__doc__ = \
"""int32 DAQmxSetSampQuantSampMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4546"""
DAQmxResetSampQuantSampMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampQuantSampMode
DAQmxResetSampQuantSampMode.restype = int32
DAQmxResetSampQuantSampMode.argtypes = [TaskHandle]
DAQmxResetSampQuantSampMode.__doc__ = \
"""int32 DAQmxResetSampQuantSampMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4547"""
DAQmxGetSampQuantSampPerChan = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampQuantSampPerChan
DAQmxGetSampQuantSampPerChan.restype = int32
DAQmxGetSampQuantSampPerChan.argtypes = [TaskHandle, POINTER(uInt64)]
DAQmxGetSampQuantSampPerChan.__doc__ = \
"""int32 DAQmxGetSampQuantSampPerChan(TaskHandle taskHandle, uInt64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4549"""
DAQmxSetSampQuantSampPerChan = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampQuantSampPerChan
DAQmxSetSampQuantSampPerChan.restype = int32
DAQmxSetSampQuantSampPerChan.argtypes = [TaskHandle, uInt64]
DAQmxSetSampQuantSampPerChan.__doc__ = \
"""int32 DAQmxSetSampQuantSampPerChan(TaskHandle taskHandle, uInt64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4550"""
DAQmxResetSampQuantSampPerChan = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampQuantSampPerChan
DAQmxResetSampQuantSampPerChan.restype = int32
DAQmxResetSampQuantSampPerChan.argtypes = [TaskHandle]
DAQmxResetSampQuantSampPerChan.__doc__ = \
"""int32 DAQmxResetSampQuantSampPerChan(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4551"""
DAQmxGetSampTimingType = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampTimingType
DAQmxGetSampTimingType.restype = int32
DAQmxGetSampTimingType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSampTimingType.__doc__ = \
"""int32 DAQmxGetSampTimingType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4554"""
DAQmxSetSampTimingType = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampTimingType
DAQmxSetSampTimingType.restype = int32
DAQmxSetSampTimingType.argtypes = [TaskHandle, int32]
DAQmxSetSampTimingType.__doc__ = \
"""int32 DAQmxSetSampTimingType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4555"""
DAQmxResetSampTimingType = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampTimingType
DAQmxResetSampTimingType.restype = int32
DAQmxResetSampTimingType.argtypes = [TaskHandle]
DAQmxResetSampTimingType.__doc__ = \
"""int32 DAQmxResetSampTimingType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4556"""
DAQmxGetSampClkRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkRate
DAQmxGetSampClkRate.restype = int32
DAQmxGetSampClkRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSampClkRate.__doc__ = \
"""int32 DAQmxGetSampClkRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4558"""
DAQmxSetSampClkRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkRate
DAQmxSetSampClkRate.restype = int32
DAQmxSetSampClkRate.argtypes = [TaskHandle, float64]
DAQmxSetSampClkRate.__doc__ = \
"""int32 DAQmxSetSampClkRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4559"""
DAQmxResetSampClkRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkRate
DAQmxResetSampClkRate.restype = int32
DAQmxResetSampClkRate.argtypes = [TaskHandle]
DAQmxResetSampClkRate.__doc__ = \
"""int32 DAQmxResetSampClkRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4560"""
DAQmxGetSampClkMaxRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkMaxRate
DAQmxGetSampClkMaxRate.restype = int32
DAQmxGetSampClkMaxRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSampClkMaxRate.__doc__ = \
"""int32 DAQmxGetSampClkMaxRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4562"""
DAQmxGetSampClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkSrc
DAQmxGetSampClkSrc.restype = int32
DAQmxGetSampClkSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetSampClkSrc.__doc__ = \
"""int32 DAQmxGetSampClkSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4564"""
DAQmxSetSampClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkSrc
DAQmxSetSampClkSrc.restype = int32
DAQmxSetSampClkSrc.argtypes = [TaskHandle, STRING]
DAQmxSetSampClkSrc.__doc__ = \
"""int32 DAQmxSetSampClkSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4565"""
DAQmxResetSampClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkSrc
DAQmxResetSampClkSrc.restype = int32
DAQmxResetSampClkSrc.argtypes = [TaskHandle]
DAQmxResetSampClkSrc.__doc__ = \
"""int32 DAQmxResetSampClkSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4566"""
DAQmxGetSampClkActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkActiveEdge
DAQmxGetSampClkActiveEdge.restype = int32
DAQmxGetSampClkActiveEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSampClkActiveEdge.__doc__ = \
"""int32 DAQmxGetSampClkActiveEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4569"""
DAQmxSetSampClkActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkActiveEdge
DAQmxSetSampClkActiveEdge.restype = int32
DAQmxSetSampClkActiveEdge.argtypes = [TaskHandle, int32]
DAQmxSetSampClkActiveEdge.__doc__ = \
"""int32 DAQmxSetSampClkActiveEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4570"""
DAQmxResetSampClkActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkActiveEdge
DAQmxResetSampClkActiveEdge.restype = int32
DAQmxResetSampClkActiveEdge.argtypes = [TaskHandle]
DAQmxResetSampClkActiveEdge.__doc__ = \
"""int32 DAQmxResetSampClkActiveEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4571"""
DAQmxGetSampClkUnderflowBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkUnderflowBehavior
DAQmxGetSampClkUnderflowBehavior.restype = int32
DAQmxGetSampClkUnderflowBehavior.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSampClkUnderflowBehavior.__doc__ = \
"""int32 DAQmxGetSampClkUnderflowBehavior(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4574"""
DAQmxSetSampClkUnderflowBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkUnderflowBehavior
DAQmxSetSampClkUnderflowBehavior.restype = int32
DAQmxSetSampClkUnderflowBehavior.argtypes = [TaskHandle, int32]
DAQmxSetSampClkUnderflowBehavior.__doc__ = \
"""int32 DAQmxSetSampClkUnderflowBehavior(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4575"""
DAQmxResetSampClkUnderflowBehavior = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkUnderflowBehavior
DAQmxResetSampClkUnderflowBehavior.restype = int32
DAQmxResetSampClkUnderflowBehavior.argtypes = [TaskHandle]
DAQmxResetSampClkUnderflowBehavior.__doc__ = \
"""int32 DAQmxResetSampClkUnderflowBehavior(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4576"""
DAQmxGetSampClkTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkTimebaseDiv
DAQmxGetSampClkTimebaseDiv.restype = int32
DAQmxGetSampClkTimebaseDiv.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetSampClkTimebaseDiv.__doc__ = \
"""int32 DAQmxGetSampClkTimebaseDiv(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4578"""
DAQmxSetSampClkTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkTimebaseDiv
DAQmxSetSampClkTimebaseDiv.restype = int32
DAQmxSetSampClkTimebaseDiv.argtypes = [TaskHandle, uInt32]
DAQmxSetSampClkTimebaseDiv.__doc__ = \
"""int32 DAQmxSetSampClkTimebaseDiv(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4579"""
DAQmxResetSampClkTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkTimebaseDiv
DAQmxResetSampClkTimebaseDiv.restype = int32
DAQmxResetSampClkTimebaseDiv.argtypes = [TaskHandle]
DAQmxResetSampClkTimebaseDiv.__doc__ = \
"""int32 DAQmxResetSampClkTimebaseDiv(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4580"""
DAQmxGetSampClkTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkTimebaseRate
DAQmxGetSampClkTimebaseRate.restype = int32
DAQmxGetSampClkTimebaseRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSampClkTimebaseRate.__doc__ = \
"""int32 DAQmxGetSampClkTimebaseRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4582"""
DAQmxSetSampClkTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkTimebaseRate
DAQmxSetSampClkTimebaseRate.restype = int32
DAQmxSetSampClkTimebaseRate.argtypes = [TaskHandle, float64]
DAQmxSetSampClkTimebaseRate.__doc__ = \
"""int32 DAQmxSetSampClkTimebaseRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4583"""
DAQmxResetSampClkTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkTimebaseRate
DAQmxResetSampClkTimebaseRate.restype = int32
DAQmxResetSampClkTimebaseRate.argtypes = [TaskHandle]
DAQmxResetSampClkTimebaseRate.__doc__ = \
"""int32 DAQmxResetSampClkTimebaseRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4584"""
DAQmxGetSampClkTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkTimebaseSrc
DAQmxGetSampClkTimebaseSrc.restype = int32
DAQmxGetSampClkTimebaseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetSampClkTimebaseSrc.__doc__ = \
"""int32 DAQmxGetSampClkTimebaseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4586"""
DAQmxSetSampClkTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkTimebaseSrc
DAQmxSetSampClkTimebaseSrc.restype = int32
DAQmxSetSampClkTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetSampClkTimebaseSrc.__doc__ = \
"""int32 DAQmxSetSampClkTimebaseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4587"""
DAQmxResetSampClkTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkTimebaseSrc
DAQmxResetSampClkTimebaseSrc.restype = int32
DAQmxResetSampClkTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetSampClkTimebaseSrc.__doc__ = \
"""int32 DAQmxResetSampClkTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4588"""
DAQmxGetSampClkTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkTimebaseActiveEdge
DAQmxGetSampClkTimebaseActiveEdge.restype = int32
DAQmxGetSampClkTimebaseActiveEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSampClkTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxGetSampClkTimebaseActiveEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4591"""
DAQmxSetSampClkTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkTimebaseActiveEdge
DAQmxSetSampClkTimebaseActiveEdge.restype = int32
DAQmxSetSampClkTimebaseActiveEdge.argtypes = [TaskHandle, int32]
DAQmxSetSampClkTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxSetSampClkTimebaseActiveEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4592"""
DAQmxResetSampClkTimebaseActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkTimebaseActiveEdge
DAQmxResetSampClkTimebaseActiveEdge.restype = int32
DAQmxResetSampClkTimebaseActiveEdge.argtypes = [TaskHandle]
DAQmxResetSampClkTimebaseActiveEdge.__doc__ = \
"""int32 DAQmxResetSampClkTimebaseActiveEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4593"""
DAQmxGetSampClkTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkTimebaseMasterTimebaseDiv
DAQmxGetSampClkTimebaseMasterTimebaseDiv.restype = int32
DAQmxGetSampClkTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetSampClkTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxGetSampClkTimebaseMasterTimebaseDiv(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4595"""
DAQmxSetSampClkTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkTimebaseMasterTimebaseDiv
DAQmxSetSampClkTimebaseMasterTimebaseDiv.restype = int32
DAQmxSetSampClkTimebaseMasterTimebaseDiv.argtypes = [TaskHandle, uInt32]
DAQmxSetSampClkTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxSetSampClkTimebaseMasterTimebaseDiv(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4596"""
DAQmxResetSampClkTimebaseMasterTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkTimebaseMasterTimebaseDiv
DAQmxResetSampClkTimebaseMasterTimebaseDiv.restype = int32
DAQmxResetSampClkTimebaseMasterTimebaseDiv.argtypes = [TaskHandle]
DAQmxResetSampClkTimebaseMasterTimebaseDiv.__doc__ = \
"""int32 DAQmxResetSampClkTimebaseMasterTimebaseDiv(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4597"""
DAQmxGetSampClkDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkDigFltrEnable
DAQmxGetSampClkDigFltrEnable.restype = int32
DAQmxGetSampClkDigFltrEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetSampClkDigFltrEnable.__doc__ = \
"""int32 DAQmxGetSampClkDigFltrEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4599"""
DAQmxSetSampClkDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkDigFltrEnable
DAQmxSetSampClkDigFltrEnable.restype = int32
DAQmxSetSampClkDigFltrEnable.argtypes = [TaskHandle, bool32]
DAQmxSetSampClkDigFltrEnable.__doc__ = \
"""int32 DAQmxSetSampClkDigFltrEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4600"""
DAQmxResetSampClkDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkDigFltrEnable
DAQmxResetSampClkDigFltrEnable.restype = int32
DAQmxResetSampClkDigFltrEnable.argtypes = [TaskHandle]
DAQmxResetSampClkDigFltrEnable.__doc__ = \
"""int32 DAQmxResetSampClkDigFltrEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4601"""
DAQmxGetSampClkDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkDigFltrMinPulseWidth
DAQmxGetSampClkDigFltrMinPulseWidth.restype = int32
DAQmxGetSampClkDigFltrMinPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSampClkDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetSampClkDigFltrMinPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4603"""
DAQmxSetSampClkDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkDigFltrMinPulseWidth
DAQmxSetSampClkDigFltrMinPulseWidth.restype = int32
DAQmxSetSampClkDigFltrMinPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetSampClkDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetSampClkDigFltrMinPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4604"""
DAQmxResetSampClkDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkDigFltrMinPulseWidth
DAQmxResetSampClkDigFltrMinPulseWidth.restype = int32
DAQmxResetSampClkDigFltrMinPulseWidth.argtypes = [TaskHandle]
DAQmxResetSampClkDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetSampClkDigFltrMinPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4605"""
DAQmxGetSampClkDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkDigFltrTimebaseSrc
DAQmxGetSampClkDigFltrTimebaseSrc.restype = int32
DAQmxGetSampClkDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetSampClkDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetSampClkDigFltrTimebaseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4607"""
DAQmxSetSampClkDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkDigFltrTimebaseSrc
DAQmxSetSampClkDigFltrTimebaseSrc.restype = int32
DAQmxSetSampClkDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetSampClkDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetSampClkDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4608"""
DAQmxResetSampClkDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkDigFltrTimebaseSrc
DAQmxResetSampClkDigFltrTimebaseSrc.restype = int32
DAQmxResetSampClkDigFltrTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetSampClkDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetSampClkDigFltrTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4609"""
DAQmxGetSampClkDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkDigFltrTimebaseRate
DAQmxGetSampClkDigFltrTimebaseRate.restype = int32
DAQmxGetSampClkDigFltrTimebaseRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSampClkDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetSampClkDigFltrTimebaseRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4611"""
DAQmxSetSampClkDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkDigFltrTimebaseRate
DAQmxSetSampClkDigFltrTimebaseRate.restype = int32
DAQmxSetSampClkDigFltrTimebaseRate.argtypes = [TaskHandle, float64]
DAQmxSetSampClkDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetSampClkDigFltrTimebaseRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4612"""
DAQmxResetSampClkDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkDigFltrTimebaseRate
DAQmxResetSampClkDigFltrTimebaseRate.restype = int32
DAQmxResetSampClkDigFltrTimebaseRate.argtypes = [TaskHandle]
DAQmxResetSampClkDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetSampClkDigFltrTimebaseRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4613"""
DAQmxGetSampClkDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkDigSyncEnable
DAQmxGetSampClkDigSyncEnable.restype = int32
DAQmxGetSampClkDigSyncEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetSampClkDigSyncEnable.__doc__ = \
"""int32 DAQmxGetSampClkDigSyncEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4615"""
DAQmxSetSampClkDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkDigSyncEnable
DAQmxSetSampClkDigSyncEnable.restype = int32
DAQmxSetSampClkDigSyncEnable.argtypes = [TaskHandle, bool32]
DAQmxSetSampClkDigSyncEnable.__doc__ = \
"""int32 DAQmxSetSampClkDigSyncEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4616"""
DAQmxResetSampClkDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkDigSyncEnable
DAQmxResetSampClkDigSyncEnable.restype = int32
DAQmxResetSampClkDigSyncEnable.argtypes = [TaskHandle]
DAQmxResetSampClkDigSyncEnable.__doc__ = \
"""int32 DAQmxResetSampClkDigSyncEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4617"""
DAQmxGetHshkDelayAfterXfer = _stdcall_libraries['nicaiu.dll'].DAQmxGetHshkDelayAfterXfer
DAQmxGetHshkDelayAfterXfer.restype = int32
DAQmxGetHshkDelayAfterXfer.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetHshkDelayAfterXfer.__doc__ = \
"""int32 DAQmxGetHshkDelayAfterXfer(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4619"""
DAQmxSetHshkDelayAfterXfer = _stdcall_libraries['nicaiu.dll'].DAQmxSetHshkDelayAfterXfer
DAQmxSetHshkDelayAfterXfer.restype = int32
DAQmxSetHshkDelayAfterXfer.argtypes = [TaskHandle, float64]
DAQmxSetHshkDelayAfterXfer.__doc__ = \
"""int32 DAQmxSetHshkDelayAfterXfer(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4620"""
DAQmxResetHshkDelayAfterXfer = _stdcall_libraries['nicaiu.dll'].DAQmxResetHshkDelayAfterXfer
DAQmxResetHshkDelayAfterXfer.restype = int32
DAQmxResetHshkDelayAfterXfer.argtypes = [TaskHandle]
DAQmxResetHshkDelayAfterXfer.__doc__ = \
"""int32 DAQmxResetHshkDelayAfterXfer(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4621"""
DAQmxGetHshkStartCond = _stdcall_libraries['nicaiu.dll'].DAQmxGetHshkStartCond
DAQmxGetHshkStartCond.restype = int32
DAQmxGetHshkStartCond.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetHshkStartCond.__doc__ = \
"""int32 DAQmxGetHshkStartCond(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4624"""
DAQmxSetHshkStartCond = _stdcall_libraries['nicaiu.dll'].DAQmxSetHshkStartCond
DAQmxSetHshkStartCond.restype = int32
DAQmxSetHshkStartCond.argtypes = [TaskHandle, int32]
DAQmxSetHshkStartCond.__doc__ = \
"""int32 DAQmxSetHshkStartCond(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4625"""
DAQmxResetHshkStartCond = _stdcall_libraries['nicaiu.dll'].DAQmxResetHshkStartCond
DAQmxResetHshkStartCond.restype = int32
DAQmxResetHshkStartCond.argtypes = [TaskHandle]
DAQmxResetHshkStartCond.__doc__ = \
"""int32 DAQmxResetHshkStartCond(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4626"""
DAQmxGetHshkSampleInputDataWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetHshkSampleInputDataWhen
DAQmxGetHshkSampleInputDataWhen.restype = int32
DAQmxGetHshkSampleInputDataWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetHshkSampleInputDataWhen.__doc__ = \
"""int32 DAQmxGetHshkSampleInputDataWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4629"""
DAQmxSetHshkSampleInputDataWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetHshkSampleInputDataWhen
DAQmxSetHshkSampleInputDataWhen.restype = int32
DAQmxSetHshkSampleInputDataWhen.argtypes = [TaskHandle, int32]
DAQmxSetHshkSampleInputDataWhen.__doc__ = \
"""int32 DAQmxSetHshkSampleInputDataWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4630"""
DAQmxResetHshkSampleInputDataWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetHshkSampleInputDataWhen
DAQmxResetHshkSampleInputDataWhen.restype = int32
DAQmxResetHshkSampleInputDataWhen.argtypes = [TaskHandle]
DAQmxResetHshkSampleInputDataWhen.__doc__ = \
"""int32 DAQmxResetHshkSampleInputDataWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4631"""
DAQmxGetChangeDetectDIRisingEdgePhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetChangeDetectDIRisingEdgePhysicalChans
DAQmxGetChangeDetectDIRisingEdgePhysicalChans.restype = int32
DAQmxGetChangeDetectDIRisingEdgePhysicalChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetChangeDetectDIRisingEdgePhysicalChans.__doc__ = \
"""int32 DAQmxGetChangeDetectDIRisingEdgePhysicalChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4633"""
DAQmxSetChangeDetectDIRisingEdgePhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxSetChangeDetectDIRisingEdgePhysicalChans
DAQmxSetChangeDetectDIRisingEdgePhysicalChans.restype = int32
DAQmxSetChangeDetectDIRisingEdgePhysicalChans.argtypes = [TaskHandle, STRING]
DAQmxSetChangeDetectDIRisingEdgePhysicalChans.__doc__ = \
"""int32 DAQmxSetChangeDetectDIRisingEdgePhysicalChans(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4634"""
DAQmxResetChangeDetectDIRisingEdgePhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxResetChangeDetectDIRisingEdgePhysicalChans
DAQmxResetChangeDetectDIRisingEdgePhysicalChans.restype = int32
DAQmxResetChangeDetectDIRisingEdgePhysicalChans.argtypes = [TaskHandle]
DAQmxResetChangeDetectDIRisingEdgePhysicalChans.__doc__ = \
"""int32 DAQmxResetChangeDetectDIRisingEdgePhysicalChans(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4635"""
DAQmxGetChangeDetectDIFallingEdgePhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetChangeDetectDIFallingEdgePhysicalChans
DAQmxGetChangeDetectDIFallingEdgePhysicalChans.restype = int32
DAQmxGetChangeDetectDIFallingEdgePhysicalChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetChangeDetectDIFallingEdgePhysicalChans.__doc__ = \
"""int32 DAQmxGetChangeDetectDIFallingEdgePhysicalChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4637"""
DAQmxSetChangeDetectDIFallingEdgePhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxSetChangeDetectDIFallingEdgePhysicalChans
DAQmxSetChangeDetectDIFallingEdgePhysicalChans.restype = int32
DAQmxSetChangeDetectDIFallingEdgePhysicalChans.argtypes = [TaskHandle, STRING]
DAQmxSetChangeDetectDIFallingEdgePhysicalChans.__doc__ = \
"""int32 DAQmxSetChangeDetectDIFallingEdgePhysicalChans(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4638"""
DAQmxResetChangeDetectDIFallingEdgePhysicalChans = _stdcall_libraries['nicaiu.dll'].DAQmxResetChangeDetectDIFallingEdgePhysicalChans
DAQmxResetChangeDetectDIFallingEdgePhysicalChans.restype = int32
DAQmxResetChangeDetectDIFallingEdgePhysicalChans.argtypes = [TaskHandle]
DAQmxResetChangeDetectDIFallingEdgePhysicalChans.__doc__ = \
"""int32 DAQmxResetChangeDetectDIFallingEdgePhysicalChans(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4639"""
DAQmxGetOnDemandSimultaneousAOEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetOnDemandSimultaneousAOEnable
DAQmxGetOnDemandSimultaneousAOEnable.restype = int32
DAQmxGetOnDemandSimultaneousAOEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetOnDemandSimultaneousAOEnable.__doc__ = \
"""int32 DAQmxGetOnDemandSimultaneousAOEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4641"""
DAQmxSetOnDemandSimultaneousAOEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetOnDemandSimultaneousAOEnable
DAQmxSetOnDemandSimultaneousAOEnable.restype = int32
DAQmxSetOnDemandSimultaneousAOEnable.argtypes = [TaskHandle, bool32]
DAQmxSetOnDemandSimultaneousAOEnable.__doc__ = \
"""int32 DAQmxSetOnDemandSimultaneousAOEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4642"""
DAQmxResetOnDemandSimultaneousAOEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetOnDemandSimultaneousAOEnable
DAQmxResetOnDemandSimultaneousAOEnable.restype = int32
DAQmxResetOnDemandSimultaneousAOEnable.argtypes = [TaskHandle]
DAQmxResetOnDemandSimultaneousAOEnable.__doc__ = \
"""int32 DAQmxResetOnDemandSimultaneousAOEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4643"""
DAQmxGetAIConvRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvRate
DAQmxGetAIConvRate.restype = int32
DAQmxGetAIConvRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAIConvRate.__doc__ = \
"""int32 DAQmxGetAIConvRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4645"""
DAQmxSetAIConvRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvRate
DAQmxSetAIConvRate.restype = int32
DAQmxSetAIConvRate.argtypes = [TaskHandle, float64]
DAQmxSetAIConvRate.__doc__ = \
"""int32 DAQmxSetAIConvRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4646"""
DAQmxResetAIConvRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvRate
DAQmxResetAIConvRate.restype = int32
DAQmxResetAIConvRate.argtypes = [TaskHandle]
DAQmxResetAIConvRate.__doc__ = \
"""int32 DAQmxResetAIConvRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4647"""
DAQmxGetAIConvRateEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvRateEx
DAQmxGetAIConvRateEx.restype = int32
DAQmxGetAIConvRateEx.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIConvRateEx.__doc__ = \
"""int32 DAQmxGetAIConvRateEx(TaskHandle taskHandle, unknown * deviceNames, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4648"""
DAQmxSetAIConvRateEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvRateEx
DAQmxSetAIConvRateEx.restype = int32
DAQmxSetAIConvRateEx.argtypes = [TaskHandle, STRING, float64]
DAQmxSetAIConvRateEx.__doc__ = \
"""int32 DAQmxSetAIConvRateEx(TaskHandle taskHandle, unknown * deviceNames, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4649"""
DAQmxResetAIConvRateEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvRateEx
DAQmxResetAIConvRateEx.restype = int32
DAQmxResetAIConvRateEx.argtypes = [TaskHandle, STRING]
DAQmxResetAIConvRateEx.__doc__ = \
"""int32 DAQmxResetAIConvRateEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4650"""
DAQmxGetAIConvMaxRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvMaxRate
DAQmxGetAIConvMaxRate.restype = int32
DAQmxGetAIConvMaxRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAIConvMaxRate.__doc__ = \
"""int32 DAQmxGetAIConvMaxRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4652"""
DAQmxGetAIConvMaxRateEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvMaxRateEx
DAQmxGetAIConvMaxRateEx.restype = int32
DAQmxGetAIConvMaxRateEx.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetAIConvMaxRateEx.__doc__ = \
"""int32 DAQmxGetAIConvMaxRateEx(TaskHandle taskHandle, unknown * deviceNames, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4653"""
DAQmxGetAIConvSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvSrc
DAQmxGetAIConvSrc.restype = int32
DAQmxGetAIConvSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAIConvSrc.__doc__ = \
"""int32 DAQmxGetAIConvSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4655"""
DAQmxSetAIConvSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvSrc
DAQmxSetAIConvSrc.restype = int32
DAQmxSetAIConvSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAIConvSrc.__doc__ = \
"""int32 DAQmxSetAIConvSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4656"""
DAQmxResetAIConvSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvSrc
DAQmxResetAIConvSrc.restype = int32
DAQmxResetAIConvSrc.argtypes = [TaskHandle]
DAQmxResetAIConvSrc.__doc__ = \
"""int32 DAQmxResetAIConvSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4657"""
DAQmxGetAIConvSrcEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvSrcEx
DAQmxGetAIConvSrcEx.restype = int32
DAQmxGetAIConvSrcEx.argtypes = [TaskHandle, STRING, STRING, uInt32]
DAQmxGetAIConvSrcEx.__doc__ = \
"""int32 DAQmxGetAIConvSrcEx(TaskHandle taskHandle, unknown * deviceNames, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4658"""
DAQmxSetAIConvSrcEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvSrcEx
DAQmxSetAIConvSrcEx.restype = int32
DAQmxSetAIConvSrcEx.argtypes = [TaskHandle, STRING, STRING]
DAQmxSetAIConvSrcEx.__doc__ = \
"""int32 DAQmxSetAIConvSrcEx(TaskHandle taskHandle, unknown * deviceNames, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4659"""
DAQmxResetAIConvSrcEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvSrcEx
DAQmxResetAIConvSrcEx.restype = int32
DAQmxResetAIConvSrcEx.argtypes = [TaskHandle, STRING]
DAQmxResetAIConvSrcEx.__doc__ = \
"""int32 DAQmxResetAIConvSrcEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4660"""
DAQmxGetAIConvActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvActiveEdge
DAQmxGetAIConvActiveEdge.restype = int32
DAQmxGetAIConvActiveEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAIConvActiveEdge.__doc__ = \
"""int32 DAQmxGetAIConvActiveEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4663"""
DAQmxSetAIConvActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvActiveEdge
DAQmxSetAIConvActiveEdge.restype = int32
DAQmxSetAIConvActiveEdge.argtypes = [TaskHandle, int32]
DAQmxSetAIConvActiveEdge.__doc__ = \
"""int32 DAQmxSetAIConvActiveEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4664"""
DAQmxResetAIConvActiveEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvActiveEdge
DAQmxResetAIConvActiveEdge.restype = int32
DAQmxResetAIConvActiveEdge.argtypes = [TaskHandle]
DAQmxResetAIConvActiveEdge.__doc__ = \
"""int32 DAQmxResetAIConvActiveEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4665"""
DAQmxGetAIConvActiveEdgeEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvActiveEdgeEx
DAQmxGetAIConvActiveEdgeEx.restype = int32
DAQmxGetAIConvActiveEdgeEx.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIConvActiveEdgeEx.__doc__ = \
"""int32 DAQmxGetAIConvActiveEdgeEx(TaskHandle taskHandle, unknown * deviceNames, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4666"""
DAQmxSetAIConvActiveEdgeEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvActiveEdgeEx
DAQmxSetAIConvActiveEdgeEx.restype = int32
DAQmxSetAIConvActiveEdgeEx.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIConvActiveEdgeEx.__doc__ = \
"""int32 DAQmxSetAIConvActiveEdgeEx(TaskHandle taskHandle, unknown * deviceNames, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4667"""
DAQmxResetAIConvActiveEdgeEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvActiveEdgeEx
DAQmxResetAIConvActiveEdgeEx.restype = int32
DAQmxResetAIConvActiveEdgeEx.argtypes = [TaskHandle, STRING]
DAQmxResetAIConvActiveEdgeEx.__doc__ = \
"""int32 DAQmxResetAIConvActiveEdgeEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4668"""
DAQmxGetAIConvTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvTimebaseDiv
DAQmxGetAIConvTimebaseDiv.restype = int32
DAQmxGetAIConvTimebaseDiv.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetAIConvTimebaseDiv.__doc__ = \
"""int32 DAQmxGetAIConvTimebaseDiv(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4670"""
DAQmxSetAIConvTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvTimebaseDiv
DAQmxSetAIConvTimebaseDiv.restype = int32
DAQmxSetAIConvTimebaseDiv.argtypes = [TaskHandle, uInt32]
DAQmxSetAIConvTimebaseDiv.__doc__ = \
"""int32 DAQmxSetAIConvTimebaseDiv(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4671"""
DAQmxResetAIConvTimebaseDiv = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvTimebaseDiv
DAQmxResetAIConvTimebaseDiv.restype = int32
DAQmxResetAIConvTimebaseDiv.argtypes = [TaskHandle]
DAQmxResetAIConvTimebaseDiv.__doc__ = \
"""int32 DAQmxResetAIConvTimebaseDiv(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4672"""
DAQmxGetAIConvTimebaseDivEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvTimebaseDivEx
DAQmxGetAIConvTimebaseDivEx.restype = int32
DAQmxGetAIConvTimebaseDivEx.argtypes = [TaskHandle, STRING, POINTER(uInt32)]
DAQmxGetAIConvTimebaseDivEx.__doc__ = \
"""int32 DAQmxGetAIConvTimebaseDivEx(TaskHandle taskHandle, unknown * deviceNames, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4673"""
DAQmxSetAIConvTimebaseDivEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvTimebaseDivEx
DAQmxSetAIConvTimebaseDivEx.restype = int32
DAQmxSetAIConvTimebaseDivEx.argtypes = [TaskHandle, STRING, uInt32]
DAQmxSetAIConvTimebaseDivEx.__doc__ = \
"""int32 DAQmxSetAIConvTimebaseDivEx(TaskHandle taskHandle, unknown * deviceNames, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4674"""
DAQmxResetAIConvTimebaseDivEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvTimebaseDivEx
DAQmxResetAIConvTimebaseDivEx.restype = int32
DAQmxResetAIConvTimebaseDivEx.argtypes = [TaskHandle, STRING]
DAQmxResetAIConvTimebaseDivEx.__doc__ = \
"""int32 DAQmxResetAIConvTimebaseDivEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4675"""
DAQmxGetAIConvTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvTimebaseSrc
DAQmxGetAIConvTimebaseSrc.restype = int32
DAQmxGetAIConvTimebaseSrc.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAIConvTimebaseSrc.__doc__ = \
"""int32 DAQmxGetAIConvTimebaseSrc(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4678"""
DAQmxSetAIConvTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvTimebaseSrc
DAQmxSetAIConvTimebaseSrc.restype = int32
DAQmxSetAIConvTimebaseSrc.argtypes = [TaskHandle, int32]
DAQmxSetAIConvTimebaseSrc.__doc__ = \
"""int32 DAQmxSetAIConvTimebaseSrc(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4679"""
DAQmxResetAIConvTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvTimebaseSrc
DAQmxResetAIConvTimebaseSrc.restype = int32
DAQmxResetAIConvTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetAIConvTimebaseSrc.__doc__ = \
"""int32 DAQmxResetAIConvTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4680"""
DAQmxGetAIConvTimebaseSrcEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetAIConvTimebaseSrcEx
DAQmxGetAIConvTimebaseSrcEx.restype = int32
DAQmxGetAIConvTimebaseSrcEx.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetAIConvTimebaseSrcEx.__doc__ = \
"""int32 DAQmxGetAIConvTimebaseSrcEx(TaskHandle taskHandle, unknown * deviceNames, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4681"""
DAQmxSetAIConvTimebaseSrcEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetAIConvTimebaseSrcEx
DAQmxSetAIConvTimebaseSrcEx.restype = int32
DAQmxSetAIConvTimebaseSrcEx.argtypes = [TaskHandle, STRING, int32]
DAQmxSetAIConvTimebaseSrcEx.__doc__ = \
"""int32 DAQmxSetAIConvTimebaseSrcEx(TaskHandle taskHandle, unknown * deviceNames, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4682"""
DAQmxResetAIConvTimebaseSrcEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetAIConvTimebaseSrcEx
DAQmxResetAIConvTimebaseSrcEx.restype = int32
DAQmxResetAIConvTimebaseSrcEx.argtypes = [TaskHandle, STRING]
DAQmxResetAIConvTimebaseSrcEx.__doc__ = \
"""int32 DAQmxResetAIConvTimebaseSrcEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4683"""
DAQmxGetDelayFromSampClkDelayUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetDelayFromSampClkDelayUnits
DAQmxGetDelayFromSampClkDelayUnits.restype = int32
DAQmxGetDelayFromSampClkDelayUnits.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDelayFromSampClkDelayUnits.__doc__ = \
"""int32 DAQmxGetDelayFromSampClkDelayUnits(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4686"""
DAQmxSetDelayFromSampClkDelayUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetDelayFromSampClkDelayUnits
DAQmxSetDelayFromSampClkDelayUnits.restype = int32
DAQmxSetDelayFromSampClkDelayUnits.argtypes = [TaskHandle, int32]
DAQmxSetDelayFromSampClkDelayUnits.__doc__ = \
"""int32 DAQmxSetDelayFromSampClkDelayUnits(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4687"""
DAQmxResetDelayFromSampClkDelayUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetDelayFromSampClkDelayUnits
DAQmxResetDelayFromSampClkDelayUnits.restype = int32
DAQmxResetDelayFromSampClkDelayUnits.argtypes = [TaskHandle]
DAQmxResetDelayFromSampClkDelayUnits.__doc__ = \
"""int32 DAQmxResetDelayFromSampClkDelayUnits(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4688"""
DAQmxGetDelayFromSampClkDelayUnitsEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetDelayFromSampClkDelayUnitsEx
DAQmxGetDelayFromSampClkDelayUnitsEx.restype = int32
DAQmxGetDelayFromSampClkDelayUnitsEx.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetDelayFromSampClkDelayUnitsEx.__doc__ = \
"""int32 DAQmxGetDelayFromSampClkDelayUnitsEx(TaskHandle taskHandle, unknown * deviceNames, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4689"""
DAQmxSetDelayFromSampClkDelayUnitsEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetDelayFromSampClkDelayUnitsEx
DAQmxSetDelayFromSampClkDelayUnitsEx.restype = int32
DAQmxSetDelayFromSampClkDelayUnitsEx.argtypes = [TaskHandle, STRING, int32]
DAQmxSetDelayFromSampClkDelayUnitsEx.__doc__ = \
"""int32 DAQmxSetDelayFromSampClkDelayUnitsEx(TaskHandle taskHandle, unknown * deviceNames, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4690"""
DAQmxResetDelayFromSampClkDelayUnitsEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetDelayFromSampClkDelayUnitsEx
DAQmxResetDelayFromSampClkDelayUnitsEx.restype = int32
DAQmxResetDelayFromSampClkDelayUnitsEx.argtypes = [TaskHandle, STRING]
DAQmxResetDelayFromSampClkDelayUnitsEx.__doc__ = \
"""int32 DAQmxResetDelayFromSampClkDelayUnitsEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4691"""
DAQmxGetDelayFromSampClkDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetDelayFromSampClkDelay
DAQmxGetDelayFromSampClkDelay.restype = int32
DAQmxGetDelayFromSampClkDelay.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDelayFromSampClkDelay.__doc__ = \
"""int32 DAQmxGetDelayFromSampClkDelay(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4693"""
DAQmxSetDelayFromSampClkDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetDelayFromSampClkDelay
DAQmxSetDelayFromSampClkDelay.restype = int32
DAQmxSetDelayFromSampClkDelay.argtypes = [TaskHandle, float64]
DAQmxSetDelayFromSampClkDelay.__doc__ = \
"""int32 DAQmxSetDelayFromSampClkDelay(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4694"""
DAQmxResetDelayFromSampClkDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetDelayFromSampClkDelay
DAQmxResetDelayFromSampClkDelay.restype = int32
DAQmxResetDelayFromSampClkDelay.argtypes = [TaskHandle]
DAQmxResetDelayFromSampClkDelay.__doc__ = \
"""int32 DAQmxResetDelayFromSampClkDelay(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4695"""
DAQmxGetDelayFromSampClkDelayEx = _stdcall_libraries['nicaiu.dll'].DAQmxGetDelayFromSampClkDelayEx
DAQmxGetDelayFromSampClkDelayEx.restype = int32
DAQmxGetDelayFromSampClkDelayEx.argtypes = [TaskHandle, STRING, POINTER(float64)]
DAQmxGetDelayFromSampClkDelayEx.__doc__ = \
"""int32 DAQmxGetDelayFromSampClkDelayEx(TaskHandle taskHandle, unknown * deviceNames, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4696"""
DAQmxSetDelayFromSampClkDelayEx = _stdcall_libraries['nicaiu.dll'].DAQmxSetDelayFromSampClkDelayEx
DAQmxSetDelayFromSampClkDelayEx.restype = int32
DAQmxSetDelayFromSampClkDelayEx.argtypes = [TaskHandle, STRING, float64]
DAQmxSetDelayFromSampClkDelayEx.__doc__ = \
"""int32 DAQmxSetDelayFromSampClkDelayEx(TaskHandle taskHandle, unknown * deviceNames, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4697"""
DAQmxResetDelayFromSampClkDelayEx = _stdcall_libraries['nicaiu.dll'].DAQmxResetDelayFromSampClkDelayEx
DAQmxResetDelayFromSampClkDelayEx.restype = int32
DAQmxResetDelayFromSampClkDelayEx.argtypes = [TaskHandle, STRING]
DAQmxResetDelayFromSampClkDelayEx.__doc__ = \
"""int32 DAQmxResetDelayFromSampClkDelayEx(TaskHandle taskHandle, unknown * deviceNames)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4698"""
DAQmxGetMasterTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetMasterTimebaseRate
DAQmxGetMasterTimebaseRate.restype = int32
DAQmxGetMasterTimebaseRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetMasterTimebaseRate.__doc__ = \
"""int32 DAQmxGetMasterTimebaseRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4700"""
DAQmxSetMasterTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetMasterTimebaseRate
DAQmxSetMasterTimebaseRate.restype = int32
DAQmxSetMasterTimebaseRate.argtypes = [TaskHandle, float64]
DAQmxSetMasterTimebaseRate.__doc__ = \
"""int32 DAQmxSetMasterTimebaseRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4701"""
DAQmxResetMasterTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetMasterTimebaseRate
DAQmxResetMasterTimebaseRate.restype = int32
DAQmxResetMasterTimebaseRate.argtypes = [TaskHandle]
DAQmxResetMasterTimebaseRate.__doc__ = \
"""int32 DAQmxResetMasterTimebaseRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4702"""
DAQmxGetMasterTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetMasterTimebaseSrc
DAQmxGetMasterTimebaseSrc.restype = int32
DAQmxGetMasterTimebaseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetMasterTimebaseSrc.__doc__ = \
"""int32 DAQmxGetMasterTimebaseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4704"""
DAQmxSetMasterTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetMasterTimebaseSrc
DAQmxSetMasterTimebaseSrc.restype = int32
DAQmxSetMasterTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetMasterTimebaseSrc.__doc__ = \
"""int32 DAQmxSetMasterTimebaseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4705"""
DAQmxResetMasterTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetMasterTimebaseSrc
DAQmxResetMasterTimebaseSrc.restype = int32
DAQmxResetMasterTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetMasterTimebaseSrc.__doc__ = \
"""int32 DAQmxResetMasterTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4706"""
DAQmxGetRefClkRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetRefClkRate
DAQmxGetRefClkRate.restype = int32
DAQmxGetRefClkRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetRefClkRate.__doc__ = \
"""int32 DAQmxGetRefClkRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4708"""
DAQmxSetRefClkRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetRefClkRate
DAQmxSetRefClkRate.restype = int32
DAQmxSetRefClkRate.argtypes = [TaskHandle, float64]
DAQmxSetRefClkRate.__doc__ = \
"""int32 DAQmxSetRefClkRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4709"""
DAQmxResetRefClkRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetRefClkRate
DAQmxResetRefClkRate.restype = int32
DAQmxResetRefClkRate.argtypes = [TaskHandle]
DAQmxResetRefClkRate.__doc__ = \
"""int32 DAQmxResetRefClkRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4710"""
DAQmxGetRefClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetRefClkSrc
DAQmxGetRefClkSrc.restype = int32
DAQmxGetRefClkSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetRefClkSrc.__doc__ = \
"""int32 DAQmxGetRefClkSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4712"""
DAQmxSetRefClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetRefClkSrc
DAQmxSetRefClkSrc.restype = int32
DAQmxSetRefClkSrc.argtypes = [TaskHandle, STRING]
DAQmxSetRefClkSrc.__doc__ = \
"""int32 DAQmxSetRefClkSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4713"""
DAQmxResetRefClkSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetRefClkSrc
DAQmxResetRefClkSrc.restype = int32
DAQmxResetRefClkSrc.argtypes = [TaskHandle]
DAQmxResetRefClkSrc.__doc__ = \
"""int32 DAQmxResetRefClkSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4714"""
DAQmxGetSyncPulseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetSyncPulseSrc
DAQmxGetSyncPulseSrc.restype = int32
DAQmxGetSyncPulseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetSyncPulseSrc.__doc__ = \
"""int32 DAQmxGetSyncPulseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4716"""
DAQmxSetSyncPulseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetSyncPulseSrc
DAQmxSetSyncPulseSrc.restype = int32
DAQmxSetSyncPulseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetSyncPulseSrc.__doc__ = \
"""int32 DAQmxSetSyncPulseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4717"""
DAQmxResetSyncPulseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetSyncPulseSrc
DAQmxResetSyncPulseSrc.restype = int32
DAQmxResetSyncPulseSrc.argtypes = [TaskHandle]
DAQmxResetSyncPulseSrc.__doc__ = \
"""int32 DAQmxResetSyncPulseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4718"""
DAQmxGetSyncPulseSyncTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetSyncPulseSyncTime
DAQmxGetSyncPulseSyncTime.restype = int32
DAQmxGetSyncPulseSyncTime.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSyncPulseSyncTime.__doc__ = \
"""int32 DAQmxGetSyncPulseSyncTime(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4720"""
DAQmxGetSyncPulseMinDelayToStart = _stdcall_libraries['nicaiu.dll'].DAQmxGetSyncPulseMinDelayToStart
DAQmxGetSyncPulseMinDelayToStart.restype = int32
DAQmxGetSyncPulseMinDelayToStart.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetSyncPulseMinDelayToStart.__doc__ = \
"""int32 DAQmxGetSyncPulseMinDelayToStart(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4722"""
DAQmxSetSyncPulseMinDelayToStart = _stdcall_libraries['nicaiu.dll'].DAQmxSetSyncPulseMinDelayToStart
DAQmxSetSyncPulseMinDelayToStart.restype = int32
DAQmxSetSyncPulseMinDelayToStart.argtypes = [TaskHandle, float64]
DAQmxSetSyncPulseMinDelayToStart.__doc__ = \
"""int32 DAQmxSetSyncPulseMinDelayToStart(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4723"""
DAQmxResetSyncPulseMinDelayToStart = _stdcall_libraries['nicaiu.dll'].DAQmxResetSyncPulseMinDelayToStart
DAQmxResetSyncPulseMinDelayToStart.restype = int32
DAQmxResetSyncPulseMinDelayToStart.argtypes = [TaskHandle]
DAQmxResetSyncPulseMinDelayToStart.__doc__ = \
"""int32 DAQmxResetSyncPulseMinDelayToStart(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4724"""
DAQmxGetSampTimingEngine = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampTimingEngine
DAQmxGetSampTimingEngine.restype = int32
DAQmxGetSampTimingEngine.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetSampTimingEngine.__doc__ = \
"""int32 DAQmxGetSampTimingEngine(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4726"""
DAQmxSetSampTimingEngine = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampTimingEngine
DAQmxSetSampTimingEngine.restype = int32
DAQmxSetSampTimingEngine.argtypes = [TaskHandle, uInt32]
DAQmxSetSampTimingEngine.__doc__ = \
"""int32 DAQmxSetSampTimingEngine(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4727"""
DAQmxResetSampTimingEngine = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampTimingEngine
DAQmxResetSampTimingEngine.restype = int32
DAQmxResetSampTimingEngine.argtypes = [TaskHandle]
DAQmxResetSampTimingEngine.__doc__ = \
"""int32 DAQmxResetSampTimingEngine(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4728"""
DAQmxGetStartTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetStartTrigType
DAQmxGetStartTrigType.restype = int32
DAQmxGetStartTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetStartTrigType.__doc__ = \
"""int32 DAQmxGetStartTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4733"""
DAQmxSetStartTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetStartTrigType
DAQmxSetStartTrigType.restype = int32
DAQmxSetStartTrigType.argtypes = [TaskHandle, int32]
DAQmxSetStartTrigType.__doc__ = \
"""int32 DAQmxSetStartTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4734"""
DAQmxResetStartTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetStartTrigType
DAQmxResetStartTrigType.restype = int32
DAQmxResetStartTrigType.argtypes = [TaskHandle]
DAQmxResetStartTrigType.__doc__ = \
"""int32 DAQmxResetStartTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4735"""
DAQmxGetDigEdgeStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigSrc
DAQmxGetDigEdgeStartTrigSrc.restype = int32
DAQmxGetDigEdgeStartTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeStartTrigSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4737"""
DAQmxSetDigEdgeStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigSrc
DAQmxSetDigEdgeStartTrigSrc.restype = int32
DAQmxSetDigEdgeStartTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeStartTrigSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4738"""
DAQmxResetDigEdgeStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigSrc
DAQmxResetDigEdgeStartTrigSrc.restype = int32
DAQmxResetDigEdgeStartTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4739"""
DAQmxGetDigEdgeStartTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigEdge
DAQmxGetDigEdgeStartTrigEdge.restype = int32
DAQmxGetDigEdgeStartTrigEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigEdgeStartTrigEdge.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4742"""
DAQmxSetDigEdgeStartTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigEdge
DAQmxSetDigEdgeStartTrigEdge.restype = int32
DAQmxSetDigEdgeStartTrigEdge.argtypes = [TaskHandle, int32]
DAQmxSetDigEdgeStartTrigEdge.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4743"""
DAQmxResetDigEdgeStartTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigEdge
DAQmxResetDigEdgeStartTrigEdge.restype = int32
DAQmxResetDigEdgeStartTrigEdge.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigEdge.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4744"""
DAQmxGetDigEdgeStartTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigDigFltrEnable
DAQmxGetDigEdgeStartTrigDigFltrEnable.restype = int32
DAQmxGetDigEdgeStartTrigDigFltrEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigEdgeStartTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigDigFltrEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4746"""
DAQmxSetDigEdgeStartTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigDigFltrEnable
DAQmxSetDigEdgeStartTrigDigFltrEnable.restype = int32
DAQmxSetDigEdgeStartTrigDigFltrEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigEdgeStartTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigDigFltrEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4747"""
DAQmxResetDigEdgeStartTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigDigFltrEnable
DAQmxResetDigEdgeStartTrigDigFltrEnable.restype = int32
DAQmxResetDigEdgeStartTrigDigFltrEnable.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigDigFltrEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4748"""
DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth
DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth.restype = int32
DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4750"""
DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth
DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth.restype = int32
DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigDigFltrMinPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4751"""
DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth
DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth.restype = int32
DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigDigFltrMinPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4752"""
DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc
DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc.restype = int32
DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4754"""
DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc
DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc.restype = int32
DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4755"""
DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc
DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc.restype = int32
DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigDigFltrTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4756"""
DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate
DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate.restype = int32
DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4758"""
DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate
DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate.restype = int32
DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate.argtypes = [TaskHandle, float64]
DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigDigFltrTimebaseRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4759"""
DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate
DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate.restype = int32
DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigDigFltrTimebaseRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4760"""
DAQmxGetDigEdgeStartTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeStartTrigDigSyncEnable
DAQmxGetDigEdgeStartTrigDigSyncEnable.restype = int32
DAQmxGetDigEdgeStartTrigDigSyncEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigEdgeStartTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxGetDigEdgeStartTrigDigSyncEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4762"""
DAQmxSetDigEdgeStartTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeStartTrigDigSyncEnable
DAQmxSetDigEdgeStartTrigDigSyncEnable.restype = int32
DAQmxSetDigEdgeStartTrigDigSyncEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigEdgeStartTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxSetDigEdgeStartTrigDigSyncEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4763"""
DAQmxResetDigEdgeStartTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeStartTrigDigSyncEnable
DAQmxResetDigEdgeStartTrigDigSyncEnable.restype = int32
DAQmxResetDigEdgeStartTrigDigSyncEnable.argtypes = [TaskHandle]
DAQmxResetDigEdgeStartTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxResetDigEdgeStartTrigDigSyncEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4764"""
DAQmxGetDigPatternStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternStartTrigSrc
DAQmxGetDigPatternStartTrigSrc.restype = int32
DAQmxGetDigPatternStartTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigPatternStartTrigSrc.__doc__ = \
"""int32 DAQmxGetDigPatternStartTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4766"""
DAQmxSetDigPatternStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternStartTrigSrc
DAQmxSetDigPatternStartTrigSrc.restype = int32
DAQmxSetDigPatternStartTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigPatternStartTrigSrc.__doc__ = \
"""int32 DAQmxSetDigPatternStartTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4767"""
DAQmxResetDigPatternStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternStartTrigSrc
DAQmxResetDigPatternStartTrigSrc.restype = int32
DAQmxResetDigPatternStartTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigPatternStartTrigSrc.__doc__ = \
"""int32 DAQmxResetDigPatternStartTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4768"""
DAQmxGetDigPatternStartTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternStartTrigPattern
DAQmxGetDigPatternStartTrigPattern.restype = int32
DAQmxGetDigPatternStartTrigPattern.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigPatternStartTrigPattern.__doc__ = \
"""int32 DAQmxGetDigPatternStartTrigPattern(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4770"""
DAQmxSetDigPatternStartTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternStartTrigPattern
DAQmxSetDigPatternStartTrigPattern.restype = int32
DAQmxSetDigPatternStartTrigPattern.argtypes = [TaskHandle, STRING]
DAQmxSetDigPatternStartTrigPattern.__doc__ = \
"""int32 DAQmxSetDigPatternStartTrigPattern(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4771"""
DAQmxResetDigPatternStartTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternStartTrigPattern
DAQmxResetDigPatternStartTrigPattern.restype = int32
DAQmxResetDigPatternStartTrigPattern.argtypes = [TaskHandle]
DAQmxResetDigPatternStartTrigPattern.__doc__ = \
"""int32 DAQmxResetDigPatternStartTrigPattern(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4772"""
DAQmxGetDigPatternStartTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternStartTrigWhen
DAQmxGetDigPatternStartTrigWhen.restype = int32
DAQmxGetDigPatternStartTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigPatternStartTrigWhen.__doc__ = \
"""int32 DAQmxGetDigPatternStartTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4775"""
DAQmxSetDigPatternStartTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternStartTrigWhen
DAQmxSetDigPatternStartTrigWhen.restype = int32
DAQmxSetDigPatternStartTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetDigPatternStartTrigWhen.__doc__ = \
"""int32 DAQmxSetDigPatternStartTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4776"""
DAQmxResetDigPatternStartTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternStartTrigWhen
DAQmxResetDigPatternStartTrigWhen.restype = int32
DAQmxResetDigPatternStartTrigWhen.argtypes = [TaskHandle]
DAQmxResetDigPatternStartTrigWhen.__doc__ = \
"""int32 DAQmxResetDigPatternStartTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4777"""
DAQmxGetAnlgEdgeStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeStartTrigSrc
DAQmxGetAnlgEdgeStartTrigSrc.restype = int32
DAQmxGetAnlgEdgeStartTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAnlgEdgeStartTrigSrc.__doc__ = \
"""int32 DAQmxGetAnlgEdgeStartTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4779"""
DAQmxSetAnlgEdgeStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeStartTrigSrc
DAQmxSetAnlgEdgeStartTrigSrc.restype = int32
DAQmxSetAnlgEdgeStartTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAnlgEdgeStartTrigSrc.__doc__ = \
"""int32 DAQmxSetAnlgEdgeStartTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4780"""
DAQmxResetAnlgEdgeStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeStartTrigSrc
DAQmxResetAnlgEdgeStartTrigSrc.restype = int32
DAQmxResetAnlgEdgeStartTrigSrc.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeStartTrigSrc.__doc__ = \
"""int32 DAQmxResetAnlgEdgeStartTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4781"""
DAQmxGetAnlgEdgeStartTrigSlope = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeStartTrigSlope
DAQmxGetAnlgEdgeStartTrigSlope.restype = int32
DAQmxGetAnlgEdgeStartTrigSlope.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgEdgeStartTrigSlope.__doc__ = \
"""int32 DAQmxGetAnlgEdgeStartTrigSlope(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4784"""
DAQmxSetAnlgEdgeStartTrigSlope = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeStartTrigSlope
DAQmxSetAnlgEdgeStartTrigSlope.restype = int32
DAQmxSetAnlgEdgeStartTrigSlope.argtypes = [TaskHandle, int32]
DAQmxSetAnlgEdgeStartTrigSlope.__doc__ = \
"""int32 DAQmxSetAnlgEdgeStartTrigSlope(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4785"""
DAQmxResetAnlgEdgeStartTrigSlope = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeStartTrigSlope
DAQmxResetAnlgEdgeStartTrigSlope.restype = int32
DAQmxResetAnlgEdgeStartTrigSlope.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeStartTrigSlope.__doc__ = \
"""int32 DAQmxResetAnlgEdgeStartTrigSlope(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4786"""
DAQmxGetAnlgEdgeStartTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeStartTrigLvl
DAQmxGetAnlgEdgeStartTrigLvl.restype = int32
DAQmxGetAnlgEdgeStartTrigLvl.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgEdgeStartTrigLvl.__doc__ = \
"""int32 DAQmxGetAnlgEdgeStartTrigLvl(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4788"""
DAQmxSetAnlgEdgeStartTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeStartTrigLvl
DAQmxSetAnlgEdgeStartTrigLvl.restype = int32
DAQmxSetAnlgEdgeStartTrigLvl.argtypes = [TaskHandle, float64]
DAQmxSetAnlgEdgeStartTrigLvl.__doc__ = \
"""int32 DAQmxSetAnlgEdgeStartTrigLvl(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4789"""
DAQmxResetAnlgEdgeStartTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeStartTrigLvl
DAQmxResetAnlgEdgeStartTrigLvl.restype = int32
DAQmxResetAnlgEdgeStartTrigLvl.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeStartTrigLvl.__doc__ = \
"""int32 DAQmxResetAnlgEdgeStartTrigLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4790"""
DAQmxGetAnlgEdgeStartTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeStartTrigHyst
DAQmxGetAnlgEdgeStartTrigHyst.restype = int32
DAQmxGetAnlgEdgeStartTrigHyst.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgEdgeStartTrigHyst.__doc__ = \
"""int32 DAQmxGetAnlgEdgeStartTrigHyst(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4792"""
DAQmxSetAnlgEdgeStartTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeStartTrigHyst
DAQmxSetAnlgEdgeStartTrigHyst.restype = int32
DAQmxSetAnlgEdgeStartTrigHyst.argtypes = [TaskHandle, float64]
DAQmxSetAnlgEdgeStartTrigHyst.__doc__ = \
"""int32 DAQmxSetAnlgEdgeStartTrigHyst(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4793"""
DAQmxResetAnlgEdgeStartTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeStartTrigHyst
DAQmxResetAnlgEdgeStartTrigHyst.restype = int32
DAQmxResetAnlgEdgeStartTrigHyst.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeStartTrigHyst.__doc__ = \
"""int32 DAQmxResetAnlgEdgeStartTrigHyst(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4794"""
DAQmxGetAnlgEdgeStartTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeStartTrigCoupling
DAQmxGetAnlgEdgeStartTrigCoupling.restype = int32
DAQmxGetAnlgEdgeStartTrigCoupling.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgEdgeStartTrigCoupling.__doc__ = \
"""int32 DAQmxGetAnlgEdgeStartTrigCoupling(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4797"""
DAQmxSetAnlgEdgeStartTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeStartTrigCoupling
DAQmxSetAnlgEdgeStartTrigCoupling.restype = int32
DAQmxSetAnlgEdgeStartTrigCoupling.argtypes = [TaskHandle, int32]
DAQmxSetAnlgEdgeStartTrigCoupling.__doc__ = \
"""int32 DAQmxSetAnlgEdgeStartTrigCoupling(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4798"""
DAQmxResetAnlgEdgeStartTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeStartTrigCoupling
DAQmxResetAnlgEdgeStartTrigCoupling.restype = int32
DAQmxResetAnlgEdgeStartTrigCoupling.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeStartTrigCoupling.__doc__ = \
"""int32 DAQmxResetAnlgEdgeStartTrigCoupling(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4799"""
DAQmxGetAnlgWinStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinStartTrigSrc
DAQmxGetAnlgWinStartTrigSrc.restype = int32
DAQmxGetAnlgWinStartTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAnlgWinStartTrigSrc.__doc__ = \
"""int32 DAQmxGetAnlgWinStartTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4801"""
DAQmxSetAnlgWinStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinStartTrigSrc
DAQmxSetAnlgWinStartTrigSrc.restype = int32
DAQmxSetAnlgWinStartTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAnlgWinStartTrigSrc.__doc__ = \
"""int32 DAQmxSetAnlgWinStartTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4802"""
DAQmxResetAnlgWinStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinStartTrigSrc
DAQmxResetAnlgWinStartTrigSrc.restype = int32
DAQmxResetAnlgWinStartTrigSrc.argtypes = [TaskHandle]
DAQmxResetAnlgWinStartTrigSrc.__doc__ = \
"""int32 DAQmxResetAnlgWinStartTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4803"""
DAQmxGetAnlgWinStartTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinStartTrigWhen
DAQmxGetAnlgWinStartTrigWhen.restype = int32
DAQmxGetAnlgWinStartTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgWinStartTrigWhen.__doc__ = \
"""int32 DAQmxGetAnlgWinStartTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4806"""
DAQmxSetAnlgWinStartTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinStartTrigWhen
DAQmxSetAnlgWinStartTrigWhen.restype = int32
DAQmxSetAnlgWinStartTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetAnlgWinStartTrigWhen.__doc__ = \
"""int32 DAQmxSetAnlgWinStartTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4807"""
DAQmxResetAnlgWinStartTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinStartTrigWhen
DAQmxResetAnlgWinStartTrigWhen.restype = int32
DAQmxResetAnlgWinStartTrigWhen.argtypes = [TaskHandle]
DAQmxResetAnlgWinStartTrigWhen.__doc__ = \
"""int32 DAQmxResetAnlgWinStartTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4808"""
DAQmxGetAnlgWinStartTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinStartTrigTop
DAQmxGetAnlgWinStartTrigTop.restype = int32
DAQmxGetAnlgWinStartTrigTop.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgWinStartTrigTop.__doc__ = \
"""int32 DAQmxGetAnlgWinStartTrigTop(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4810"""
DAQmxSetAnlgWinStartTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinStartTrigTop
DAQmxSetAnlgWinStartTrigTop.restype = int32
DAQmxSetAnlgWinStartTrigTop.argtypes = [TaskHandle, float64]
DAQmxSetAnlgWinStartTrigTop.__doc__ = \
"""int32 DAQmxSetAnlgWinStartTrigTop(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4811"""
DAQmxResetAnlgWinStartTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinStartTrigTop
DAQmxResetAnlgWinStartTrigTop.restype = int32
DAQmxResetAnlgWinStartTrigTop.argtypes = [TaskHandle]
DAQmxResetAnlgWinStartTrigTop.__doc__ = \
"""int32 DAQmxResetAnlgWinStartTrigTop(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4812"""
DAQmxGetAnlgWinStartTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinStartTrigBtm
DAQmxGetAnlgWinStartTrigBtm.restype = int32
DAQmxGetAnlgWinStartTrigBtm.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgWinStartTrigBtm.__doc__ = \
"""int32 DAQmxGetAnlgWinStartTrigBtm(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4814"""
DAQmxSetAnlgWinStartTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinStartTrigBtm
DAQmxSetAnlgWinStartTrigBtm.restype = int32
DAQmxSetAnlgWinStartTrigBtm.argtypes = [TaskHandle, float64]
DAQmxSetAnlgWinStartTrigBtm.__doc__ = \
"""int32 DAQmxSetAnlgWinStartTrigBtm(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4815"""
DAQmxResetAnlgWinStartTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinStartTrigBtm
DAQmxResetAnlgWinStartTrigBtm.restype = int32
DAQmxResetAnlgWinStartTrigBtm.argtypes = [TaskHandle]
DAQmxResetAnlgWinStartTrigBtm.__doc__ = \
"""int32 DAQmxResetAnlgWinStartTrigBtm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4816"""
DAQmxGetAnlgWinStartTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinStartTrigCoupling
DAQmxGetAnlgWinStartTrigCoupling.restype = int32
DAQmxGetAnlgWinStartTrigCoupling.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgWinStartTrigCoupling.__doc__ = \
"""int32 DAQmxGetAnlgWinStartTrigCoupling(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4819"""
DAQmxSetAnlgWinStartTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinStartTrigCoupling
DAQmxSetAnlgWinStartTrigCoupling.restype = int32
DAQmxSetAnlgWinStartTrigCoupling.argtypes = [TaskHandle, int32]
DAQmxSetAnlgWinStartTrigCoupling.__doc__ = \
"""int32 DAQmxSetAnlgWinStartTrigCoupling(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4820"""
DAQmxResetAnlgWinStartTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinStartTrigCoupling
DAQmxResetAnlgWinStartTrigCoupling.restype = int32
DAQmxResetAnlgWinStartTrigCoupling.argtypes = [TaskHandle]
DAQmxResetAnlgWinStartTrigCoupling.__doc__ = \
"""int32 DAQmxResetAnlgWinStartTrigCoupling(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4821"""
DAQmxGetStartTrigDelay = _stdcall_libraries['nicaiu.dll'].DAQmxGetStartTrigDelay
DAQmxGetStartTrigDelay.restype = int32
DAQmxGetStartTrigDelay.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetStartTrigDelay.__doc__ = \
"""int32 DAQmxGetStartTrigDelay(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4823"""
DAQmxSetStartTrigDelay = _stdcall_libraries['nicaiu.dll'].DAQmxSetStartTrigDelay
DAQmxSetStartTrigDelay.restype = int32
DAQmxSetStartTrigDelay.argtypes = [TaskHandle, float64]
DAQmxSetStartTrigDelay.__doc__ = \
"""int32 DAQmxSetStartTrigDelay(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4824"""
DAQmxResetStartTrigDelay = _stdcall_libraries['nicaiu.dll'].DAQmxResetStartTrigDelay
DAQmxResetStartTrigDelay.restype = int32
DAQmxResetStartTrigDelay.argtypes = [TaskHandle]
DAQmxResetStartTrigDelay.__doc__ = \
"""int32 DAQmxResetStartTrigDelay(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4825"""
DAQmxGetStartTrigDelayUnits = _stdcall_libraries['nicaiu.dll'].DAQmxGetStartTrigDelayUnits
DAQmxGetStartTrigDelayUnits.restype = int32
DAQmxGetStartTrigDelayUnits.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetStartTrigDelayUnits.__doc__ = \
"""int32 DAQmxGetStartTrigDelayUnits(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4828"""
DAQmxSetStartTrigDelayUnits = _stdcall_libraries['nicaiu.dll'].DAQmxSetStartTrigDelayUnits
DAQmxSetStartTrigDelayUnits.restype = int32
DAQmxSetStartTrigDelayUnits.argtypes = [TaskHandle, int32]
DAQmxSetStartTrigDelayUnits.__doc__ = \
"""int32 DAQmxSetStartTrigDelayUnits(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4829"""
DAQmxResetStartTrigDelayUnits = _stdcall_libraries['nicaiu.dll'].DAQmxResetStartTrigDelayUnits
DAQmxResetStartTrigDelayUnits.restype = int32
DAQmxResetStartTrigDelayUnits.argtypes = [TaskHandle]
DAQmxResetStartTrigDelayUnits.__doc__ = \
"""int32 DAQmxResetStartTrigDelayUnits(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4830"""
DAQmxGetStartTrigRetriggerable = _stdcall_libraries['nicaiu.dll'].DAQmxGetStartTrigRetriggerable
DAQmxGetStartTrigRetriggerable.restype = int32
DAQmxGetStartTrigRetriggerable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetStartTrigRetriggerable.__doc__ = \
"""int32 DAQmxGetStartTrigRetriggerable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4832"""
DAQmxSetStartTrigRetriggerable = _stdcall_libraries['nicaiu.dll'].DAQmxSetStartTrigRetriggerable
DAQmxSetStartTrigRetriggerable.restype = int32
DAQmxSetStartTrigRetriggerable.argtypes = [TaskHandle, bool32]
DAQmxSetStartTrigRetriggerable.__doc__ = \
"""int32 DAQmxSetStartTrigRetriggerable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4833"""
DAQmxResetStartTrigRetriggerable = _stdcall_libraries['nicaiu.dll'].DAQmxResetStartTrigRetriggerable
DAQmxResetStartTrigRetriggerable.restype = int32
DAQmxResetStartTrigRetriggerable.argtypes = [TaskHandle]
DAQmxResetStartTrigRetriggerable.__doc__ = \
"""int32 DAQmxResetStartTrigRetriggerable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4834"""
DAQmxGetRefTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetRefTrigType
DAQmxGetRefTrigType.restype = int32
DAQmxGetRefTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetRefTrigType.__doc__ = \
"""int32 DAQmxGetRefTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4837"""
DAQmxSetRefTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetRefTrigType
DAQmxSetRefTrigType.restype = int32
DAQmxSetRefTrigType.argtypes = [TaskHandle, int32]
DAQmxSetRefTrigType.__doc__ = \
"""int32 DAQmxSetRefTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4838"""
DAQmxResetRefTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetRefTrigType
DAQmxResetRefTrigType.restype = int32
DAQmxResetRefTrigType.argtypes = [TaskHandle]
DAQmxResetRefTrigType.__doc__ = \
"""int32 DAQmxResetRefTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4839"""
DAQmxGetRefTrigPretrigSamples = _stdcall_libraries['nicaiu.dll'].DAQmxGetRefTrigPretrigSamples
DAQmxGetRefTrigPretrigSamples.restype = int32
DAQmxGetRefTrigPretrigSamples.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetRefTrigPretrigSamples.__doc__ = \
"""int32 DAQmxGetRefTrigPretrigSamples(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4841"""
DAQmxSetRefTrigPretrigSamples = _stdcall_libraries['nicaiu.dll'].DAQmxSetRefTrigPretrigSamples
DAQmxSetRefTrigPretrigSamples.restype = int32
DAQmxSetRefTrigPretrigSamples.argtypes = [TaskHandle, uInt32]
DAQmxSetRefTrigPretrigSamples.__doc__ = \
"""int32 DAQmxSetRefTrigPretrigSamples(TaskHandle taskHandle, uInt32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4842"""
DAQmxResetRefTrigPretrigSamples = _stdcall_libraries['nicaiu.dll'].DAQmxResetRefTrigPretrigSamples
DAQmxResetRefTrigPretrigSamples.restype = int32
DAQmxResetRefTrigPretrigSamples.argtypes = [TaskHandle]
DAQmxResetRefTrigPretrigSamples.__doc__ = \
"""int32 DAQmxResetRefTrigPretrigSamples(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4843"""
DAQmxGetDigEdgeRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeRefTrigSrc
DAQmxGetDigEdgeRefTrigSrc.restype = int32
DAQmxGetDigEdgeRefTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeRefTrigSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeRefTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4845"""
DAQmxSetDigEdgeRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeRefTrigSrc
DAQmxSetDigEdgeRefTrigSrc.restype = int32
DAQmxSetDigEdgeRefTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeRefTrigSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeRefTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4846"""
DAQmxResetDigEdgeRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeRefTrigSrc
DAQmxResetDigEdgeRefTrigSrc.restype = int32
DAQmxResetDigEdgeRefTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeRefTrigSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeRefTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4847"""
DAQmxGetDigEdgeRefTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeRefTrigEdge
DAQmxGetDigEdgeRefTrigEdge.restype = int32
DAQmxGetDigEdgeRefTrigEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigEdgeRefTrigEdge.__doc__ = \
"""int32 DAQmxGetDigEdgeRefTrigEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4850"""
DAQmxSetDigEdgeRefTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeRefTrigEdge
DAQmxSetDigEdgeRefTrigEdge.restype = int32
DAQmxSetDigEdgeRefTrigEdge.argtypes = [TaskHandle, int32]
DAQmxSetDigEdgeRefTrigEdge.__doc__ = \
"""int32 DAQmxSetDigEdgeRefTrigEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4851"""
DAQmxResetDigEdgeRefTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeRefTrigEdge
DAQmxResetDigEdgeRefTrigEdge.restype = int32
DAQmxResetDigEdgeRefTrigEdge.argtypes = [TaskHandle]
DAQmxResetDigEdgeRefTrigEdge.__doc__ = \
"""int32 DAQmxResetDigEdgeRefTrigEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4852"""
DAQmxGetDigPatternRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternRefTrigSrc
DAQmxGetDigPatternRefTrigSrc.restype = int32
DAQmxGetDigPatternRefTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigPatternRefTrigSrc.__doc__ = \
"""int32 DAQmxGetDigPatternRefTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4854"""
DAQmxSetDigPatternRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternRefTrigSrc
DAQmxSetDigPatternRefTrigSrc.restype = int32
DAQmxSetDigPatternRefTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigPatternRefTrigSrc.__doc__ = \
"""int32 DAQmxSetDigPatternRefTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4855"""
DAQmxResetDigPatternRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternRefTrigSrc
DAQmxResetDigPatternRefTrigSrc.restype = int32
DAQmxResetDigPatternRefTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigPatternRefTrigSrc.__doc__ = \
"""int32 DAQmxResetDigPatternRefTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4856"""
DAQmxGetDigPatternRefTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternRefTrigPattern
DAQmxGetDigPatternRefTrigPattern.restype = int32
DAQmxGetDigPatternRefTrigPattern.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigPatternRefTrigPattern.__doc__ = \
"""int32 DAQmxGetDigPatternRefTrigPattern(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4858"""
DAQmxSetDigPatternRefTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternRefTrigPattern
DAQmxSetDigPatternRefTrigPattern.restype = int32
DAQmxSetDigPatternRefTrigPattern.argtypes = [TaskHandle, STRING]
DAQmxSetDigPatternRefTrigPattern.__doc__ = \
"""int32 DAQmxSetDigPatternRefTrigPattern(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4859"""
DAQmxResetDigPatternRefTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternRefTrigPattern
DAQmxResetDigPatternRefTrigPattern.restype = int32
DAQmxResetDigPatternRefTrigPattern.argtypes = [TaskHandle]
DAQmxResetDigPatternRefTrigPattern.__doc__ = \
"""int32 DAQmxResetDigPatternRefTrigPattern(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4860"""
DAQmxGetDigPatternRefTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternRefTrigWhen
DAQmxGetDigPatternRefTrigWhen.restype = int32
DAQmxGetDigPatternRefTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigPatternRefTrigWhen.__doc__ = \
"""int32 DAQmxGetDigPatternRefTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4863"""
DAQmxSetDigPatternRefTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternRefTrigWhen
DAQmxSetDigPatternRefTrigWhen.restype = int32
DAQmxSetDigPatternRefTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetDigPatternRefTrigWhen.__doc__ = \
"""int32 DAQmxSetDigPatternRefTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4864"""
DAQmxResetDigPatternRefTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternRefTrigWhen
DAQmxResetDigPatternRefTrigWhen.restype = int32
DAQmxResetDigPatternRefTrigWhen.argtypes = [TaskHandle]
DAQmxResetDigPatternRefTrigWhen.__doc__ = \
"""int32 DAQmxResetDigPatternRefTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4865"""
DAQmxGetAnlgEdgeRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeRefTrigSrc
DAQmxGetAnlgEdgeRefTrigSrc.restype = int32
DAQmxGetAnlgEdgeRefTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAnlgEdgeRefTrigSrc.__doc__ = \
"""int32 DAQmxGetAnlgEdgeRefTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4867"""
DAQmxSetAnlgEdgeRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeRefTrigSrc
DAQmxSetAnlgEdgeRefTrigSrc.restype = int32
DAQmxSetAnlgEdgeRefTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAnlgEdgeRefTrigSrc.__doc__ = \
"""int32 DAQmxSetAnlgEdgeRefTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4868"""
DAQmxResetAnlgEdgeRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeRefTrigSrc
DAQmxResetAnlgEdgeRefTrigSrc.restype = int32
DAQmxResetAnlgEdgeRefTrigSrc.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeRefTrigSrc.__doc__ = \
"""int32 DAQmxResetAnlgEdgeRefTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4869"""
DAQmxGetAnlgEdgeRefTrigSlope = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeRefTrigSlope
DAQmxGetAnlgEdgeRefTrigSlope.restype = int32
DAQmxGetAnlgEdgeRefTrigSlope.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgEdgeRefTrigSlope.__doc__ = \
"""int32 DAQmxGetAnlgEdgeRefTrigSlope(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4872"""
DAQmxSetAnlgEdgeRefTrigSlope = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeRefTrigSlope
DAQmxSetAnlgEdgeRefTrigSlope.restype = int32
DAQmxSetAnlgEdgeRefTrigSlope.argtypes = [TaskHandle, int32]
DAQmxSetAnlgEdgeRefTrigSlope.__doc__ = \
"""int32 DAQmxSetAnlgEdgeRefTrigSlope(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4873"""
DAQmxResetAnlgEdgeRefTrigSlope = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeRefTrigSlope
DAQmxResetAnlgEdgeRefTrigSlope.restype = int32
DAQmxResetAnlgEdgeRefTrigSlope.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeRefTrigSlope.__doc__ = \
"""int32 DAQmxResetAnlgEdgeRefTrigSlope(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4874"""
DAQmxGetAnlgEdgeRefTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeRefTrigLvl
DAQmxGetAnlgEdgeRefTrigLvl.restype = int32
DAQmxGetAnlgEdgeRefTrigLvl.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgEdgeRefTrigLvl.__doc__ = \
"""int32 DAQmxGetAnlgEdgeRefTrigLvl(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4876"""
DAQmxSetAnlgEdgeRefTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeRefTrigLvl
DAQmxSetAnlgEdgeRefTrigLvl.restype = int32
DAQmxSetAnlgEdgeRefTrigLvl.argtypes = [TaskHandle, float64]
DAQmxSetAnlgEdgeRefTrigLvl.__doc__ = \
"""int32 DAQmxSetAnlgEdgeRefTrigLvl(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4877"""
DAQmxResetAnlgEdgeRefTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeRefTrigLvl
DAQmxResetAnlgEdgeRefTrigLvl.restype = int32
DAQmxResetAnlgEdgeRefTrigLvl.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeRefTrigLvl.__doc__ = \
"""int32 DAQmxResetAnlgEdgeRefTrigLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4878"""
DAQmxGetAnlgEdgeRefTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeRefTrigHyst
DAQmxGetAnlgEdgeRefTrigHyst.restype = int32
DAQmxGetAnlgEdgeRefTrigHyst.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgEdgeRefTrigHyst.__doc__ = \
"""int32 DAQmxGetAnlgEdgeRefTrigHyst(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4880"""
DAQmxSetAnlgEdgeRefTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeRefTrigHyst
DAQmxSetAnlgEdgeRefTrigHyst.restype = int32
DAQmxSetAnlgEdgeRefTrigHyst.argtypes = [TaskHandle, float64]
DAQmxSetAnlgEdgeRefTrigHyst.__doc__ = \
"""int32 DAQmxSetAnlgEdgeRefTrigHyst(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4881"""
DAQmxResetAnlgEdgeRefTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeRefTrigHyst
DAQmxResetAnlgEdgeRefTrigHyst.restype = int32
DAQmxResetAnlgEdgeRefTrigHyst.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeRefTrigHyst.__doc__ = \
"""int32 DAQmxResetAnlgEdgeRefTrigHyst(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4882"""
DAQmxGetAnlgEdgeRefTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgEdgeRefTrigCoupling
DAQmxGetAnlgEdgeRefTrigCoupling.restype = int32
DAQmxGetAnlgEdgeRefTrigCoupling.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgEdgeRefTrigCoupling.__doc__ = \
"""int32 DAQmxGetAnlgEdgeRefTrigCoupling(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4885"""
DAQmxSetAnlgEdgeRefTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgEdgeRefTrigCoupling
DAQmxSetAnlgEdgeRefTrigCoupling.restype = int32
DAQmxSetAnlgEdgeRefTrigCoupling.argtypes = [TaskHandle, int32]
DAQmxSetAnlgEdgeRefTrigCoupling.__doc__ = \
"""int32 DAQmxSetAnlgEdgeRefTrigCoupling(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4886"""
DAQmxResetAnlgEdgeRefTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgEdgeRefTrigCoupling
DAQmxResetAnlgEdgeRefTrigCoupling.restype = int32
DAQmxResetAnlgEdgeRefTrigCoupling.argtypes = [TaskHandle]
DAQmxResetAnlgEdgeRefTrigCoupling.__doc__ = \
"""int32 DAQmxResetAnlgEdgeRefTrigCoupling(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4887"""
DAQmxGetAnlgWinRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinRefTrigSrc
DAQmxGetAnlgWinRefTrigSrc.restype = int32
DAQmxGetAnlgWinRefTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAnlgWinRefTrigSrc.__doc__ = \
"""int32 DAQmxGetAnlgWinRefTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4889"""
DAQmxSetAnlgWinRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinRefTrigSrc
DAQmxSetAnlgWinRefTrigSrc.restype = int32
DAQmxSetAnlgWinRefTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAnlgWinRefTrigSrc.__doc__ = \
"""int32 DAQmxSetAnlgWinRefTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4890"""
DAQmxResetAnlgWinRefTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinRefTrigSrc
DAQmxResetAnlgWinRefTrigSrc.restype = int32
DAQmxResetAnlgWinRefTrigSrc.argtypes = [TaskHandle]
DAQmxResetAnlgWinRefTrigSrc.__doc__ = \
"""int32 DAQmxResetAnlgWinRefTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4891"""
DAQmxGetAnlgWinRefTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinRefTrigWhen
DAQmxGetAnlgWinRefTrigWhen.restype = int32
DAQmxGetAnlgWinRefTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgWinRefTrigWhen.__doc__ = \
"""int32 DAQmxGetAnlgWinRefTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4894"""
DAQmxSetAnlgWinRefTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinRefTrigWhen
DAQmxSetAnlgWinRefTrigWhen.restype = int32
DAQmxSetAnlgWinRefTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetAnlgWinRefTrigWhen.__doc__ = \
"""int32 DAQmxSetAnlgWinRefTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4895"""
DAQmxResetAnlgWinRefTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinRefTrigWhen
DAQmxResetAnlgWinRefTrigWhen.restype = int32
DAQmxResetAnlgWinRefTrigWhen.argtypes = [TaskHandle]
DAQmxResetAnlgWinRefTrigWhen.__doc__ = \
"""int32 DAQmxResetAnlgWinRefTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4896"""
DAQmxGetAnlgWinRefTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinRefTrigTop
DAQmxGetAnlgWinRefTrigTop.restype = int32
DAQmxGetAnlgWinRefTrigTop.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgWinRefTrigTop.__doc__ = \
"""int32 DAQmxGetAnlgWinRefTrigTop(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4898"""
DAQmxSetAnlgWinRefTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinRefTrigTop
DAQmxSetAnlgWinRefTrigTop.restype = int32
DAQmxSetAnlgWinRefTrigTop.argtypes = [TaskHandle, float64]
DAQmxSetAnlgWinRefTrigTop.__doc__ = \
"""int32 DAQmxSetAnlgWinRefTrigTop(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4899"""
DAQmxResetAnlgWinRefTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinRefTrigTop
DAQmxResetAnlgWinRefTrigTop.restype = int32
DAQmxResetAnlgWinRefTrigTop.argtypes = [TaskHandle]
DAQmxResetAnlgWinRefTrigTop.__doc__ = \
"""int32 DAQmxResetAnlgWinRefTrigTop(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4900"""
DAQmxGetAnlgWinRefTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinRefTrigBtm
DAQmxGetAnlgWinRefTrigBtm.restype = int32
DAQmxGetAnlgWinRefTrigBtm.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgWinRefTrigBtm.__doc__ = \
"""int32 DAQmxGetAnlgWinRefTrigBtm(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4902"""
DAQmxSetAnlgWinRefTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinRefTrigBtm
DAQmxSetAnlgWinRefTrigBtm.restype = int32
DAQmxSetAnlgWinRefTrigBtm.argtypes = [TaskHandle, float64]
DAQmxSetAnlgWinRefTrigBtm.__doc__ = \
"""int32 DAQmxSetAnlgWinRefTrigBtm(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4903"""
DAQmxResetAnlgWinRefTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinRefTrigBtm
DAQmxResetAnlgWinRefTrigBtm.restype = int32
DAQmxResetAnlgWinRefTrigBtm.argtypes = [TaskHandle]
DAQmxResetAnlgWinRefTrigBtm.__doc__ = \
"""int32 DAQmxResetAnlgWinRefTrigBtm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4904"""
DAQmxGetAnlgWinRefTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinRefTrigCoupling
DAQmxGetAnlgWinRefTrigCoupling.restype = int32
DAQmxGetAnlgWinRefTrigCoupling.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgWinRefTrigCoupling.__doc__ = \
"""int32 DAQmxGetAnlgWinRefTrigCoupling(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4907"""
DAQmxSetAnlgWinRefTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinRefTrigCoupling
DAQmxSetAnlgWinRefTrigCoupling.restype = int32
DAQmxSetAnlgWinRefTrigCoupling.argtypes = [TaskHandle, int32]
DAQmxSetAnlgWinRefTrigCoupling.__doc__ = \
"""int32 DAQmxSetAnlgWinRefTrigCoupling(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4908"""
DAQmxResetAnlgWinRefTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinRefTrigCoupling
DAQmxResetAnlgWinRefTrigCoupling.restype = int32
DAQmxResetAnlgWinRefTrigCoupling.argtypes = [TaskHandle]
DAQmxResetAnlgWinRefTrigCoupling.__doc__ = \
"""int32 DAQmxResetAnlgWinRefTrigCoupling(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4909"""
DAQmxGetRefTrigAutoTrigEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetRefTrigAutoTrigEnable
DAQmxGetRefTrigAutoTrigEnable.restype = int32
DAQmxGetRefTrigAutoTrigEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetRefTrigAutoTrigEnable.__doc__ = \
"""int32 DAQmxGetRefTrigAutoTrigEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4911"""
DAQmxSetRefTrigAutoTrigEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetRefTrigAutoTrigEnable
DAQmxSetRefTrigAutoTrigEnable.restype = int32
DAQmxSetRefTrigAutoTrigEnable.argtypes = [TaskHandle, bool32]
DAQmxSetRefTrigAutoTrigEnable.__doc__ = \
"""int32 DAQmxSetRefTrigAutoTrigEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4912"""
DAQmxResetRefTrigAutoTrigEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetRefTrigAutoTrigEnable
DAQmxResetRefTrigAutoTrigEnable.restype = int32
DAQmxResetRefTrigAutoTrigEnable.argtypes = [TaskHandle]
DAQmxResetRefTrigAutoTrigEnable.__doc__ = \
"""int32 DAQmxResetRefTrigAutoTrigEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4913"""
DAQmxGetRefTrigAutoTriggered = _stdcall_libraries['nicaiu.dll'].DAQmxGetRefTrigAutoTriggered
DAQmxGetRefTrigAutoTriggered.restype = int32
DAQmxGetRefTrigAutoTriggered.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetRefTrigAutoTriggered.__doc__ = \
"""int32 DAQmxGetRefTrigAutoTriggered(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4915"""
DAQmxGetAdvTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetAdvTrigType
DAQmxGetAdvTrigType.restype = int32
DAQmxGetAdvTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAdvTrigType.__doc__ = \
"""int32 DAQmxGetAdvTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4918"""
DAQmxSetAdvTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetAdvTrigType
DAQmxSetAdvTrigType.restype = int32
DAQmxSetAdvTrigType.argtypes = [TaskHandle, int32]
DAQmxSetAdvTrigType.__doc__ = \
"""int32 DAQmxSetAdvTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4919"""
DAQmxResetAdvTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetAdvTrigType
DAQmxResetAdvTrigType.restype = int32
DAQmxResetAdvTrigType.argtypes = [TaskHandle]
DAQmxResetAdvTrigType.__doc__ = \
"""int32 DAQmxResetAdvTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4920"""
DAQmxGetDigEdgeAdvTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeAdvTrigSrc
DAQmxGetDigEdgeAdvTrigSrc.restype = int32
DAQmxGetDigEdgeAdvTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeAdvTrigSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeAdvTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4922"""
DAQmxSetDigEdgeAdvTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeAdvTrigSrc
DAQmxSetDigEdgeAdvTrigSrc.restype = int32
DAQmxSetDigEdgeAdvTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeAdvTrigSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeAdvTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4923"""
DAQmxResetDigEdgeAdvTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeAdvTrigSrc
DAQmxResetDigEdgeAdvTrigSrc.restype = int32
DAQmxResetDigEdgeAdvTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeAdvTrigSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeAdvTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4924"""
DAQmxGetDigEdgeAdvTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeAdvTrigEdge
DAQmxGetDigEdgeAdvTrigEdge.restype = int32
DAQmxGetDigEdgeAdvTrigEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigEdgeAdvTrigEdge.__doc__ = \
"""int32 DAQmxGetDigEdgeAdvTrigEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4927"""
DAQmxSetDigEdgeAdvTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeAdvTrigEdge
DAQmxSetDigEdgeAdvTrigEdge.restype = int32
DAQmxSetDigEdgeAdvTrigEdge.argtypes = [TaskHandle, int32]
DAQmxSetDigEdgeAdvTrigEdge.__doc__ = \
"""int32 DAQmxSetDigEdgeAdvTrigEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4928"""
DAQmxResetDigEdgeAdvTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeAdvTrigEdge
DAQmxResetDigEdgeAdvTrigEdge.restype = int32
DAQmxResetDigEdgeAdvTrigEdge.argtypes = [TaskHandle]
DAQmxResetDigEdgeAdvTrigEdge.__doc__ = \
"""int32 DAQmxResetDigEdgeAdvTrigEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4929"""
DAQmxGetDigEdgeAdvTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeAdvTrigDigFltrEnable
DAQmxGetDigEdgeAdvTrigDigFltrEnable.restype = int32
DAQmxGetDigEdgeAdvTrigDigFltrEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigEdgeAdvTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxGetDigEdgeAdvTrigDigFltrEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4931"""
DAQmxSetDigEdgeAdvTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeAdvTrigDigFltrEnable
DAQmxSetDigEdgeAdvTrigDigFltrEnable.restype = int32
DAQmxSetDigEdgeAdvTrigDigFltrEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigEdgeAdvTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxSetDigEdgeAdvTrigDigFltrEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4932"""
DAQmxResetDigEdgeAdvTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeAdvTrigDigFltrEnable
DAQmxResetDigEdgeAdvTrigDigFltrEnable.restype = int32
DAQmxResetDigEdgeAdvTrigDigFltrEnable.argtypes = [TaskHandle]
DAQmxResetDigEdgeAdvTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxResetDigEdgeAdvTrigDigFltrEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4933"""
DAQmxGetHshkTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetHshkTrigType
DAQmxGetHshkTrigType.restype = int32
DAQmxGetHshkTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetHshkTrigType.__doc__ = \
"""int32 DAQmxGetHshkTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4936"""
DAQmxSetHshkTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetHshkTrigType
DAQmxSetHshkTrigType.restype = int32
DAQmxSetHshkTrigType.argtypes = [TaskHandle, int32]
DAQmxSetHshkTrigType.__doc__ = \
"""int32 DAQmxSetHshkTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4937"""
DAQmxResetHshkTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetHshkTrigType
DAQmxResetHshkTrigType.restype = int32
DAQmxResetHshkTrigType.argtypes = [TaskHandle]
DAQmxResetHshkTrigType.__doc__ = \
"""int32 DAQmxResetHshkTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4938"""
DAQmxGetInterlockedHshkTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetInterlockedHshkTrigSrc
DAQmxGetInterlockedHshkTrigSrc.restype = int32
DAQmxGetInterlockedHshkTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetInterlockedHshkTrigSrc.__doc__ = \
"""int32 DAQmxGetInterlockedHshkTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4940"""
DAQmxSetInterlockedHshkTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetInterlockedHshkTrigSrc
DAQmxSetInterlockedHshkTrigSrc.restype = int32
DAQmxSetInterlockedHshkTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetInterlockedHshkTrigSrc.__doc__ = \
"""int32 DAQmxSetInterlockedHshkTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4941"""
DAQmxResetInterlockedHshkTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetInterlockedHshkTrigSrc
DAQmxResetInterlockedHshkTrigSrc.restype = int32
DAQmxResetInterlockedHshkTrigSrc.argtypes = [TaskHandle]
DAQmxResetInterlockedHshkTrigSrc.__doc__ = \
"""int32 DAQmxResetInterlockedHshkTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4942"""
DAQmxGetInterlockedHshkTrigAssertedLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetInterlockedHshkTrigAssertedLvl
DAQmxGetInterlockedHshkTrigAssertedLvl.restype = int32
DAQmxGetInterlockedHshkTrigAssertedLvl.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetInterlockedHshkTrigAssertedLvl.__doc__ = \
"""int32 DAQmxGetInterlockedHshkTrigAssertedLvl(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4945"""
DAQmxSetInterlockedHshkTrigAssertedLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetInterlockedHshkTrigAssertedLvl
DAQmxSetInterlockedHshkTrigAssertedLvl.restype = int32
DAQmxSetInterlockedHshkTrigAssertedLvl.argtypes = [TaskHandle, int32]
DAQmxSetInterlockedHshkTrigAssertedLvl.__doc__ = \
"""int32 DAQmxSetInterlockedHshkTrigAssertedLvl(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4946"""
DAQmxResetInterlockedHshkTrigAssertedLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetInterlockedHshkTrigAssertedLvl
DAQmxResetInterlockedHshkTrigAssertedLvl.restype = int32
DAQmxResetInterlockedHshkTrigAssertedLvl.argtypes = [TaskHandle]
DAQmxResetInterlockedHshkTrigAssertedLvl.__doc__ = \
"""int32 DAQmxResetInterlockedHshkTrigAssertedLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4947"""
DAQmxGetPauseTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetPauseTrigType
DAQmxGetPauseTrigType.restype = int32
DAQmxGetPauseTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetPauseTrigType.__doc__ = \
"""int32 DAQmxGetPauseTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4950"""
DAQmxSetPauseTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetPauseTrigType
DAQmxSetPauseTrigType.restype = int32
DAQmxSetPauseTrigType.argtypes = [TaskHandle, int32]
DAQmxSetPauseTrigType.__doc__ = \
"""int32 DAQmxSetPauseTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4951"""
DAQmxResetPauseTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetPauseTrigType
DAQmxResetPauseTrigType.restype = int32
DAQmxResetPauseTrigType.argtypes = [TaskHandle]
DAQmxResetPauseTrigType.__doc__ = \
"""int32 DAQmxResetPauseTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4952"""
DAQmxGetAnlgLvlPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgLvlPauseTrigSrc
DAQmxGetAnlgLvlPauseTrigSrc.restype = int32
DAQmxGetAnlgLvlPauseTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAnlgLvlPauseTrigSrc.__doc__ = \
"""int32 DAQmxGetAnlgLvlPauseTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4954"""
DAQmxSetAnlgLvlPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgLvlPauseTrigSrc
DAQmxSetAnlgLvlPauseTrigSrc.restype = int32
DAQmxSetAnlgLvlPauseTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAnlgLvlPauseTrigSrc.__doc__ = \
"""int32 DAQmxSetAnlgLvlPauseTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4955"""
DAQmxResetAnlgLvlPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgLvlPauseTrigSrc
DAQmxResetAnlgLvlPauseTrigSrc.restype = int32
DAQmxResetAnlgLvlPauseTrigSrc.argtypes = [TaskHandle]
DAQmxResetAnlgLvlPauseTrigSrc.__doc__ = \
"""int32 DAQmxResetAnlgLvlPauseTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4956"""
DAQmxGetAnlgLvlPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgLvlPauseTrigWhen
DAQmxGetAnlgLvlPauseTrigWhen.restype = int32
DAQmxGetAnlgLvlPauseTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgLvlPauseTrigWhen.__doc__ = \
"""int32 DAQmxGetAnlgLvlPauseTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4959"""
DAQmxSetAnlgLvlPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgLvlPauseTrigWhen
DAQmxSetAnlgLvlPauseTrigWhen.restype = int32
DAQmxSetAnlgLvlPauseTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetAnlgLvlPauseTrigWhen.__doc__ = \
"""int32 DAQmxSetAnlgLvlPauseTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4960"""
DAQmxResetAnlgLvlPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgLvlPauseTrigWhen
DAQmxResetAnlgLvlPauseTrigWhen.restype = int32
DAQmxResetAnlgLvlPauseTrigWhen.argtypes = [TaskHandle]
DAQmxResetAnlgLvlPauseTrigWhen.__doc__ = \
"""int32 DAQmxResetAnlgLvlPauseTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4961"""
DAQmxGetAnlgLvlPauseTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgLvlPauseTrigLvl
DAQmxGetAnlgLvlPauseTrigLvl.restype = int32
DAQmxGetAnlgLvlPauseTrigLvl.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgLvlPauseTrigLvl.__doc__ = \
"""int32 DAQmxGetAnlgLvlPauseTrigLvl(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4963"""
DAQmxSetAnlgLvlPauseTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgLvlPauseTrigLvl
DAQmxSetAnlgLvlPauseTrigLvl.restype = int32
DAQmxSetAnlgLvlPauseTrigLvl.argtypes = [TaskHandle, float64]
DAQmxSetAnlgLvlPauseTrigLvl.__doc__ = \
"""int32 DAQmxSetAnlgLvlPauseTrigLvl(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4964"""
DAQmxResetAnlgLvlPauseTrigLvl = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgLvlPauseTrigLvl
DAQmxResetAnlgLvlPauseTrigLvl.restype = int32
DAQmxResetAnlgLvlPauseTrigLvl.argtypes = [TaskHandle]
DAQmxResetAnlgLvlPauseTrigLvl.__doc__ = \
"""int32 DAQmxResetAnlgLvlPauseTrigLvl(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4965"""
DAQmxGetAnlgLvlPauseTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgLvlPauseTrigHyst
DAQmxGetAnlgLvlPauseTrigHyst.restype = int32
DAQmxGetAnlgLvlPauseTrigHyst.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgLvlPauseTrigHyst.__doc__ = \
"""int32 DAQmxGetAnlgLvlPauseTrigHyst(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4967"""
DAQmxSetAnlgLvlPauseTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgLvlPauseTrigHyst
DAQmxSetAnlgLvlPauseTrigHyst.restype = int32
DAQmxSetAnlgLvlPauseTrigHyst.argtypes = [TaskHandle, float64]
DAQmxSetAnlgLvlPauseTrigHyst.__doc__ = \
"""int32 DAQmxSetAnlgLvlPauseTrigHyst(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4968"""
DAQmxResetAnlgLvlPauseTrigHyst = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgLvlPauseTrigHyst
DAQmxResetAnlgLvlPauseTrigHyst.restype = int32
DAQmxResetAnlgLvlPauseTrigHyst.argtypes = [TaskHandle]
DAQmxResetAnlgLvlPauseTrigHyst.__doc__ = \
"""int32 DAQmxResetAnlgLvlPauseTrigHyst(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4969"""
DAQmxGetAnlgLvlPauseTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgLvlPauseTrigCoupling
DAQmxGetAnlgLvlPauseTrigCoupling.restype = int32
DAQmxGetAnlgLvlPauseTrigCoupling.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgLvlPauseTrigCoupling.__doc__ = \
"""int32 DAQmxGetAnlgLvlPauseTrigCoupling(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4972"""
DAQmxSetAnlgLvlPauseTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgLvlPauseTrigCoupling
DAQmxSetAnlgLvlPauseTrigCoupling.restype = int32
DAQmxSetAnlgLvlPauseTrigCoupling.argtypes = [TaskHandle, int32]
DAQmxSetAnlgLvlPauseTrigCoupling.__doc__ = \
"""int32 DAQmxSetAnlgLvlPauseTrigCoupling(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4973"""
DAQmxResetAnlgLvlPauseTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgLvlPauseTrigCoupling
DAQmxResetAnlgLvlPauseTrigCoupling.restype = int32
DAQmxResetAnlgLvlPauseTrigCoupling.argtypes = [TaskHandle]
DAQmxResetAnlgLvlPauseTrigCoupling.__doc__ = \
"""int32 DAQmxResetAnlgLvlPauseTrigCoupling(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4974"""
DAQmxGetAnlgWinPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinPauseTrigSrc
DAQmxGetAnlgWinPauseTrigSrc.restype = int32
DAQmxGetAnlgWinPauseTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetAnlgWinPauseTrigSrc.__doc__ = \
"""int32 DAQmxGetAnlgWinPauseTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4976"""
DAQmxSetAnlgWinPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinPauseTrigSrc
DAQmxSetAnlgWinPauseTrigSrc.restype = int32
DAQmxSetAnlgWinPauseTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetAnlgWinPauseTrigSrc.__doc__ = \
"""int32 DAQmxSetAnlgWinPauseTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4977"""
DAQmxResetAnlgWinPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinPauseTrigSrc
DAQmxResetAnlgWinPauseTrigSrc.restype = int32
DAQmxResetAnlgWinPauseTrigSrc.argtypes = [TaskHandle]
DAQmxResetAnlgWinPauseTrigSrc.__doc__ = \
"""int32 DAQmxResetAnlgWinPauseTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4978"""
DAQmxGetAnlgWinPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinPauseTrigWhen
DAQmxGetAnlgWinPauseTrigWhen.restype = int32
DAQmxGetAnlgWinPauseTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgWinPauseTrigWhen.__doc__ = \
"""int32 DAQmxGetAnlgWinPauseTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4981"""
DAQmxSetAnlgWinPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinPauseTrigWhen
DAQmxSetAnlgWinPauseTrigWhen.restype = int32
DAQmxSetAnlgWinPauseTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetAnlgWinPauseTrigWhen.__doc__ = \
"""int32 DAQmxSetAnlgWinPauseTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4982"""
DAQmxResetAnlgWinPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinPauseTrigWhen
DAQmxResetAnlgWinPauseTrigWhen.restype = int32
DAQmxResetAnlgWinPauseTrigWhen.argtypes = [TaskHandle]
DAQmxResetAnlgWinPauseTrigWhen.__doc__ = \
"""int32 DAQmxResetAnlgWinPauseTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4983"""
DAQmxGetAnlgWinPauseTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinPauseTrigTop
DAQmxGetAnlgWinPauseTrigTop.restype = int32
DAQmxGetAnlgWinPauseTrigTop.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgWinPauseTrigTop.__doc__ = \
"""int32 DAQmxGetAnlgWinPauseTrigTop(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4985"""
DAQmxSetAnlgWinPauseTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinPauseTrigTop
DAQmxSetAnlgWinPauseTrigTop.restype = int32
DAQmxSetAnlgWinPauseTrigTop.argtypes = [TaskHandle, float64]
DAQmxSetAnlgWinPauseTrigTop.__doc__ = \
"""int32 DAQmxSetAnlgWinPauseTrigTop(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4986"""
DAQmxResetAnlgWinPauseTrigTop = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinPauseTrigTop
DAQmxResetAnlgWinPauseTrigTop.restype = int32
DAQmxResetAnlgWinPauseTrigTop.argtypes = [TaskHandle]
DAQmxResetAnlgWinPauseTrigTop.__doc__ = \
"""int32 DAQmxResetAnlgWinPauseTrigTop(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4987"""
DAQmxGetAnlgWinPauseTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinPauseTrigBtm
DAQmxGetAnlgWinPauseTrigBtm.restype = int32
DAQmxGetAnlgWinPauseTrigBtm.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetAnlgWinPauseTrigBtm.__doc__ = \
"""int32 DAQmxGetAnlgWinPauseTrigBtm(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4989"""
DAQmxSetAnlgWinPauseTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinPauseTrigBtm
DAQmxSetAnlgWinPauseTrigBtm.restype = int32
DAQmxSetAnlgWinPauseTrigBtm.argtypes = [TaskHandle, float64]
DAQmxSetAnlgWinPauseTrigBtm.__doc__ = \
"""int32 DAQmxSetAnlgWinPauseTrigBtm(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4990"""
DAQmxResetAnlgWinPauseTrigBtm = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinPauseTrigBtm
DAQmxResetAnlgWinPauseTrigBtm.restype = int32
DAQmxResetAnlgWinPauseTrigBtm.argtypes = [TaskHandle]
DAQmxResetAnlgWinPauseTrigBtm.__doc__ = \
"""int32 DAQmxResetAnlgWinPauseTrigBtm(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4991"""
DAQmxGetAnlgWinPauseTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxGetAnlgWinPauseTrigCoupling
DAQmxGetAnlgWinPauseTrigCoupling.restype = int32
DAQmxGetAnlgWinPauseTrigCoupling.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetAnlgWinPauseTrigCoupling.__doc__ = \
"""int32 DAQmxGetAnlgWinPauseTrigCoupling(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4994"""
DAQmxSetAnlgWinPauseTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxSetAnlgWinPauseTrigCoupling
DAQmxSetAnlgWinPauseTrigCoupling.restype = int32
DAQmxSetAnlgWinPauseTrigCoupling.argtypes = [TaskHandle, int32]
DAQmxSetAnlgWinPauseTrigCoupling.__doc__ = \
"""int32 DAQmxSetAnlgWinPauseTrigCoupling(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4995"""
DAQmxResetAnlgWinPauseTrigCoupling = _stdcall_libraries['nicaiu.dll'].DAQmxResetAnlgWinPauseTrigCoupling
DAQmxResetAnlgWinPauseTrigCoupling.restype = int32
DAQmxResetAnlgWinPauseTrigCoupling.argtypes = [TaskHandle]
DAQmxResetAnlgWinPauseTrigCoupling.__doc__ = \
"""int32 DAQmxResetAnlgWinPauseTrigCoupling(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4996"""
DAQmxGetDigLvlPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigSrc
DAQmxGetDigLvlPauseTrigSrc.restype = int32
DAQmxGetDigLvlPauseTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigLvlPauseTrigSrc.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4998"""
DAQmxSetDigLvlPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigSrc
DAQmxSetDigLvlPauseTrigSrc.restype = int32
DAQmxSetDigLvlPauseTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigLvlPauseTrigSrc.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:4999"""
DAQmxResetDigLvlPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigSrc
DAQmxResetDigLvlPauseTrigSrc.restype = int32
DAQmxResetDigLvlPauseTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigSrc.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5000"""
DAQmxGetDigLvlPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigWhen
DAQmxGetDigLvlPauseTrigWhen.restype = int32
DAQmxGetDigLvlPauseTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigLvlPauseTrigWhen.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5003"""
DAQmxSetDigLvlPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigWhen
DAQmxSetDigLvlPauseTrigWhen.restype = int32
DAQmxSetDigLvlPauseTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetDigLvlPauseTrigWhen.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5004"""
DAQmxResetDigLvlPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigWhen
DAQmxResetDigLvlPauseTrigWhen.restype = int32
DAQmxResetDigLvlPauseTrigWhen.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigWhen.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5005"""
DAQmxGetDigLvlPauseTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigDigFltrEnable
DAQmxGetDigLvlPauseTrigDigFltrEnable.restype = int32
DAQmxGetDigLvlPauseTrigDigFltrEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigLvlPauseTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigDigFltrEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5007"""
DAQmxSetDigLvlPauseTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigDigFltrEnable
DAQmxSetDigLvlPauseTrigDigFltrEnable.restype = int32
DAQmxSetDigLvlPauseTrigDigFltrEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigLvlPauseTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigDigFltrEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5008"""
DAQmxResetDigLvlPauseTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigDigFltrEnable
DAQmxResetDigLvlPauseTrigDigFltrEnable.restype = int32
DAQmxResetDigLvlPauseTrigDigFltrEnable.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigDigFltrEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5009"""
DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth
DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth.restype = int32
DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5011"""
DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth
DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth.restype = int32
DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigDigFltrMinPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5012"""
DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth
DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth.restype = int32
DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigDigFltrMinPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5013"""
DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc
DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc.restype = int32
DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5015"""
DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc
DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc.restype = int32
DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5016"""
DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc
DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc.restype = int32
DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigDigFltrTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5017"""
DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate
DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate.restype = int32
DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5019"""
DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate
DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate.restype = int32
DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate.argtypes = [TaskHandle, float64]
DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigDigFltrTimebaseRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5020"""
DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate
DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate.restype = int32
DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigDigFltrTimebaseRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5021"""
DAQmxGetDigLvlPauseTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigLvlPauseTrigDigSyncEnable
DAQmxGetDigLvlPauseTrigDigSyncEnable.restype = int32
DAQmxGetDigLvlPauseTrigDigSyncEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigLvlPauseTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxGetDigLvlPauseTrigDigSyncEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5023"""
DAQmxSetDigLvlPauseTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigLvlPauseTrigDigSyncEnable
DAQmxSetDigLvlPauseTrigDigSyncEnable.restype = int32
DAQmxSetDigLvlPauseTrigDigSyncEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigLvlPauseTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxSetDigLvlPauseTrigDigSyncEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5024"""
DAQmxResetDigLvlPauseTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigLvlPauseTrigDigSyncEnable
DAQmxResetDigLvlPauseTrigDigSyncEnable.restype = int32
DAQmxResetDigLvlPauseTrigDigSyncEnable.argtypes = [TaskHandle]
DAQmxResetDigLvlPauseTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxResetDigLvlPauseTrigDigSyncEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5025"""
DAQmxGetDigPatternPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternPauseTrigSrc
DAQmxGetDigPatternPauseTrigSrc.restype = int32
DAQmxGetDigPatternPauseTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigPatternPauseTrigSrc.__doc__ = \
"""int32 DAQmxGetDigPatternPauseTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5027"""
DAQmxSetDigPatternPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternPauseTrigSrc
DAQmxSetDigPatternPauseTrigSrc.restype = int32
DAQmxSetDigPatternPauseTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigPatternPauseTrigSrc.__doc__ = \
"""int32 DAQmxSetDigPatternPauseTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5028"""
DAQmxResetDigPatternPauseTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternPauseTrigSrc
DAQmxResetDigPatternPauseTrigSrc.restype = int32
DAQmxResetDigPatternPauseTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigPatternPauseTrigSrc.__doc__ = \
"""int32 DAQmxResetDigPatternPauseTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5029"""
DAQmxGetDigPatternPauseTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternPauseTrigPattern
DAQmxGetDigPatternPauseTrigPattern.restype = int32
DAQmxGetDigPatternPauseTrigPattern.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigPatternPauseTrigPattern.__doc__ = \
"""int32 DAQmxGetDigPatternPauseTrigPattern(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5031"""
DAQmxSetDigPatternPauseTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternPauseTrigPattern
DAQmxSetDigPatternPauseTrigPattern.restype = int32
DAQmxSetDigPatternPauseTrigPattern.argtypes = [TaskHandle, STRING]
DAQmxSetDigPatternPauseTrigPattern.__doc__ = \
"""int32 DAQmxSetDigPatternPauseTrigPattern(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5032"""
DAQmxResetDigPatternPauseTrigPattern = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternPauseTrigPattern
DAQmxResetDigPatternPauseTrigPattern.restype = int32
DAQmxResetDigPatternPauseTrigPattern.argtypes = [TaskHandle]
DAQmxResetDigPatternPauseTrigPattern.__doc__ = \
"""int32 DAQmxResetDigPatternPauseTrigPattern(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5033"""
DAQmxGetDigPatternPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigPatternPauseTrigWhen
DAQmxGetDigPatternPauseTrigWhen.restype = int32
DAQmxGetDigPatternPauseTrigWhen.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigPatternPauseTrigWhen.__doc__ = \
"""int32 DAQmxGetDigPatternPauseTrigWhen(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5036"""
DAQmxSetDigPatternPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigPatternPauseTrigWhen
DAQmxSetDigPatternPauseTrigWhen.restype = int32
DAQmxSetDigPatternPauseTrigWhen.argtypes = [TaskHandle, int32]
DAQmxSetDigPatternPauseTrigWhen.__doc__ = \
"""int32 DAQmxSetDigPatternPauseTrigWhen(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5037"""
DAQmxResetDigPatternPauseTrigWhen = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigPatternPauseTrigWhen
DAQmxResetDigPatternPauseTrigWhen.restype = int32
DAQmxResetDigPatternPauseTrigWhen.argtypes = [TaskHandle]
DAQmxResetDigPatternPauseTrigWhen.__doc__ = \
"""int32 DAQmxResetDigPatternPauseTrigWhen(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5038"""
DAQmxGetArmStartTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetArmStartTrigType
DAQmxGetArmStartTrigType.restype = int32
DAQmxGetArmStartTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetArmStartTrigType.__doc__ = \
"""int32 DAQmxGetArmStartTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5041"""
DAQmxSetArmStartTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetArmStartTrigType
DAQmxSetArmStartTrigType.restype = int32
DAQmxSetArmStartTrigType.argtypes = [TaskHandle, int32]
DAQmxSetArmStartTrigType.__doc__ = \
"""int32 DAQmxSetArmStartTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5042"""
DAQmxResetArmStartTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetArmStartTrigType
DAQmxResetArmStartTrigType.restype = int32
DAQmxResetArmStartTrigType.argtypes = [TaskHandle]
DAQmxResetArmStartTrigType.__doc__ = \
"""int32 DAQmxResetArmStartTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5043"""
DAQmxGetDigEdgeArmStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigSrc
DAQmxGetDigEdgeArmStartTrigSrc.restype = int32
DAQmxGetDigEdgeArmStartTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeArmStartTrigSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5045"""
DAQmxSetDigEdgeArmStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigSrc
DAQmxSetDigEdgeArmStartTrigSrc.restype = int32
DAQmxSetDigEdgeArmStartTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeArmStartTrigSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5046"""
DAQmxResetDigEdgeArmStartTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigSrc
DAQmxResetDigEdgeArmStartTrigSrc.restype = int32
DAQmxResetDigEdgeArmStartTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5047"""
DAQmxGetDigEdgeArmStartTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigEdge
DAQmxGetDigEdgeArmStartTrigEdge.restype = int32
DAQmxGetDigEdgeArmStartTrigEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigEdgeArmStartTrigEdge.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5050"""
DAQmxSetDigEdgeArmStartTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigEdge
DAQmxSetDigEdgeArmStartTrigEdge.restype = int32
DAQmxSetDigEdgeArmStartTrigEdge.argtypes = [TaskHandle, int32]
DAQmxSetDigEdgeArmStartTrigEdge.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5051"""
DAQmxResetDigEdgeArmStartTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigEdge
DAQmxResetDigEdgeArmStartTrigEdge.restype = int32
DAQmxResetDigEdgeArmStartTrigEdge.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigEdge.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5052"""
DAQmxGetDigEdgeArmStartTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigDigFltrEnable
DAQmxGetDigEdgeArmStartTrigDigFltrEnable.restype = int32
DAQmxGetDigEdgeArmStartTrigDigFltrEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigEdgeArmStartTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigDigFltrEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5054"""
DAQmxSetDigEdgeArmStartTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigDigFltrEnable
DAQmxSetDigEdgeArmStartTrigDigFltrEnable.restype = int32
DAQmxSetDigEdgeArmStartTrigDigFltrEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigEdgeArmStartTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigDigFltrEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5055"""
DAQmxResetDigEdgeArmStartTrigDigFltrEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigDigFltrEnable
DAQmxResetDigEdgeArmStartTrigDigFltrEnable.restype = int32
DAQmxResetDigEdgeArmStartTrigDigFltrEnable.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigDigFltrEnable.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigDigFltrEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5056"""
DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth
DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth.restype = int32
DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5058"""
DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth
DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth.restype = int32
DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth.argtypes = [TaskHandle, float64]
DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigDigFltrMinPulseWidth(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5059"""
DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth
DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth.restype = int32
DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigDigFltrMinPulseWidth(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5060"""
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc.restype = int32
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5062"""
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc.restype = int32
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5063"""
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc.restype = int32
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5064"""
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate.restype = int32
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5066"""
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate.restype = int32
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate.argtypes = [TaskHandle, float64]
DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigDigFltrTimebaseRate(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5067"""
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate.restype = int32
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigDigFltrTimebaseRate(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5068"""
DAQmxGetDigEdgeArmStartTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeArmStartTrigDigSyncEnable
DAQmxGetDigEdgeArmStartTrigDigSyncEnable.restype = int32
DAQmxGetDigEdgeArmStartTrigDigSyncEnable.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetDigEdgeArmStartTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxGetDigEdgeArmStartTrigDigSyncEnable(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5070"""
DAQmxSetDigEdgeArmStartTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeArmStartTrigDigSyncEnable
DAQmxSetDigEdgeArmStartTrigDigSyncEnable.restype = int32
DAQmxSetDigEdgeArmStartTrigDigSyncEnable.argtypes = [TaskHandle, bool32]
DAQmxSetDigEdgeArmStartTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxSetDigEdgeArmStartTrigDigSyncEnable(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5071"""
DAQmxResetDigEdgeArmStartTrigDigSyncEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeArmStartTrigDigSyncEnable
DAQmxResetDigEdgeArmStartTrigDigSyncEnable.restype = int32
DAQmxResetDigEdgeArmStartTrigDigSyncEnable.argtypes = [TaskHandle]
DAQmxResetDigEdgeArmStartTrigDigSyncEnable.__doc__ = \
"""int32 DAQmxResetDigEdgeArmStartTrigDigSyncEnable(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5072"""
DAQmxGetWatchdogTimeout = _stdcall_libraries['nicaiu.dll'].DAQmxGetWatchdogTimeout
DAQmxGetWatchdogTimeout.restype = int32
DAQmxGetWatchdogTimeout.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetWatchdogTimeout.__doc__ = \
"""int32 DAQmxGetWatchdogTimeout(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5076"""
DAQmxSetWatchdogTimeout = _stdcall_libraries['nicaiu.dll'].DAQmxSetWatchdogTimeout
DAQmxSetWatchdogTimeout.restype = int32
DAQmxSetWatchdogTimeout.argtypes = [TaskHandle, float64]
DAQmxSetWatchdogTimeout.__doc__ = \
"""int32 DAQmxSetWatchdogTimeout(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5077"""
DAQmxResetWatchdogTimeout = _stdcall_libraries['nicaiu.dll'].DAQmxResetWatchdogTimeout
DAQmxResetWatchdogTimeout.restype = int32
DAQmxResetWatchdogTimeout.argtypes = [TaskHandle]
DAQmxResetWatchdogTimeout.__doc__ = \
"""int32 DAQmxResetWatchdogTimeout(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5078"""
DAQmxGetWatchdogExpirTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxGetWatchdogExpirTrigType
DAQmxGetWatchdogExpirTrigType.restype = int32
DAQmxGetWatchdogExpirTrigType.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetWatchdogExpirTrigType.__doc__ = \
"""int32 DAQmxGetWatchdogExpirTrigType(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5081"""
DAQmxSetWatchdogExpirTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxSetWatchdogExpirTrigType
DAQmxSetWatchdogExpirTrigType.restype = int32
DAQmxSetWatchdogExpirTrigType.argtypes = [TaskHandle, int32]
DAQmxSetWatchdogExpirTrigType.__doc__ = \
"""int32 DAQmxSetWatchdogExpirTrigType(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5082"""
DAQmxResetWatchdogExpirTrigType = _stdcall_libraries['nicaiu.dll'].DAQmxResetWatchdogExpirTrigType
DAQmxResetWatchdogExpirTrigType.restype = int32
DAQmxResetWatchdogExpirTrigType.argtypes = [TaskHandle]
DAQmxResetWatchdogExpirTrigType.__doc__ = \
"""int32 DAQmxResetWatchdogExpirTrigType(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5083"""
DAQmxGetDigEdgeWatchdogExpirTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeWatchdogExpirTrigSrc
DAQmxGetDigEdgeWatchdogExpirTrigSrc.restype = int32
DAQmxGetDigEdgeWatchdogExpirTrigSrc.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetDigEdgeWatchdogExpirTrigSrc.__doc__ = \
"""int32 DAQmxGetDigEdgeWatchdogExpirTrigSrc(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5085"""
DAQmxSetDigEdgeWatchdogExpirTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeWatchdogExpirTrigSrc
DAQmxSetDigEdgeWatchdogExpirTrigSrc.restype = int32
DAQmxSetDigEdgeWatchdogExpirTrigSrc.argtypes = [TaskHandle, STRING]
DAQmxSetDigEdgeWatchdogExpirTrigSrc.__doc__ = \
"""int32 DAQmxSetDigEdgeWatchdogExpirTrigSrc(TaskHandle taskHandle, unknown * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5086"""
DAQmxResetDigEdgeWatchdogExpirTrigSrc = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeWatchdogExpirTrigSrc
DAQmxResetDigEdgeWatchdogExpirTrigSrc.restype = int32
DAQmxResetDigEdgeWatchdogExpirTrigSrc.argtypes = [TaskHandle]
DAQmxResetDigEdgeWatchdogExpirTrigSrc.__doc__ = \
"""int32 DAQmxResetDigEdgeWatchdogExpirTrigSrc(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5087"""
DAQmxGetDigEdgeWatchdogExpirTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxGetDigEdgeWatchdogExpirTrigEdge
DAQmxGetDigEdgeWatchdogExpirTrigEdge.restype = int32
DAQmxGetDigEdgeWatchdogExpirTrigEdge.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetDigEdgeWatchdogExpirTrigEdge.__doc__ = \
"""int32 DAQmxGetDigEdgeWatchdogExpirTrigEdge(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5090"""
DAQmxSetDigEdgeWatchdogExpirTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxSetDigEdgeWatchdogExpirTrigEdge
DAQmxSetDigEdgeWatchdogExpirTrigEdge.restype = int32
DAQmxSetDigEdgeWatchdogExpirTrigEdge.argtypes = [TaskHandle, int32]
DAQmxSetDigEdgeWatchdogExpirTrigEdge.__doc__ = \
"""int32 DAQmxSetDigEdgeWatchdogExpirTrigEdge(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5091"""
DAQmxResetDigEdgeWatchdogExpirTrigEdge = _stdcall_libraries['nicaiu.dll'].DAQmxResetDigEdgeWatchdogExpirTrigEdge
DAQmxResetDigEdgeWatchdogExpirTrigEdge.restype = int32
DAQmxResetDigEdgeWatchdogExpirTrigEdge.argtypes = [TaskHandle]
DAQmxResetDigEdgeWatchdogExpirTrigEdge.__doc__ = \
"""int32 DAQmxResetDigEdgeWatchdogExpirTrigEdge(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5092"""
DAQmxGetWatchdogDOExpirState = _stdcall_libraries['nicaiu.dll'].DAQmxGetWatchdogDOExpirState
DAQmxGetWatchdogDOExpirState.restype = int32
DAQmxGetWatchdogDOExpirState.argtypes = [TaskHandle, STRING, POINTER(int32)]
DAQmxGetWatchdogDOExpirState.__doc__ = \
"""int32 DAQmxGetWatchdogDOExpirState(TaskHandle taskHandle, unknown * lines, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5095"""
DAQmxSetWatchdogDOExpirState = _stdcall_libraries['nicaiu.dll'].DAQmxSetWatchdogDOExpirState
DAQmxSetWatchdogDOExpirState.restype = int32
DAQmxSetWatchdogDOExpirState.argtypes = [TaskHandle, STRING, int32]
DAQmxSetWatchdogDOExpirState.__doc__ = \
"""int32 DAQmxSetWatchdogDOExpirState(TaskHandle taskHandle, unknown * lines, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5096"""
DAQmxResetWatchdogDOExpirState = _stdcall_libraries['nicaiu.dll'].DAQmxResetWatchdogDOExpirState
DAQmxResetWatchdogDOExpirState.restype = int32
DAQmxResetWatchdogDOExpirState.argtypes = [TaskHandle, STRING]
DAQmxResetWatchdogDOExpirState.__doc__ = \
"""int32 DAQmxResetWatchdogDOExpirState(TaskHandle taskHandle, unknown * lines)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5097"""
DAQmxGetWatchdogHasExpired = _stdcall_libraries['nicaiu.dll'].DAQmxGetWatchdogHasExpired
DAQmxGetWatchdogHasExpired.restype = int32
DAQmxGetWatchdogHasExpired.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetWatchdogHasExpired.__doc__ = \
"""int32 DAQmxGetWatchdogHasExpired(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5099"""
DAQmxGetWriteRelativeTo = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteRelativeTo
DAQmxGetWriteRelativeTo.restype = int32
DAQmxGetWriteRelativeTo.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetWriteRelativeTo.__doc__ = \
"""int32 DAQmxGetWriteRelativeTo(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5104"""
DAQmxSetWriteRelativeTo = _stdcall_libraries['nicaiu.dll'].DAQmxSetWriteRelativeTo
DAQmxSetWriteRelativeTo.restype = int32
DAQmxSetWriteRelativeTo.argtypes = [TaskHandle, int32]
DAQmxSetWriteRelativeTo.__doc__ = \
"""int32 DAQmxSetWriteRelativeTo(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5105"""
DAQmxResetWriteRelativeTo = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteRelativeTo
DAQmxResetWriteRelativeTo.restype = int32
DAQmxResetWriteRelativeTo.argtypes = [TaskHandle]
DAQmxResetWriteRelativeTo.__doc__ = \
"""int32 DAQmxResetWriteRelativeTo(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5106"""
DAQmxGetWriteOffset = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteOffset
DAQmxGetWriteOffset.restype = int32
DAQmxGetWriteOffset.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetWriteOffset.__doc__ = \
"""int32 DAQmxGetWriteOffset(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5108"""
DAQmxSetWriteOffset = _stdcall_libraries['nicaiu.dll'].DAQmxSetWriteOffset
DAQmxSetWriteOffset.restype = int32
DAQmxSetWriteOffset.argtypes = [TaskHandle, int32]
DAQmxSetWriteOffset.__doc__ = \
"""int32 DAQmxSetWriteOffset(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5109"""
DAQmxResetWriteOffset = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteOffset
DAQmxResetWriteOffset.restype = int32
DAQmxResetWriteOffset.argtypes = [TaskHandle]
DAQmxResetWriteOffset.__doc__ = \
"""int32 DAQmxResetWriteOffset(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5110"""
DAQmxGetWriteRegenMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteRegenMode
DAQmxGetWriteRegenMode.restype = int32
DAQmxGetWriteRegenMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetWriteRegenMode.__doc__ = \
"""int32 DAQmxGetWriteRegenMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5113"""
DAQmxSetWriteRegenMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetWriteRegenMode
DAQmxSetWriteRegenMode.restype = int32
DAQmxSetWriteRegenMode.argtypes = [TaskHandle, int32]
DAQmxSetWriteRegenMode.__doc__ = \
"""int32 DAQmxSetWriteRegenMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5114"""
DAQmxResetWriteRegenMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteRegenMode
DAQmxResetWriteRegenMode.restype = int32
DAQmxResetWriteRegenMode.argtypes = [TaskHandle]
DAQmxResetWriteRegenMode.__doc__ = \
"""int32 DAQmxResetWriteRegenMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5115"""
DAQmxGetWriteCurrWritePos = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteCurrWritePos
DAQmxGetWriteCurrWritePos.restype = int32
DAQmxGetWriteCurrWritePos.argtypes = [TaskHandle, POINTER(uInt64)]
DAQmxGetWriteCurrWritePos.__doc__ = \
"""int32 DAQmxGetWriteCurrWritePos(TaskHandle taskHandle, uInt64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5117"""
DAQmxGetWriteOvercurrentChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteOvercurrentChansExist
DAQmxGetWriteOvercurrentChansExist.restype = int32
DAQmxGetWriteOvercurrentChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetWriteOvercurrentChansExist.__doc__ = \
"""int32 DAQmxGetWriteOvercurrentChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5119"""
DAQmxGetWriteOvercurrentChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteOvercurrentChans
DAQmxGetWriteOvercurrentChans.restype = int32
DAQmxGetWriteOvercurrentChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetWriteOvercurrentChans.__doc__ = \
"""int32 DAQmxGetWriteOvercurrentChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5121"""
DAQmxGetWriteOvertemperatureChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteOvertemperatureChansExist
DAQmxGetWriteOvertemperatureChansExist.restype = int32
DAQmxGetWriteOvertemperatureChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetWriteOvertemperatureChansExist.__doc__ = \
"""int32 DAQmxGetWriteOvertemperatureChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5123"""
DAQmxGetWriteOpenCurrentLoopChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteOpenCurrentLoopChansExist
DAQmxGetWriteOpenCurrentLoopChansExist.restype = int32
DAQmxGetWriteOpenCurrentLoopChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetWriteOpenCurrentLoopChansExist.__doc__ = \
"""int32 DAQmxGetWriteOpenCurrentLoopChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5125"""
DAQmxGetWriteOpenCurrentLoopChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteOpenCurrentLoopChans
DAQmxGetWriteOpenCurrentLoopChans.restype = int32
DAQmxGetWriteOpenCurrentLoopChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetWriteOpenCurrentLoopChans.__doc__ = \
"""int32 DAQmxGetWriteOpenCurrentLoopChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5127"""
DAQmxGetWritePowerSupplyFaultChansExist = _stdcall_libraries['nicaiu.dll'].DAQmxGetWritePowerSupplyFaultChansExist
DAQmxGetWritePowerSupplyFaultChansExist.restype = int32
DAQmxGetWritePowerSupplyFaultChansExist.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetWritePowerSupplyFaultChansExist.__doc__ = \
"""int32 DAQmxGetWritePowerSupplyFaultChansExist(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5129"""
DAQmxGetWritePowerSupplyFaultChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetWritePowerSupplyFaultChans
DAQmxGetWritePowerSupplyFaultChans.restype = int32
DAQmxGetWritePowerSupplyFaultChans.argtypes = [TaskHandle, STRING, uInt32]
DAQmxGetWritePowerSupplyFaultChans.__doc__ = \
"""int32 DAQmxGetWritePowerSupplyFaultChans(TaskHandle taskHandle, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5131"""
DAQmxGetWriteSpaceAvail = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteSpaceAvail
DAQmxGetWriteSpaceAvail.restype = int32
DAQmxGetWriteSpaceAvail.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetWriteSpaceAvail.__doc__ = \
"""int32 DAQmxGetWriteSpaceAvail(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5133"""
DAQmxGetWriteTotalSampPerChanGenerated = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteTotalSampPerChanGenerated
DAQmxGetWriteTotalSampPerChanGenerated.restype = int32
DAQmxGetWriteTotalSampPerChanGenerated.argtypes = [TaskHandle, POINTER(uInt64)]
DAQmxGetWriteTotalSampPerChanGenerated.__doc__ = \
"""int32 DAQmxGetWriteTotalSampPerChanGenerated(TaskHandle taskHandle, uInt64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5135"""
DAQmxGetWriteRawDataWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteRawDataWidth
DAQmxGetWriteRawDataWidth.restype = int32
DAQmxGetWriteRawDataWidth.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetWriteRawDataWidth.__doc__ = \
"""int32 DAQmxGetWriteRawDataWidth(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5137"""
DAQmxGetWriteNumChans = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteNumChans
DAQmxGetWriteNumChans.restype = int32
DAQmxGetWriteNumChans.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetWriteNumChans.__doc__ = \
"""int32 DAQmxGetWriteNumChans(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5139"""
DAQmxGetWriteWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteWaitMode
DAQmxGetWriteWaitMode.restype = int32
DAQmxGetWriteWaitMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetWriteWaitMode.__doc__ = \
"""int32 DAQmxGetWriteWaitMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5142"""
DAQmxSetWriteWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetWriteWaitMode
DAQmxSetWriteWaitMode.restype = int32
DAQmxSetWriteWaitMode.argtypes = [TaskHandle, int32]
DAQmxSetWriteWaitMode.__doc__ = \
"""int32 DAQmxSetWriteWaitMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5143"""
DAQmxResetWriteWaitMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteWaitMode
DAQmxResetWriteWaitMode.restype = int32
DAQmxResetWriteWaitMode.argtypes = [TaskHandle]
DAQmxResetWriteWaitMode.__doc__ = \
"""int32 DAQmxResetWriteWaitMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5144"""
DAQmxGetWriteSleepTime = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteSleepTime
DAQmxGetWriteSleepTime.restype = int32
DAQmxGetWriteSleepTime.argtypes = [TaskHandle, POINTER(float64)]
DAQmxGetWriteSleepTime.__doc__ = \
"""int32 DAQmxGetWriteSleepTime(TaskHandle taskHandle, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5146"""
DAQmxSetWriteSleepTime = _stdcall_libraries['nicaiu.dll'].DAQmxSetWriteSleepTime
DAQmxSetWriteSleepTime.restype = int32
DAQmxSetWriteSleepTime.argtypes = [TaskHandle, float64]
DAQmxSetWriteSleepTime.__doc__ = \
"""int32 DAQmxSetWriteSleepTime(TaskHandle taskHandle, float64 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5147"""
DAQmxResetWriteSleepTime = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteSleepTime
DAQmxResetWriteSleepTime.restype = int32
DAQmxResetWriteSleepTime.argtypes = [TaskHandle]
DAQmxResetWriteSleepTime.__doc__ = \
"""int32 DAQmxResetWriteSleepTime(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5148"""
DAQmxGetWriteNextWriteIsLast = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteNextWriteIsLast
DAQmxGetWriteNextWriteIsLast.restype = int32
DAQmxGetWriteNextWriteIsLast.argtypes = [TaskHandle, POINTER(bool32)]
DAQmxGetWriteNextWriteIsLast.__doc__ = \
"""int32 DAQmxGetWriteNextWriteIsLast(TaskHandle taskHandle, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5150"""
DAQmxSetWriteNextWriteIsLast = _stdcall_libraries['nicaiu.dll'].DAQmxSetWriteNextWriteIsLast
DAQmxSetWriteNextWriteIsLast.restype = int32
DAQmxSetWriteNextWriteIsLast.argtypes = [TaskHandle, bool32]
DAQmxSetWriteNextWriteIsLast.__doc__ = \
"""int32 DAQmxSetWriteNextWriteIsLast(TaskHandle taskHandle, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5151"""
DAQmxResetWriteNextWriteIsLast = _stdcall_libraries['nicaiu.dll'].DAQmxResetWriteNextWriteIsLast
DAQmxResetWriteNextWriteIsLast.restype = int32
DAQmxResetWriteNextWriteIsLast.argtypes = [TaskHandle]
DAQmxResetWriteNextWriteIsLast.__doc__ = \
"""int32 DAQmxResetWriteNextWriteIsLast(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5152"""
DAQmxGetWriteDigitalLinesBytesPerChan = _stdcall_libraries['nicaiu.dll'].DAQmxGetWriteDigitalLinesBytesPerChan
DAQmxGetWriteDigitalLinesBytesPerChan.restype = int32
DAQmxGetWriteDigitalLinesBytesPerChan.argtypes = [TaskHandle, POINTER(uInt32)]
DAQmxGetWriteDigitalLinesBytesPerChan.__doc__ = \
"""int32 DAQmxGetWriteDigitalLinesBytesPerChan(TaskHandle taskHandle, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5154"""
DAQmxGetPhysicalChanAITermCfgs = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanAITermCfgs
DAQmxGetPhysicalChanAITermCfgs.restype = int32
DAQmxGetPhysicalChanAITermCfgs.argtypes = [STRING, POINTER(int32)]
DAQmxGetPhysicalChanAITermCfgs.__doc__ = \
"""int32 DAQmxGetPhysicalChanAITermCfgs(unknown * physicalChannel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5159"""
DAQmxGetPhysicalChanAOTermCfgs = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanAOTermCfgs
DAQmxGetPhysicalChanAOTermCfgs.restype = int32
DAQmxGetPhysicalChanAOTermCfgs.argtypes = [STRING, POINTER(int32)]
DAQmxGetPhysicalChanAOTermCfgs.__doc__ = \
"""int32 DAQmxGetPhysicalChanAOTermCfgs(unknown * physicalChannel, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5162"""
DAQmxGetPhysicalChanAOManualControlEnable = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanAOManualControlEnable
DAQmxGetPhysicalChanAOManualControlEnable.restype = int32
DAQmxGetPhysicalChanAOManualControlEnable.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPhysicalChanAOManualControlEnable.__doc__ = \
"""int32 DAQmxGetPhysicalChanAOManualControlEnable(unknown * physicalChannel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5164"""
DAQmxSetPhysicalChanAOManualControlEnable = _stdcall_libraries['nicaiu.dll'].DAQmxSetPhysicalChanAOManualControlEnable
DAQmxSetPhysicalChanAOManualControlEnable.restype = int32
DAQmxSetPhysicalChanAOManualControlEnable.argtypes = [STRING, bool32]
DAQmxSetPhysicalChanAOManualControlEnable.__doc__ = \
"""int32 DAQmxSetPhysicalChanAOManualControlEnable(unknown * physicalChannel, bool32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5165"""
DAQmxResetPhysicalChanAOManualControlEnable = _stdcall_libraries['nicaiu.dll'].DAQmxResetPhysicalChanAOManualControlEnable
DAQmxResetPhysicalChanAOManualControlEnable.restype = int32
DAQmxResetPhysicalChanAOManualControlEnable.argtypes = [STRING]
DAQmxResetPhysicalChanAOManualControlEnable.__doc__ = \
"""int32 DAQmxResetPhysicalChanAOManualControlEnable(unknown * physicalChannel)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5166"""
DAQmxGetPhysicalChanAOManualControlShortDetected = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanAOManualControlShortDetected
DAQmxGetPhysicalChanAOManualControlShortDetected.restype = int32
DAQmxGetPhysicalChanAOManualControlShortDetected.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPhysicalChanAOManualControlShortDetected.__doc__ = \
"""int32 DAQmxGetPhysicalChanAOManualControlShortDetected(unknown * physicalChannel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5168"""
DAQmxGetPhysicalChanAOManualControlAmplitude = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanAOManualControlAmplitude
DAQmxGetPhysicalChanAOManualControlAmplitude.restype = int32
DAQmxGetPhysicalChanAOManualControlAmplitude.argtypes = [STRING, POINTER(float64)]
DAQmxGetPhysicalChanAOManualControlAmplitude.__doc__ = \
"""int32 DAQmxGetPhysicalChanAOManualControlAmplitude(unknown * physicalChannel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5170"""
DAQmxGetPhysicalChanAOManualControlFreq = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanAOManualControlFreq
DAQmxGetPhysicalChanAOManualControlFreq.restype = int32
DAQmxGetPhysicalChanAOManualControlFreq.argtypes = [STRING, POINTER(float64)]
DAQmxGetPhysicalChanAOManualControlFreq.__doc__ = \
"""int32 DAQmxGetPhysicalChanAOManualControlFreq(unknown * physicalChannel, float64 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5172"""
DAQmxGetPhysicalChanDIPortWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanDIPortWidth
DAQmxGetPhysicalChanDIPortWidth.restype = int32
DAQmxGetPhysicalChanDIPortWidth.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetPhysicalChanDIPortWidth.__doc__ = \
"""int32 DAQmxGetPhysicalChanDIPortWidth(unknown * physicalChannel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5174"""
DAQmxGetPhysicalChanDISampClkSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanDISampClkSupported
DAQmxGetPhysicalChanDISampClkSupported.restype = int32
DAQmxGetPhysicalChanDISampClkSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPhysicalChanDISampClkSupported.__doc__ = \
"""int32 DAQmxGetPhysicalChanDISampClkSupported(unknown * physicalChannel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5176"""
DAQmxGetPhysicalChanDIChangeDetectSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanDIChangeDetectSupported
DAQmxGetPhysicalChanDIChangeDetectSupported.restype = int32
DAQmxGetPhysicalChanDIChangeDetectSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPhysicalChanDIChangeDetectSupported.__doc__ = \
"""int32 DAQmxGetPhysicalChanDIChangeDetectSupported(unknown * physicalChannel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5178"""
DAQmxGetPhysicalChanDOPortWidth = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanDOPortWidth
DAQmxGetPhysicalChanDOPortWidth.restype = int32
DAQmxGetPhysicalChanDOPortWidth.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetPhysicalChanDOPortWidth.__doc__ = \
"""int32 DAQmxGetPhysicalChanDOPortWidth(unknown * physicalChannel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5180"""
DAQmxGetPhysicalChanDOSampClkSupported = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanDOSampClkSupported
DAQmxGetPhysicalChanDOSampClkSupported.restype = int32
DAQmxGetPhysicalChanDOSampClkSupported.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPhysicalChanDOSampClkSupported.__doc__ = \
"""int32 DAQmxGetPhysicalChanDOSampClkSupported(unknown * physicalChannel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5182"""
DAQmxGetPhysicalChanTEDSMfgID = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSMfgID
DAQmxGetPhysicalChanTEDSMfgID.restype = int32
DAQmxGetPhysicalChanTEDSMfgID.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetPhysicalChanTEDSMfgID.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSMfgID(unknown * physicalChannel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5184"""
DAQmxGetPhysicalChanTEDSModelNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSModelNum
DAQmxGetPhysicalChanTEDSModelNum.restype = int32
DAQmxGetPhysicalChanTEDSModelNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetPhysicalChanTEDSModelNum.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSModelNum(unknown * physicalChannel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5186"""
DAQmxGetPhysicalChanTEDSSerialNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSSerialNum
DAQmxGetPhysicalChanTEDSSerialNum.restype = int32
DAQmxGetPhysicalChanTEDSSerialNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetPhysicalChanTEDSSerialNum.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSSerialNum(unknown * physicalChannel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5188"""
DAQmxGetPhysicalChanTEDSVersionNum = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSVersionNum
DAQmxGetPhysicalChanTEDSVersionNum.restype = int32
DAQmxGetPhysicalChanTEDSVersionNum.argtypes = [STRING, POINTER(uInt32)]
DAQmxGetPhysicalChanTEDSVersionNum.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSVersionNum(unknown * physicalChannel, uInt32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5190"""
DAQmxGetPhysicalChanTEDSVersionLetter = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSVersionLetter
DAQmxGetPhysicalChanTEDSVersionLetter.restype = int32
DAQmxGetPhysicalChanTEDSVersionLetter.argtypes = [STRING, STRING, uInt32]
DAQmxGetPhysicalChanTEDSVersionLetter.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSVersionLetter(unknown * physicalChannel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5192"""
DAQmxGetPhysicalChanTEDSBitStream = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSBitStream
DAQmxGetPhysicalChanTEDSBitStream.restype = int32
DAQmxGetPhysicalChanTEDSBitStream.argtypes = [STRING, POINTER(uInt8), uInt32]
DAQmxGetPhysicalChanTEDSBitStream.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSBitStream(unknown * physicalChannel, uInt8 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5194"""
DAQmxGetPhysicalChanTEDSTemplateIDs = _stdcall_libraries['nicaiu.dll'].DAQmxGetPhysicalChanTEDSTemplateIDs
DAQmxGetPhysicalChanTEDSTemplateIDs.restype = int32
DAQmxGetPhysicalChanTEDSTemplateIDs.argtypes = [STRING, POINTER(uInt32), uInt32]
DAQmxGetPhysicalChanTEDSTemplateIDs.__doc__ = \
"""int32 DAQmxGetPhysicalChanTEDSTemplateIDs(unknown * physicalChannel, uInt32 * data, uInt32 arraySizeInSamples)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5196"""
DAQmxGetPersistedTaskAuthor = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedTaskAuthor
DAQmxGetPersistedTaskAuthor.restype = int32
DAQmxGetPersistedTaskAuthor.argtypes = [STRING, STRING, uInt32]
DAQmxGetPersistedTaskAuthor.__doc__ = \
"""int32 DAQmxGetPersistedTaskAuthor(unknown * taskName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5200"""
DAQmxGetPersistedTaskAllowInteractiveEditing = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedTaskAllowInteractiveEditing
DAQmxGetPersistedTaskAllowInteractiveEditing.restype = int32
DAQmxGetPersistedTaskAllowInteractiveEditing.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPersistedTaskAllowInteractiveEditing.__doc__ = \
"""int32 DAQmxGetPersistedTaskAllowInteractiveEditing(unknown * taskName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5202"""
DAQmxGetPersistedTaskAllowInteractiveDeletion = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedTaskAllowInteractiveDeletion
DAQmxGetPersistedTaskAllowInteractiveDeletion.restype = int32
DAQmxGetPersistedTaskAllowInteractiveDeletion.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPersistedTaskAllowInteractiveDeletion.__doc__ = \
"""int32 DAQmxGetPersistedTaskAllowInteractiveDeletion(unknown * taskName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5204"""
DAQmxGetPersistedChanAuthor = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedChanAuthor
DAQmxGetPersistedChanAuthor.restype = int32
DAQmxGetPersistedChanAuthor.argtypes = [STRING, STRING, uInt32]
DAQmxGetPersistedChanAuthor.__doc__ = \
"""int32 DAQmxGetPersistedChanAuthor(unknown * channel, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5208"""
DAQmxGetPersistedChanAllowInteractiveEditing = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedChanAllowInteractiveEditing
DAQmxGetPersistedChanAllowInteractiveEditing.restype = int32
DAQmxGetPersistedChanAllowInteractiveEditing.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPersistedChanAllowInteractiveEditing.__doc__ = \
"""int32 DAQmxGetPersistedChanAllowInteractiveEditing(unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5210"""
DAQmxGetPersistedChanAllowInteractiveDeletion = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedChanAllowInteractiveDeletion
DAQmxGetPersistedChanAllowInteractiveDeletion.restype = int32
DAQmxGetPersistedChanAllowInteractiveDeletion.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPersistedChanAllowInteractiveDeletion.__doc__ = \
"""int32 DAQmxGetPersistedChanAllowInteractiveDeletion(unknown * channel, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5212"""
DAQmxGetPersistedScaleAuthor = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedScaleAuthor
DAQmxGetPersistedScaleAuthor.restype = int32
DAQmxGetPersistedScaleAuthor.argtypes = [STRING, STRING, uInt32]
DAQmxGetPersistedScaleAuthor.__doc__ = \
"""int32 DAQmxGetPersistedScaleAuthor(unknown * scaleName, char * data, uInt32 bufferSize)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5216"""
DAQmxGetPersistedScaleAllowInteractiveEditing = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedScaleAllowInteractiveEditing
DAQmxGetPersistedScaleAllowInteractiveEditing.restype = int32
DAQmxGetPersistedScaleAllowInteractiveEditing.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPersistedScaleAllowInteractiveEditing.__doc__ = \
"""int32 DAQmxGetPersistedScaleAllowInteractiveEditing(unknown * scaleName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5218"""
DAQmxGetPersistedScaleAllowInteractiveDeletion = _stdcall_libraries['nicaiu.dll'].DAQmxGetPersistedScaleAllowInteractiveDeletion
DAQmxGetPersistedScaleAllowInteractiveDeletion.restype = int32
DAQmxGetPersistedScaleAllowInteractiveDeletion.argtypes = [STRING, POINTER(bool32)]
DAQmxGetPersistedScaleAllowInteractiveDeletion.__doc__ = \
"""int32 DAQmxGetPersistedScaleAllowInteractiveDeletion(unknown * scaleName, bool32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5220"""
DAQmxGetSampClkTimingResponseMode = _stdcall_libraries['nicaiu.dll'].DAQmxGetSampClkTimingResponseMode
DAQmxGetSampClkTimingResponseMode.restype = int32
DAQmxGetSampClkTimingResponseMode.argtypes = [TaskHandle, POINTER(int32)]
DAQmxGetSampClkTimingResponseMode.__doc__ = \
"""int32 DAQmxGetSampClkTimingResponseMode(TaskHandle taskHandle, int32 * data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5225"""
DAQmxSetSampClkTimingResponseMode = _stdcall_libraries['nicaiu.dll'].DAQmxSetSampClkTimingResponseMode
DAQmxSetSampClkTimingResponseMode.restype = int32
DAQmxSetSampClkTimingResponseMode.argtypes = [TaskHandle, int32]
DAQmxSetSampClkTimingResponseMode.__doc__ = \
"""int32 DAQmxSetSampClkTimingResponseMode(TaskHandle taskHandle, int32 data)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5226"""
DAQmxResetSampClkTimingResponseMode = _stdcall_libraries['nicaiu.dll'].DAQmxResetSampClkTimingResponseMode
DAQmxResetSampClkTimingResponseMode.restype = int32
DAQmxResetSampClkTimingResponseMode.argtypes = [TaskHandle]
DAQmxResetSampClkTimingResponseMode.__doc__ = \
"""int32 DAQmxResetSampClkTimingResponseMode(TaskHandle taskHandle)
C:/Program Files/gccxml 0.9/share/gccxml-0.9/Vc9/Include/NIDAQmx.h:5227"""
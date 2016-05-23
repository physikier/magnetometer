import numpy as np
import ctypes



nidaq = ctypes.windll.nicaiu 

# typedefs are setup to correspond to NIDAQmx.h
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32
written = int32()
pointsRead = uInt32()

#constants are setup to correspond to NIDAQmx.h
DAQmx_Val_Volts = 10348
DAQmx_Val_Falling = 10171
DAQmx_Val_Rising = 10280
DAQmx_Val_Cfg_Default = int32(-1)
DAQmx_Val_ContSamps = 10123
DAQmx_Val_ChanForAllLines = 1
DAQmx_Val_RSE = 10083
DAQmx_Val_Volts = 10348
DAQmx_Val_GroupByScanNumber = 1
DAQmx_Val_FiniteSamps = 10178
DAQmx_Val_GroupByChannel = 0

# initialize variables
taskHandle = TaskHandle(0)

#range of the DAQ
min1 = float64(0.0) 
max1 = float64(5.0)
timeout = float64(10.0)
bufferSize = uInt32(10)
pointsToRead = bufferSize
pointsRead = uInt32()

sampleBufferSize = uInt64(100000)

sampleRate = float64(200000.0)  # sampling rate in samples per second
detectionTime = float(1) # detection time in seconds
numberPoints = int(sampleRate.value*detectionTime)
delta_t=1/sampleRate.value
triggerSource=ctypes.create_string_buffer('/Dev2/pfi0')
triggerLevel = float64(0.)

chan = ctypes.create_string_buffer('/Dev2/ai0')
clockSource = ctypes.create_string_buffer('OnboardClock')

def SetupTask():
    nidaq.DAQmxCreateTask("",ctypes.byref(taskHandle))
    nidaq.DAQmxCreateAIVoltageChan(taskHandle, chan, "", DAQmx_Val_Cfg_Default, min1, max1,DAQmx_Val_Volts,None)
    nidaq.DAQmxCfgSampClkTiming(taskHandle,clockSource,sampleRate,
            DAQmx_Val_Rising,DAQmx_Val_ContSamps,sampleBufferSize)
        #error.append(('DAQmxCfgAnlgEdgeStartTrig',nidaq.DAQmxCfgAnlgEdgeStartTrig(taskHandle,triggerSource,DAQmx_Val_Rising,triggerLevel)))
        #error.append(('DAQmxCfgDigEdgeStartTrig',nidaq.DAQmxCfgDigEdgeStartTrig(taskHandle,triggerSource,DAQmx_Val_Rising,triggerLevel)))
    nidaq.DAQmxCfgInputBuffer(taskHandle,200000)

    #Read Samples
def ReadSamples(points):
    bufferSize = uInt32(points)
    pointsToRead = bufferSize
    data = np.zeros((points,),dtype=np.float64)

    nidaq.DAQmxReadAnalogF64(taskHandle,pointsToRead,timeout,
            DAQmx_Val_GroupByScanNumber,data.ctypes.data,
            uInt32(2*bufferSize.value),ctypes.byref(pointsRead),None)
    return data

#Start Task
def StartTask():
    nidaq.DAQmxStartTask(taskHandle)

#stop and clear
def StopAndClearTask():
    if taskHandle.value != 0:
        nidaq.DAQmxStopTask(taskHandle)

def get(points=numberPoints):
    StartTask()
    data = ReadSamples(points)
    StopAndClearTask()
    return data
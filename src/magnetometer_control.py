import hardware.afg3000 as tek
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt
import os
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

factor=100# downsampling factor
sampleBufferSize = uInt64(100000)

sampleRate = float64(2000000.0)  # sampling rate in samples per second
sampleRateComp=sampleRate.value/factor
detectionTime = float(1) # detection time in seconds
numberPoints = int(sampleRate.value*detectionTime)
numberPointsComp=int(sampleRateComp*detectionTime)
delta_t=1/sampleRate.value
delta_tComp=1/sampleRateComp
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
    nidaq.DAQmxCfgDigEdgeStartTrig(taskHandle,triggerSource,DAQmx_Val_Rising,triggerLevel)
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

def downsampling(data):
    down = data.reshape(-1,factor).mean(axis=1)
    return down

########################################################################
#CONNECT to hameg and tektronix

tektronix=tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")


##########################################################################
#INITIALIZE measurement parameters

cell='4'
measno='7'
measurement='rb85_42.1degC_higher_than_15uW' 		#number and special features of the measurement

#initialize b1 frequency
fstart=2.0E3						#start frequency b1
fstep=0.5E3						#frequency step b1
fstop=10.0E3 						#meas1_locked_to_rb87_f2_with_0_shields_isweepstop frequency
fsteps=int((fstop-fstart)/fstep+1) #frequency steps


#initialize b1 amplitude
ampstart=50E-3					#start amplitude b1
ampstop=50E-3                    #stop amplitude b1	
ampstep=50E-3			    
asteps=int((ampstop-ampstart)/ampstep+1)

#initalize B0 field
offsetstart=0E-3
offsetstop=0E-3
offsetstep=50E-3
offsetsteps=int((offsetstop-offsetstart)/offsetstep+1)

b0amp=500E-3
b0sweepFreq=1

filename='N:/data/emily/magnetometer/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))

if os.path.exists(filename):
    print "WARNING!!! File already exists. The measurement will not be saved!"
    pass

####################################################################################
#INITIALIZE devices 
tektronix.set_waveform(func="SIN", ch=2)
tektronix.set_freq(frequency=b0sweepFreq, ch=1)
tektronix.set_waveform(func="RAMP", ch=1)
tektronix.set_freq(fstart, ch=2)		
tektronix.set_offset(offsetstart,ch=1) 
tektronix.set_amp(ampstart, ch=2)
tektronix.set_amp(b0amp, ch=1)
tektronix.run(ch=1)
tektronix.run(ch=2)


FrequencyArray=np.zeros([numberPointsComp, fsteps])
FrequencyArrayFft=np.zeros([numberPointsComp/2+1, fsteps])
SetupTask()
plt.clf()
# for j in range(offsetsteps):
#     FrequencyArray=np.zeros([numberPointsComp, fsteps])
#     FrequencyArrayFft=np.zeros([numberPointsComp/2+1, fsteps])
#     offset=offsetstart+(j)*offsetstep
#     tektronix.set_offset(offset, 2)
for k in range(fsteps):
    frequency=fstart+(k)*fstep
    tektronix.set_freq(frequency, 2)
    tektronix.trig()
    batch=get()
    data=downsampling(batch)
    FrequencyArray[:,k]=data
    FrequencyArrayFft[:,k]=abs(np.fft.rfft(data))


# np.savetxt(filename+"/offset_{0:.3f}.csv".format(offset), FrequencyArray, delimiter=",")
# np.savetxt(filename+"/offset_fft{0:.3f}.csv".format(offset), FrequencyArrayFft, delimiter=",")
# #plt.yscale('log')
# plt.plot(FrequencyArray)
# plt.savefig(filename+'/offset{0:.3f}.png'.format(offset))
if os.path.exists(filename):
    print "File already exists!"
    raise

if not os.path.exists(filename):
    os.makedirs(filename)       #create a directrory


np.savetxt(filename+"/b0sweep.csv", FrequencyArray, delimiter=",")
np.savetxt(filename+"/b0sweep_fft.csv", FrequencyArrayFft, delimiter=",")
#plt.yscale('log')
plt.plot(FrequencyArray)
plt.savefig(filename+'/b0sweep.png')
plt.clf()
plt.plot(FrequencyArrayFft[100:,:])
plt.savefig(filename+'/b0sweep_fft.png')
plt.clf()

tektronix.stop(ch=1)
tektronix.stop(ch=2)

params=[(measno, measurement), ("StartFrequency(Hz)", fstart), ("StopFrequency(Hz)", fstop),
 ("FrequencySteps(Hz)", fstep), ("StartAplitude(Vpp)", ampstart), ("StopAmplitude(Vpp)", ampstop),
("AmplitudeStep(Vpp)",ampstep), ("OffsetStart(V)", offsetstart), ("OffsetStop(V)", offsetstop),
 ("OffsetStep(V)", offsetstep), ("DownsamplingFactor", factor), ("B0SweepFreq", b0sweepFreq)]
np.savetxt(filename+"/params.csv", params, delimiter=";", fmt='%s %s')
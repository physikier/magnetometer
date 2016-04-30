import hardware.afg3000 as tek
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt
import os
import ctypes

from threading import Thread
from Queue import Queue 

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

chan = ctypes.create_string_buffer('/Dev2/ai1')
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



########################################################################
#create DO Task
do_chan = ctypes.create_string_buffer('/Dev2/port0/line0')
uInt_ArrayFactory = ctypes.c_uint8 *2 
do_data = uInt_ArrayFactory(1,0)
DAQmx_Val_ChanPerLine = 0
DAQmx_Val_GroupByChannel = 0

TaskHandle = ctypes.c_uint32
do_task = TaskHandle(1)
nidaq.DAQmxCreateTask("",ctypes.byref(do_task))
nidaq.DAQmxCreateDOChan(do_task,do_chan,"output",DAQmx_Val_ChanPerLine)

########################################################################

def pulse(length=0.5):
    return nidaq.DAQmxWriteDigitalLines(do_task,2,1,-1,DAQmx_Val_GroupByChannel,do_data,None,None)


#Start Task
def StartTask():
    nidaq.DAQmxStartTask(taskHandle)
    time.sleep(0.1)

#stop and clear
def StopAndClearTask():
    if taskHandle.value != 0:
        nidaq.DAQmxStopTask(taskHandle)

# def get(points=numberPoints):
#     StartTask()
#     data = ReadSamples(points)
#     StopAndClearTask()
#     return dataW


def get(q,points=numberPoints):
    StartTask()
    pulse()
    data = ReadSamples(points)
    StopAndClearTask()
    q.put(data)
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
measno='55'
measurement='rb85_42.1degC_less_than_15uW_40dB' 		#number and special features of the measurement

#initialize b1 frequency
fstart=2.0E3						#start frequency b1
fstep=1E3						#frequency step b1
fstop=6.0E3 						#meas1_locked_to_rb87_f2_with_0_shields_isweepstop frequency
fsteps=int(round((fstop-fstart)/fstep)+1) #frequency steps


#b1 amplitude
b1amp=0.5

#initialize b0 amplitude
ampstart=200E-3					#start amplitude b1
ampstop=1000E-3                    #stop amplitude b1	
ampstep=100E-3			    
ampsteps=int(round((ampstop-ampstart)/ampstep)+1)

#initalize B0 field
b0offset=0E-3
b0amp=2
b0sweepFreq=1

filename='N:/data/emily/magnetometer/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))

if os.path.exists(filename):
    print "File already exists!"
    raise

if not os.path.exists(filename):
    os.makedirs(filename)       #create a directrory

####################################################################################
#INITIALIZE devices 
tektronix.set_waveform(func="SIN", ch=2)
tektronix.set_freq(fstart, ch=2)
tektronix.set_amp(b1amp, ch=2)


tektronix.set_waveform(func="RAMP", ch=1)
tektronix.set_offset(b0offset,ch=1) 
tektronix.set_amp(b0amp, ch=1)
tektronix.set_freq(b0sweepFreq, ch=1)
tektronix.burst_state(state="ON", ch=1)
tektronix.burst_mode(mode="TRIG", ch=1)
tektronix.burst_cycles(cycles=1, ch=1)



tektronix.run(ch=1)
tektronix.run(ch=2)


FrequencyArray=np.zeros([numberPointsComp, fsteps])
FrequencyArrayFft=np.zeros([numberPointsComp/2+1, fsteps])
SetupTask()
plt.clf()

for j in range(ampsteps):
    FrequencyArray=np.zeros([numberPointsComp, fsteps])
    FrequencyArrayFft=np.zeros([numberPointsComp/2+1, fsteps])
    amp=ampstart+(j)*ampstep
    tektronix.set_amp(amp, 1)
    q=Queue()
    for k in range(fsteps):
        frequency=fstart+(k)*fstep
        tektronix.set_freq(frequency, 2)
        
        get_thread = Thread(target=get,args=[q])
        get_thread.start()
        pulse()
        get_thread.join()
        batch=q.get()
        # tektronix.trig()
        #batch=get()
        
        data=downsampling(batch)
        FrequencyArray[:,k]=data
        FrequencyArrayFft[:,k]=abs(np.fft.rfft(data))

    np.savetxt(filename+"/b0sweep{0:.3f}.csv".format(amp), FrequencyArray, delimiter=",")
    np.savetxt(filename+"/b0sweep_fft{0:.3f}.csv".format(amp), FrequencyArrayFft, delimiter=",")
    #plt.yscale('log')
    plt.plot(FrequencyArray)
    plt.savefig(filename+'/b0sweep{0:.3f}.png'.format(amp))
    plt.clf()
    plt.plot(FrequencyArrayFft[100:,:])
    plt.savefig(filename+'/b0sweep_fft{0:.3f}.png'.format(amp))
    plt.clf()




# np.savetxt(filename+"/offset_{0:.3f}.csv".format(offset), FrequencyArray, delimiter=",")
# np.savetxt(filename+"/offset_fft{0:.3f}.csv".format(offset), FrequencyArrayFft, delimiter=",")
# #plt.yscale('log')
# plt.plot(FrequencyArray)
# plt.savefig(filename+'/offset{0:.3f}.png'.format(offset))



tektronix.burst_state(state="OFF", ch=1)

tektronix.stop(ch=1)
tektronix.stop(ch=2)

params=[(measno, measurement), ("StartFrequency(Hz)", fstart), ("StopFrequency(Hz)", fstop),
 ("FrequencySteps(Hz)", fstep), ("B1StartAplitude(Vpp)", ampstart), ("B1StopAmplitude(Vpp)", ampstop),
("B1AmplitudeStep(Vpp)",ampstep),
 ("DownsamplingFactor", factor), ("B0SweepFreq", b0sweepFreq), ("B0Offset(V)", b0offset),
  ("B0SweepAmp(V)", b0amp)]
np.savetxt(filename+"/params.csv", params, delimiter=";", fmt='%s %s')
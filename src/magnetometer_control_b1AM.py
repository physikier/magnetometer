import hardware.afg3000 as tek
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt
import os
import ctypes
import hardware.hameg as ha


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
min1 = float64(-5.0)
max1 = float64(5.0)
timeout = float64(10.0)
bufferSize = uInt32(10)
pointsToRead = bufferSize
pointsRead = uInt32()

factor=1000# downsampling factor
sampleBufferSize = uInt64(100000)

sampleRate = float64(2000000.0)  # sampling rate in samples per second
sampleRateComp=sampleRate.value/factor
detectionTime = float(0.5) # detection time in seconds
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
hameg=ha.HMP2030(device="hameg01", voltage_max=20., current_max=0.07)

##########################################################################
#INITIALIZE measurement parameters

cell='4'
measno='44'
measurement='B1AMmod_rb85_42.1degC_less_than_12uW_40dB_R0asB0_R1asB1_withHighPass_lockin_5mV_1ms' 		#number and special features of the measurement

#initialize b1 frequency
fstart = 5.E3						#start frequency b1
fstep = 5.E3						#frequency step b1
fstop = 5.E3 						#meas1_locked_to_rb87_f2_with_0_shields_isweepstop frequency
fsteps=int(round((fstop-fstart)/fstep)+1) #frequency steps


#initialize b1 amplitude
b1amp=800E-3					#start amplitude b1

#initialize AM modulation
amfreqstart = 10
amfreqstop = 300
amfreqstep = 10
amfreqsteps = int(round((amfreqstop - amfreqstart)/amfreqstep))

amdepth = 20
amwaveform = "SIN"

#initalize B0 field

b0offsetstart=85E-3
b0offsetstop=100E-3
b0offsetstep=1E-3
b0offsetsteps=int(round((b0offsetstop-b0offsetstart)/b0offsetstep)+1)



volR3=0.003
volR4=0.041

filename='N:/data/emily/magnetometer/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))

if os.path.exists(filename):
    print "File already exists!"
    raise

if not os.path.exists(filename):
    os.makedirs(filename)       #create a directrory

####################################################################################
#INITIALIZE devices 
tektronix.set_waveform(func="SIN", ch=1)
tektronix.set_freq(fstart, ch=1)
tektronix.set_amp(b1amp, ch=1) #checken eventuell alle messunegn mit diesem programm verwerfen
tektronix.set_AMmod_state(arg="ON",ch=1)
tektronix.set_AMmod_internal(func="INT", ch=1)
tektronix.set_AMmod_waveform(func=amwaveform, ch=1)
tektronix.set_AMmod_freq(freq=amfreqstart, ch=1)
tektronix.set_AMmod_depth(depth=amdepth, ch=1)

tektronix.set_waveform(func="DC", ch=2)
tektronix.set_offset(b0offsetstart,ch=2) 


tektronix.run(ch=1)
tektronix.run(ch=2)



hameg.set_max_voltage(ch=1, max_voltage=1.)
hameg.set_voltage(volR3,ch=1)
hameg.run(ch=1)

hameg.set_max_voltage(ch=2, max_voltage=1.)
hameg.set_voltage(volR4,ch=2)
hameg.run(ch=2)

time.sleep(0.5)

FrequencyArray=np.zeros([numberPointsComp, amfreqsteps])
FrequencyArrayFft=np.zeros([numberPointsComp/2+1, amfreqsteps])
SetupTask()
plt.clf()

for j in range(b0offsetsteps):
    FrequencyArray=np.zeros([numberPointsComp, amfreqsteps])
    FrequencyArrayFft=np.zeros([numberPointsComp/2+1, amfreqsteps])
    b0offset=b0offsetstart+j*b0offsetstep
    tektronix.set_offset(b0offset, ch=2)
    for k in range(amfreqsteps):

        amfreq=amfreqstart+(k)*amfreqstep
        tektronix.set_AMmod_freq(amfreq, 1)
        hameg.set_voltage(volR3,ch=1)
        hameg.set_voltage(volR4,ch=2)
        time.sleep(0.5)
        batch=get()
        data=downsampling(batch)
        FrequencyArray[:,k]=data
        FrequencyArrayFft[:,k]=abs(np.fft.rfft(data))

    np.savetxt(filename+"/b0offset{0:.3f}V.csv".format(b0offset), FrequencyArray, delimiter=",")
    np.savetxt(filename+"/b0offset{0:.3f}V_fft.csv".format(b0offset), FrequencyArrayFft, delimiter=",")
    #plt.yscale('log')
    plt.plot(FrequencyArray)
    plt.ylim(ymax=2, ymin=-2)
    plt.savefig(filename+'/b0offset{0:.3f}V.png'.format(b0offset))
    plt.clf()
    plt.plot(FrequencyArrayFft)
    plt.ylim(ymax=10, ymin=0)
    plt.savefig(filename+'/b0offset{0:.3f}V_fft.png'.format(b0offset))
    plt.clf()




# np.savetxt(filename+"/offset_{0:.3f}.csv".format(offset), FrequencyArray, delimiter=",")
# np.savetxt(filename+"/offset_fft{0:.3f}.csv".format(offset), FrequencyArrayFft, delimiter=",")
# #plt.yscale('log')
# plt.plot(FrequencyArray)
# plt.savefig(filename+'/offset{0:.3f}.png'.format(offset))


hameg.close()
tektronix.set_AMmod_state(arg="OFF", ch=1)
tektronix.stop(ch=1)
tektronix.stop(ch=2)

params=[(measno, measurement), ("StartFrequency(Hz)", fstart), ("StopFrequency(Hz)", fstop),
 ("FrequencySteps(Hz)", fstep), ("AMmodulationFreqStart(Hz)", amfreqstart), 
 ("AMmodulationFreqStop(Hz)", amfreqstop), ("AMmodulationFreqStep(Hz)", amfreqstep),
 ("AMmodulationDepth(%)", amdepth),
 ("AMWaveform", amwaveform), ("B1Amplitude(V)", b1amp),
 ("DownsamplingFactor", factor), ("B0OffsetStart(V)", b0offsetstart), ("B0OffsetSop(V)", b0offsetstop),
  ("B0OffsetStep(V)", b0offsetstep), ("R3(V)", volR3), ("R4(V)", volR4)]
np.savetxt(filename+"/params.csv", params, delimiter=";", fmt='%s %s')
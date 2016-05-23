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

def get(q,points=numberPoints):
    StartTask()
    pulse()
    data = ReadSamples(points)
    StopAndClearTask()
    q.put(data)
    return data


# def get(points=numberPoints):
#     StartTask()
#     data = ReadSamples(points)
#     StopAndClearTask()
#     return data

def downsampling(data):
    down = data.reshape(-1,factor).mean(axis=1)
    return down


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


def pulse(length=0.5):
    return nidaq.DAQmxWriteDigitalLines(do_task,2,1,-1,DAQmx_Val_GroupByChannel,do_data,None,None)

########################################################################
#CONNECT to hameg and tektronix
hameg=ha.HMP2030(device="hameg01", voltage_max=20., current_max=0.07)
tektronix=tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")


##########################################################################
#INITIALIZE measurement parameters

cell='4'
measno='47'
measurement='b1sweep_rb85_50degC_less_than_12uW_40dB_R0asB0_R1asB1_withHighPass_SR83010ms5mV24dB'

#initialize b1 frequency
fcenter=5E3						#start frequency b1
fspan=5E3				#frequency step b1
b1sweepFreq=2




#initialize b1 amplitude
ampstart=200E-3					#start amplitude b1
ampstop=400E-3                    #stop amplitude b1	
ampstep=100E-3			    
ampsteps=int((ampstop-ampstart)/ampstep+1)

#initalize B0 field
offsetstart=0E-3
offsetstop=100E-3
offsetstep=10E-3
offsetsteps=round((offsetstop-offsetstart)/offsetstep+1)
b0waveform="DC"

volR3=0.000
volR4=0.00
volR2=0.00

filename='N:/data/emily/magnetometer/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))

if os.path.exists(filename):
    print "File already exists!"
    raise

if not os.path.exists(filename):
    os.makedirs(filename)       #create a directrory

####################################################################################
#INITIALIZE devices 
tektronix.set_waveform(func="SIN", ch=2)

tektronix.set_frequency_mode(mode="SWE", ch=2)
tektronix.set_frequency_sweep_span(span=fspan, ch=2)
tektronix.set_center_frequency(center=fcenter, ch=2)
tektronix.set_sweep_mode(mode="MAN", ch=2)
tektronix.set_sweep_time(time=0.5, ch=2)
tektronix.set_sweep_rtime(rtime=0.5, ch=2)
tektronix.set_sweep_htime(htime=0, ch=2)
tektronix.set_sweep_form(form="LIN", ch=2)
tektronix.set_amp(ampstart, ch=2)

tektronix.set_waveform(func='DC', ch=1)
tektronix.set_offset(offsetstart, ch=1)

tektronix.run(ch=1)
tektronix.run(ch=2)

hameg.set_max_voltage(ch=1, max_voltage=1.)
hameg.set_voltage(volR3,ch=1)
hameg.run(ch=1)

hameg.set_max_voltage(ch=2, max_voltage=1.)
hameg.set_voltage(volR4,ch=2)
hameg.run(ch=2)

hameg.set_max_voltage(ch=3, max_voltage=1.)
hameg.set_voltage(volR2,ch=3)
hameg.run(ch=2)


FrequencyArray=np.zeros([numberPointsComp, offsetsteps])
FrequencyArrayFft=np.zeros([numberPointsComp/2+1, offsetsteps])
SetupTask()
plt.clf()

from threading import Thread
from Queue import Queue 

for j in range(int(ampsteps)):
    FrequencyArray=np.zeros([numberPointsComp, offsetsteps])
    FrequencyArrayFft=np.zeros([numberPointsComp/2+1, offsetsteps])
    amp=ampstart+(j)*ampstep
    tektronix.set_amp(amp, 2)
    q=Queue()
    for k in range(int(offsetsteps)):
        offset=offsetstart+(k)*offsetstep
        tektronix.set_offset(offset, 1)
        get_thread = Thread(target=get,args=[q])
        get_thread.start()
        pulse()
        get_thread.join()
        batch=q.get()
        # tektronix.trig()
        # batch=get()
        data=downsampling(batch)
        FrequencyArray[:,k]=data
        FrequencyArrayFft[:,k]=abs(np.fft.rfft(data))

    np.savetxt(filename+"/b1sweep{0:.3f}V_B1amp.csv".format(amp), FrequencyArray, delimiter=",")
    np.savetxt(filename+"/b1sweep_fft{0:.3f}V_B1amp.csv".format(amp), FrequencyArrayFft, delimiter=",")
    #plt.yscale('log')
    plt.plot(np.linspace(fcenter-fspan/2,fcenter+fspan/2, num=len(FrequencyArray)), FrequencyArray)
    plt.savefig(filename+'/b1sweep{0:.3f}V_B1amp.png'.format(amp))
    plt.clf()
    plt.plot(FrequencyArrayFft[100:,:])
    plt.savefig(filename+'/b1sweep_fft{0:.3f}V_B1amp.png'.format(amp))
    plt.clf()




# np.savetxt(filename+"/offset_{0:.3f}.csv".format(offset), FrequencyArray, delimiter=",")
# np.savetxt(filename+"/offset_fft{0:.3f}.csv".format(offset), FrequencyArrayFft, delimiter=",")
# #plt.yscale('log')
# plt.plot(FrequencyArray)
# plt.savefig(filename+'/offset{0:.3f}.png'.format(offset))



hameg.close()
tektronix.set_frequency_mode(mode="CW", ch=2)
tektronix.stop(ch=1)
tektronix.stop(ch=2)

params=[(measno, measurement), ("CenterFrequency(Hz)", fcenter), ("FrequencyDevi(Hz)", fspan),
 ("StartB1Aplitude(Vpp)", ampstart), ("StopB1Amplitude(Vpp)", ampstop),
("B1AmplitudeStep(Vpp)",ampstep), ("B0OffsetStart(V)", offsetstart), ("B0OffsetStop(V)", offsetstop),
 ("B0OffsetStep(V)", offsetstep), ("DownsamplingFactor", factor), ("B1SweepFreq", b1sweepFreq),
 ("B0Waveform", b0waveform), ("R3(V)", volR3), ("R4(V)", volR4), ("R2(V)", volR2)]
np.savetxt(filename+"/params.csv", params, delimiter=";", fmt='%s %s')
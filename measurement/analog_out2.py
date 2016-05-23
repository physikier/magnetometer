import numpy
import threading
#import ctypes
from PyDAQmx import *

#taskHandle=TaskHandle()

class WaveformThread(threading.Thread):

  def __init__(self, waveform, sampleRate):
    
    self.running = True
    self.sampleRate = sampleRate
    self.periodLength = waveform.size
    self.taskHandle = TaskHandle()
    self.data = numpy.zeros(self.periodLength, dtype=numpy.float64)
    self.pointsRead = int32()
    self.data=waveform
    sampsPerChanWritten=int32()

    self.CHK(DAQmxCreateTask(b'',self.taskHandle))
    self.CHK(DAQmxCreateAOVoltageChan(self.taskHandle,b'/Dev2/ao0',b'',-5.,5.,DAQmx_Val_Volts,None))
    self.CHK(DAQmxCfgSampClkTiming(self.taskHandle, b'', self.sampleRate, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength))
    #self.CHK(DAQmxSetWriteAttribute(self.taskHandle, DAQmx_Write_RegenMode, DAQmx_Val_AllowRegen))
    # #self.CHK(DAQmxCfgPipelinedSampClkTiming(self.taskHandle, b'', 2e6, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength))
    # self.CHK(DAQmxCfgOutputBuffer(self.taskHandle, 2000000))
    # #self.CHK(DAQmxSetAODataXferReqCond(self.taskHandle,b'/Dev2/ao0',10240))
    # self.CHK(DAQmxSetAODataXferMech(self.taskHandle, b'/Dev2/ao0',DAQmx_Val_USBbulk))
    # #self.CHK(DAQmxCfgInputBuffer(self.taskHandle, 1))
    # #print(DAQmx_Val_FiniteSamps)
    
    
    self.CHK(DAQmxWriteAnalogF64(self.taskHandle, self.periodLength, 0, 100.0, DAQmx_Val_GroupByChannel, self.data, None, None))
    threading.Thread.__init__(self)

  def CHK( self, err ):
      """a simple error checking routine"""
      if err < 0:
          buf_size = 100
          buf = '\000' * buf_size
          DAQmxGetErrorString(err,byref(buf),buf_size)
          raise RuntimeError('nidaq call failed with error %d: %s'%(err,repr(buf)))
      if err > 0:
          buf_size = 100
          buf = '\000' * buf_size
          DAQmxGetErrorString(err,byref(buf),buf_size)
          raise RuntimeError('nidaq generated warning %d: %s'%(err,repr(buf)))
  def run( self ):
      counter = 0
      self.CHK(DAQmxStartTask(self.taskHandle))
  def stop( self ):
      zero = numpy.zeros(1, dtype=numpy.float64)
      zeroLength = zero.size
      #self.running = False
      DAQmxStopTask(self.taskHandle)
      DAQmxClearTask(self.taskHandle)
      self.CHK(DAQmxCreateTask(b'',byref(self.taskHandle)))
      self.CHK(DAQmxCreateAOVoltageChan(self.taskHandle,b'/Dev2/ao0',b'',-10.,10.,DAQmx_Val_Volts,None))
      DAQmxWriteAnalogF64(self.taskHandle, zeroLength, 1, 100.0, DAQmx_Val_GroupByChannel, zero , None, None)
      self.running = False
      DAQmxStopTask(self.taskHandle)
      DAQmxClearTask(self.taskHandle)

def func_ramp(amplitude, period, samples):
    t = numpy.arange(0, period, 1.0/samples, endpoint=False)
    period_half_int = int(len(t)/2)
    #print('periodhalfint: ' + str(period_half_int))
    x = numpy.array([])
    for i in range(len(t)):
      if i <= period_half_int:
        #print('erste haelfte')
        #print(x[i])
        x = numpy.append(x, [(2*amplitude/period)*t[i] - amplitude/2])
        #print('amplitude/2: ' + str(amplitude/2))
        #print('x[periodhalfint]: ' + str(x[period_half_int]))
        #print(f_x)
        #print()
      else:
        #print('zweite haelfte')
        #print(x[i])
        x = numpy.append(x, [(-2*amplitude/period)*t[i] + 3*amplitude/2])
        #print('P=' +str(x[-1]))
        #print(t[-1])
        #print()
    #print(x, t)
    return x, samples

def func_sin(period, samples):
    t = numpy.arange(0, 50*period, 1.0/samples)
    x = numpy.sin(2*numpy.pi*t/period)
    return x, samples




if __name__ == '__main__':
  import time
# generate a time signal 5 seconds long with 250Hz sample rate
  #t = numpy.arange( 0, 1., 1.0/100 )
  # generate sine wave
  #x = numpy.sin(2*numpy.pi*t/1.)
  #x = t - 2
  #x = func_ramp(t, 2)


  x, samplerate = func_sin(0.00001, 2.6e6)
  #x, samplerate = func_ramp(3, 0.001, 2e6)

  #print(type(x))
  # mythread = WaveformThread( x, 100 )
  mythread = WaveformThread( x, samplerate)
  mythread.start()
  time.sleep(5)
  mythread.stop()
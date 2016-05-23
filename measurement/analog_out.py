import numpy
import threading
#import ctypes
from PyDAQmx import *

#taskHandle=TaskHandle()

class WaveformThread(threading.Thread):

  def __init__(self, waveform, sampleRate):
    
    self.running = True
    self.sampleRate = sampleRate
    self.periodLength = len(waveform)
    self.taskHandle = TaskHandle()
    self.data = numpy.zeros(self.periodLength, dtype=numpy.float64)
    self.pointsRead = int32()
    for i in range(self.periodLength):
      self.data[i]=waveform[i]
      sampsPerChanWritten=int32()

      self.CHK(DAQmxCreateTask(b'',byref(self.taskHandle)))
      self.CHK(DAQmxCreateAOVoltageChan(self.taskHandle,b'/Dev2/ao0',b'',-2.,2.,DAQmx_Val_Volts,None))
      print(DAQmx_Val_FiniteSamps)
      self.CHK(DAQmxCfgSampClkTiming(self.taskHandle, b'', self.sampleRate, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength));
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
      self.running = False
      DAQmxStopTask(self.taskHandle)
      DAQmxClearTask(self.taskHandle)

if __name__ == '__main__':
  import time
# generate a time signal 5 seconds long with 250Hz sample rate
  t = numpy.arange( 0, 5, 1.0/200.0 )
  # generate sine wave
  x = numpy.sin( t )
  mythread = WaveformThread( x, 200 )
  mythread.start()
  time.sleep(5)
  mythread.stop()
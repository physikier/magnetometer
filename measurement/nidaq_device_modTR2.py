import ctypes
import numpy as np
import time
from PyDAQmx import *


class NidaqDevice(object):
    

    taskHandle = TaskHandle()
    
    def __init__(self, 
                 detection_time=1.0, # detection time in seconds
                 downsampling_factor=100,
                 sample_rate=2000000.0, # sampling rate in samples per second
                 trigger_level=0.,
                 trigger_source=b'/Dev2/pfi0', 
                 channel_photodiode=b'/Dev2/ai0',  # channel to read photo diode signal

                 channel_lock_in=b'/Dev2/ai1',   # channel to read lock-in signal
                 clock_source=b'OnboardClock'
                ):
        # Declaration of variable passed by reference
        
        self.read = int32() 
        #self.taskHandle = self.TaskHandle()
        
        self.min1 = -5.0
        self.max1 = 5.0
        self.timeout = 10.0
        self.bufferSize = 10
        self.pointsToRead = self.bufferSize
        self.pointsRead = int32()
        
        self.downsampling_factor = downsampling_factor
        self.sampleBufferSize = 100000

        self.sampleRate = sample_rate
        self.detectionTime = detection_time
        self.triggerSource = trigger_source
        self.triggerLevel = trigger_level
        
        self._channel_photodiode = channel_photodiode
        self._channel_lock_in = channel_lock_in
        self.channel = ctypes.create_string_buffer(channel_photodiode)
        self.clockSource = clock_source
        
        self._calc_deps()




        self.do_chan = b'Dev2/port0/line0'
        #uInt_ArrayFactory = ctypes.c_uint8 *2 
        #self.do_data = uInt_ArrayFactory(1,0)
        self.do_data = np.array([1,0], np.uint8)
        print(self.do_data)
        self.DAQmx_Val_ChanPerLine = 0
        self.DAQmx_Val_GroupByChannel = 0

        #TaskHandle = ctypes.c_uint32
        self.do_task = TaskHandle(1)
        DAQmxCreateTask(b"",byref(self.do_task))
        DAQmxCreateDOChan(self.do_task, self.do_chan,b"output", self.DAQmx_Val_ChanPerLine)



    def connect_pipes(self,source,destination): #  modTR : example: source= '/Dev1/PFI12'| destination= '/Dev2/PFI36'
        DAQmxConnectTerms(source,destination)
    def disconnect_pipes(self,source,destination):# modTR : example: source= '/Dev1/PFI12'| destination= '/Dev2/PFI36' 
        DAQmxDisconnectTerms((source,destination))
      
    def setup_task(self):
        print('im in setup task')
        DAQmxCreateTask(b"",byref(self.taskHandle))
        DAQmxCreateAIVoltageChan(
            self.taskHandle, 
            self.channel,
            b"", 
            DAQmx_Val_Cfg_Default, 
            self.min1, 
            self.max1, 
            DAQmx_Val_Volts,
            None
        )
        DAQmxCfgSampClkTiming(
            self.taskHandle,
            self.clockSource,
            self.sampleRate,
            DAQmx_Val_Rising,
            DAQmx_Val_ContSamps,
            self.sampleBufferSize
        )
#         error.append(
#             (
#                 'DAQmxCfgAnlgEdgeStartTrig',
#                 self.instance.DAQmxCfgAnlgEdgeStartTrig(
#                     self.taskHandle,
#                     self.triggerSource,
#                     self.DAQmx_Val_Rising,
#                     self.triggerLevel
#                 )
#             )
#         )
        DAQmxCfgDigEdgeStartTrig(
            self.taskHandle,
            self.triggerSource,
            #DAQmx_Val_FiniteSamps,
            DAQmx_Val_Rising)

        DAQmxCfgInputBuffer(self.taskHandle, 200000)
        
    def read_samples(self, points):
        self.bufferSize = points
        # print('points=' + str(points))
        self.pointsToRead = self.bufferSize
        data = np.zeros((points,),dtype=np.float64)

        # print( "using timeout: "+str(self.timeout) )

        DAQmxReadAnalogF64(
            self.taskHandle,
            self.pointsToRead,
            self.timeout,
            DAQmx_Val_GroupByScanNumber,
            data,
            2*self.bufferSize,
            byref(self.pointsRead),
            None
        )
        # print('timeout=' + str(self.timeout))
        # f = open('data', "w+")
        # for item in data:
        #     f.write("%s\n" % item)
        # #f.write(str(data))
        # print("pointstoread=" + str(self.pointsToRead))
        # print('data=' + str(data))
        # print('2*buffersize=' + str( 2*self.bufferSize))
        return data

    def pulse(self, length=0.5):
        return DAQmxWriteDigitalLines(self.do_task,2,1,-1,DAQmx_Val_GroupByChannel,self.do_data,None,None)

    
    def start_task(self):
        DAQmxStartTask(self.taskHandle)
    
    def stop_and_clear_task(self):
        if self.taskHandle.value != 0:
            DAQmxStopTask(self.taskHandle)
    
    def get_data(self, q, points=None):
        # if no points are given, use the default number points
        print("Getting data...")
        if points is None:
            points = self.numberPoints
        self.start_task()
        self.pulse()
        time_start = time.time()
        data = self.read_samples(points)
        time_end = time.time()
        # print("Reading "+ str(points)+" samples took "+str(time_end-time_start))
        self.stop_and_clear_task()
        q.put(data)
        # print('data2=' + str(data))
        return data
    
    def downsampling(self, data):
        downsampled_data = data.reshape(-1, self.downsampling_factor).mean(axis=1)
        return downsampled_data
    
    def _calc_deps(self):
        self.sampleRateComp = self.sampleRate/self.downsampling_factor
        self.numberPoints = int(self.sampleRate*self.detectionTime)
        self.numberPointsComp = int(self.sampleRateComp*self.detectionTime)
        self.delta_t = 1/self.sampleRate
        self.delta_tComp = 1/self.sampleRateComp
        
    
    def load_config(self, config, use_lock_in=False):
        self.detectionTime = config['measurement_time_s']
        self.downsampling_factor = config['downsampling_factor']
        self.sampleRate = config['sample_rate']
        if use_lock_in:
            self.channel = self._channel_lock_in
        else:
            self.channel = self._channel_photodiode
        
        self._calc_deps()

if __name__ != '__main__':
    print('this module was successfully imported')
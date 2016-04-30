from __future__ import division
import ctypes
import numpy as np


class NidaqDevice(object):
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
    DAQmx_Val_FiniteSamps = 10178
    DAQmx_Val_ChanForAllLines = 1
    DAQmx_Val_RSE = 10083
    DAQmx_Val_Volts = 10348
    DAQmx_Val_GroupByScanNumber = 1
    DAQmx_Val_GroupByChannel = 0
    
    
    def __init__(self, 
                 detection_time=1.0, # detection time in seconds
                 downsampling_factor=100,
                 sample_rate=float64(2000000.0), # sampling rate in samples per second
                 trigger_level=float64(0.),
                 trigger_source='/Dev2/pfi0', 
                 channel_photodiode='/Dev2/ai0',  # channel to read photo diode signal
                 channel_lock_in='/Dev2/ai1',   # channel to read lock-in signal
                 clock_source='OnboardClock'

                ):
        self.instance = ctypes.windll.nicaiu 
        self.taskHandle = self.TaskHandle(0)
        
        self.min1 = self.float64(-5.0) 
        self.max1 = self.float64(5.0)
        self.timeout = self.float64(10.0)
        self.bufferSize = self.uInt32(10)
        self.pointsToRead = self.bufferSize
        self.pointsRead = self.uInt32()
        
        self.downsampling_factor = downsampling_factor
        self.sampleBufferSize = self.uInt64(100000)

        self.sampleRate = sample_rate
        self.detectionTime = detection_time
        self.triggerSource = ctypes.create_string_buffer(trigger_source.encode('utf-8'))
        self.triggerLevel = trigger_level
        
        self._channel_photodiode = channel_photodiode
        self._channel_lock_in = channel_lock_in
        self.channel = ctypes.create_string_buffer(channel_photodiode.encode('utf-8'))
        self.clockSource = ctypes.create_string_buffer(clock_source.encode('utf-8'))
        
        self._calc_deps()




        self.do_chan = ctypes.create_string_buffer(b'/Dev2/port0/line0')
        uInt_ArrayFactory = ctypes.c_uint8 *2 
        self.do_data = uInt_ArrayFactory(1,0)
        self.DAQmx_Val_ChanPerLine = 0
        self.DAQmx_Val_GroupByChannel = 0

        TaskHandle = ctypes.c_uint32
        self.do_task = TaskHandle(1)
        self.instance.DAQmxCreateTask("",ctypes.byref(self.do_task))
        self.instance.DAQmxCreateDOChan(self.do_task, self.do_chan,"output", self.DAQmx_Val_ChanPerLine)



    def connect_pipes(self,source,destination): #  modTR : example: source= '/Dev1/PFI12'| destination= '/Dev2/PFI36'
        self.instance.DAQmxConnectTerms(source,destination)
    def disconnect_pipes(self,source,destination):# modTR : example: source= '/Dev1/PFI12'| destination= '/Dev2/PFI36' 
        self.instance.DAQmxDisconnectTerms((source,destination))
      
    def setup_task(self):
        self.instance.DAQmxCreateTask("",ctypes.byref(self.taskHandle))
        self.instance.DAQmxCreateAIVoltageChan(
            self.taskHandle, 
            self.channel, 
            "", 
            self.DAQmx_Val_Cfg_Default, 
            self.min1, 
            self.max1, 
            self.DAQmx_Val_Volts,
            None
        )
        self.instance.DAQmxCfgSampClkTiming(
            self.taskHandle,
            self.clockSource,
            self.sampleRate,
            self.DAQmx_Val_Rising,
            self.DAQmx_Val_ContSamps,
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
        self.instance.DAQmxCfgDigEdgeStartTrig(
            self.taskHandle,
            self.triggerSource,
            self.DAQmx_Val_FiniteSamps,
            self.DAQmx_Val_Rising)

        self.instance.DAQmxCfgInputBuffer(self.taskHandle, 200000)
        
    def read_samples(self, points):
        bufferSize = self.uInt32(points)
        pointsToRead = bufferSize
        data = np.zeros((points,),dtype=np.float64)

        self.instance.DAQmxReadAnalogF64(
            self.taskHandle,
            pointsToRead,
            self.timeout,
            self.DAQmx_Val_GroupByScanNumber,
            data.ctypes.data,
            self.uInt32(2*bufferSize.value),
            ctypes.byref(self.pointsRead),
            None
        )
        
        return data

    def pulse(self, length=0.5):
        return self.instance.DAQmxWriteDigitalLines(self.do_task,2,1,-1,self.DAQmx_Val_GroupByChannel,self.do_data,None,None)

    
    def start_task(self):
        self.instance.DAQmxStartTask(self.taskHandle)
    
    def stop_and_clear_task(self):
        if self.taskHandle.value != 0:
            self.instance.DAQmxStopTask(self.taskHandle)
    
    def get_data(self, q, points=None):
        # if no points are given, use the default number points
        if points is None:
            points = self.numberPoints
        self.start_task()
        self.pulse()
        data = self.read_samples(points)
        self.stop_and_clear_task()
        q.put(data)
        return data
    
    def downsampling(self, data):
        downsampled_data = data.reshape(-1, self.downsampling_factor).mean(axis=1)
        return downsampled_data
    
    def _calc_deps(self):
        self.sampleRateComp = self.sampleRate.value/self.downsampling_factor
        self.numberPoints = int(self.sampleRate.value*self.detectionTime)
        self.numberPointsComp = int(self.sampleRateComp*self.detectionTime)
        self.delta_t = 1/self.sampleRate.value
        self.delta_tComp = 1/self.sampleRateComp
        
    
    def load_config(self, config, use_lock_in=False):
        self.detectionTime = config['measurement_time_s']
        self.downsampling_factor = config['downsampling_factor']
        self.sampleRate = self.float64(config['sample_rate'])
        if use_lock_in:
            self.channel = ctypes.create_string_buffer(self._channel_lock_in.encode('utf-8'))
        else:
            self.channel = ctypes.create_string_buffer(self._channel_photodiode.encode('utf-8'))
        
        self._calc_deps()
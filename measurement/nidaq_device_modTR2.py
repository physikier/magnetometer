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



class NidaqDevice_simAoAi(object):

    
    # taskHandleAO = TaskHandle()
    # taskHandleAI = TaskHandle()

    def __init__(self, 
                 detection_time=1.0, # detection time in seconds
                 downsampling_factor=100,
                 sample_rate=2000000.0, # sampling rate in samples per second 
                 channel_photodiode=b'/Dev2/ai0',  # channel to read photo diode signal
                 channel_AO=b'',
                 channel_lock_in=b'/Dev2/ai1',   # channel to read lock-in signal
                 clock_source=b'OnboardClock'):

        self._channel_photodiode = channel_photodiode
        self._channel_lock_in = channel_lock_in
        self.clockSource = clock_source
        self.pointsRead = int32()


        # Voltage ai ao max & min
        self.min_V = -10.
        self.max_V = 10.

        self.taskHandleAO = TaskHandle()
        self.taskHandleAI = TaskHandle()

        self.sampleRate = sample_rate
        self.downsampling_factor = downsampling_factor
        self.detectionTime = detection_time
        self.numberPointsComp = 0
        
        self.bufferSize = int(self.numberPointsComp*self.detectionTime) #200 
        self.waveform = numpy.zeros(self.numberPointsComp, dtype=numpy.float64)
        self.waveform2 = numpy.zeros(self.numberPointsComp, dtype=numpy.float64)
        self.periodLength = int((self.waveform.size/10)*detection_time)
        self.pointsToRead = self.periodLength
        self.data_in = numpy.zeros(self.periodLength, dtype=numpy.float64)
        self.method_freq = False
        self.scaling_fac = 100
        # print('pointscomp' + str(self.numberPointsComp))
        # print('buffer=' + str(self.bufferSize))
        # print('points=' + str(self.pointsToRead))
        
        


    def setup_task_aoai(self):
        # AO Channel
        self.CHK(DAQmxCreateTask(b'',byref(self.taskHandleAO)))
        self.CHK(DAQmxCreateAOVoltageChan(self.taskHandleAO,b'/Dev2/ao0',b'',self.min_V, self.max_V,DAQmx_Val_Volts,None))
        self.CHK(DAQmxCfgSampClkTiming(self.taskHandleAO, b'OnboardClock', self.sampleRate, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength));
        
        # AI Channel
        self.CHK(DAQmxCreateTask(b'',self.taskHandleAI))
        self.CHK(DAQmxCreateAIVoltageChan(self.taskHandleAI, b'/Dev2/ai1',b'',DAQmx_Val_Cfg_Default,self.min_V,self.max_V, DAQmx_Val_Volts, None))
        self.CHK(DAQmxCfgSampClkTiming(self.taskHandleAI,b'/Dev2/ao/SampleClock',self.sampleRate, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength))

    def setup_task_2ao1ai(self):
        # AO Channels
        self.CHK(DAQmxCreateTask(b'',byref(self.taskHandleAO)))
        self.CHK(DAQmxCreateAOVoltageChan(self.taskHandleAO,b'/Dev2/ao0:1',b'',self.min_V, self.max_V,DAQmx_Val_Volts,None))
        self.CHK(DAQmxCfgSampClkTiming(self.taskHandleAO, b'OnboardClock', self.sampleRate, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength));

        # AI Channel
        self.CHK(DAQmxCreateTask(b'',self.taskHandleAI))
        self.CHK(DAQmxCreateAIVoltageChan(self.taskHandleAI, b'/Dev2/ai1',b'',DAQmx_Val_Cfg_Default,self.min_V, self.max_V, DAQmx_Val_Volts, None))
        self.CHK(DAQmxCfgSampClkTiming(self.taskHandleAI,b'/Dev2/ao/SampleClock',self.sampleRate, DAQmx_Val_Rising, DAQmx_Val_ContSamps, self.periodLength))

    def run_aoai(self):
        self._calc_daq_deps()
        self.setup_task_aoai()
        self.running = True
        counter = 0
        self.data=self.waveform
        print('periodLength', self.periodLength)
        print('data', self.data.size)
        self.CHK(DAQmxWriteAnalogF64(self.taskHandleAO, self.periodLength, 0, 100.0, DAQmx_Val_GroupByChannel, self.data, None, None))
        
        self.CHK(DAQmxStartTask(self.taskHandleAI)) 
        self.CHK(DAQmxStartTask(self.taskHandleAO)) 
        print('bufferinrun=' + str(self.bufferSize))
        print('pointsinrun=' + str(self.pointsToRead))
        #self.pointsToRead = self.numberPoints
        print(self.pointsToRead, type(self.pointsToRead))
        self.CHK(DAQmxReadAnalogF64(self.taskHandleAI, self.pointsToRead, 100., DAQmx_Val_GroupByChannel, self.data_in, self.bufferSize, self.pointsRead, None))
        return self.data_in
        
    def stop_aoai(self):
        
        DAQmxStopTask(self.taskHandleAI)
        DAQmxClearTask(self.taskHandleAI)
        DAQmxStopTask(self.taskHandleAO)
        DAQmxClearTask(self.taskHandleAO)
        # set output to zero
        # zero = numpy.zeros(1, dtype=numpy.float64)
        # zeroLength = zero.size
        # self.CHK(DAQmxCreateTask(b'',byref(self.taskHandleAO)))
        # self.CHK(DAQmxCreateAOVoltageChan(self.taskHandleAO,b'/Dev2/ao0',b'',-10.,10.,DAQmx_Val_Volts,None))
        # DAQmxWriteAnalogF64(self.taskHandleAO, zeroLength, 1, 100.0, DAQmx_Val_GroupByChannel, zero , None, None)
        # self.running = False
        # DAQmxStopTask(self.taskHandleAO)
        # DAQmxClearTask(self.taskHandleAO)

    def get_data(self, q):
        # if no points are given, use the default number points
        print("Getting data...")
        #if points is None:
        #    points = self.numberPoints
        # self.start_task()
        #self.pulse()
        time_start = time.time()
        print('waveform:' , self.waveform.size)
        print('pointstoread:', self.pointsToRead)
        data = self.run_aoai()
        time_end = time.time()
        # print("Reading "+ str(points)+" samples took "+str(time_end-time_start))
        self.stop_aoai()
        q.put(data)
        # print('data2=' + str(data))
        print('read datapoints', data.size)
        return data

    def downsampling(self, data):
        downsampled_data = data.reshape(-1, self.downsampling_factor).mean(axis=1)
        return downsampled_data

    ################ Erorr Handling Ni Daq ##################
    def CHK( self, err ):
        """a simple error checking routine"""
        if err < 0:
            buf_size = 100
            buf = '\000' * buf_size
            DAQmxGetErrorString(err,buf,buf_size)
            raise RuntimeError('nidaq call failed with error %d: %s'%(err,repr(buf)))
        if err > 0:
            buf_size = 100
            buf = '\000' * buf_size
            DAQmxGetErrorString(err,buf,buf_size)
            raise RuntimeError('nidaq generated warning %d: %s'%(err,repr(buf)))


    #################### Define Waveforms ####################

    # def set_waveform(self, func, freq, amp, off):
    #     self.waveform = self.calc_waveform(func, freq, amp, off)

    def set_waveform(self, func, freq, amp, off):
        samples = self.sampleRateComp
        if self.method_freq == True:
            print('m in init t')
            self.t = self.init_t
        else:
            print('m in  t')
            self.t = numpy.arange(0, (1./freq)*self.scaling_fac, 1.0/samples)
        return self.calc_waveform(func, freq, amp, off, self.t)

    def set_init_waveform(self, func, freq, amp, off):
        samples = self.sampleRateComp
        # self.t = numpy.arange(0, (1./freq), 1.0/samples)
        # self.init_t = numpy.array([])
        # for i in range(1,10):
        #     i+=1
        #     numpy.append(self.init_t,self.t)
        # print('size init t:', self.init_t.size)

        self.init_t = numpy.arange(0, (1./freq)*self.scaling_fac, 1.0/(samples))
        self.init_waveform = self.calc_waveform(func, freq, amp, off, self.init_t)
        self.method_freq = True
        self.numberPointsComp = int((self.init_waveform.size/self.scaling_fac)*self.detectionTime)

    def calc_waveform(self, func, freq, amp, off, t):
        print('im in set waveform')
        #samples = self.sampleRateComp
        if func == 'SIN':
            #print('sin')
            #self.freq = freq
            #print(self.freq)
            return self.func_sin(freq, amp, off, t)
        elif func == 'RAMP':
           #print('ramp')
            return self.func_saw(freq, amp, off, t)
            
        else:
            print('waveform not implemented')
            return 0

    # def set_waveform(self, func, freq, amp, off):
    #     print('im in set waveform')
    #     samples = self.sampleRateComp
    #     if func == 'SIN':
    #         print('sin')
    #         self.freq = freq
    #         print(self.freq)
    #         return self.func_sin(frequency=freq, amplitude=amp, offset=off, samples=samples)
    #     elif func == 'RAMP':
    #         print('ramp')
    #         self.waveform = self.func_saw(freq, amp, off, samples)
            
    #     else:
    #         print('waveform not implemented')
    #         return 0

    def func_saw(self, frequency, amplitude, offset, t):
        from scipy import signal
        #t = numpy.arange(0, (1./frequency)*10, 1.0/samples)
        f_t = amplitude*signal.sawtooth(2*numpy.pi*frequency*t) + offset
        return f_t

    def func_sin(self, frequency, amplitude, offset, t):
        #t = numpy.arange(0, (1./frequency)*10, 1.0/samples)
        f_t = amplitude*numpy.sin(2*numpy.pi*frequency*t) + offset
        return f_t

    ##################### Data/Measurement Scaling ####################
    def _calc_deps(self):
        self.sampleRateComp = self.sampleRate/self.downsampling_factor
        self.numberPoints = int(self.sampleRate*self.detectionTime)
        self.numberPointsComp = int(self.sampleRateComp*self.detectionTime)
        
        self.delta_t = 1/self.sampleRate
        self.delta_tComp = 1/self.sampleRateComp
        # print('calc deps samples' + str(self.sampleRate))
        # print('calc deps down' + str(self.downsampling_factor))
        # print('calc deps samplesdown' + str(self.sampleRateComp))
        # print('pointscomp' + str(self.numberPointsComp))
        # print('buffer=' + str(self.bufferSize))
        # print('points=' + str(self.pointsToRead))

    def _calc_daq_deps(self):
        if self.method_freq == True:
            print('im in freq mode')
            self.periodLength = int((self.init_waveform.size)*self.detectionTime)
        else:
            self.periodLength = int((self.waveform.size)*self.detectionTime)

        self.pointsToRead = int(self.periodLength/self.scaling_fac)
        self.bufferSize = int(self.numberPointsComp*self.detectionTime) #200  
        #self.bufferSize = self.pointsToRead
        #self.pointsToRead = int(self.numberPointsComp*self.detectionTime)
        self.data_in = numpy.zeros(self.pointsToRead, dtype=numpy.float64)

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
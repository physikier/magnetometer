import time
import pyvisa
import visa
import numpy as np


class DG3000(object):

    def __init__(self,device, channel=None):

        self.__connect_serial(device)

    def __write(self, cmd):
        self.__instr.write(cmd)


    def __query(self, cmd):
        return self.__instr.query(cmd)

    
    def __read(self):
        return self.__instr.read()



    def __connect_serial(self, device, timeout=1):
        """connects to the tektronix function generator"""
        if hasattr(visa,"instrument"): #old visa
            instr=visa.instrument(device)
            instr.timeout=1
            print 'connecting with old visa'
        else:
            print 'connecting with new visa'
            instr = visa.ResourceManager().open_resource(device)
        #instr.timeout=1*2000
        instr.query_delay = 2.5
        instr.read_termination = '\n'
        instr.write_termination = '\n'          
        #instr.chunk_size=4096  
        
        self.__instr = instr

    def identification(self):
        """asks for identification information"""
        return self.__query('*IDN?')



    def close_rigol(self):
        self.ser.close()



    def check_ch(self,ch):
        """checks the channel number"""
        if ch in [1,2]:
            return ch
        else:
            raise ValueError('Wrong channel number. Chose 1 or 2.')



    def get_output(self, channel=1):
        """asks if output is ON/OFF"""
        self.check_ch(channel)
        if channel == 1:
            output = self.__query('OUTP?')
        else:
            output = self.__query('OUTP:CH2?')
        return output



    def set_output(self, channel=1, output="OFF"):
        """sets output ON/OFF"""
        self.check_ch(channel)
        if output in ["OFF", "ON"]:
            if channel == 1:
                set_output = self.__write('OUTP {:s}'.format(output))
            else:
                set_output = self.__write('OUTP:CH2 {:s}'.format(output))
        else:
            raise ValueError('wrong input string (only: OFF/ON)')

   

    def get_waveform(self, channel=1):
        """ask for waveform (function)"""
        self.check_ch(channel)
        if channel == 1:
            waveform = self.__query('FUNC?')
        else:
            waveform = self.__query('FUNC:CH2?')
        return waveform


    
    def set_waveform(self, channel=1, function="SIN"):
        """set desired waveform (functions available: SINusoid, SQUare, RAMP, PULSe, NOISe, DC, USER)"""
        self.check_ch(channel)
        if channel == 1:
            set_waveform = self.__write('FUNC {:s}'.format(function))
        else:
            set_waveform = self.__write('FUNC:CH2 {:s}'.format(function))


    
    def get_freq(self, channel=1,):
        """asks for frequency"""
        self.check_ch(channel)
        if channel == 1:
            freq = self.__query('FREQ?')
        else:
            freq = self.__query('FREQ:CH2?')
        return freq


    
    def set_freq(self, channel=1, frequency=1):
        """set desired frequency value [Hz]"""
        self.check_ch(channel)
        if frequency <= 0:
            raise ValueError('The selected frequency must be greater than zero. Or maybe you are just dumb!')
        if frequency > 200e6:
            raise ValueError('The selected frequency is too high, max frequency: 200MHz. Or maybe you are just dumb!')
        else:
            if channel == 1:
                set_freq = self.__write('FREQ {:1.5f}'.format(frequency))
            else:
                set_freq = self.__write('FREQ:CH2 {:1.5f}'.format(frequency))


    
    def get_ampl(self, channel=1):
        """asks for amplitude [Vpp]"""
        self.check_ch(channel)
        if channel == 1:
            amplitude = self.__query('VOLT?')
        else:
            amplitude = self.__query('VOLT:CH2?')
        return amplitude


    
    def set_ampl(self, channel=1, amplitude=0):
        """set desired amplitude [Vpp]"""
        self.check_ch(channel)
        if amplitude < 0:
            raise ValueError('The selected amplitude [Vpp] must be greater than zero. Or maybe you are just dumb!')
        if amplitude > 20.0 :
            raise ValueError('The selected amplitude [Vpp] is too high, max amplitude: 20 Vpp. Or maybe you are just dumb!')
        else:
            if channel == 1:
                set_ampl = self.__write('VOLT {:f}'.format(amplitude))
            else:
                set_ampl = self.__write('VOLT:CH2 {:f}'.format(amplitude))



    def get_off(self, channel=1):
        """asks for offset [VDC]"""
        self.check_ch(channel)
        if channel == 1:
            offset = self.__query('VOLT:OFFS?')
        else:
            offset = self.__query('VOLT:OFFS:CH2?')
        return offset



    def set_off(self, channel=1, offset=0):
        """set desired offset [VDC]"""
        self.check_ch(channel)
        if offset < 0:
            raise ValueError('The selected offset [VDC] must be greater than zero. Or maybe you are just dumb!')
        if offset > 20.0 :
            raise ValueError('The selected offset [VDC] is too high, max offset: 20 VDC. Or maybe you are just dumb!')
        else:
            if channel == 1:
                set_off = self.__write('VOLT:OFFS {:f}'.format(offset))
            else:
                set_off = self.__write('VOLT:OFFS:CH2 {:f}'.format(offset))


    
    def get_phase(self, channel=1):
        """asks for phase"""
        self.check_ch(channel)
        if channel == 1:
            phase = self.__query('PHAS?')
        else:
            phase = self.__query('PHAS:CH2?')
        return phase

   
   
    def set_phase(self, channel=1, phase=0):
        """sets phase to the desired value [deg]"""
        self.check_ch(channel)
        if channel == 1:
            set_phase = self.__write('PHAS {:f}'.format(phase))
        else:
            set_phase = self.__write('PHAS:CH2 {:f}'.format(phase))

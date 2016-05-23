import time
import pyvisa
import visa
import numpy as np


class SR844():

    def __init__(self,device, channel=None):
        """
        Provides communication with a Stanford Research Lock-In
        Amplifier via GPIB connection
        
        Connection Examples:
        
            lockin = SR844("GPIB::08::INSTR)
        """
        rm = pyvisa.ResourceManager()
        instr = rm.open_resource(device)
        self.instr = instr

    
    def identification(self):
        """asks for identification information"""
        idn = self.instr.query('*IDN?')
        return idn

    def get_frequency(self):
        """asks for detection frequency"""
        getfreq=self.instr.query('FREQ?')
        return getfreq

    def set_frequency(self,frequency):
        """set detection frequency"""
        if frequency >= 2.5E4 and frequency <= 2.0E8:
            mode = self.getreferencemode()
            if mode == 1:
                self.instr.write('FREQ {0:1.5f}'.format(frequency))
            else:
                raise ValueError('this command is allowed only if the reference mode is Internal (mode = 1)')
        else:
            raise ValueError('frequency is not in the allowed range (2.5E4 <= f <= 2.0E8)')
        
    def get_reference_mode(self):
        """ask for reference mode (Internal: i=1, External: i=0)"""
        reference = self.instr.query('FMOD?')
        return int(reference)

    def set_reference_mode(self,mode):
        """set refernce mode (modes: Internal: i=1, External: i=0"""
        if mode in [0,1]:
            self.instr.write('FMOD {0:d}'.format(mode))
        else:
            raise ValueError('refernce mode has to be 0 or 1. (Internal: i=1, External: i=0)')

    def get_detection_mode(self):
        """ask for detection mode (F: i=0, 2F: i=1)"""
        detectionmode = self.instr.query('HARM?')
        return int(detectionmode)

    def set_detection_mode(self,mode):
        """ set detection mode (detect at F: i=0, detect at 2F: i=1)"""
        if mode in [0,1]:
            self.instr.write('HARM {0:d}'.format(mode))
        else:
            raise ValueError('detection mode hast to be 0 or 1 (F: i=0, 2F: i=1)')

class SR830():


    def __init__(self, device, channel=None):
        """
        Provides communication with a Stanford Research Lock-In
        Amplifier via GPIB connection
        
        Connection Examples:
        
            lockin = SR844("GPIB::10::INSTR)

        The address is set
        with the [Setup] key on the front panel of the SR830 and may be set between 1
        and 30
        Make sure that the interface is set to GPIB via the [Setup] key]
        """
        rm = pyvisa.ResourceManager()
        instr = rm.open_resource(device)
        self.instr = instr

    def identification(self):
        """asks for identification information"""
        idn = self.instr.query('*IDN?')
        return idn

    def get_phase(self):
        """Queries the reference phase shift"""
        phase = self.instr.query('PHAS?')
        return phase

    def set_phase(self, phase):
        """Sets the reference phase shift in the range of -180.00 to +180.00"""
        if phase >= -180 and phase <= 180:
            self.instr.write('PHAS {0:.2f}'.format(phase))
        else: 
            raise ValueError('Phase value out of range. Select a reference phase in the range from -180 to +180')
   
    def get_reference_mode(self):
        """Queries the reference mode"""
        reference = self.instr.query('FMOD?')
        reference = int(reference)
        if reference == 1: 
            return "Internal reference"
        elif reference == 0: 
            return "External reference"
        else: return int(reference)

    def set_reference_mode(self, mode):
        """Sets the refernce mode (modes: Internal: i=1, External: i=0"""
        if mode in [0,1]:
            self.instr.write('FMOD {0:d}'.format(mode))
        else:
            raise ValueError('Reference mode has to be 0 or 1. (Internal: i=1, External: i=0)')

    def get_frequency(self):
        """Queries the reference frequency"""
        getfreq=self.instr.query('FREQ?')
        return getfreq

    def set_frequency(self, frequency):
        """Sets the reference frequency"""
        if frequency >= 0.001 and frequency <= 102000:
            mode = self.get_reference_mode()
            if mode == "Internal reference":
                harm = self.get_harmonic()
                harm = int(harm)
                if harm*frequency <= 102000:
                    self.instr.write('FREQ {0:.5f}'.format(frequency))
                else: 
                    raise ValueError('Value for the harmonic is too high. Keyword harm has to fulfill the condition harm*freq<=102kHz.')
            else:
                raise ValueError('This command is allowed only if the reference mode is Internal (mode = 1)')
        else:
            raise ValueError('Frequency is not in the allowed range (0.001 Hz <= f <= 102000 Hz)')

    def get_harmonic(self):
        """Queries the detection harmonic."""
        harm = self.instr.query('HARM?')
        return harm

    def set_harmonic(self, harm):
        """Sets the detection harmonic. Keyword argument harm has to be an integer"""
        if harm >=1 and harm <=19999:
            freq = float(self.get_frequency())
            if harm*freq <= 102000:
                self.instr.write('HARM {0:d}'.format(harm))
            else:
                raise ValueError('Value for the harmonic is too high. Keyword harm has to fulfill the condition harm*freq<=102kHz.')
        else:  raise ValueError('Value for the harmonic has to be between 1 and 19999.')

    def get_sensitivity(self):
        """Queries the sensitivity
        i=0:2nV/fA, i=1:5nV/fA, i=2: 10nV/fA, i=3: 20nV/fA, i=4: 50nV/fA, i=5: 100nV/fA
        i=6: 200nV/fA, i=7: 500nV/fA, i=8: 1uV/pA, 
        i=9: 2uV/pA, i=10: 5uV/pA, 
        i=11: 10uV/pA, i=12: 20uV/pA, i=13: 50uV/pA,
        i=14: 100uV/pA, i=15: 200uV/pA,
        i=16:500uV/pA, i=17: 1mV/nA, i=18: 2mV/nA, 
        i=19: 5mV/nA, i=20: 10mV/nA,
        i=21: 20mV/nA, i=22: 50mV/nA, i=23: 100mV/nA, 
        i=24: 200mV/nA, i=25: 500mV/nA,
        i=26: 1V/uA"""
        sensi = self.instr.query("SENS?")
        sensi = int(sensi)
        return sensi

    def set_sensitivity(self, sensi):
        """Queries the sensitivity. Argument sensi has to be an integer in the range from 0 to 26
        i=0:2nV/fA, i=1:5nV/fA, i=2: 10nV/fA, 
        i=3: 20nV/fA, i=4: 50nV/fA, i=5: 100nV/fA
        i=6: 200nV/fA, i=7: 500nV/fA, i=8: 1uV/pA,
        i=9: 2uV/pA, i=10: 5uV/pA, 
        i=11: 10uV/pA, i=12: 20uV/pA, i=13: 50uV/pA,
        i=14: 100uV/pA, i=15: 200uV/pA,
        i=16:500uV/pA, i=17: 1mV/nA, i=18: 2mV/nA,
        i=19: 5mV/nA, i=20: 10mV/nA,
        i=21: 20mV/nA, i=22: 50mV/nA, i=23: 100mV/nA,
        i=24: 200mV/nA, i=25: 500mV/nA,
        i=26: 1V/uA"""

        if sensi in list(range(27)):
            self.instr.write("SENS {0:d}".format(sensi))
        else: 
            raise ValueError('Keyword has to be an integer between 0 and 26.')


    def get_time_constant(self):
        """ Queries the time constant
        i=0: 10us, i=1: 30us, i=2: 100us, i=3: 300us,
        i=4: 1ms, i=5: 3ms, i=6: 10ms, i=7: 30ms,
        i=8: 100ms, i=9: 300ms, i=10: 1s, i=11: 3s,
        i=12: 10s, i=13: 30s, i=14: 100s, i=15: 300s,
        i=16: 1ks, i-17: 3ks, i=18: 10ks, i=19: 30ks"""
        time = self.instr.query("OFLT?")
        time = int(time)
        return time

    def set_time_constant(self, time):
        """ Sets the time constant
        i=0: 10us, i=1: 30us, i=2: 100us, i=3: 300us,
        i=4: 1ms, i=5: 3ms, i=6: 10ms, i=7: 30ms,
        i=8: 100ms, i=9: 300ms, i=10: 1s, i=11: 3s,
        i=12: 10s, i=13: 30s, i=14: 100s, i=15: 300s,
        i=16: 1ks, i-17: 3ks, i=18: 10ks, i=19: 30ks"""
        if type(time) == int:
            if time in list(range(20)):
                self.instr.write("OFLT {0:d}".format(time))
            else: 
                raise ValueError('Argument has to be an integer between 0 and 19.')
        else: 
            raise ValueError('Argument has to be an integer between 0 and 19.')

    def get_low_pass_filter(self):
        """Queries the low pass filter slope. 
        The parameter i means: i=0: 6dB/oct, 
        i=1: 12dB/oct, i=2: 18dB/oct, i=3: 24dB/oct"""
        fil = self.instr.query("OFSL?")
        fil = int(fil)
        return fil

    def set_low_pass_filter(self, fil):
        """Sets the low pass filter slope. 
        The parameter i means: i=0: 6dB/oct, 
        i=1: 12dB/oct, i=2: 18dB/oct, i=3: 24dB/oct"""
        if type(fil) == int:
            if fil in list(range(4)):
                self.instr.write("OFSL {0:d}".format(fil))
            else: 
                raise ValueError('Argument has to be in the range of 0 to 3.')
        else: 
            raise ValueError('Argument has to be an integer.')

    def get_sync(self):
        """Queries the synchronous filter status. 
        The parameter i means: i=0: Off and i=1: synchronous filtering below 200 Hz.
        Synchronous filtering is tuned on only if the detection frequency is less than 200 Hz"""
        sync = self.instr.query("SYNC?")
        sync = int(sync)
        return sync

    def set_sync(self, sync):
        """Sets the synchronous filter status. 
        The parameter i means: i=0: Off and i=1: synchronous filtering below 200 Hz.
        Synchronous filtering is tuned on only if the detection frequency is less than 200 Hz"""
        if type(sync) == int:
            if sync in [0, 1]:
                self.instr.write("SYNC {0:d}".format(sync))
            else:
                raise ValueError('Argument has to be either 0 or 1.')
        else: 
            raise ValueError('Argument has to be an integer.')

    # def get_output_source(self):
    #     """Queries the front panel output source (channel1 or channnel2).
    #     The out parameter defines weather the channel display (out=0) or
    #     X/Y (out=1) is selected"""
    #     params = self.instr.query("FPOP?")
    #     return params

    def get_output(self):
        """Queries the outout interface: i=0 for RS232 and i=1 for GPIB"""
        out = self.instr.query('OUTX?')
        return out

    def set_output(self, out):
        """Sets the outout interface: i=0 for RS232 and i=1 for GPIB.
        If you are connected only via one of the interfaces do not use set output, 
        otherwise you have to change the output interface via the fron panel."""

        if type(out) ==int:
            if out in [0,1]:
                out = self.instr.write('OUTX {0:d}'.format(out))
            else:
               raise ValueError('Argument has to be either 0 or 1.')
        else: 
            raise ValueError('Argument has to be an integer.')

    def get_grounding(self):
        """Queries the input shield grounding.
        The parameter i means Float (i=0) or Ground (i=1)"""
        grounding = self.instr.query("IGND?")
        grounding = int(grounding)
        return grounding

    def set_grounding(self, grounding):
        """Sets the input shield grounding.
        The parameter i selects Float (i=0) or Ground (i=1)"""
        if grounding in [0,1]:
            self.instr.write("IGND {0:d}".format(grounding))
        else:
            raise ValueError('Argument has to be either 0 or 1.')


    def get_coupling(self):
        """Queries the input coupling.
        The parameter i means AC (i=0) or DC(i=1)"""
        coupling = self.instr.query("ICPL?")
        coupling = int(coupling)
        return coupling

    def set_coupling(self, coupling):
        """Sets the input shield coupling.
        The parameter i selects AC (i=0) or DC (i=1)"""
        if coupling in [0,1]:
            self.instr.write("ICPL {0:d}".format(coupling))
        else:
            raise ValueError('Argument has to be either 0 or 1.')

    def get_filter_status(self):
        """Queries the input line notch filter status.
        The parameter i means no filters (i=0), Line notch in (i=1), 
        2xLine notch in (i=2) or both notch filters in (i=3)"""
        filters = self.instr.query("ILIN?")
        filters = int(filters)
        return filters

    def set_filter_status(self, filters):
        """Sets the input line notch filter status.
        The parameter i means no filters (i=0), Line notch in (i=1), 
        2xLine notch in (i=2) or both notch filters in (i=3)"""
        if filters in [0, 1, 2, 3]:
            self.instr.write("ILIN {0:d}".format(filters))
        else:
            raise ValueError('Argument has to be either 0, 1, 2 or 3.')

    def get_reserve_mode(self):
        """Queries the reserve mode.
        The parameter i means High Reserve (i=0), Normal (i=1) or
        Low Noise (i=2)"""
        reserve = self.instr.query("RMOD?")
        reserve = int(reserve)
        return reserve

    def set_reserve_mode(self, reserve):
        """Sets the reserve mode.
        The parameter i means High Reserve (i=0), Normal (i=1) or
        Low Noise (i=2)"""
        if reserve in [0, 1, 2]:
            self.instr.write("RMOD {0:d}".format(reserve))
        else:
            raise ValueError('Argument has to be either 0, 1, or 2.')

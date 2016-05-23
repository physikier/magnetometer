'''
Created on 20.04.2012

author: Helmut Fedder
'''

import time
import visa
import numpy as np

# helper class to represent a visa instrument via a socket
class SocketInstrument():
    def __init__(self, device):
        import socket
        host,port = device.split(':')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        self.sock = sock
        
    def write(self, cmd):
        """Sends a command over the socket"""
        cmd_string = cmd + '\n'
        sent = self.sock.sendall(cmd_string)
        if sent != None:
            raise RuntimeError('Transmission failed')
        time.sleep(.1) #add a timeout for the transfer to take place. Should be replaced by a proper error handling at some point
        
    def ask(self,question):
        """sends the question and receives the answer"""
        self.write(question)
        answer = self.sock.recv(2000)#2000#2048
        return answer[:-2]
        
    def close(self):
        self.sock.close()


class HMP2030():

    voltage_max = [0.,0.,0.]
    current_max = [0.,0.,0.]

    def __init__(self,device, channel=None, voltage_max=20., current_max=2.0, fuse_voltage_max=20.0, fuse_current_max=2.5):
        """
        Provides communication with a HMP2030 power supply
        via USB (virtual COM) or LAN.
        
        Usage Examples:
        
            hmp = HMP2030('ASRL11::INSTR')
            hmp = HMP2030('192.168.0.11:50000')
        
        Parameters:
        
            device:        string that describes the device (see examples above)
            
        Optional Parameters:
            voltage_max:   maximum allowed voltage
            current_max:   maximum allowed current
            fuse_voltage_max:    maximum allowed fuse voltage
            fuse_current_max:    maximum allowed fuse current
        """
        if 'ASRL' in device:
            self.__connect_serial(device)
        else:
            self.__connectLAN(device)
            

        self.fuse_voltage_max=fuse_voltage_max
        self.fuse_current_max=fuse_current_max
        if channel == None:
            self.channel = 1
        else: 
            self.channel = channel 
        self.set_ch(self.channel)

        
        self.voltage_max[self.channel-1]=voltage_max
        self.current_max[self.channel-1]=current_max
        

    def __connect_serial(self, device):
        #old visa
        if hasattr(visa,"instrument"):
            instr=visa.instrument(device)
            instr.timeout=1
        else:
            instr = visa.ResourceManager().open_resource(device)
            instr.timeout=1000
        #instr.term_chars='\n'
        #instr.chunk_size=4096
        
        self.instr = instr

    # def _connectLAN(self, device):
    #     """connects to the hameg powersupply"""
    #     self.instr=SocketInstrument(device)    

    def __connectLAN(self, device):
        """connects to the rigol powersupply"""
        if hasattr(visa,"instrument"):
            self.__ip = device
            self.__instr = visa.Instrument(self.__ip,term_chars='\n')
            self.__instr.timeout=2
        else:
            self.__ip = device
            self.__instr = visa.ResourceManager().open_resource(device) 
            self.__instr.read_termination = '\n'
            self.__instr.write_termination = '\n'
            self.__instr.timeout=2000
        self.__instr.chunk_size=4096         
    
    # convenience method
    def set_output(self,current,ch=None):
        """Set the current on the given channel. Turn output on or off depending on the specified current."""
        print("CALL TO DEPRECATED FUNCTION \"set_output\" in Hameg. Use \"set_current\" instead!")
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        if current<=0 or current is None:
            self.stop()
        else:
            self.set_current(current)
            self.run()
    
    #functions to perform different SCPI-commands            
    def set_ch(self,ch):
        """sets the channel 1, 2 or 3"""
        if ch in [1,2,3]:
            self.__instr.write('INST OUT' + str(ch))
            self.channel = ch
        else:
            raise ValueError('Wrong channel number. Chose 1, 2 or 3.')
    
    def get_ch(self):
        """asks for the selected channel"""
        channel = int(self.__instr.ask('INST:NSEL?'))
        return channel
    
    def status(self,ch=None):
        """gets the current status of the selected channel (CC or CV)"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch==None:
            raise ValueError("No channeld specified.")
        state = self.__instr.ask('STAT:QUES:INST:ISUM' + str(ch) + ':COND?')
        if state == 1:
            return 'CC'
        elif state == 2:
            return 'CV'
        else:
            print("Couldn't read the status of the selected channel.")
    
    def set_voltage(self,volt,ch=None):
        """sets the voltage to the desired value"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        if volt < 0:
            print('The selected voltage cannot be set.')
        elif volt > self.voltage_max[ch-1] :     #the voltage_max will be set on the power supply if volt exceed voltage_max 
            self.__instr.write('VOLT %1.5f' %self.voltage_max[ch-1])
            print('The set voltage exceed the maximum voltage: %1.5f' %self.voltage_max[ch-1])
        else:
            self.__instr.write('VOLT %1.5f' %volt)
     
    def set_voltage_step(self,vstep,ch=None):
        """increases the voltage by a desired step"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        vset = get_voltage()
        set_voltage(vset + vstep)
    
    def get_voltage(self,ch=None):
        """measures the voltage"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        voltage = float(self.__instr.ask('MEAS:VOLT?'))
        return voltage
        
    def set_current(self,curr,ch=None):
        """sets the current to the desired value"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        if curr < 0:
            raise ValueError('The selected current must be greater than zero.')
        elif curr > self.current_max[ch-1]:    #the voltage_max will be set on the power supply if volt exceed voltage_max 
            self.__instr.write('CURR %1.5f' %self.current_max[ch-1])
            raise ValueError('The set current exceed the maximum current: %1.5f' %self.current_max[ch-1])
        else:
            self.__instr.write('CURR %1.5f' %curr)
    
    def set_current_step(self,cstep,ch=None):
        """increases the current by a desired step"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        cset = get_current()
        set_current(cset + cstep)
    
    def get_current(self,ch=None):
        """measures the current"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        current = float(self.__instr.ask('MEAS:CURR?'))
        return current

    def set_max_voltage(self,ch, max_voltage):
        if ch==None and self.channel != None:
            ch=self.channel
        if ch==None:
            raise ValueError("No channel specified.")
        self.voltage_max[ch-1] = max_voltage

    def set_max_current(self,ch, max_current):
        if ch==None and self.channel != None:
            ch=self.channel
        if ch==None:
            raise ValueError("No channel specified.")
        self.current_max[ch-1] = max_current
        
    def set_arbitrary(self,seq,N,ch=None):
        """performs a sequence of voltage and current values for a given time on one channel with a number of repetitions.
           ch: channel for output
           seq: sequence to be set in form of a nested list = [(voltage,current,time),(..),(..),...]
           N: number of repetitions [1..255]. 0 means infinite repetitions."""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch==None:
            raise ValueError("No channel specified.")

        seq_ary = np.array(seq)
        if max(seq_ary[:,0]) > self.voltage_max[ch-1]:
            print('The set voltage exceed the maximum voltage: %1.5f' %self.voltage_max[ch-1])
        elif max(seq_ary[:,1]) > self.current_max[ch-1]:
            print('The set current exceed the maximum current: %1.5f' %self.current_max[ch-1])
        elif min(seq_ary[:,2]) < .5:
            print('The set time is shorter than 0.5s.')
        elif seq >= 0:
            print('Negative value of voltage, current or time.')
        elif ch != [1,2,3]:
            print('Wrong channel number. Chose 1, 2 or 3.')
        elif N != range(0,256):
            print('The set repetitions are outside the range [0,255].')
        else:
            self.__instr.write('ARB:DATA' + ' ' + str(seq).translate(None, '[()] '))
            self.__instr.write('ARB:REP' + ' ' + str(N))
            self.__instr.write('ARB:TRANS' + ' ' + str(ch))
            self.__instr.write('ARB:STAR' + ' ' + str(ch))
            set_ch(ch)
            run()
    
    def stop_arbitrary(self,ch=None):
        """stops the arbitrary sequence of a specified channel ch, but leafs the output on."""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch==None:
            raise ValueError("No channel specified.")
        self.__instr.write('ARB:STOP' + ' ' + str(ch))
    
    def get_arbitrary(self,ch=None):
        """gets the number of performed repetitions of the arbitrary sequence"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        num = int(self.__instr.ask('ARB:REP?'))
        return num
        
    def get_all(self):
        """gets the measured values for all channels in the form [(ch,V,A),]"""
        l = []
        for i in [1,2,3]:
            set_ch(i)
            vset = get_voltage()
            cset = get_current()
            l.append((i,vset,cset))
        return l
    
    def run(self,ch=None):
        if ch==None and self.channel != None:
            ch=self.channel
            self.set_ch(ch)
        """turns the output from the chosen channel on"""
        self.__instr.write('OUTP ON')
        
    def run_all(self):
        """turns the output from all channels on"""
        self.set_ch(1)
        self.__instr.write('OUTP:SEL ON')
        self.set_ch(2)
        self.__instr.write('OUTP:SEL ON')
        self.set_ch(3)
        self.__instr.write('OUTP:SEL ON')
        self.__instr.write('OUTP:GEN ON')
    
    def stop(self,ch=None):
        """turns the output from the chosen channel off"""
        if ch==None and self.channel!=None:
            ch=self.channel
            self.set_ch(ch)  
        self.set_ch(ch)
        self.__instr.write('OUTP OFF')
            
    def stop_all(self):
        """stops the output of all channels"""
        self.set_ch(1)
        self.__instr.write('OUTP:SEL OFF')
        self.set_ch(2)
        self.__instr.write('OUTP:SEL OFF')
        self.set_ch(3)
        self.__instr.write('OUTP:SEL OFF')
        self.__instr.write('OUTP:GEN OFF')
    
    def start(self):
        """starts up the whole system"""
        self.__instr.write('*RST') #resets the device
        self.__instr.write('SYST:REM') #sets the instrument to remote control
        
    def close(self):
        """stops and disconnects the device"""
        self.stop_all()
        self.__instr.close()
        
    def beep(self):
        """gives an acoustical signal from the device"""
        self.__instr.write('SYST:BEEP')
        
    def error_list(self):
        """prints all errors from the error register."""
        error = str(self.__instr.ask('SYST:ERR?'))
        return error
    
    def OVP(self,fuse_voltage_max,ch=None):
        """sets the Over-Voltage-Protection to the value fuse_voltage_max for a selected channel"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        if fuse_voltage_max < 0:
            print('The selected value for voltage protection cannot be set.')
        elif fuse_voltage_max > 32.0: #the maximal voltage which the HMP2030 supplies
            print('The set voltage exceed the maximum voltage: 32V' )
        else:
            self.__instr.write('VOLT:PROT %1.5f' %fuse_voltage_max)
        
    def FUSE(self,fuse_current_max,ch=None):
        """sets the fuse to the value fuse_current_max and the delay time to 0ms for a selected channel"""
        if ch==None and self.channel != None:
            ch=self.channel
        if ch!=None:
            self.set_ch(ch)
        self.__instr.write('FUSE ON')
        if fuse_current_max < 0:
            print('The selected value for current fuse cannot be set.')
        elif fuse_current_max > 5.0: #the maximal current which the HMP2030 supplies
            print('The set current exceed the maximum current: 5A' )
        else:
            self.__instr.write('CURR %1.5f' %fuse_current_max)
        self.__instr.write('FUSE:DEL 0')


class BipolarHMP2030():
    
    def __init__(self, hmp, relais):
        self.hmp = hmp
        self.relais = relais

    def _get_polarity(self,ch=None):
        """returns the polarity p of a given channel ch.
           The polarity is 1 for (+ -> 1, - -> 2 | [1,0,1,0,1,0,0,0])
           and -1 for (+ -> 2, - -> 1 | [0,1,0,1,0,1,0,0])."""
        if ch==None and self.hmp.channel != None:
            ch=self.hmp.channel
        r = self.relais.getPort()
        if ch not in [1,2,3]:
            raise ValueError('Wrong channel number. Chose 1, 2 or 3.')
        elif r[2*ch-2]==r[2*ch-1]:
            raise ValueError('Undefined polarity.')
        elif r[2*ch-2]==1 and r[2*ch-1]==0:
            return 1
        elif r[2*ch-2]==0 and r[2*ch-1]==1:
            return -1
        else:
            raise ValueError("Couldn't get the polarity.")
        
    def _set_polarity(self,p,ch=None):
        """sets the polarity p of a given channel ch.
           It ramps down the current and changes the polarity.
           The output is turned off when the polarity is switched"""
        if ch==None and self.hmp.channel != None:
            ch=self.hmp.channel   
        r = self._get_polarity(ch)
        if ch not in [1,2,3]:
            raise ValueError('Wrong channel number. Chose 1, 2 or 3.')
        elif p not in [-1,1]:
            raise ValueError('Undefined polarity.')                
        elif r != p:
            self.hmp.set_ch(ch)
            self.hmp.set_voltage(0.0)
            time.sleep(0.5) # add a timeout for the current to settle
            self.hmp.stop()
            time.sleep(0.1)
            x = [0,0,0,0,0,0,0,0]
            x[2*ch-2] = 1
            x[2*ch-1] = 1
            self.relais.Toggle(x)
            time.sleep(0.1)
            s = self._get_polarity(ch)
            if s != p:
                raise ValueError("cannot change polarity")
    
    def set_voltage(self, voltage,ch=None):
        if ch==None and self.hmp.channel != None:
            ch=self.hmp.channel
        if ch==None:
            raise ValueError("No channel specified.")
        polarity = np.sign(voltage)
        if polarity == 0:
            polarity = 1
        self._set_polarity(1, polarity,ch=ch)
        self.hmp.set_ch(1)
        self.hmp.run()        
        self.hmp.set_voltage(abs(voltage),ch=ch)

# environment variable to qt4, to tell Traits that we will use Qt.
import os
os.environ['ETS_TOOLKIT'] = 'qt4'
from traits.api import HasTraits, Range, Enum, Float, on_trait_change
from traitsui.api import View, Item, CheckListEditor

class HMP2030Traits( HMP2030, HasTraits ):
    
    current_max_value = Float(default_value=2.0)
    voltage_max_value = Float(default_value=20.0)

    def __init__(self, device, channel=None,voltage_max=20.0, current_max=2.0, fuse_voltage_max=20.0, fuse_current_max=2.5, **kwargs):
        HMP2030.__init__(self, device, channel, voltage_max, current_max, fuse_voltage_max, fuse_current_max)
        self.add_trait('current', Range(low=0.0, high='current_max_value', value=self.get_current(), label='Current [A]', auto_set=False, enter_set=True))
        self.add_trait('voltage', Range(low=0.0, high='voltage_max_value', value=self.get_voltage(), label='Voltage [V]', auto_set=False, enter_set=True))
        self.add_trait('channel', Enum())
        HasTraits.__init__(self, **kwargs)


    def _current_changed(self, new):
        self.set_current(new)
    
    def _voltage_changed(self, new):
        self.set_voltage(new)

    

    view = View(
        Item('current'),
        Item('voltage'),
        title='HMP2030',
        buttons=[],
        resizable=True)


#-------------------------------------------------------------------------------------------------------------------------

#define the sub-function including:set_channel, set_voltage, set_current and run    
#def set(ch):
#    write('SYST REM')
#    write('INST OUPT1')
#    write('OUTP OFF')

#
#write('SYST REM')   #to remote control 
#write('INST OUPT1') #select channel 1
#stop()

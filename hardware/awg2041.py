import time
from threading import Thread
import numpy as np
import visa
from socket import SOL_SOCKET, SO_KEEPALIVE
from ftplib import FTP, error_temp
#from waveform import *
import array
# UI
from traits.api import HasTraits, Range, Float, Bool, Int, Str, Enum, Button, Property, Instance, on_trait_change
from traitsui.api import View, VGroup, HGroup, Item, TextEditor, EnumEditor


# TODO: File-transfer via GPIB as emergency
def zerosTR(value):
        return value*0.

class AWG2041( object ):
    """Controller for the Tektronix AWG520 device.
    
    SCPI commands are issued via gpib.
    See device manual for command documentation.
    File management is done via FTP.
    
    """
    
    def __init__(self, gpib='GPIB0::04::INSTR' ):
        #print 'gpib_addr: ',gpib
        self.gpib_addr = gpib
        if hasattr(visa,'instrument'):
            self.gpib = visa.instrument(self.gpib_addr)
        else:
            self.gpib = visa.ResourceManager().open_resource(self.gpib_addr)
        self.gpib.timeout = 5.0
        
    def __del__(self):
        if hasattr(self, "gpib"):
            self.gpib.close()

    # very basic communiation commands
    
    def tell(self, command):
        """Send a command string to the AWG."""
        self.gpib.write(command)
        
    def ask(self, query):
        """Send a query string to AWG and return the response."""
        self.gpib.write(query)
        try:
            res = self.gpib.read()
        except visa.VisaIOError as e:
            res = ''
            if 'Timeout' in e.message:
                res = 'No response from AWG for: "' + query + '"'
            else:
                raise e
        return res
        
    # basic operation and set get commands
    def set_output(self,state='OFF', channel='NORM'):
        self.tell('OUTP:CH1:'+channel+':STAT '+state)
	
    def get_output(self):
        pass
        return self.ask('OUTP?')
    
    def set_WF_amplitude(self,amplitude=0.):
        if amplitude >2:
            print 'amplitude cannot be bigger than 2V'
        else:
            self.tell('CH1:AMPL '+str(amplitude))
    def get_WF_amplitude(self,amplitude=0.):
        pass
        return self.ask('CH1:AMPL?')
        
    def set_WF_power(self, power):
        newamp = np.sqrt(.1*10**(power/10.))
        print 'awg amplitude:', newamp
        self.tell(':CH1:AMPL %3.2fV' % newamp)
    def get_WF_power(self):
        amp = float(self.ask(':CH1:AMPLITUDE?'))
        return 10*np.log10(amp**2 / 50./2. / 1e-3)
        
        
    def set_WF_offset(self,offset=0.):
        if np.abs(offset) >1:
            print 'np.abs(offset) >1V not allowed'
        else:
            self.tell('CH1:OFFS '+ str(offset))
    def get_WF_offset(self):
        pass
        return self.ask('CH1:OFFS?')
    def set_WF_activewf(self,wfname,ftag='.WFM'):
        self.tell('CH1:WAV "'+wfname+ftag+'"')
    def get_WF_activewf(self):
        self.ask('CH1:WAV?')
    def set_WF_samplerate(self,samplerate):
        if samplerate > 1.024e9 or samplerate < 1.0e3:
            print 'samplerate excite allowed frequency range (1kHz-1.024GHz)'
        else:
            self.tell('CLOC:FREQ '+ str(samplerate))
    def get_WF_samplerate(self):
        pass
        return self.ask('CLOC:FREQ?')
    def set_bandwidth(self,bandwidth='full'):
        look_up = {'10':'M10','20':'M20','50':'M50','100':'M100','full':'THRU'}
        self.tell('CH1:FILT %s' % look_up[bandwidth])	
    def get_bandwidth(self):
        bandwidth = self.ask('CH1:FILT?')	
        look_up = {'M10':'10','M20':'20','M50':'50','M100':'100','THRU':'full'}
        return look_up[bandwidth]
    def set_trig_source(self,source):
        look_up = {'INT':'INTERNAL','EXT':'EXTERNAL'}
        self.tell('CLOC:SOUR '+ look_up[source])
    def get_trig_source(self):
        source=self.ask('CLOC:SOUR?')
        look_up = {'INTERNAL':'INT','EXTERNAL':'EXT'}
        return look_up[source]
    def set_wf_data(self,curve):
        self.tell('DATA:WIDTH 1')
        curve_length=np.size(curve)
        if np.mod(curve_length,32)!=0 or curve_length<1024:
            print 'sample length of curve must be a multiple of 32 and must have at least 1024 sample points'
        else:    
            curve_tosend = array.array('B',curve)
            self.tell('CURVE #%u%u%s\n' % (len( len(curve_tosend).__str__() ), len(curve_tosend), curve_tosend.tostring()))
    def get_wf_data(self):
        curve= self.ask('CURV?')
        if curve[0+7]=='#':
            curve_int =map(ord,curve[int(curve[1+7])+2+7::])
        else:
            curve_int =map(ord,curve[int(curve[1+7])+1+7::])
        return curve_int
    def set_wf_destfile(self,wfname):
        self.tell('DATA:DEST "'+wfname+'.WFM"')
    def get_wf_destfile(self):
        pass
        return self.ask('DATA:DEST?')
    def run(self):
        self.tell('START')
    def stop(self):
        self.tell('STOP')
    def set_mode(self, mode):
        """Change the output mode.
        
        Options for mode (case-insensitive):
        continuous - 'C', 'CONT'
        triggered  - 'T', 'TRIG'
        gated      - 'G', 'GAT'
        sequence   - 'S', 'SEQ'
        
        """
        look_up = {'C' : 'CONTINUOUS', 'CON' : 'CONTINUOUS', 'CONT' : 'CONTINUOUS',
                   'T' : 'TRIGGERED', 'TRI' : 'TRIGGERED', 'TRIG' : 'TRIGGERED',
                  
                  }
        self.tell(':MODE %s' % look_up[mode.upper()])
    def reset(self):
        """ Reset the AWG settings. """
        self.tell('*RST')
    
    # wf = waveform
    # t= timebase; standard is seconds
    
    
    
    def update_waveform(self,t,wf,wfname='cwf',onezero=True,paramset=None,mode='T'):
        #convert waveform to AWG output
        self.set_output('OFF')
        
        self.set_wf_destfile(wfname)
        wf_length=len(wf)
        if paramset==None:
            wf_range=(np.max(wf)-np.min(wf))
            wf_Offset=(np.max(wf)+np.min(wf))/2
            wf_shift=np.min(wf)
        else:
            wf_range=paramset[0]
            wf_Offset=paramset[1]
            wf_shift=paramset[2]
        if onezero:
            wf_rescaled=np.hstack([0,wf])
        else:
            wf_rescaled=wf
        missing= 1024-len(wf_rescaled) ;      # signal must have at least 1024 sample points
        '''print missing'''
        if missing >0:
            Zeros=np.zeros([1,missing])
            wf_rescaled=np.hstack([wf_rescaled,Zeros.flatten()])
        missing2 = (np.mod(len(wf_rescaled),32))   # signal must be a multiple of 32
        if missing2 !=0:
            missing2=32-missing2
            Zeros=np.zeros([1,missing2])
            wf_rescaled=np.hstack([wf_rescaled,Zeros.flatten()])
        
        wf_rescaled=wf_rescaled-wf_shift
        wf_rescaled=wf_rescaled/wf_range
        
        wf_conv=list()
        for w in wf_rescaled:
            wf_conv.append(np.uint8(w*255))
        self.set_wf_data(curve=wf_conv)
        if paramset==None:
            self.set_WF_activewf(wfname=wfname)
            self.set_WF_amplitude(wf_range)
            self.set_WF_offset(wf_Offset)
            dt=np.mean(t[1:]-t[:-1])
            self.set_WF_samplerate(1/dt)
            self.set_mode(mode)
        #return wf_conv,missing, missing2
        
        
    def update_waveform_advanced(self,t,wf,wfname='cwf',mode='T'):
        #convert waveform to AWG output
        self.set_output('OFF')
        
        if len(wf)>64000-1:  # check if the wf is to long and has to splited up in a sequence
            wf_range=(np.max(wf)-np.min(wf))
            wf_Offset=(np.max(wf)+np.min(wf))/2
            wf_shift=np.min(wf)
            paramset=list([wf_range,wf_Offset,wf_shift])
            wf=np.hstack([0,wf])
            missingpart = (np.mod(len(wf),64000))   
            if missingpart !=0:
                missingpart=64000-missingpart
            iterations=np.round((len(wf)+missingpart)/64000)
            wfIndex=map(str,range(iterations))
            wflist=list()
            
            for Iter,Index in zip(range(iterations),wfIndex):
                print 'uploading '+wfname+Index+'.wfm...\n'
                wflist.append(wfname+Index)
                self.update_waveform(t[Iter*64000:(Iter+1)*64000],wf[Iter*64000:(Iter+1)*64000],wfname=wfname+Index,onezero=False,paramset=paramset)
                print str(Iter*100/iterations)+'% done\n'
                
            self.define_sequence(seqname='CSEQ',wflist=wflist,repetition=1)
            self.set_WF_activewf(wfname='CSEQ',ftag='.SEQ')
            self.set_WF_amplitude(wf_range)
            self.set_WF_offset(wf_Offset)
            dt=np.mean(t[1:]-t[:-1])
            self.set_WF_samplerate(1/dt)
            self.set_mode(mode)
        
        else:
            self.update_waveform(t,wf,wfname=wfname)
        
        
    def define_sequence(self,seqname='cseq',wflist=list(['cwf']),repetition=1):
        wfstack=''
        for wf in wflist:
            wfstack=wfstack+wf.upper()+'.WFM, '+str(repetition)+'\n'
        wfstack=wfstack[:-1]
        message=':SEQUENCE:DEFINE "'+seqname.upper()+'.SEQ",#'+ str(len(str(len(wfstack))))+ str(len(wfstack))+ wfstack+'\n'
        self.tell(message)
        return message
        #wflist=list([['function',freq,phase,apply for x seconds],....
    
    
    def compile_standard_wf(self,wflist=list([['cos',10e6,np.pi,1e-4],['off',1.,np.pi,1e-4],['sin',20e6,np.pi,1e-4]]),resolution=1e-9):
        look_up={'cos':np.cos,'off':zerosTR,'sin':np.sin}
        wflength=0;wfplength=list() # get the full sample length
        for wfl in wflist: 
            wfplength.append(int(np.round(wfl[3]/resolution)))
            wflength=wflength+wfplength[-1]
            if np.abs(np.mod(wfl[3],resolution)-resolution)>0.00001:
                print 'warning: resolution should correspond to individual seq length'
        t=np.zeros([1,wflength]);t=t[0] # construct time trace
        for step in range(wflength):
            t[step]=step*resolution
        wf=np.zeros([1,wflength]);wf=wf[0] # construct wf
        flag=0
        for wfl,step in zip(wflist,wfplength):
            wf[flag:flag+step]=map(look_up[wfl[0]],((t[flag:flag+step]-t[flag])*2*np.pi*wfl[1]+wfl[2]))
            #print wf[flag:flag+step]
            flag=flag+step
        return t,wf 
    def set_DC_offset(self,offset):
        t=np.linspace(0,10e-3,1024)
        wf=np.ones([1024,1])*offset
        self.update_waveform(t,wf,wfname='DC',onezero=False)
        self.set_mode('C')

        
        















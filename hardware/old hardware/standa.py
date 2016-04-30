"""
This file provides control of standa stages using the c DLL functions via ctypes.

www.standa.lt
"""

import time

import inspect, os, cPickle

persistent_file = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),'standa.dat')

from ctypes import *

class USMC_Devices(Structure):
    _fields_ = [('NOD', c_long),
                ('Serial', POINTER(POINTER(c_char))),
                ('Version', POINTER(POINTER(c_char)))
                ]

class USMC_Parameters(Structure):
    _fields_ = [('AccelT',      c_float), # Acceleration time (in ms)
                ('DecelT',      c_float), # Deceleration time (in ms)
                ('PTimeout',    c_float), # Time (in ms) after which current will be reduced to 60% of normal
                ('BTimeout1',   c_float), # Time (in ms) after which speed of step motor rotation will be equal to the one specified at BTO1P field (see below). (This parameter is used when controlling step motor using buttons)
                ('BTimeout2',   c_float),
                ('BTimeout3',   c_float),
                ('BTimeout4',   c_float),
                ('BTimeoutR',   c_float), # Time (in ms) after which reset command will be performed
                ('BTimeoutD',   c_float), # This field is reserved for future use
                ('MinP',        c_float), # Speed (steps/sec) while performing reset operation. (This parameter is used when controlling step motor using buttons)
                ('BTO1P',       c_float), # Speed (steps/sec) after BTIMEOUT 1 time have passed. (This parameter is used when controlling step motor using buttons)
                ('BTO2P',       c_float),
                ('BTO3P',       c_float),
                ('BTO4P',       c_float),
                ('MaxLoft',     c_long),  # Value in full steps that will be used performing backlash operation
                ('StartPos',    c_long),  # Current Position Saved to FLASH see Test MicroSMC.cpp
                ('RTDelta',     c_uint),  # Revolution distance - number of full steps per one full revolution                
                ('RTMinError',  c_uint),  # Number of full steps missed to raise the error flag
                ('MaxTemp',     c_float), # Maximum allowed temperature (Celsius)
                ('SynOUTP',     c_long),  # Duration of the output synchronization pulse
                ('LoftPeriod',  c_float), # Speed of the last phase of the backlash operation.
                ('EncMult',     c_float), # Should be <Encoder Steps per Evolution> / <SM Steps per Evolution> and should be integer multiplied by 0.25
                ('Reserved',    c_byte*16), ### WARNING: according to the USMCDLL.h, it should be 16 bytes, however, in this case it crashes
                ]

class USMC_State(Structure):
    _fields_ = [('CurPos',      c_long),
                ('Temp',        c_float),
                ('SDivisor',    c_long),
                ('Loft',        c_long),
                ('FullPower',   c_long),
                ('CW_CCW',      c_long),
                ('Power',       c_long),
                ('FullSpeed',   c_long),
                ('AReset',      c_long),
                ('RUN',         c_long),
                ('SyncIN',      c_long),
                ('SyncOUT',     c_long),
                ('RotTr',       c_long),
                ('RotTrErr',    c_long),
                ('EmReset',     c_long),
                ('Trailer1',    c_long),
                ('Trailer2',    c_long),
                ('Voltage',     c_float), ### WARNING: 2.4 version only!!! ###
                ('Reserved',    c_byte*8), ### WARNING: according to the USMCDLL.h, it should be 8 bytes, however, in this case it crashes
                ]
    
#class USMC_Test(Structure):
#    _fields_ = [('all', c_byte*256)]
      
class USMC_EncoderState (Structure):
    _fields_ = [('EncoderPos',  c_long),
                ('ECurPos',     c_long),
                ('Reserved',    c_byte*8), ### WARNING: according to the USMCDLL.h, it should be 8 bytes, however, in this case it crashes
                ]

class USMC_Mode (Structure):
    _fields_ = [('PMode',       c_long),
                ('PReg',        c_long),
                ('ResetD',      c_long),
                ('EMReset',     c_long),
                ('Tr1T',        c_long),
                ('Tr2T',        c_long),
                ('RotTrT',      c_long),
                ('TrSwap',      c_long),
                ('Tr1En',       c_long),
                ('Tr2En',       c_long),
                ('RotTeEn',     c_long),
                ('RotTrOp',     c_long),
                ('Butt1T',      c_long),
                ('Butt2T',      c_long),
                ('ResetRT',     c_long),
                ('SyncOUTEn',   c_long),
                ('SyncOUTR',    c_long),
                ('SyncINOp',    c_long),
                ('SyncCount',   c_long),
                ('SyncInvert',  c_long),
                ('EncoderEn',   c_long),
                ('EncoderInv',  c_long),
                ('ResBEnc',     c_long),
                ('ResEnc',      c_long),
                ('Reserved',    c_byte*8),
                ]

class USMC_StartParameters (Structure):
    _fields_ = [('SDivisor',    c_long),
                ('DefDir',      c_long),
                ('LoftEn',      c_long),
                ('SlStart',     c_long),
                ('WSyncIN',     c_long),
                ('SyncOUTR',    c_long),
                ('ForceLoft',   c_long),
                ('Reserved',    c_byte*4),
                ]

dll = cdll.LoadLibrary('C:/WINDOWS/system32/USMCDLL.dll')
#dll = windll.LoadLibrary('C:/WINDOWS/system32/USMCDLL.dll')

#dll = cdll.LoadLibrary('C:/src/pi3diamond/standa_test/standa_test/USMCDLL.dll')
#dll = cdll.LoadLibrary('C:/WINDOWS/SysWOW64/USMCDLL.dll')
dll.USMC_Init.argtypes=[POINTER(USMC_Devices)]
dll.USMC_GetMode.argtypes=[c_long,POINTER(USMC_Mode)]
dll.USMC_SetMode.argtypes=[c_long,POINTER(USMC_Mode)]
dll.USMC_GetParameters.argtypes=[c_long,POINTER(USMC_Parameters)]
dll.USMC_SetParameters.argtypes=[c_long,POINTER(USMC_Parameters)]
dll.USMC_SaveParametersToFlash.argtypes=[c_long]
dll.USMC_GetState.argtypes=[c_long,POINTER(USMC_State)]
dll.USMC_GetStartParameters.argtypes=[c_long,POINTER(USMC_StartParameters)]
dll.USMC_GetEncoderState.argtypes=[c_long,POINTER(USMC_EncoderState)]
dll.USMC_Start.argtypes=[c_long,c_long,POINTER(c_float), POINTER(USMC_StartParameters)]

def chk( result ):
    if result == 0:
        return None
    else:
        s = c_char_p(' '*1024)
        n = c_long(1024)
        code = dll.USMC_GetLastErr(s,n)
        raise RuntimeError('Error code: '+str(code)+' '+s.value)

class Stage( object ):
    
    """Provides control over a Standa 8SMC1-USBhF stepper motor stage controller box."""

    def __init__(self):
        try:
            fil = open(persistent_file,'r')
            pos = cPickle.load(fil)
            fil.close()
        except:
            pos = [0,0,0]
        dev = USMC_Devices()
        chk( dll.USMC_Init(byref(dev)) )
        chk( dll.USMC_Init(byref(dev)) )
        #for i in range(dev.NOD):
        #    print dev.Serial[i][:16]
        #    print dev.Version[i][:4]
        self.n_dev = dev.NOD
        for i in range(self.n_dev):
            if self.get_state(i).AReset:
                self.motor_on(i)
                self.set_current_position(i, pos[i])
                #self.set_current_position(i, self.get_parameters(i).StartPos)
            

    def motor_on(self,axis):
        mode = self.get_mode(axis)
        mode.ResetD = False
        self.set_mode(axis,mode)

    def motor_off(self,axis):
        mode = self.get_mode(axis)
        mode.ResetD = True
        self.set_mode(axis,mode)
    
    def get_parameters(self,axis):
        params = USMC_Parameters()
        chk( dll.USMC_GetParameters(c_long(axis),byref(params)) )
        return params

    def set_parameters(self,axis,params):
        chk( dll.USMC_GetParameters(c_long(axis),byref(params)) )

    def get_mode(self,axis):
        mode = USMC_Mode()
        chk( dll.USMC_GetMode(c_long(axis),byref(mode)) )
        return mode

    def set_mode(self,axis,mode):
        chk( dll.USMC_SetMode(c_long(axis),byref(mode)) )

    def get_state(self,axis):
        state = USMC_State()
        chk( dll.USMC_GetState(c_long(axis),byref(state)) )
        return state

#    def get_test(self,axis):
#        state = USMC_Test()
#        chk( dll.USMC_GetState(c_long(axis),byref(state)) )
#        return state

    def get_encoder_state(self,axis):
        enc_state = USMC_EncoderState()
        chk( dll.USMC_GetEncoderState(c_long(axis), byref(enc_state)) )
        return enc_state

    def set_position(self, axis, position, speed=1000.0):
        params = USMC_StartParameters()
        chk( dll.USMC_GetStartParameters(c_long(axis), byref(params)) )
        chk( dll.USMC_Start(c_long(axis), c_long(int(position)), byref(c_float(speed)), byref(params)) )

    def get_position(self, axis):
        return self.get_state(axis).CurPos
        
    def set_current_position(self, axis, position):
        chk( dll.USMC_SetCurrentPosition(c_long(axis), c_long(position)) )
        
    def set_position_blocking(self, axis, position, speed=1000.0, timeout=60):
        pos = position/8*8
        self.set_position(axis,pos,speed)
        start_time = time.time()
        while self.get_position(axis) != pos and (time.time() - start_time ) < timeout:
            time.sleep(0.1)
            
    def shutdown(self,axis):
        #params = self.get_parameters(axis)
        #self.motor_off(axis)
        #while self.get_state(axis).Power: time.sleep(0.1)
        return self.get_position(axis)
        # params.StartPos = self.get_position(axis)
        #self.set_parameters(axis,params)
        #chk( dll.USMC_SaveParametersToFlash(c_long(axis)) ) # does not work
        
    def __del__(self):
        pos = [ self.shutdown(i) for i in range(self.n_dev) ]
        fil = open(persistent_file,'w')
        cPickle.dump(pos, fil)
        fil.close()
        chk( dll.USMC_Close() )
        
class XYPhiStage( Stage ):
    
    """x-y-phi stage based on a standa x-y-stage and a rotation stage."""
        
    def set_x(self, x, speed=600.0):
        """Set the x-position in mm."""
        pos = int(x/0.0025)*8
        self.set_position_blocking(0,pos,speed)
            
    def set_y(self, y, speed=600.0):
        """Sets the y-position in mm."""
        pos = int(y/0.0025)*8
        self.set_position_blocking(1,pos,speed)
    
    def set_phi(self, phi, speed=600.0):
        """Sets the angle phi in deg."""
        pos = int(phi/0.015)*8
        self.set_position_blocking(2,pos,speed)

    def get_x(self):
        """Get the actual x-position in mm"""
        return (self.get_position(0)/8)*0.0025
    def get_y(self):
        """Read the actual y-position in mm"""
        return (self.get_position(1)/8)*0.0025
    def get_phi(self):
        """Read the actual angle phi in deg"""
        return (self.get_position(2)/8)*0.015
       
from traits.api import HasTraits, Range, Float
from traitsui.api import View, Item, VGrid
        
class XYPhiStageTraits( XYPhiStage, HasTraits ):

    x = Float(default_value=0., mode='text', auto_set=False, enter_set=True)
    y = Float(default_value=0., mode='text', auto_set=False, enter_set=True)
    phi = Float(default_value=0., mode='text', auto_set=False, enter_set=True)

    actual_x = Float()
    actual_y = Float()
    actual_phi = Float()
    
    def __init__(self):
        XYPhiStage.__init__(self)
        HasTraits.__init__(self)
        self.x = self.actual_x = self.get_x()
        self.y = self.actual_y = self.get_y()
        self.phi = self.actual_phi = self.get_phi()
        self.on_trait_change(self.on_x_change, 'x')
        self.on_trait_change(self.on_y_change, 'y')
        self.on_trait_change(self.on_phi_change, 'phi')
    
    def on_x_change(self, new):
        self.set_x(new)
        self.actual_x = self.get_x()
    
    def on_y_change(self, new):
        self.set_y(new)
        self.actual_y = self.get_y()
    
    def on_phi_change(self, new):
        self.set_phi(new)
        self.actual_phi = self.get_phi()
    
    traits_view = View(VGrid(Item('x'),
                             Item('actual_x', style='readonly', show_label=False),
                             Item('y'),
                             Item('actual_y', style='readonly', show_label=False),
                             Item('phi'),
                             Item('actual_phi', style='readonly', show_label=False)),
                       )

if __name__ == '__main__':

    #stage = Stage()
    stage = XYPhiStageTraits()
    stage.edit_traits()
    
    
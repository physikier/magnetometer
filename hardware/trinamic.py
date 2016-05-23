"""
Provides control of trinamic BLDC motor module TMCM 1640.
"""

import numpy as np

import struct

import serial

class TMCM1640:
    
    """Provides control of trinamic BLDC motor module TMCM 1640."""

    def __init__(self, device, addr=1, mot=0):
        """
        Arguments:
            device     The COM port, such as 'COM12'. Use the TMCM-FOC program
                       to find out the COM port of the motor.
            [addr]     defaults to 1. Address of the controller.
            [mot]      defaults to 0. The motor bank.
        """
        self._connect_serial(device)
        self.addr=addr
        self.mot=mot
        
    def _connect_serial(self, device):
        self.dev = serial.Serial(device)

    def _calc_checksum(self, buf):
        return np.sum(struct.unpack('8B',buf))&0xff

    def _send_cmd(self, cmd, typ, val):
        buf=struct.pack('>4Bi',self.addr, cmd, typ, self.mot, val)
        chk = self._calc_checksum(buf)
        buf += struct.pack('B',chk)
        self.dev.write(buf)
        
    def _read_cmd(self):
        buf = self.dev.read(9)
        addr, dum1, stat, dum2, val, chk = struct.unpack('>4BiB',buf)
        chk2 = self._calc_checksum(buf[:-1])
        if chk2 != chk:
            raise RuntimeError('Wrong checksum in motor reply.')
        elif stat != 100 and stat != 101:
            raise RuntimeError('Motor replied with error "'+{1:'Wrong checksum',
                                                             2:'Invalid Command',
                                                             3:'Wrong type',
                                                             4:'Invalid value',
                                                             5:'Configuration EEPROM locked',
                                                             6:'Command not available'}[stat]+'".')
        else:
            return addr, stat, val

    def _ask(self, cmd, typ, val):
        self._send_cmd(cmd, typ, val)
        return self._read_cmd()

    def set_speed(self, rpm):
        """
        Set the motor speed.
        
        Input:
            rpm        rotations per minute. positive value rotates right,
                       negative value rotates left.
        returns:
            None
        """
        if rpm == 0:
            self._ask(3,0,0)
        elif rpm > 0:
            self._ask(1,0,int(rpm))
        else:
            self._ask(2,0,int(-rpm))

    def get_speed(self):
        """
        Returns the current motor speed.
        """
        return self._ask(6,3,0)[2]
    

if __name__ == '__main__':
    
    """
    Test code.
    """
    
    motor = TMCM1640('COM12')
    
    
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
        idn = self.__instr.ask('*IDN?')
        return idn

    
"""
This file is part of pi3diamond.

pi3diamond is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pi3diamond is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with diamond. If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2009-2011 Helmut Fedder <helmut.fedder@gmail.com>
"""

import visa
import time

class PM100D():
    """Provides control of thorlabs powermeter PM100D."""
    
    def __init__(self, visa_address='USB0::0x1313::0x8078::PM002838::INSTR'):
        self.visa_address = visa_address
        if hasattr(visa,'instrument'):
            self.instr = visa.instrument(self.visa_address)
        else:
            self.instr = visa.ResourceManager().open_resource(self.visa_address)
            
    def _write(self, string):
        try: # if the connection is already open, this will work
            self.instr.write(string)
        except: # else we attempt to open the connection and try again
            try: # silently ignore possible exceptions raised by del
                del self.instr
            except Exception:
                pass
            self.instr = visa.instrument(self.visa_address)
            self.instr.write(string)

    def _ask(self, str):
        try:
            val = self.instr.ask(str)
        except:
            self.instr = visa.instrument(self.visa_address)
            val = self.instr.ask(str)
        return val

    def getPower(self):
        return float(self._ask('read?'))

    def getMeanPower(self, t=0.5):
        val = []
        if (t<0.01): #don't stress the lazy power_meter too much...
            print "Minimum time: 5ms. Set time to 5ms."
            t=0.01

        timeout = time.time() + t
        while(timeout >time.time()):
            val.extend([float(self._ask('read?'))]) 
            time.sleep(0.01)
        try:
            return sum(val)/float(len(val))
        except ZeroDivisionError:
            print "No value aquired!"
            return None

    def disconnect(self):
        if hasattr(self,"instr"):
            self.instr.close()

    def __del__(self):
        if hasattr(self,"instr"):
            self.instr.close()


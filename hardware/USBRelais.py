import time
import operator

class USBRelais():
    """To control the Conrad '8fach Relaiskarte' (Bestnr.: 197720)
       via USB (virtual COM). Needs "pyserial" to run.
        
        Usage Examples:
        
            hmpbipolar = BipolarHMP2030(serPort)
            
            The status of the relais is changed according to self.status or self.select.
            In the list [K1,K2,K3,K4,K5,K6,K7,K8] the relais can be addressed using (1=on,select) and (0=off,not selcted). 
                    
        Optional Parameters:
        
            serPort:    Serial Port (normally COM3 -> serPort=2)"""
    
    def __init__(self, serPort=2):
        self.nBits = 8
        self.vBits = map(lambda b: 2**b, range(self.nBits))
        
        import serial
        self.port = serial.Serial(serPort-1, 19200, timeout=1, xonxoff=0, rtscts=0)
        self.status = []
        self.select = []
        self.reset()
        
        #if not self.NOP() == 1:
        #    raise ValueError("Couldn't connect to BipolarHMP2030.")
    
    #helper functions to convert bit into integer and vice versa
    def bit(self, i):
        """convert values to 0 or 1, depending on the truth value"""
        if i: return 1
        else: return 0
    
    def intConvert(self, x, n=8):
        """return a bitlist from integer x, using n bits (1 == [1,0,0,0,0,0,0,0])"""
        if not 0 <= x <= ((2**n)-1):
            raise ValueError("number to large")
        return map(lambda b: self.bit(x&b), self.vBits[:n])
    
    def bitConvert(self, l):
        """return an integer from bitlist ([1,0,0,0,0,0,0,0] == 1)"""
        if len(l) > self.nBits:
            raise ValueError("number of digits to large")
        return reduce(operator.add, map(lambda a,b: self.bit(a)*b, l, self.vBits[:len(l)]))
        
    #functions to communicate with the device
    def sendFrame(self, a, b, c):
        """The frame consists of 4byts (CMD,Address,Data,Checksum)"""
        self.port.write('%c%c%c%c' % (chr(a), chr(b), chr(c), chr(a^b^c)))
        print "request:", ":".join("{:02x}".format(ord(c)) for c in chr(a)+chr(b)+chr(c)+chr(a^b^c))
        time.sleep(0.1)
        self.port.flushOutput()

    def readFrame(self):
        """Also the answer consists of 4byts"""
        s = self.port.read(4)
        self.port.flushInput()
        print "answer:",":".join("{:02x}".format(ord(c)) for c in s)
        if not s:
            return s
        r = tuple(map(ord, s))
        if not r[0]^r[1]^r[2] == r[3]:
            raise RuntimeError('Checksum error: ' + str(r))
        if r[0] == 255:
            raise RuntimeError('Received error frame: ' + str(r))
        return r[:3]
    
    def sendCmd(self, a, b, c):
        """The device answers with an answer frame on every send
           frame containing (inverted CMD,Address,Data, new Checksum)"""
        for i in range(3): # retries
            self.sendFrame(a, b, c)
            time.sleep(0.5)
            f = self.readFrame()
            if f and f[0]==255-a and f[1]==b:
                return f
            time.sleep(i*0.1)
        raise RuntimeError('Command failed: %d-%d-%d -> %d-%d-%d' % (a, b, c, f[0], f[1], f[2]))
    
    #functions to perform commands
    def NOP(self):
        """No Operation: receives an error (CMD=255) and returns 1"""
        self.sendFrame(0, 1, 0)
        time.sleep(0.5)
        s = self.port.read(4)
        print "answer:",":".join("{:02x}".format(ord(c)) for c in s)
        self.port.flushInput()
        if not s:
            raise RuntimeError('Communication failure error: received empty string')
        r = tuple(map(ord, s))
        if not r[0]^r[1]^r[2] == r[3]:
            raise ValueError('Checksum error: ' + str(r))
        if r[0] == 255:
            return 1
        return 0
        
    def cardInit(self):
        print 'deprecated, use reset instead'
        self.reset()

    def reset(self):
        """(re)initialize card and get status"""
        f = self.sendCmd(1, 1, 0)
        return f[2] #returns version of microcontroller-software
        
    #functions to control the relais            
    def getPort(self):
        """asks for the status of each port (answer in form of [K1,K2,K3,K4,K5,K6,K7,K8])"""
        f = self.sendCmd(2, 1, 0)
        return self.intConvert(int(f[2]))
    
    def setPort(self, x):
        """set relay status from self.status (x in form of [K1,K2,K3,K4,K5,K6,K7,K8])"""
        self.status = x
        c = self.bitConvert(self.status)
        r = self.sendCmd(3, 1, c)
        
    def onSinglePort(self, x):
        """switch single relay on from self.select without changing the others (x in form of [K1,K2,K3,K4,K5,K6,K7,K8])"""
        self.select = x
        c = self.bitConvert(self.select)
        r = self.sendCmd(6, 1, c)
    
    def offSinglePort(self, x):
        """switch single relay off from self.select without changing the others (x in form of [K1,K2,K3,K4,K5,K6,K7,K8])"""
        self.select = x
        c = self.bitConvert(self.select)
        r = self.sendCmd(7, 1, c)
        
    def Toggle(self, x):
        """switch status of selected relais according to self.select (x in form of [K1,K2,K3,K4,K5,K6,K7,K8])"""
        self.select = x
        c = self.bitConvert(self.select)
        r = self.sendCmd(8, 1, c)
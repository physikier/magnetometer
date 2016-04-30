import visa
import vxi11
import time


### USB: USB0::0x1AB1::0x0E10::DP1C134500306::INSTR
### LAN: TCPIP0::129.69.46.218::INSTR
### GPIB:


class DP1116A():
  def __init__(self,device):
    if 'ASRL' in device:
      self.__connect_serial(device)
    else:
      self.__connectLAN(device)

    time.sleep(0.1)
    self.__timerList = []
    self.activeRange = self.getRange()
    #self.OutputDisable()
    #self.setOutput(0,0)

  def __connectSerial(self, device):
      import visa
      #old visa
      if hasattr(visa,"instrument"):
          instr=visa.instrument(device)
          instr.timeout=2
          instr.term_chars='\n'
      else:
          instr = visa.ResourceManager().open_resource(device)
          instr.timeout=2000
          instr.read_termination = '\n'
          instr.write_termination = '\n'          
      
      instr.chunk_size=4096      
      self.instr = instr

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
      
    


  #def __connectLAN(self,device):
  #  self.__ip = device
  #  self.__instr = visa.Instrument(self.__ip,term_chars='\n')
  
  def __connectUSB(self,device):
    self.__instr = visa.Instrument(device)
  
  def __connectGPIB(self,device):
    self.__instr = visa.Instrument(device)

  def __display(self, enable=True):
    if enable:
      self.write("DISP:CLAS ON")
    else:
      self.write("DISP:CLAS OFF")

  def __beeper(self, enable=True):
    if enable:
      self.write("SYST:BEEP ON")
    else:
      self.write("SYST:BEEP OFF")

  def __enableOCP(self, enable=True):
    if enable:
      self.write("OUTP:OCP:STAT ON")
    else:
      self.write("OUTP:OCP:STAT OFF")

  def __enableOVP(self, enable=True):
    if enable:
      self.write("OUTP:OVP:STAT ON")
    else:
      self.write("OUTP:OVP:STAT OFF")   

  def __enableOutput(self, enable=True):
    if enable:
      self.write("OUTP ON")
    else:
      self.write("OUTP OFF")      

  def __enableWaveform(self, enable=True):
    if enable:
      self.write("OUTP:WAVE ON")
    else:
      self.write("OUTP:WAVE OFF")

  def __enableTimer(self, enable=True):
    if enable:
      self.write("OUTP:TIME:STAT ON")
    else:
      self.write("OUTP:TIME:STAT OFF")

  def __enableOTP(self, enable=True):
    if enable:
      self.write("SYST:OTP ON")
    else:
      self.write("SYST:OTP OFF")

  def __enableDHCP(self,enable=True):
    if enable:
      self.write("SYST:COMM:LAN:DHCP ON")
    else:
      self.write("SYST:COMM:LAN:DHCP OFF")    

  def __enableAutoIP(self,enable=True):
    if enable:
      self.write("SYST:COMM:LAN:AUTO ON")
    else:
      self.write("SYST:COMM:LAN:AUTO OFF")    


  def __enableManualConfig(self,enable=True):
    if enable:
      self.write("SYST:COMM:LAN:MAN ON")
    else:
      self.write("SYST:COMM:LAN:MAN OFF")    


  def local(self):
    self.write("SYST:LOC")

  def remote(self):
    self.write("SYST:REM")
  
  def close(self):
    self.local()

  def ask(self,cmd):
    response = self.__instr.ask(cmd)
    time.sleep(0.5)
    return response

  def write(self,cmd):
    self.__instr.write(cmd)
    time.sleep(0.5)

  def read(self,cmd):
    response =  self.__instr.read()
    time.sleep(0.5)
    return response

  def apply(self, cmd):
    self.write("APPL "+cmd)
    time.sleep(0.5)

  def getIDN(self):
    self.IDN = self.ask("*IDN?")
    return  self.IDN

  def setOutput(self, voltage, current, ch="1"):
    if self.__checkVoltage(voltage) and self.__checkCurrent(current):
      self.apply(str(float("{0:.3f}".format(voltage)))+","+str(float("{0:.3f}".format(current))))
      self.VoltageSet = str(voltage)
      self.CurrentSet = str(current)

  def getOutput(self, ch="1"):
    response = self.ask("APPL?")
    self.VoltageSet = response.split(",")[0]
    self.CurrentSet = response.split(",")[1]

    
  def getVoltage(self,ch="1"):
    return self.ask("APPL?").split(",")[0]


  def setVoltage(self, voltage,ch="1"):
    if self.__checkVoltage(voltage):
      self.apply(str(float("{0:.3f}".format(voltage))))
      self.VoltageSet = str(voltage)


  def getCurrent(self,ch="1"):
    self.VoltageSet = self.ask("APPL?").split(",")[1]
    return self.VoltageSet

  def setCurrent(self, current,ch="1"):
    if self.__checkCurrent(current):
      self.apply(str(float("{0:.3f}".format(self.VoltageSet)))+","+str(float("{0:.3f}".format(current))))
      self.CurrentSet = str(current)

  def measureCurrent(self,ch="1"):
    self.CurrentMeasured = self.ask("MEAS:CURR?")
    return self.CurrentMeasured

  def measureVoltage(self,ch="1"):
    self.VoltageMeasured = self.ask("MEAS:VOLT?")
    return self.VoltageMeasured 

  def measurePower(self, ch="1"):
    self.PowerMeasured = self.ask("MEAS:POWE?")
    return self.PowerMeasured


  def OutputDisable(self,enable=False,ch="1"):
    self.__enableOutput(enable)
  def OutputEnable(self, enable=True,ch="1"):
    self.__enableOutput(enable)

  def disableOutput(self,enable=False,ch="1"):
    self.__enableOutput(enable)
  def enableOutput(self, enable=True,ch="1"):
    self.__enableOutput(enable)

  def setOCP(self, current,ch="1"):
    self.write("OUTP:OCP "+str(float("{0:.3f}".format(current))))

  def getOCP(self,ch="1"):
    return self.ask("OUTP:OCP?")

  def enableOCP(self, enable=True,ch="1"):
    self.__enableOCP(enable=enable)

  def disableOCP(self, disable=True,ch="1"):
    self.__enableOCP(enable=(not disable))   

  def enableOVP(self, enable=True,ch="1"):
    self.__enableOVP(enable=enable)

  def disableOVP(self, disable=True,ch="1"):
    self.__enableOVP(enable=(not disable))  

  def getOVP(self,ch="1"):
    return self.ask("OUTP:OVP?") 

  def setOVP(self,voltage,ch="1"):
    self.write("OUTP:OVP "+str(float("{0:.3f}".format(voltage))))

  def setRange(self, outputrange):
    if outputrange == "16V":
      self.write("OUTP:RANG "+outputrange)
      self.activeRange = outputrange
    elif outputrange == "32V": 
      self.write("OUTP:RANG "+outputrange)
      self.activeRange = outputrange

  def getRange(self):
    return self.ask("OUTP:RANG?")

  def reset(self):
    self.write('*RST')

  def selftest(self):
    if self.ask('*TST?') == 'Pass':
      return True
    else:
      return False

  def selftestDA(self):
    if self.ask('SYST:SELF:TEST:DA?') == 'Pass':
      return True
    else:
      return False    

  def selftestAD(self):
    if self.ask('SYST:SELF:TEST:AD?') == 'Pass':
      return True
    else:
      return False

  def selftestFPGA(self):
    if self.ask('SYST:SELF:TEST:FPGA?') == 'Pass':
      return True
    else:
      return False

  def selftestLAN(self):
    if self.ask('SYST:SELF:TEST:LAN?') == 'Pass':
      return True
    else:
      return False

  def selftestUSB(self):
    if self.ask('SYST:SELF:TEST:USB?') == 'Pass':
      return True
    else:
      return False

  def selftestFAN(self):
    if self.ask('SYST:SELF:TEST:FAN?') == 'Pass':
      return True
    else:
      return False

  def save_status(self,name,savestate="1"):
    self.write("*SAV "+savestate+","+name)

  def recall_status(self,savestate="1"):
    self.write("*RCL "+savestate)

  def enableClassicalDisplay(self,enable=True):
    self.__display(enable=enable)

  def disableClassicalDisplay(self,disable=True):
    self.__display(enable=(not disable))


  def setLanguage(self,language='EN'):
    if language == "EN" or language == "CH":
      self.write("SYST:LANG "+language)

  def enableBeeper(self,enable="True"):
    self.__beeper(enable=enable)
  def disableBeeper(self,disable="True"):
    self.__beeper(enable=(not disable))

  def setBrightness(self,level="5"):
    self.write("SYST:BRIG "+level)

  def getBrightness(self):
    return self.aks("SYST:BRIG")

  def enableWaveform(self,enable=True):
    self.__enableWaveform(enable=enable)
 
  def disableWaveform(self,disable=True):
    self.__enableWaveform(enable=(not disable))


  def saveTimer(self):
    self.write("OUTP:TIME:SAVE")

  def setTimerLoop(self,n="inf"):
    if n == "inf":
      self.write("OUTP:TIME:CIR INF")
    elif type(n) == int:
      self.write("OUTP:TIME:CIR " + str(n))

  def getTimerLoop(self):
    return self.ask("OUTP:TIME:CIR?")

  def enableTimer(self,enable=True):
    self.__enableTimer(enable=enable)
 
  def disableTimer(self,disable=True):
    self.__enableTimer(enable=(not disable))

  def sendTimerList(self):
    for i,timer  in enumerate(self.__timerList,start=0):
      if i >= 100:
        print "Max. 100 values in timerlist allowed"
        break
      self.write("OUTP:TIME "+str(i)+","+str(timer[0])+","+str(timer[1])+","+str(timer[2]))

  def createTimer(self,valuelist):
    """ List specification:
      [(volt, current, time)]
    """
    self.__timerList = []
    for i, timer in enumerate(valuelist):
      if self.__checkVoltage(timer[0]) and self.__checkCurrent(timer[1]) and timer[2] < 99999:
        self.__timerList.append(timer)

  def appendTimer(self, valuelist):
    for timer in valuelist:
      if self.__checkVoltage(timer[0]) and self.__checkCurrent(timer[1]) and timer[2] < 99999:
        self.__timerList.append(timer)

  def delTimerStep(self,id):
    self.__timerList.remove(self.__timerList[id])

  def insertTimerStep(self,id,voltage,current,time):
    if self.__checkVoltage(voltage) and self.__checkCurrent(current):
      self.__timerList.insert(id,(str(float("{0:.3f}".format(voltage))),str(float("{0:.3f}".format(current))),time))


  def __checkVoltage(self,voltage):
    if self.activeRange == "16V" and voltage > 16.8:
      print "Range error! 16V range set, not possible to set "+str(voltage)+" Volts!"
      return False
    if self.activeRange == "32V" and voltage > 33.6:
      print "Range error! 32V range set, not possible to set "+str(voltage)+" Volts!"
      return False
    return True

  def __checkCurrent(self,current):
    if self.activeRange == "16V" and current > 10.5:
      print "Range error! 16V range set, not possible to set "+str(current)+" Amps!"
      return False
    if self.activeRange == "32V" and current > 5.25:
      print "Range error! 32V range set, not possible to set "+str(current)+" Amps!"
      return False
    return True

  def startTimer(self):
    self.enableTimer()
    self.enableOutput()

  def getTimerState(self):
    return self.ask("OUTP:TIME:STAT?")    

  def getTimer(self):
    return self.ask("OUTP:TIME?")


  def enableOTP(self,enable=True):
    self.__enableOTP(enable=enable)

  def disableOTP(self,disable=True):
    self.__enableOTP(enable=(not disable))

  def setSource(self, voltage,current,ch=1):
    if self.__checkCurrent(current) and self.__checkVoltage(voltage):
      self.write("SOUR:VOLT:LEV:IMM:AMPL "+str(float("{0:.3f}".format(voltage))))
      self.write("SOUR:CURR:LEV:IMM:AMPL "+str(float("{0:.3f}".format(current))))

  def setSourceVoltage(self,voltage,ch=1):
    if self.__checkVoltage(voltage):
      self.write("SOUR:VOLT:LEV:IMM:AMPL "+str(float("{0:.3f}".format(voltage))))

  def setSourceCurrent(self,current,ch=1):
    if self.__checkCurrent(current):
      self.write("SOUR:CURR:LEV:IMM:AMPL "+str(float("{0:.3f}".format(current))))    


  def onPowerReset(mode="last"):
    if mode=="last":
      self.write("SYST:OMPO LAST")
    elif mode =="default":
      self.write("SYST:OMPO DEF")

  def getOnPowerReset(self):
    return self.ask("SYST:ONPO?")

  def enableDHCP(self,enable=True):
    self.__enableDHCP(enable)

  def disableDHCP(self,disable=True):
    self.__enableDHCP(enable=(not disable)) 

  def enableAutoIP(self, enable=True):
    self.__enableAutoIPg(enable)    

  def enableAutoIP(self, disable=True):
    self.__enableAutoIP(enable=(not disable))  

  def enableManualIPConfig(self, enable=True):
    self.__enableManualConfig(enable)

  def disableManualIPConfig(self, disable=True):
    self.__enableManualConfig(enable=(not disable))

  def setIPAdress(self, ip):
    self.write("SYST:COMM:LAN:IPAD "+ip)
  
  def getIPAdress(self):
    return self.ask("SYST:COMM:LAN:IPAD?")

  def setNetmask(self, mask):
    self.write("SYST:COMM:LAN:SMAS "+mask)

  def getNetmask(self):
    return self.ask("SYST:COMM:LAN:SMAS?")

  def setGateway(self, gateway):
    self.write("SYST:COMM:LAN:GATE "+gateway)

  def getGateway(self):
    return self.ask("SYST:COMM:LAN:GATE?")

  def setDNS(self, dns):
    self.write("SYST:COMM:LAN:DNS "+dns)

  def getDNS(self):
    return self.ask("SYST:COMM:LAN:DNS?")

  def applyLANConfig(self):
    self.write("SYST:COMM:LAN:APPL")

  def setGPIBAddress(self, gpib):
    self.write("SYST:COMM:GPIB:ADDR "+gpib)

  def getGPIBAddress(self):
    return self.ask("SYST:COMM:GPIB:ADD?")

  def storeLocal(self,slot=1,name=""):
    self.write("STOR:LOC "+str(slot)+","+name)

  def recallLocal(self, slot=1):
    self.write("RECA:LOC "+str(slot))

  def storeUSB(self,filename=""):
    self.write("STOR:EXTE "+filename)

  def recallUSB(self,filename=""):
    self.write("RECA:EXTE "+filename)


##TODO:
# min/default/max values for current etc.
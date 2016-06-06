from PyQt4 import QtCore, QtGui
import hardware.Motordriver_py3 as mo
import numpy as np
import hardware.power_meter_py3 as po
import scipy.interpolate as si
import time



class calibrationThread(QtCore.QThread):

  calibration_ready = QtCore.pyqtSignal(object)

#---------------------------
  def __init__(self, step_size, integration_time):
    QtCore.QThread.__init__(self) # this must be the first line here
    self.motor0 = mo.Motordriver("COM4")
    self.powermeter = po.PM100D('USB0::0x1313::0x8078::P0012965::INSTR')
    self.step_size = step_size
    self.integration_time = integration_time
    
    self.isFinalized = False

#--------------------------------
  def __del__(self):
    self.finalize()

#--------------------------------
  def finalize(self):
    self.isFinalized = True
    self.motor0.stopAllMovements()
    
    #print("getPosition ist", self.motor0.getPosition(motor=0), "und sein type ist",type(self.motor0.getPosition(motor=0)))
    

    self.motor0.disconnect()    
    del self.motor0

    self.powermeter.disconnect()
    del self.powermeter
    #empty_result = np.zeros((1,2,2))
    #self.calibration_ready.emit(empty_result)

#--------------------------------
  def motor0_move_in(self):

    self.motor0.moveRelative(motor=0, pos=-42)

#--------------------------------
  def calibration(self, step_size=5., integration_time=1.):
    #before measurement, make sure that motors are in starting position
    
    self.motor0.goHomeDirected(motor=0)

    self.motor0.goHomeDirected(motor=1)
    

    

    ##############     for random value generation      ###########################
    a=0
    art_measurement=[]
    art_degrees=np.arange(0,360,self.step_size)
    #art_measurement = np.arange(0,360,self.step_size)
    art_measurement = np.random.normal(size=len(art_degrees))
    art_measure_return = np.transpose(np.array([art_degrees, art_measurement]))
    
    #----------------------------------------------------------------------------------------

    ################    actual measurement     #######################################
    self.motor0_move_in()    
    start = 0
    stop = 360
    step = self.step_size
    step_new = 0.1
    position = np.arange(start, stop+step, step)
    power = []
    for deg in position:
      if not self.isFinalized:
        self.motor0.moveToAbsolutePosition(motor=1, pos=deg)
        while self.motor0.isMoving(motor=1) and not self.isFinalized:
          time.sleep(0.1)
        a = self.powermeter.getMeanPower(t=self.integration_time)
        power.append(a)
      else:
        continue
    
    if not self.isFinalized: 
      f = si.interp1d(position, power)
      xnew = np.arange(start, stop+step_new, step_new)
      ynew = f(xnew)
      # print("xnew is type ", type(xnew))
      # print("ynew is type ", type(ynew))
      int_values = np.transpose(np.array([xnew, ynew]))
      # print("int_values is type ", type(int_values))
      values = np.transpose([position, power])
      # print("the values are: " + str(values))
      # print("the int_values are: " + str(int_values))
      np.savetxt('power_calibration_interpolated_values.txt', int_values)
      np.savetxt('power_calibration.txt', values)
      # plt.plot(position, power)
      # plt.xlabel('Motordriver position in degree')
      # plt.ylabel('Power in W')
      # plt.show()
      # plt.savefig('power_calibration.png', dpi=300)
        #finally:
      
    
      self.motor0.goHomeDirected(motor=0)
      while self.motor0.isMoving(motor=0):
        time.sleep(0.1)

      self.motor0.goHomeDirected(motor=1)
      while self.motor0.isMoving(motor=1):
        time.sleep(0.1)


      print('calibration done')
      
    
    #return art_measure_return
      return int_values


#-------------------------------
  def run(self):
    result = self.calibration()
    self.calibration_ready.emit(result)
    time.sleep(1)
    self.finalize()
    time.sleep(1)
    self.exit()

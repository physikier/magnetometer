#-------------------------------------------------
#motor number in Motordriver_py3 refers to port on motor driver
#-------------------------------------------------



import sys
from PyQt4 import QtCore, QtGui, uic, Qt
import pyqtgraph as pg
import serial
import hardware.Motordriver_py3 as mo
import hardware.power_meter_py3 as po

import ControllerUtils as ControllerUtils

import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.interpolate as si
from pyqtgraph.Point import Point
from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot

from TestThread import TestThread
from calibrationThread import calibrationThread
#myTestThread = TestThread()
#myTestThread.testSignal.connect(self.mySignalHandler)
#self.threads.append(myTestThread)
#myTestThread.start()





data = np.zeros((1,2,2))

# Main QT Window Class
# The Class which conations all QT Widgets and so on
class ControllerGui(QtGui.QMainWindow):
    # controller_utils is an instance of the ControllerUtils class (Singleton)
    controller_utils = None
    # ui_utils is an instance of the UIUtils class (Singleton)
    ui_utils = None

    def __init__(self):
        super(ControllerGui, self).__init__()
        uic.loadUi("../remote_power_measurement/remote_power_measurement.ui", self)

        ControllerGui.controller_utils = ControllerUtils(self)
        ControllerGui.ui_utils = UIUtils(self)
        

        self.btn_start_calibration.clicked.connect(self.controller_utils.run_calibration)
        #self.controller_utils.run_calibration

        # settings plot1 window
        #label = pg.LabelItem(justify='right')
        #self.plot1.addItem(label)
        self.plot1.setTitle(title='Power measurement')
        self.plot1.setLabel('left', "Power in W", units='A')
        self.plot1.setLabel('bottom', "Position in degrees", units='B')
        self.plot1.setLabel('right', '')
        self.plot1.setLabel('top', '')
        self.plot1.getAxis('top').setStyle(showValues=False)
        self.plot1.getAxis('right').setStyle(showValues=False)


        self.show()
        self.btn_apply.clicked.connect(self.ui_utils.moveToPosition)

        #------------------doesn't make sense yet
        self.btn_abort.clicked.connect(self.ui_utils.abort_all)
        #----------------------------------------

        self.btn_check_current_power.clicked.connect(self.ui_utils.check_current_power)
        self.lineEdit_power.textChanged.connect(self.ui_utils.lineEdit_power_value)

        self.connect(self, Qt.SIGNAL('triggered()'), self.closeEvent)

    #def __del__(self):
    #    pass

    

    def closeEvent(self, event):
        for th in self.controller_utils.threads:
            if th.isRunning():
                th.finalize()
                th.quit()
            del th


    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
   # Function Generator Utils
class ControllerUtils(): 
    # the gui is the instance of the main Qt Window (ControllerGui class)
    gui = None
    # This is an instance of the YamlConfigHandler class

    def __init__(self, gui):
        ControllerUtils.gui = gui

        self.threads = []

    def calibration_is_ready(self, values):
        global data
        data = values
        self.gui.ui_utils.plot1()

    def run_calibration(self):
        global data
        step_size = self.gui.spinBox_step_size.value()
        integration_time = self.gui.spinBox_integration_time.value()

        calibration = calibrationThread(step_size, integration_time)
        calibration.calibration_ready.connect(self.calibration_is_ready)
        self.threads.append(calibration)
        calibration.start()

 # User Interface Utils
class UIUtils():

    gui = None
    
    def __init__(self, gui):
        UIUtils.gui = gui

    #no sense behind this function
    def mySignalHandler(self, var): 
        print(var)

    def abort_all(self):
        for th in self.gui.controller_utils.threads:
            if th.isRunning():
                th.finalize()
                th.quit()
            del th   

    def find_nearest(self, array, value):
        idx = (np.abs(array-value)).argmin()
        return array[idx]
    
    def check_current_power(self):

        integration_time = self.gui.spinBox_integration_time.value()
        powermeter = po.PM100D('USB0::0x1313::0x8078::P0012965::INSTR')
        mean_power = round(powermeter.getMeanPower(t=integration_time), 0.01)
        self.gui.lineEdit_current_power.setText(str(mean_power))
        powermeter.disconnect()

    def moveToPosition(self):
        motor1 = mo.Motordriver('COM4')
        bernd = float(self.gui.lineEdit_degree.text())
        motor1.moveToAbsolutePosition(motor=0, pos= bernd)
        while motor1.isMoving(motor=1):
                time.sleep(1)
        print("position is" , bernd)
        del motor1

    def motor0_move_in(self):
        motor0 = mo.Motordriver('COM4')
        motor0.moveToAbsolutePosition(motor=0, pos=90.0)
        while motor0.isMoving(motor=0):
                time.sleep(1)

    def motor0_move_out(self):
        motor0 = mo.Motordriver('COM4')
        motor0.moveToAbsolutePosition(motor=0, pos=0)
        while motor0.isMoving(motor=0):
                time.sleep(1)
        del motor0

    
    def lineEdit_power_value(self):
        if not self.gui.lineEdit_power.text():
            pass
        else:
            self.set_fixed_crosshair()
    def set_fixed_crosshair(self):

        global data
        degreeData = data[:,0]
        powerData = data[:,1]
        vLine2 = pg.InfiniteLine(angle=90,pen = [0,191,255], movable=False)
        hLine2 = pg.InfiniteLine(angle=0, pen = [0,191,255], movable=False)
        crosshair_label = pg.TextItem()
        self.gui.plot1.addItem(crosshair_label)
        self.gui.plot1.addItem(vLine2, ignoreBound=True)
        self.gui.plot1.addItem(hLine2, ignoreBound=True)
        
        index = self.find_degree()
        vLine2.setPos(degreeData[index])

        hLine2.setPos(powerData[index])

        crosshair_label.setText(str(hLine2.value()), color = (0,191,255))
        crosshair_label.setPos(degreeData[index], np.max(powerData))
        crosshair_label.setHtml("<span style='font-size: 10pt'>power=%0.3f" % (hLine2.value()))

        #print(hLine2.value())
        self.gui.lineEdit_power.textChanged.connect(lambda: self.gui.plot1.removeItem(vLine2))
        self.gui.lineEdit_power.textChanged.connect(lambda: self.gui.plot1.removeItem(hLine2))
        self.gui.lineEdit_power.textChanged.connect(lambda: self.gui.plot1.removeItem(crosshair_label))


    def find_degree(self):
        #vLine2 = pg.InfiniteLine(angle=90,pen = [0,0,255], movable=False)
        global data
        degreeData = data[:,0]
        powerData = data[:,1]
        index_calc1 = np.where(powerData == self.find_nearest(powerData, float(self.gui.lineEdit_power.text())))
        index_calc2 = np.concatenate(index_calc1).tolist()
        index = index_calc2[0] 
        corresponding_degree = data[:,0][index]  
        #print("wanted value of", self.gui.lineEdit_power.text(), "was rounded to ", data[:,1][index]  ,"which has the index" , index)
        #print("the corresponding degree is", corresponding_degree)
        self.gui.lineEdit_degree.setText(str(corresponding_degree))
        return index
        
        
        
                

########################################################
    def setCrosshair(self, index): #for some reason doesn't work, but also doesn't cause problems
        global data
        degreeData = data[:,0]
        powerData = data[:,1]
        vLine = pg.InfiniteLine(angle=90, movable=False)
        hLine = pg.InfiniteLine(angle=0, movable=False)
        
        vLine.setPos(degreeData[index])
        hLine.setPos(powerData[index])
        hLine.setLabel("jo")
#########################################################
    #Plot Window
    def plot1(self):
        self.gui.plot1.clear()
        global data
        step_size = self.gui.spinBox_step_size.value()
        integration_time = self.gui.spinBox_integration_time.value()
        label = pg.TextItem()
        #label.anchor(itemPos=(1,0), parentPos=(1,0), offset=(-10,10))
        #l = pg.LegendItem((100,60), (60,10))  # args are (size, position)
        #l.setParentItem(self.gui.plot1.graphicsItem())
        
        self.gui.plot1.plot(data[:,0], data[:,1], pen=(255,0,0))
         #cross hair
        vLine = pg.InfiniteLine(angle=90, movable=False)
        hLine = pg.InfiniteLine(angle=0, movable=False)
        # self.gui.plot1.setLabel('right', '')
        # self.gui.plot1.setLabel('top', '')
        # self.gui.plot1.getAxis('top').setStyle(showValues=False)
        # self.gui.plot1.getAxis('right').setStyle(showValues=False)
        self.gui.plot1.addItem(vLine, ignoreBounds=True)
        self.gui.plot1.addItem(hLine, ignoreBounds=True)
        vb = self.gui.plot1.plotItem.vb

        #print('data to plot: ', data)
        #print(data1)
        #art_degrees = np.arange(0,360,step_size)

        def mouseMoved(evt):
            global data
            degreeData = data[:,0]
            powerData = data[:,1] 
            dataLength = len(degreeData)

            pos = evt[0] ## using signal proxy turns original arguments into a tuple
            if self.gui.plot1.sceneBoundingRect().contains(pos):
                mousePoint = vb.mapSceneToView(pos)
                index_calc1 = np.where(degreeData == self.find_nearest(degreeData, mousePoint.x()))
                index_calc2 = np.concatenate(index_calc1).tolist()
                index = index_calc2[0]
                if index >= 0 and index <= dataLength:
                    #label.setHtml("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (mousePoint.x(), data1[index]))
                    self.gui.plot1.setLabel('top', "<span style='font-size: 10pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (degreeData[index], powerData[index]))
                    #pg.GraphicsScene.mouseEvents.mouseClickEvent.double()
                    #self.gui.plot1.addItem(textItem)
                vLine.setPos(mousePoint.x())
                hLine.setPos(powerData[index])


        #self.ui_utils.mouseMoved()
        self.proxy = pg.SignalProxy(self.gui.plot1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
        #p1.scene().sigMouseMoved.connect(mouseMoved)

    #def mouseMoved(self, evt, data1):
        
       # pos = evt[0] ## using signal proxy turns original arguments into a tuple
       # if self.gui.plot1.sceneBoundingRect().contains(pos):
       #     mousePoint = vb.mapSceneToView(pos)
       #     index = int(mousePoint.x())
       #     if index > 0 and index < len(data1):
       #         label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (mousePoint.x(), data[index]))
       #     vLine.setPos(mousePoint.x())
       #     hLine.setPos(mousePoint.y())
        


def main():
    app = QtGui.QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon("icon1.png"));
    window = ControllerGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

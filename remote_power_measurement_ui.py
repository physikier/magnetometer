import sys
from PyQt4 import QtCore, QtGui, uic
import pyqtgraph as pg
import serial
import hardware.Motordriver_py3 as mo
import hardware.power_meter_py3 as po
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.interpolate as si
from pyqtgraph.Point import Point
from pyqtgraph.Qt import QtGui, QtCore




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

   
   # Function Generator Utils
class ControllerUtils():

    # the gui is the instance of the main Qt Window (ControllerGui class)
    gui = None
    # This is an instance of the YamlConfigHandler class

    def __init__(self, gui):
        ControllerUtils.gui = gui

    def run_calibration(self):
        step_size = self.gui.spinBox_step_size.value()
        integration_time = self.gui.spinBox_integration_time.value()
        
        data = self.gui.ui_utils.calibration(step_size, integration_time)
        self.gui.ui_utils.plot1(data)
        #x='calibration done'
        #print(x)
    def andreas(self):
        print("great")
 # User Interface Utils
class UIUtils():

    gui = None

    def __init__(self, gui):
        UIUtils.gui = gui


    def calibration(self, step_size=5., integration_time=1.):

        motor1 = mo.Motordriver('COM4')
        powermeter = po.PM100D('USB0::0x1313::0x8078::P0012965::INSTR')
        
        #####  for artificial value generation   ######
        a=0
        art_measurement=[]
        art_degrees=np.arange(0,360,step_size)
        #print(len(art_degrees), type(art_degrees))
        art_measurement = np.random.normal(size=len(art_degrees))
        index = art_measurement.np.where(float(self.gui.lineEdit_power.text()))
        print(float(self.gui.lineEdit_power.text()))
        #print(index)
        #searched_deg = art_degrees[index]
        # while a<360/step_size:
        #     art_measurement.append(np.random.uniform(0.,20.))
        #     a = a+1
        art_measure_return = np.transpose(np.array([art_degrees, art_measurement]))
        return art_measure_return
        ################################################


        #try:  
        #    start = 0
        #    stop = 360
        #    step = step_size
        #    step_new = 0.1
        #    motor1.moveToAbsolutePosition(motor=1, pos=0)
        #    while motor1.isMoving(motor=1):
        #        time.sleep(1)
        #    position = np.arange(start, stop+step, step)
        #    power = []
        #    for deg in position:
        #        motor1.moveToAbsolutePosition(motor=1, pos=deg)
        #        while motor1.isMoving(motor=1):
        #            time.sleep(1)
        #        a = powermeter.getMeanPower(t=integration_time)
        #        power.append(a)
        #    print("power is type " + str(type(power)))
        #    f = si.interp1d(position, power)
        #    xnew = np.arange(start, stop+step_new, step_new)
        #    ynew = f(xnew)
        #    print("xnew is type ", type(xnew))
        #    print("ynew is type ", type(ynew))
        #    int_values = np.transpose(np.array([xnew, ynew]))
        #    print("int_values is type ", type(int_values))
        #    values = np.transpose([position, power])
        #    print("the values are: " + str(values))
        #    print("the int_values are: " + str(int_values))
        #    np.savetxt('power_calibration_interpolated_values.txt', int_values)
        #    np.savetxt('power_calibration.txt', values)
        #    plt.plot(position, power)
        #    plt.xlabel('Motordriver position in degree')
        #    plt.ylabel('Power in W')
        #    plt.show()
        #    plt.savefig('power_calibration.png', dpi=300)

            

        #finally:
        #    motor1.goHome()
        #    del motor1
        #    powermeter.disconnect()
        #    print('calibration done')
#
        #return int_values

    #Plot Window
    def plot1(self, data):
        
        step_size = self.gui.spinBox_step_size.value()
        integration_time = self.gui.spinBox_integration_time.value()
        data =  self.gui.ui_utils.calibration(step_size, integration_time)
            #print(data[:,i])
        label = pg.TextItem()
        #label.anchor(itemPos=(1,0), parentPos=(1,0), offset=(-10,10))
        #l = pg.LegendItem((100,60), (60,10))  # args are (size, position)
        #l.setParentItem(self.gui.plot1.graphicsItem())
        
        #label.setPos()
        #label.setHtml()
        #label = pg.LabelItem(justify='right')##for plotitem
        #self.gui.plot1.addItem(label)
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

        print('data to plot: ', data)
        data1 = [row[1] for row in data]
        print(data1)
        art_degrees = np.arange(0,360,step_size)

        def mouseMoved(evt):
            pos = evt[0] ## using signal proxy turns original arguments into a tuple
            if self.gui.plot1.sceneBoundingRect().contains(pos):
                mousePoint = vb.mapSceneToView(pos)
                index = int(round(mousePoint.x()/step_size, 0))
                if index >= 0 and index < 360:
                    #label.setHtml("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (mousePoint.x(), data1[index]))
                    self.gui.plot1.setLabel('top', "<span style='font-size: 10pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>" % (art_degrees[index], data1[index]))
                    #pg.GraphicsScene.mouseEvents.mouseClickEvent.double()
                    #self.gui.plot1.addItem(textItem)
                vLine.setPos(mousePoint.x())
                hLine.setPos(mousePoint.y())

        




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

import sys
import numpy
import yaml_writer as yw
from PyQt4 import QtCore, QtGui, uic

# Main QT Window Class
# The Class which conations all QT Widgets and so on
class ControllerGui(QtGui.QMainWindow):
    # controller_utils is an instance of the ControllerUtils class (Singleton)
    controller_utils = None
    # ui_utils is an instance of the UIUtils class (Singleton)
    ui_utils = None

    def __init__(self):
        super(ControllerGui, self).__init__()
        uic.loadUi("./hanle_measurement_worker/hanle_measurement_worker.ui", self)
        
        ControllerGui.controller_utils = ControllerUtils(self)
        ControllerGui.ui_utils = UIUtils(self)

        self.checkBox_B0.stateChanged.connect(self.controller_utils.apply_B0_stat)
        self.checkBox_B1.stateChanged.connect(self.controller_utils.apply_B1_stat)

        self.comboBox_method_B0.currentIndexChanged.connect(self.controller_utils.apply_method_B0)
        self.comboBox_method_B1.currentIndexChanged.connect(self.controller_utils.apply_method_B1)

        self.spinBox_freq_start_B0.valueChanged.connect(self.controller_utils.apply_freq_start_B0)
        self.spinBox_freq_start_B1.valueChanged.connect(self.controller_utils.apply_freq_start_B1)
        self.spinBox_freq_stop_B0.valueChanged.connect(self.controller_utils.apply_freq_stop_B0)
        self.spinBox_freq_stop_B1.valueChanged.connect(self.controller_utils.apply_freq_stop_B1)
        self.spinBox_freq_step_B0.valueChanged.connect(self.controller_utils.apply_freq_step_B0)
        self.spinBox_freq_step_B1.valueChanged.connect(self.controller_utils.apply_freq_step_B1)


        self.spinBox_ampl_start_B0.valueChanged.connect(self.controller_utils.apply_ampl_start_B0)
        self.spinBox_ampl_start_B1.valueChanged.connect(self.controller_utils.apply_ampl_start_B1)
        self.spinBox_ampl_stop_B0.valueChanged.connect(self.controller_utils.apply_ampl_stop_B0)
        self.spinBox_ampl_stop_B1.valueChanged.connect(self.controller_utils.apply_ampl_stop_B1)
        self.spinBox_ampl_step_B0.valueChanged.connect(self.controller_utils.apply_ampl_step_B0)
        self.spinBox_ampl_step_B1.valueChanged.connect(self.controller_utils.apply_ampl_step_B1)


        self.spinBox_off_start_B0.valueChanged.connect(self.controller_utils.apply_off_start_B0)
        self.spinBox_off_start_B1.valueChanged.connect(self.controller_utils.apply_off_start_B1)       
        self.spinBox_off_stop_B0.valueChanged.connect(self.controller_utils.apply_off_stop_B0)
        self.spinBox_off_stop_B1.valueChanged.connect(self.controller_utils.apply_off_stop_B1)
        self.spinBox_off_step_B0.valueChanged.connect(self.controller_utils.apply_off_step_B0)
        self.spinBox_off_step_B1.valueChanged.connect(self.controller_utils.apply_off_step_B1)


        self.spinBox_measure_no.valueChanged.connect(self.controller_utils.apply_meas_no)
        self.spinBox_cell_id.valueChanged.connect(self.controller_utils.apply_cell_id)
        self.spinBox_temp.valueChanged.connect(self.controller_utils.apply_temp)
        self.spinBox_lpower.valueChanged.connect(self.controller_utils.apply_lpower)
        self.spinBox_diode_gain.valueChanged.connect(self.controller_utils.apply_diode_gain)
        self.spinBox_samples.valueChanged.connect(self.controller_utils.apply_samples)
        self.spinBox_downsampling.valueChanged.connect(self.controller_utils.apply_downsampling)
        self.spinBox_mtime.valueChanged.connect(self.controller_utils.apply_measure_time)

        
        self.show()

# Function Generator Utils
class ControllerUtils():
    # the gui is the instance of the main Qt Window (ControllerGui class)
    gui = None

    def __init__(self, gui):
        ControllerUtils.gui = gui

    def apply_B0_stat(self):
        value_stat = self.gui.checkBox_B0.checkState()
        if value_stat == 2:
            yw.yaml_writer_hanle(active_B0='true')
            print('[SET] B0 active: true')
        else:
            yw.yaml_writer_hanle(active_B0='false')
            print('[SET] B0 active: false')

    def apply_B1_stat(self):
        value_stat = self.gui.checkBox_B1.checkState()
        if value_stat == 2:
            yw.yaml_writer_hanle(active_B1='true')
            print('[SET] B1 active: true')
        else:
            yw.yaml_writer_hanle(active_B1='false')
            print('[SET] B1 active: false')

    def apply_freq_start_B0(self):
        value_freq_start = self.gui.spinBox_freq_start_B0.value()
        yw.yaml_writer_hanle(freq_start_B0=value_freq_start)
        print('[SET] B0 freqency start value: ' + str(value_freq_start))

    def apply_freq_start_B1(self):
        value_freq_start = self.gui.spinBox_freq_start_B1.value()
        yw.yaml_writer_hanle(freq_start_B1=value_freq_start)
        print('[SET] B1 freqency start value: ' + str(value_freq_start))

    def apply_freq_stop_B0(self):
        value_freq_stop = self.gui.spinBox_freq_stop_B0.value()
        yw.yaml_writer_hanle(freq_stop_B0=value_freq_stop)
        print('[SET] B0 freqency stop value: ' + str(value_freq_stop))

    def apply_freq_stop_B1(self):
        value_freq_stop = self.gui.spinBox_freq_stop_B1.value()
        yw.yaml_writer_hanle(freq_stop_B1=value_freq_stop)
        print('[SET] B1 freqency stop value: ' + str(value_freq_stop))

    def apply_freq_step_B0(self):
        value_freq_step = self.gui.spinBox_freq_step_B0.value()
        yw.yaml_writer_hanle(freq_step_B0=value_freq_step)
        print('[SET] B0 freqency step size: ' + str(value_freq_step))

    def apply_freq_step_B1(self):
        value_freq_step = self.gui.spinBox_freq_step_B1.value()
        yw.yaml_writer_hanle(freq_step_B1=value_freq_step)
        print('[SET] B1 freqency step size: ' + str(value_freq_step))

    def apply_ampl_start_B0(self):
        value_ampl_start = self.gui.spinBox_ampl_start_B0.value()
        yw.yaml_writer_hanle(ampl_start_B0=value_ampl_start)
        print('[SET] B0 amplitude start value: ' + str(value_ampl_start))

    def apply_ampl_start_B1(self):
        value_ampl_start = self.gui.spinBox_ampl_start_B1.value()
        yw.yaml_writer_hanle(ampl_start_B1=value_ampl_start)
        print('[SET] B1 amplitude start value: ' + str(value_ampl_start))

    def apply_ampl_stop_B0(self):
        value_ampl_stop = self.gui.spinBox_ampl_stop_B0.value()
        yw.yaml_writer_hanle(ampl_stop_B0=value_ampl_stop)
        print('[SET] B0 amplitude stop value: ' + str(value_ampl_stop))

    def apply_ampl_stop_B1(self):
        value_ampl_stop = self.gui.spinBox_ampl_stop_B1.value()
        yw.yaml_writer_hanle(ampl_stop_B1=value_ampl_stop)
        print('[SET] B1 amplitude stop value: ' + str(value_ampl_stop))

    def apply_ampl_step_B0(self):
        value_ampl_step = self.gui.spinBox_ampl_step_B0.value()
        yw.yaml_writer_hanle(ampl_step_B0=value_ampl_step)
        print('[SET] B0 amplitude step value: ' + str(value_ampl_step))

    def apply_ampl_step_B1(self):
        value_ampl_step = self.gui.spinBox_ampl_step_B1.value()
        yw.yaml_writer_hanle(ampl_step_B1=value_ampl_step)
        print('[SET] B1 amplitude step value: ' + str(value_ampl_step))

    def apply_off_start_B0(self):
        value_off_start = self.gui.spinBox_off_start_B0.value()
        yw.yaml_writer_hanle(off_start_B0=value_off_start)
        print('[SET] B0 offset start value: ' + str(value_off_start))

    def apply_off_start_B1(self):
        value_off_start = self.gui.spinBox_off_start_B1.value()
        yw.yaml_writer_hanle(off_start_B1=value_off_start)
        print('[SET] B1 offset start value: ' + str(value_off_start))

    def apply_off_stop_B0(self):
        value_off_stop = self.gui.spinBox_off_stop_B0.value()
        yw.yaml_writer_hanle(off_stop_B0=value_off_stop)
        print('[SET] B0 offset stop value: ' + str(value_off_stop))

    def apply_off_stop_B1(self):
        value_off_stop = self.gui.spinBox_off_stop_B1.value()
        yw.yaml_writer_hanle(off_stop_B1=value_off_stop)
        print('[SET] B1 offset stop value: ' + str(value_off_stop))

    def apply_off_step_B0(self):
        value_off_step = self.gui.spinBox_off_step_B0.value()
        yw.yaml_writer_hanle(off_step_B0=value_off_step)
        print('[SET] B0 offset step value: ' + str(value_off_step))

    def apply_off_step_B1(self):
        value_off_step = self.gui.spinBox_off_step_B1.value()
        yw.yaml_writer_hanle(off_step_B1=value_off_step)
        print('[SET] B1 offset step value: ' + str(value_off_step))

    def apply_meas_no(self):
        meas_no = self.gui.spinBox_measure_no.value()
        yw.yaml_writer_hanle(measurement=meas_no)
        print('[SET] measurement number: ' + str(meas_no))

    def apply_cell_id(self):
        cell_id = self.gui.spinBox_cell_id.value()
        yw.yaml_writer_hanle(cell=cell_id)
        print('[SET] cell\'s id: ' + str(cell_id))

    def apply_temp(self):
        temp = self.gui.spinBox_temp.value()
        yw.yaml_writer_hanle(temp=temp)
        print('[SET] temperature [°C] : ' + str(temp))

    def apply_lpower(self):
        power = self.gui.spinBox_lpower.value()
        yw.yaml_writer_hanle(power=power)
        print('[SET] laser power [uW] : ' + str(power))

    def apply_diode_gain(self):
        gain = self.gui.spinBox_diode_gain.value()
        yw.yaml_writer_hanle(diode_gain=gain)
        print('[SET] photo diode gain: ' + str(gain))

    def apply_samples(self):
        samples = self.gui.spinBox_samples.value()
        yw.yaml_writer_hanle(samples=samples)
        print('[SET] sample rate: ' + str(samples))

    def apply_downsampling(self):
        downsamples = self.gui.spinBox_downsampling.value()
        yw.yaml_writer_hanle(downsampling=downsamples)
        print('[SET] downsampling factor: ' + str(downsamples))

    def apply_measure_time(self):
        mtime = self.gui.spinBox_mtime.value()
        yw.yaml_writer_hanle(meas_time=mtime)
        print('[SET] measurement time [s]: ' + str(mtime))

    def apply_method_B0(self):
        method = self.gui.comboBox_method_B0.currentText()
        yw.yaml_writer_hanle(method_B0=method)
        print('[SET] B0 measuring method: ' + method)

    def apply_method_B1(self):
        method = self.gui.comboBox_method_B1.currentText()
        yw.yaml_writer_hanle(method_B1=method)
        print('[SET] B1 measuring method: ' + method)
        if method == 'const':
            self.gui.spinBox_freq_stop_B1.setEnabled(False)
            self.gui.spinBox_freq_step_B1.setEnabled(False)
            self.gui.spinBox_ampl_stop_B1.setEnabled(False)
            self.gui.spinBox_ampl_step_B1.setEnabled(False)
            self.gui.spinBox_off_stop_B1.setEnabled(False)
            self.gui.spinBox_off_step_B1.setEnabled(False)




# User Interface Utils
class UIUtils():
    gui = None

    def __init__(self, gui):
        UIUtils.gui = gui

def main():
    app = QtGui.QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon("icon1.png"));
    window = ControllerGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
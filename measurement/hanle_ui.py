import sys
import numpy
from threading import Thread
import yaml_writer as yw
import auto_measurement_worker as amw

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

        self.ui_utils.disable_widgets(key='B0')
        self.ui_utils.disable_widgets(key='B1')
        self.ui_utils.disable_widgets_init()
        self.controller_utils.get_cell_id_measurement_no()


        self.plotWidget_plot1.setTitle(title='data')
        self.plotWidget_plot1.setLabel('left', "Y Axis", units='A')
        self.plotWidget_plot1.setLabel('bottom', "time", units='seconds')
        self.plotWidget_plot1.setLabel('right', '')
        self.plotWidget_plot1.setLabel('top', '')
        self.plotWidget_plot1.getAxis('top').setStyle(showValues=False)
        self.plotWidget_plot1.getAxis('right').setStyle(showValues=False)

        self.checkBox_B0.stateChanged.connect(lambda: self.ui_utils.edit_stack(key='B0'))
        self.spinBox_stack_B0.valueChanged.connect(lambda: self.ui_utils.edit_stack_pos(key1='B0', key2='B1'))
        self.checkBox_B1.stateChanged.connect(lambda: self.ui_utils.edit_stack(key='B1'))
        self.spinBox_stack_B1.valueChanged.connect(lambda: self.ui_utils.edit_stack_pos(key1='B1', key2='B0'))

        self.comboBox_device_B0.currentIndexChanged.connect(lambda: self.ui_utils.synchronize_devices(key1='B0', key2='B1'))
        self.comboBox_device_B1.currentIndexChanged.connect(lambda: self.ui_utils.synchronize_devices(key1='B1', key2='B0'))
        self.comboBox_method_B0.currentIndexChanged.connect(lambda: self.ui_utils.disable_widgets(key='B0'))
        self.comboBox_method_B1.currentIndexChanged.connect(lambda: self.ui_utils.disable_widgets(key='B1'))
        self.comboBox_method_B1.currentIndexChanged.connect(lambda: self.ui_utils.edit_stack(key='B1'))

        # self.spinBox_freq_start_B0.valueChanged.connect(self.controller_utils.apply_freq_start_B0)
        # self.spinBox_freq_start_B1.valueChanged.connect(self.controller_utils.apply_freq_start_B1)
        # self.spinBox_freq_stop_B0.valueChanged.connect(self.controller_utils.apply_freq_stop_B0)
        # self.spinBox_freq_stop_B1.valueChanged.connect(self.controller_utils.apply_freq_stop_B1)
        # self.spinBox_freq_step_B0.valueChanged.connect(self.controller_utils.apply_freq_step_B0)
        # self.spinBox_freq_step_B1.valueChanged.connect(self.controller_utils.apply_freq_step_B1)

        # self.spinBox_ampl_start_B0.valueChanged.connect(self.controller_utils.apply_ampl_start_B0)
        # self.spinBox_ampl_start_B1.valueChanged.connect(self.controller_utils.apply_ampl_start_B1)
        # self.spinBox_ampl_stop_B0.valueChanged.connect(self.controller_utils.apply_ampl_stop_B0)
        # self.spinBox_ampl_stop_B1.valueChanged.connect(self.controller_utils.apply_ampl_stop_B1)
        # self.spinBox_ampl_step_B0.valueChanged.connect(self.controller_utils.apply_ampl_step_B0)
        # self.spinBox_ampl_step_B1.valueChanged.connect(self.controller_utils.apply_ampl_step_B1)

        # self.spinBox_off_start_B0.valueChanged.connect(self.controller_utils.apply_off_start_B0)
        # self.spinBox_off_start_B1.valueChanged.connect(self.controller_utils.apply_off_start_B1)       
        # self.spinBox_off_stop_B0.valueChanged.connect(self.controller_utils.apply_off_stop_B0)
        # self.spinBox_off_stop_B1.valueChanged.connect(self.controller_utils.apply_off_stop_B1)
        # self.spinBox_off_step_B0.valueChanged.connect(self.controller_utils.apply_off_step_B0)
        # self.spinBox_off_step_B1.valueChanged.connect(self.controller_utils.apply_off_step_B1)

        # self.spinBox_measure_no.valueChanged.connect(self.controller_utils.apply_meas_no)
        # self.spinBox_cell_id.valueChanged.connect(self.controller_utils.apply_cell_id)
        # self.spinBox_temp.valueChanged.connect(self.controller_utils.apply_temp)
        # self.spinBox_lpower.valueChanged.connect(self.controller_utils.apply_lpower)
        # self.spinBox_diode_gain.valueChanged.connect(self.controller_utils.apply_diode_gain)
        # self.spinBox_samples.valueChanged.connect(self.controller_utils.apply_samples)
        # self.spinBox_downsampling.valueChanged.connect(self.controller_utils.apply_downsampling)
        # self.spinBox_mtime.valueChanged.connect(self.controller_utils.apply_measure_time)

        self.btn_load_config.clicked.connect(self.controller_utils.load_yaml_config)
        self.btn_start_measurement.clicked.connect(self.controller_utils.run_measurement)

        self.show()


# Function Generator Utils
class ControllerUtils():

    # the gui is the instance of the main Qt Window (ControllerGui class)
    gui = None
    # This is an instance of the YamlConfigHandler class
    yaml_config_handler = None
    auto_measurement_worker = None

    def __init__(self, gui):
        ControllerUtils.gui = gui
        #self.apply_meas_no()

    def load_yaml_config(self):
        self.apply_meas_no()
        self.apply_B0_stat()
        self.apply_B0_device()
        self.apply_B1_device()
        self.apply_B1_stat()
        self.apply_freq_start_B0()
        self.apply_freq_start_B1()
        self.apply_freq_stop_B0()
        self.apply_freq_stop_B1()
        self.apply_freq_step_B0()
        self.apply_freq_step_B1()
        self.apply_ampl_start_B0()
        self.apply_ampl_start_B1()
        self.apply_ampl_stop_B0()
        self.apply_ampl_stop_B1()
        self.apply_ampl_step_B0()
        self.apply_ampl_step_B1()
        self.apply_off_start_B0()
        self.apply_off_start_B1()
        self.apply_off_stop_B0()
        self.apply_off_stop_B1()
        self.apply_off_step_B0()
        self.apply_off_step_B1()
        
        self.apply_cell_id()
        self.apply_temp()
        self.apply_lpower()
        self.apply_diode_gain()
        self.apply_samples()
        self.apply_downsampling()
        self.apply_measure_time()
        self.apply_method_B0()
        self.apply_method_B1()
        self.apply_stack()

        self.gui.textBrowser_load_config.append('config-' + str(self.gui.spinBox_measure_no.value()) + '.yaml loaded...')

    def run_measurement(self):
        try:
            self.auto_measurement_worker = amw.MagnetometerWorker()
            data, downsampled_data = self.auto_measurement_worker.run_measurement()
            # plot measured data
            self.plot_data(data=data, samples=self.gui.spinBox_samples.value(), downsampling=self.gui.spinBox_downsampling.value(), measure_time=self.gui.spinBox_mtime.value())
            # delete config files from temporary config folder
            self.yaml_config_handler.delete_config_files()
        except IOError:
            print('some shit happend with the hardware interfaces')
        except IndexError:
            print('some shit with data reading happend, so data array has wrong dimensions')
        finally:
            
            # delete config files from temporary config folder
            self.yaml_config_handler.delete_config_files()

    def plot_data(self, data, samples, downsampling, measure_time):
        from random import randint
        y = data
        x = numpy.arange(0, measure_time, (1/samples)*downsampling)
        for i in range(y.shape[1]):
            #c=numpy.max(y[:,i])-numpy.min(y[:,i])
            d=numpy.mean(y[:,i])
            off = i*d/50
            #line color RGB
            R = randint(0,255)
            G = randint(0,255)
            B = randint(0,255)

            self.gui.plotWidget_plot1.plot(x,y[:,i]+off, pen=[R,G,B])

    def apply_B0_stat(self):
        value_stat = self.gui.checkBox_B0.checkState()
        if value_stat == 2:
            self.yaml_config_handler.write_hanle_config(active_B0=True)
            print('[SET] B0 active: true')
        else:
            self.yaml_config_handler.write_hanle_config(active_B0=False)
            print('[SET] B0 active: false')

    def apply_B1_stat(self):
        value_stat = self.gui.checkBox_B1.checkState()
        if value_stat == 2:
            self.yaml_config_handler.write_hanle_config(active_B1=True)
            print('[SET] B1 active: true')
        else:
            self.yaml_config_handler.write_hanle_config(active_B1=False)
            print('[SET] B1 active: false')

    def apply_B0_device(self):
        device = self.gui.comboBox_device_B0.currentText()
        self.yaml_config_handler.write_hanle_config(device_B0=device)
        print('[SET] B0 device: ' + device)

    def apply_B1_device(self):
        device = self.gui.comboBox_device_B1.currentText()
        self.yaml_config_handler.write_hanle_config(device_B1=device)
        print('[SET] B1 device: ' + device)

    def apply_freq_start_B0(self):
        value_freq_start = self.gui.spinBox_freq_start_B0.value()
        self.yaml_config_handler.write_hanle_config(freq_start_B0=value_freq_start)
        print('[SET] B0 freqency start value: ' + str(value_freq_start))

    def apply_freq_start_B1(self):
        value_freq_start = self.gui.spinBox_freq_start_B1.value()
        self.yaml_config_handler.write_hanle_config(freq_start_B1=value_freq_start)
        print('[SET] B1 freqency start value: ' + str(value_freq_start))

    def apply_freq_stop_B0(self):
        value_freq_stop = self.gui.spinBox_freq_stop_B0.value()
        self.yaml_config_handler.write_hanle_config(freq_stop_B0=value_freq_stop)
        print('[SET] B0 freqency stop value: ' + str(value_freq_stop))

    def apply_freq_stop_B1(self):
        value_freq_stop = self.gui.spinBox_freq_stop_B1.value()
        self.yaml_config_handler.write_hanle_config(freq_stop_B1=value_freq_stop)
        print('[SET] B1 freqency stop value: ' + str(value_freq_stop))

    def apply_freq_step_B0(self):
        value_freq_step = self.gui.spinBox_freq_step_B0.value()
        self.yaml_config_handler.write_hanle_config(freq_step_B0=value_freq_step)
        print('[SET] B0 freqency step size: ' + str(value_freq_step))

    def apply_freq_step_B1(self):
        value_freq_step = self.gui.spinBox_freq_step_B1.value()
        self.yaml_config_handler.write_hanle_config(freq_step_B1=value_freq_step)
        print('[SET] B1 freqency step size: ' + str(value_freq_step))

    def apply_ampl_start_B0(self):
        value_ampl_start = self.gui.spinBox_ampl_start_B0.value()
        self.yaml_config_handler.write_hanle_config(ampl_start_B0=value_ampl_start)
        print('[SET] B0 amplitude start value: ' + str(value_ampl_start))

    def apply_ampl_start_B1(self):
        value_ampl_start = self.gui.spinBox_ampl_start_B1.value()
        self.yaml_config_handler.write_hanle_config(ampl_start_B1=value_ampl_start)
        print('[SET] B1 amplitude start value: ' + str(value_ampl_start))

    def apply_ampl_stop_B0(self):
        value_ampl_stop = self.gui.spinBox_ampl_stop_B0.value()
        self.yaml_config_handler.write_hanle_config(ampl_stop_B0=value_ampl_stop)
        print('[SET] B0 amplitude stop value: ' + str(value_ampl_stop))

    def apply_ampl_stop_B1(self):
        value_ampl_stop = self.gui.spinBox_ampl_stop_B1.value()
        self.yaml_config_handler.write_hanle_config(ampl_stop_B1=value_ampl_stop)
        print('[SET] B1 amplitude stop value: ' + str(value_ampl_stop))

    def apply_ampl_step_B0(self):
        value_ampl_step = self.gui.spinBox_ampl_step_B0.value()
        self.yaml_config_handler.write_hanle_config(ampl_step_B0=value_ampl_step)
        print('[SET] B0 amplitude step value: ' + str(value_ampl_step))

    def apply_ampl_step_B1(self):
        value_ampl_step = self.gui.spinBox_ampl_step_B1.value()
        self.yaml_config_handler.write_hanle_config(ampl_step_B1=value_ampl_step)
        print('[SET] B1 amplitude step value: ' + str(value_ampl_step))

    def apply_off_start_B0(self):
        value_off_start = self.gui.spinBox_off_start_B0.value()
        self.yaml_config_handler.write_hanle_config(off_start_B0=value_off_start)
        print('[SET] B0 offset start value: ' + str(value_off_start))

    def apply_off_start_B1(self):
        value_off_start = self.gui.spinBox_off_start_B1.value()
        self.yaml_config_handler.write_hanle_config(off_start_B1=value_off_start)
        print('[SET] B1 offset start value: ' + str(value_off_start))

    def apply_off_stop_B0(self):
        value_off_stop = self.gui.spinBox_off_stop_B0.value()
        self.yaml_config_handler.write_hanle_config(off_stop_B0=value_off_stop)
        print('[SET] B0 offset stop value: ' + str(value_off_stop))

    def apply_off_stop_B1(self):
        value_off_stop = self.gui.spinBox_off_stop_B1.value()
        self.yaml_config_handler.write_hanle_config(off_stop_B1=value_off_stop)
        print('[SET] B1 offset stop value: ' + str(value_off_stop))

    def apply_off_step_B0(self):
        value_off_step = self.gui.spinBox_off_step_B0.value()
        self.yaml_config_handler.write_hanle_config(off_step_B0=value_off_step)
        print('[SET] B0 offset step value: ' + str(value_off_step))

    def apply_off_step_B1(self):
        value_off_step = self.gui.spinBox_off_step_B1.value()
        self.yaml_config_handler.write_hanle_config(off_step_B1=value_off_step)
        print('[SET] B1 offset step value: ' + str(value_off_step))

    def apply_meas_no(self):
        meas_no = self.gui.spinBox_measure_no.value()
        self.yaml_config_handler = yw.YamlConfigHandler(meas_no)
        print('[SET] measurement number: ' + str(meas_no))

    def apply_cell_id(self):
        cell_id = self.gui.spinBox_cell_id.value()
        self.gui.spinBox_measure_no.setValue(self.gui.ui_utils.find_current_measurement_number(cell_id))
        self.yaml_config_handler.write_hanle_config(cell=cell_id)
        print('[SET] cell\'s id: ' + str(cell_id))

    def apply_temp(self):
        temp = self.gui.spinBox_temp.value()
        self.yaml_config_handler.write_hanle_config(temp=temp)
        print('[SET] temperature [°C] : ' + str(temp))

    def apply_lpower(self):
        power = self.gui.spinBox_lpower.value()
        self.yaml_config_handler.write_hanle_config(power=power)
        print('[SET] laser power [uW] : ' + str(power))

    def apply_diode_gain(self):
        gain = self.gui.spinBox_diode_gain.value()
        self.yaml_config_handler.write_hanle_config(diode_gain=gain)
        print('[SET] photo diode gain: ' + str(gain))

    def apply_samples(self):
        samples = self.gui.spinBox_samples.value()
        self.yaml_config_handler.write_hanle_config(samples=samples)
        print('[SET] sample rate: ' + str(samples))

    def apply_downsampling(self):
        downsamples = self.gui.spinBox_downsampling.value()
        self.yaml_config_handler.write_hanle_config(downsampling=downsamples)
        print('[SET] downsampling factor: ' + str(downsamples))

    def apply_measure_time(self):
        mtime = self.gui.spinBox_mtime.value()
        self.yaml_config_handler.write_hanle_config(meas_time=mtime)
        print('[SET] measurement time [s]: ' + str(mtime))

    def apply_method_B0(self):
        method = self.gui.comboBox_method_B0.currentText()
        self.yaml_config_handler.write_hanle_config(method_B0=method)
        print('[SET] B0 measuring method: ' + method)

    def apply_method_B1(self):
        method = self.gui.comboBox_method_B1.currentText()
        self.yaml_config_handler.write_hanle_config(method_B1=method)
        print('[SET] B1 measuring method: ' + method)
        

    def apply_stack(self):
        stack = []
        stat_B0 = self.gui.checkBox_B0.checkState()
        stat_B1 = self.gui.checkBox_B1.checkState()
        method_B0 = self.gui.comboBox_method_B0.currentText()
        method_B1 = self.gui.comboBox_method_B1.currentText()
        # B1:
        if stat_B1 == 2 and method_B1 in ['freq', 'amp', 'offset']:
            var2 = 'B1.' + str(self.gui.spinBox_stack_B1.value())
            stack.append(var2)
        else: pass
        # B0:
        if stat_B0 == 2 and method_B0 in ['freq', 'amp', 'offset']:
            var1 = 'B0.' + str(self.gui.spinBox_stack_B0.value())
            stack.append(var1)
        else: pass
        self.yaml_config_handler.write_hanle_config(stack=stack)
        print('[SET] stack: ' + str(stack))
        #print(stack)

    def get_cell_id_measurement_no(self):
        cell_id = self.gui.ui_utils.find_recent_cell_id()
        number = self.gui.ui_utils.find_current_measurement_number(cell_id)
        self.gui.spinBox_measure_no.setValue(number)
        self.gui.spinBox_cell_id.setValue(cell_id)





# User Interface Utils
class UIUtils():
    gui = None

    def __init__(self, gui):
        UIUtils.gui = gui

    def disable_widgets_init(self):
        value_stat1 = self.gui.checkBox_B0.checkState()
        value_stat2 = self.gui.checkBox_B1.checkState()
        method1 = self.gui.comboBox_method_B1.currentText()
        method0 = self.gui.comboBox_method_B0.currentText()
        if value_stat1 == 2 and method0 in ['freq', 'amp', 'offset']:
            self.gui.spinBox_stack_B0.setEnabled(True)    
        else:
            self.gui.spinBox_stack_B0.setEnabled(False)
        if value_stat2 == 2 and method1 in ['freq', 'amp', 'offset']:
            self.gui.spinBox_stack_B1.setEnabled(True)    
        else:
            self.gui.spinBox_stack_B1.setEnabled(False)

    def disable_widgets(self, key):
        method = eval('self.gui.comboBox_method_' + key).currentText()
        if method == 'const':
            eval('self.gui.spinBox_freq_stop_' + key).setEnabled(False)
            eval('self.gui.spinBox_freq_step_' + key).setEnabled(False)
            eval('self.gui.spinBox_ampl_stop_' + key).setEnabled(False)
            eval('self.gui.spinBox_ampl_step_' + key).setEnabled(False)
            eval('self.gui.spinBox_off_stop_' + key).setEnabled(False)
            eval('self.gui.spinBox_off_step_' + key).setEnabled(False)
            eval('self.gui.spinBox_stack_' + key).setEnabled(False)
        else:
            eval('self.gui.spinBox_freq_stop_' + key).setEnabled(True)
            eval('self.gui.spinBox_freq_step_' + key).setEnabled(True)
            eval('self.gui.spinBox_ampl_stop_' + key).setEnabled(True)
            eval('self.gui.spinBox_ampl_step_' + key).setEnabled(True)
            eval('self.gui.spinBox_off_stop_' + key).setEnabled(True)
            eval('self.gui.spinBox_off_step_' + key).setEnabled(True)
            eval('self.gui.spinBox_stack_' + key).setEnabled(True)

    def find_current_measurement_number(self, cell_id):
        import glob
        import os
        import re
        #cell_id = self.find_recent_cell_id()
        try:
            newest_folder = max(glob.iglob(os.path.join('N:\\data\\2016\\magnetometer\\cell{}\\remote'.format(cell_id), '*/')), key=os.path.getctime)
            regex = re.compile(r'\d+')
            regex.findall(newest_folder)
            nums=[int(x) for x in regex.findall(newest_folder)]
            recent_measure_num=nums[-1]
            measurement_number = recent_measure_num + 1
            print(newest_folder)
            print(nums)
            print(measurement_number, type(measurement_number))
            return measurement_number
        
        except ValueError:
            print('no existing measurement in directory: start now with measurement number = 0')

            return 0

    def find_recent_cell_id(self):
        import glob
        import os
        import re

        try:
            newest_folder = max(glob.iglob(os.path.join('N:\\data\\2016\\magnetometer', '*/')), key=os.path.getctime)
            regex = re.compile(r'\d+')
            regex.findall(newest_folder)
            nums=[int(x) for x in regex.findall(newest_folder)]
            recent_cell_id=nums[-1]
            print(newest_folder)
            print(nums)
            print(recent_cell_id)
            return(recent_cell_id)
        except ValueError:
            print('no recent cell id found: set cell id = 0')
            return 0

    def synchronize_devices(self, key1, key2):
        # key = B0, B1
        print(key1, type(key1))
        var1 = eval('self.gui.comboBox_device_' + key1)
        var2 = eval('self.gui.comboBox_device_' + key2)
        dev_index = var1.currentIndex()
        var2.setCurrentIndex(dev_index)

    def edit_stack(self, key):
        value_stat = eval('self.gui.checkBox_' + key).checkState()
        method = eval('self.gui.comboBox_method_' + key).currentText()
        if value_stat == 2 and method in ['freq', 'amp', 'offset']:
            eval('self.gui.spinBox_stack_' + key).setEnabled(True)
        else:
            eval('self.gui.spinBox_stack_' + key).setEnabled(False)
        
           

    def edit_stack_pos(self, key1, key2):
        if eval('self.gui.spinBox_stack_' + key1).isEnabled() == False:
            eval('self.gui.spinBox_stack_' + key2).setValue(0)
        elif eval('self.gui.spinBox_stack_' + key1).value() == 0:
            eval('self.gui.spinBox_stack_' + key2).setValue(1)
        elif eval('self.gui.spinBox_stack_' + key1).value() == 1:
            eval('self.gui.spinBox_stack_' + key2).setValue(0)




        



def main():
    app = QtGui.QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon("icon1.png"));
    window = ControllerGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
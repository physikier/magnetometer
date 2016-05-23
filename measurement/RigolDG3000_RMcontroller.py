import hardware.RigolDG3000 as rig
import sys 
import numpy
from PyQt5 import QtWidgets, QtCore, QtGui, uic

rigol = rig.RigolDG3000("USB0::0x1AB1::0x0588::DG1D124204534::INSTR")


# Main QT Window Class
# The Class which conations all QT Widgets and so on
class ControllerGui(QtWidgets.QMainWindow):
    # controller_utils is an instance of the ControllerUtils class (Singleton)
    controller_utils = None
    # ui_utils is an instance of the UIUtils class (Singleton)
    ui_utils = None

    def __init__(self):
        super(ControllerGui, self).__init__()
        uic.loadUi("./RigolDG3000_FMspec/fm_spec_via_dg3000.ui", self)

        ControllerGui.controller_utils = ControllerUtils(self)
        ControllerGui.ui_utils = UIUtils(self)

        self.controller_utils.get_settings()

        # connect the button clicks with the specific functions
        self.button_get.clicked.connect(self.controller_utils.get_settings)
        self.button_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.checkBox_ch1_active.stateChanged.connect(self.controller_utils.apply_ch1_stat)
        self.checkBox_ch2_active.stateChanged.connect(self.controller_utils.apply_ch2_stat)

        self.box_ch1_wform.currentIndexChanged.connect(self.controller_utils.apply_ch1_wform)
        self.box_ch2_wform.currentIndexChanged.connect(self.controller_utils.apply_ch2_wform)

        self.textbox_ch1_freq.editingFinished.connect(self.controller_utils.apply_ch1_freq)
        self.textbox_ch2_freq.editingFinished.connect(self.controller_utils.apply_ch2_freq)
        self.hscrollbar_ch1_freq.sliderReleased.connect(self.controller_utils.apply_ch1_freq)
        self.hscrollbar_ch2_freq.sliderReleased.connect(self.controller_utils.apply_ch2_freq)

        self.textbox_ch1_ampl.editingFinished.connect(self.controller_utils.apply_ch1_ampl)
        self.textbox_ch2_ampl.editingFinished.connect(self.controller_utils.apply_ch2_ampl)
        self.hscrollbar_ch1_ampl.sliderReleased.connect(self.controller_utils.apply_ch1_ampl)
        self.hscrollbar_ch2_ampl.sliderReleased.connect(self.controller_utils.apply_ch2_ampl)

        self.textbox_ch1_off.editingFinished.connect(self.controller_utils.apply_ch1_off)
        self.textbox_ch2_off.editingFinished.connect(self.controller_utils.apply_ch2_off)
        self.hscrollbar_ch1_off.sliderReleased.connect(self.controller_utils.apply_ch1_off)
        self.hscrollbar_ch2_off.sliderReleased.connect(self.controller_utils.apply_ch2_off)

        self.textbox_ch1_phase.editingFinished.connect(self.controller_utils.apply_ch1_phase)
        self.textbox_ch2_phase.editingFinished.connect(self.controller_utils.apply_ch2_phase)
        self.dial_ch1_phase.sliderReleased.connect(self.controller_utils.apply_ch1_phase)
        self.dial_ch2_phase.sliderReleased.connect(self.controller_utils.apply_ch2_phase)



        # connect the sliders/dials with the textbox above (and visa versa) to see the current slider/dial value

        # Frequency
        self.hscrollbar_ch1_freq.sliderMoved.connect(lambda slider=self.hscrollbar_ch1_freq, textbox=self.textbox_ch1_freq: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch1_freq, textbox=self.textbox_ch1_freq, factor=10))
        self.hscrollbar_ch2_freq.sliderMoved.connect(lambda slider=self.hscrollbar_ch2_freq, textbox=self.textbox_ch2_freq: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch2_freq, textbox=self.textbox_ch2_freq, factor=10))
        self.hscrollbar_ch1_freq.valueChanged.connect(lambda slider=self.hscrollbar_ch1_freq, textbox=self.textbox_ch1_freq: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch1_freq, textbox=self.textbox_ch1_freq, factor=10))
        self.hscrollbar_ch2_freq.valueChanged.connect(lambda slider=self.hscrollbar_ch2_freq, textbox=self.textbox_ch2_freq: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch2_freq, textbox=self.textbox_ch2_freq, factor=10))
        self.textbox_ch1_freq.editingFinished.connect(lambda slider=self.hscrollbar_ch1_freq, textbox=self.textbox_ch1_freq: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch1_freq, slider=self.hscrollbar_ch1_freq, factor=10))
        self.textbox_ch2_freq.editingFinished.connect(lambda slider=self.hscrollbar_ch2_freq, textbox=self.textbox_ch2_freq: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch2_freq, slider=self.hscrollbar_ch2_freq, factor=10))

        # Amplitude
        self.hscrollbar_ch1_ampl.sliderMoved.connect(lambda slider=self.hscrollbar_ch1_ampl, textbox=self.textbox_ch1_ampl: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch1_ampl, textbox=self.textbox_ch1_ampl, factor=10))
        self.hscrollbar_ch2_ampl.sliderMoved.connect(lambda slider=self.hscrollbar_ch2_ampl, textbox=self.textbox_ch2_ampl: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch2_ampl, textbox=self.textbox_ch2_ampl, factor=10))
        self.hscrollbar_ch1_ampl.valueChanged.connect(lambda slider=self.hscrollbar_ch1_ampl, textbox=self.textbox_ch1_ampl: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch1_ampl, textbox=self.textbox_ch1_ampl, factor=10))
        self.hscrollbar_ch2_ampl.valueChanged.connect(lambda slider=self.hscrollbar_ch2_ampl, textbox=self.textbox_ch2_ampl: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch2_ampl, textbox=self.textbox_ch2_ampl, factor=10))
        self.textbox_ch1_ampl.editingFinished.connect(lambda slider=self.hscrollbar_ch1_ampl, textbox=self.textbox_ch1_freq: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch1_ampl, slider=self.hscrollbar_ch1_ampl, factor=10))
        self.textbox_ch2_ampl.editingFinished.connect(lambda slider=self.hscrollbar_ch2_ampl, textbox=self.textbox_ch2_freq: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch2_ampl, slider=self.hscrollbar_ch2_ampl, factor=10))

        # Offset
        self.hscrollbar_ch1_off.valueChanged.connect(lambda slider=self.hscrollbar_ch1_off, textbox=self.textbox_ch1_off: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch1_off, textbox=self.textbox_ch1_off, factor=10))
        self.hscrollbar_ch2_off.valueChanged.connect(lambda slider=self.hscrollbar_ch2_off, textbox=self.textbox_ch2_off: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch2_off, textbox=self.textbox_ch2_off, factor=10))
        self.hscrollbar_ch1_off.sliderMoved.connect(lambda slider=self.hscrollbar_ch1_off, textbox=self.textbox_ch1_off: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch1_off, textbox=self.textbox_ch1_off, factor=10))
        self.hscrollbar_ch2_off.sliderMoved.connect(lambda slider=self.hscrollbar_ch2_off, textbox=self.textbox_ch2_off: self.ui_utils.connect_slider_textbox(slider=self.hscrollbar_ch2_off, textbox=self.textbox_ch2_off, factor=10))
        self.textbox_ch1_off.editingFinished.connect(lambda slider=self.hscrollbar_ch1_off, textbox=self.textbox_ch1_off: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch1_off, slider=self.hscrollbar_ch1_off, factor=10))
        self.textbox_ch2_off.editingFinished.connect(lambda slider=self.hscrollbar_ch2_off, textbox=self.textbox_ch2_off: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch2_off, slider=self.hscrollbar_ch2_off, factor=10))


        # Phase
        self.dial_ch1_phase.sliderMoved.connect(lambda slider=self.dial_ch1_phase, textbox=self.textbox_ch1_phase: self.ui_utils.connect_slider_textbox(slider=self.dial_ch1_phase, textbox=self.textbox_ch1_phase, factor=1))
        self.dial_ch2_phase.sliderMoved.connect(lambda slider=self.dial_ch2_phase, textbox=self.textbox_ch2_phase: self.ui_utils.connect_slider_textbox(slider=self.dial_ch2_phase, textbox=self.textbox_ch2_phase, factor=1))
        self.textbox_ch1_phase.editingFinished.connect(lambda slider=self.dial_ch1_phase, textbox=self.textbox_ch1_phase: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch1_phase, slider=self.dial_ch1_phase, factor=1))
        self.textbox_ch2_phase.editingFinished.connect(lambda slider=self.dial_ch2_phase, textbox=self.textbox_ch2_phase: self.ui_utils.connect_textbox_slider(textbox=self.textbox_ch2_phase, slider=self.dial_ch2_phase, factor=1))

        #self.get_settings()
        self.show()

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ModifiedChange and source is self.box_ch1_wform):
            print('test')
        return QtWidgets.QWidget.eventFilter(self, source, event)


# Function Generator Utils
class ControllerUtils():
    # the gui is the instance of the main Qt Window (ControllerGui class)
    gui = None

    def __init__(self, gui):
        ControllerUtils.gui = gui

    def check_ch_status(self, channel):
        #print('rigol ouput value: ' + rigol.get_output(channel))
        if rigol.get_output(channel) == "ON\n":
            output = 1
        else:
            output = 0
        return output

    def get_settings(self):
        ch1_active = self.check_ch_status(1)
        print('[GET] Channel 1 Status: ' + str(ch1_active))
        #self.gui.checkBox_ch1_active.setChecked(ch1_active)
        self.gui.checkBox_ch1_active.setChecked(2)

        ch2_active = self.check_ch_status(2)
        print('[GET] Channel 2 Status: ' + str(ch2_active))
        self.gui.checkBox_ch2_active.setChecked(ch2_active)

        ch1_wform = rigol.get_waveform(1)[4:]
        print('[GET] Channel 1 Waveform: ' + str(ch1_wform))
        self.gui.box_ch1_wform.setCurrentIndex(self.gui.box_ch1_wform.findText(ch1_wform, QtCore.Qt.MatchFixedString))

        ch2_wform = rigol.get_waveform(2)[4:]
        print('[GET] Channel 2 Waveform: ' + str(ch2_wform))
        self.gui.box_ch2_wform.setCurrentIndex(self.gui.box_ch2_wform.findText(ch2_wform, QtCore.Qt.MatchFixedString))

        ch1_freq = rigol.get_freq(1)
        print('[GET] Channel 1 Frequency: ' + str(ch1_freq))
        self.gui.textbox_ch1_freq.setText(ch1_freq)
        self.gui.hscrollbar_ch1_freq.setValue(float(ch1_freq))

        ch2_freq = rigol.get_freq(2)[4:]
        print('[GET] Channel 2 Frequency: ' + str(ch2_freq))
        self.gui.textbox_ch2_freq.setText(ch2_freq)
        self.gui.hscrollbar_ch2_freq.setValue(float(ch2_freq))

        ch1_ampl = rigol.get_ampl(1)
        print('[GET] Channel 1 Amplitude: ' + str(ch1_ampl))
        self.gui.textbox_ch1_ampl.setText(ch1_ampl)
        self.gui.hscrollbar_ch1_ampl.setValue(float(ch1_ampl)*10)

        ch2_ampl = rigol.get_ampl(2)[5:]
        print('[GET] Channel 2 Amplitude: ' + str(ch2_ampl))
        self.gui.textbox_ch2_ampl.setText(ch2_ampl)
        self.gui.hscrollbar_ch2_ampl.setValue(float(ch2_ampl)*10)

        ch1_off = rigol.get_off(1)
        print('[GET] Channel 1 Offset: ' + str(ch1_off))
        self.gui.textbox_ch1_off.setText(ch1_off)
        self.gui.hscrollbar_ch1_off.setValue(float(ch1_off)*10)

        ch2_off = rigol.get_off(2)
        print('[GET] Channel 2 Offset: ' + str(ch2_off))
        self.gui.textbox_ch2_off.setText(ch2_off)
        self.gui.hscrollbar_ch2_off.setValue(float(ch2_off)*10)

        ch1_phase = rigol.get_phase(1)
        print('[GET] Channel 1 Phase: ' + str(ch1_phase))
        self.gui.textbox_ch1_phase.setText(ch1_phase)
        self.gui.dial_ch1_phase.setValue(float(ch1_phase))
        
        ch2_phase = rigol.get_phase(2)
        print('[GET] Channel 2 Phase: ' + str(ch2_phase))
        self.gui.textbox_ch2_phase.setText(ch2_phase)
        self.gui.dial_ch2_phase.setValue(float(ch2_phase))

        print('got all settings...')

    def apply_ch1_stat(self):
        value_stat = self.gui.checkBox_ch1_active.checkState()
        if value_stat == 2:
            rigol.set_output(1, "ON")
        else:
            rigol.set_output(1, "OFF")
        print('[SET] Channel 1 Status: ' + str(value_stat))

    def apply_ch2_stat(self):
        value_stat = self.gui.checkBox_ch2_active.checkState()
        if value_stat == 2:
            rigol.set_output(2, "ON")
        else:
            rigol.set_output(2, "OFF")
        print('[SET] Channel 2 Status: ' + str(value_stat))

    def apply_ch1_wform(self):
        ch1_wform = self.gui.box_ch1_wform.currentText()
        rigol.set_waveform(1, ch1_wform)
        print('[SET] Channel 1 Waveform: ' + ch1_wform)

    def apply_ch2_wform(self):
        ch2_wform = self.gui.box_ch2_wform.currentText()
        rigol.set_waveform(2, ch2_wform)
        print('[SET] Channel 2 Waveform: ' + ch2_wform)

    def apply_ch1_freq(self):
        ch1_freq = self.gui.textbox_ch1_freq.text()
        rigol.set_freq(1, float(ch1_freq))
        print('[SET] Channel 1 Frequency: ' + ch1_freq)

    def apply_ch2_freq(self):
        ch2_freq = self.gui.textbox_ch2_freq.text()
        rigol.set_freq(2, float(ch2_freq))
        print('[SET] Channel 2 Frequency: ' + ch2_freq)

    def apply_ch1_ampl(self):
        ch1_ampl = self.gui.textbox_ch1_ampl.text()
        rigol.set_ampl(1, float(ch1_ampl))
        print('[SET] Channel 1 Amplitude: ' + ch1_ampl)

    def apply_ch2_ampl(self):
        ch2_ampl = self.gui.textbox_ch2_ampl.text()
        rigol.set_ampl(2, float(ch2_ampl))
        print('[SET] Channel 2 Amplitude: ' + ch2_ampl)

    def apply_ch1_off(self):
        #ch1_off = self.ui_utils.value_handler(self.gui.textbox_ch1_off.text())
        ch1_off = self.gui.textbox_ch1_off.text()
        rigol.set_off(1, float(ch1_off))
        print('[SET] Channel 1 Offset: ' + ch1_off)

    def apply_ch2_off(self):
        ch2_off = self.gui.textbox_ch2_off.text()
        rigol.set_off(2, float(ch2_off))
        print('[SET] Channel 2 Offset: ' + ch2_off)

    def apply_ch1_phase(self):
        ch1_phase = self.gui.textbox_ch1_phase.text()
        rigol.set_phase(1, float(ch1_phase))
        print('[SET] Channel 1 offset: ' + ch1_phase)

    def apply_ch2_phase(self):
        ch2_phase = self.gui.textbox_ch2_phase.text()
        rigol.set_phase(2, float(ch2_phase))
        print('[SET] Channel 2 set: ' + ch2_phase)

    def close_rigol(self):
        rigol.close_rigol()


# User Interface Utils
class UIUtils():
    gui = None

    def __init__(self, gui):
        UIUtils.gui = gui

    def connect_slider_textbox(self, slider, textbox, factor):
        textbox.setText(str(self.value_handler(slider.value(), factor)))

    def connect_textbox_slider(self, textbox, slider, factor):
        slider.setValue(int(float(textbox.text())*factor))

    def value_handler(self, value, factor):
        scaled_value = '{0:.2f}'.format(float(value/factor))
        return scaled_value      

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon1.png"));
    window = ControllerGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
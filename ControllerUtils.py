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
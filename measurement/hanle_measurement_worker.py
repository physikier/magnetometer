import numpy as np
import ctypes
import time
import os
import sys
import copy
import matplotlib.pyplot as plt
import logging

# delete meas11 folder (not necessary for magnetometer program)
import shutil
shutil.rmtree(
    "N:\\data\\2016\\magnetometer\\cell66\\remote\\meas11",
    ignore_errors=True)

#
_import_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
if _import_path not in sys.path:
    sys.path.insert(0, _import_path)

# hardware
import pyvisa
import hardware.afg3000_py3 as tek
import hardware.hameg_py3 as ha
#import hardware.sr_lockin as lo
import hardware.Motordriver_py3 as mo

from nidaq_device_modTR2 import NidaqDevice
from configuration_parser import load_config, ConfigIntegrityException
from measurement_worker import MeasurementWorker
################################################
log_formatter = logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
logger = logging.getLogger('measurement_logger')

handlers_registered = False
if not handlers_registered:
    handlers_registered = True
    
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'log.log'))
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

logger.setLevel(logging.INFO)
logger.propagate = False
################################################
################################################
configure_folder_path = os.path.join(os.getcwd(), 'configs')
configure_filenames = os.listdir(configure_folder_path)

for config_filename in configure_filenames:
    config_filepath = os.path.join(configure_folder_path, config_filename)
    try:
        logger.info('Read config file: {}'.format(config_filepath))
        cfg = load_config(config_filepath)
    except ConfigIntegrityException:
        # TODO: add logfile
        exc_info = sys.exc_info()
        raise exc_info[0](exc_info[1]).with_traceback(exc_info[2])
    
    try:
        hameg = ha.HMP2030(device="hameg01", voltage_max=20., current_max=0.07)
        tektronix = tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")
        #lock_in = lo.SR830("GPIB0::08::INSTR")
        motor = mo.Motordriver('COM4')

        use_lock_in = cfg['outputs']['lock_in']['active']
        nidaq_config = cfg['devices']['nidaq']
        nidaq = NidaqDevice()
        nidaq.load_config(nidaq_config, use_lock_in=use_lock_in)
        mw = MeasurementWorker(nidaq=nidaq, tektronix=tektronix, hameg=hameg, lock_in=None, motor=motor, logger=logger)
        mw.set_config(cfg) # load measurement config
        mw.set_base_path(os.path.join('n:', os.sep, 'data', '2016', 'magnetometer'))

        mw.measure(save=True, config_path=config_filepath)

    except Exception as e:
    
        # TODO: add logfile
        exc_info = sys.exc_info()
        raise exc_info[0](exc_info[1]).with_traceback(exc_info[2])
    finally:
        hameg.close()
    try:
        motor.disconnect()
    except SerialException:
        pass
##############################################################################################
motor.disconnect()

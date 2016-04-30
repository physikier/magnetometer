import numpy as np
import ctypes
import time
import os
import sys
import copy
import matplotlib.pyplot as plt
import logging

_import_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
if _import_path not in sys.path:
    sys.path.insert(0, _import_path)

# hardware
import hardware.afg3000 as tek
import pyvisa
import hardware.hameg as ha

from nidaq_device_modTR import NidaqDevice
from configuration_parser import load_config, ConfigIntegrityException
from measurement_worker import MeasurementWorker

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
        raise exc_info[0], exc_info[1], exc_info[2]

    try:
        hameg = ha.HMP2030(device="hameg01", voltage_max=20., current_max=0.07)
        tektronix = tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")

        use_lock_in = cfg['measurement']['lock_in_params']['active']
        nidaq_config = cfg['devices']['nidaq']
        nidaq = NidaqDevice()
        nidaq.load_config(nidaq_config, use_lock_in=use_lock_in)
        mw = MeasurementWorker(nidaq=nidaq, tektronix=tektronix, hameg=hameg, logger=logger)
        mw.set_config(cfg) # load measurement config
        #mw.set_base_path(os.path.join('n:', os.sep, 'data', 'emily', 'magnetometer_test'))
        mw.set_base_path(os.path.join('n:', os.sep, 'data', '2016', 'magnetometer'))

        mw.measure(save=True, config_path=config_filepath)

    except Exception, e:

        # TODO: add logfile
        exc_info = sys.exc_info()
        raise exc_info[0], exc_info[1], exc_info[2]
    finally:
        hameg.close()

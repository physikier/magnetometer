import hardware.hameg as ha
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt
import os
import matplotlib.colors as cl


########################################################################
#CONNECT to hameg and tektronix


hameg=ha.HMP2030(device="hameg01", voltage_max=20., current_max=1)
hameg.close()

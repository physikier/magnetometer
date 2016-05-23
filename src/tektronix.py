import hardware.afg3000 as tek
import hardware.ni_usb_6361 as daq
import numpy as np
import time
import pyvisa
import matplotlib.pyplot as plt

tektronix=tek.AFG3252("TCPIP0::129.69.46.235::inst0::INSTR")


tektronix.set_frequency_mode(mode="SWE", ch=2)
tektronix.set_frequency_sweep_span(span=1E3, ch=2)
tektronix.set_center_frequency(center=5E3, ch=2)
tektronix.set_sweep_mode(mode="MAN", ch=2)
tektronix.set_sweep_time(time=0.5, ch=2)
tektronix.set_sweep_rtime(rtime=0.5, ch=2)
tektronix.set_sweep_htime(htime=0, ch=2)
tektronix.set_sweep_form(form="LIN", ch=2)
tektronix.set_amp(voltage=0.7, ch=2)




tektronix.set_waveform(func='DC', ch=1)
tektronix.trig_mode()
tektronix.set_offset(offset=90E-3, ch=1)
tektronix.trig_mode()
tektronix.set_freq(frequency=2 ,ch=1)
tektronix.trig_mode()

tektronix.run(ch=1)
tektronix.run(ch=2)

tektronix.trig()




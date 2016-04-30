import numpy as np
import hardware.sr_lockin as lockin

lo = lockin.SR830("GPIB0::08::INSTR")

idn = lo.identification()
print idn
freq = lo.get_frequency()
print freq
lo.set_reference_mode(1)
getrefmode = lo.get_reference_mode()
print getrefmode
lo.set_frequency(10000)
freq2 = lo.get_frequency()
print freq2
lo.set_harmonic(1)
detectionmode = lo.get_harmonic()
print detectionmode
sensi = lo.get_sensitivity()
print sensi
lo.set_sensitivity(20)
sensi = lo.get_sensitivity()
print sensi
time = lo.get_time_constant()
print time
lo.set_time_constant(7)
time = lo.get_time_constant()
print time
output = lo.get_output()
print output

x = lo.get_grounding()
print x
lo.set_grounding(1)
x = lo.get_grounding()
print x

x = lo.get_coupling()
print x
lo.set_coupling(1)
x = lo.get_coupling()
print x

x = lo.get_filter_status()
print x
lo.set_filter_status(3)
x = lo.get_filter_status()
print x

x = lo.get_reserve_mode()
print x
lo.set_reserve_mode(1)
x = lo.get_reserve_mode()
print x

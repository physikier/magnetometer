import numpy as np

from traits.api import HasTraits, Range
from traitsui.api import View, Item, RangeEditor

from hardware.nidaq import AOTask

class Laser( HasTraits ):

    def __init__(self, AO_channel='/Dev1/ao3', voltage_range=(0.,5.), **kwargs):
        self.AOTask = AOTask(Channels=AO_channel, range=voltage_range)
        self.AOTask.Write(np.array((float(voltage_range[0]),)))
        self.add_trait('voltage', Range(low=float(voltage_range[0]), high=float(voltage_range[1]), value=float(voltage_range[0]), desc='output voltage', label='Voltage [V]'))
        self.on_trait_change(self.write_voltage, 'voltage')
        HasTraits.__init__(self, **kwargs)
        self.voltage_range=voltage_range
        
    def write_voltage(self, new):
        self.AOTask.Write(np.array((new,)))

    view = View(Item('voltage'),
                title='Laser', width=400, buttons=[], resizable=True)

if __name__=='__main__':
    laser = Laser()
    laser.edit_traits()
    
import numpy as np
import time

from traits.api import HasTraits, Button
from traitsui.api import View, Item

from enthought.traits.ui.menu import Action, Menu, MenuBar

from nidaq import DOTask

class SpectrometerTrigger( HasTraits ):

    trigger = Button(desc="trigger spectrometer")
    
    def __init__(self, trigger_channels):
        super(HasTraits, self).__init__()
        self._trigger_task = DOTask(trigger_channels)

    def _trigger_changed(self):
        self._trigger_task.Write(np.array((1,), dtype=np.uint8) )
        time.sleep(0.001)
        self._trigger_task.Write(np.array((0,), dtype=np.uint8) )

    view = View(Item('trigger', show_label=False),
                title='Trigger spectrometer',
                buttons=[],
                resizable=True)
    
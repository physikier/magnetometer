import numpy as np
import time

from traits.api import HasTraits, Button
from traitsui.api       import View, Item, Group, HGroup, VGroup

from enthought.traits.ui.menu import Action, Menu, MenuBar

from nidaq import DOTask

class FlipMirror( HasTraits ):

    flip = Button(desc="flip the mirror")
    
    def __init__(self, trigger_channels):
        super(HasTraits, self).__init__()
        self._trigger_task = DOTask(trigger_channels)

    def _flip_changed(self):
        self._trigger_task.Write(np.array((1,), dtype=np.uint8) )
        time.sleep(0.01)
        self._trigger_task.Write(np.array((0,), dtype=np.uint8) )

    view = View(Item('flip', show_label=False),
                title='Flip mirror',               
                buttons=[],
                resizable=True)
    
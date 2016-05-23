import numpy
import time

from enthought.traits.api import SingletonHasTraits, Button
from enthought.traits.ui.api import View, Item

from enthought.traits.ui.menu import Action, Menu, MenuBar

from utility import CloseHandler

from NIDAQ import DOTask

class Flip( SingletonHasTraits ):

    flippen = Button(desc="flip the mirror", label="flip mirror")
    
    def __init__(self, TriggerChannels):
        self._trigger_task = DOTask(TriggerChannels)
        SingletonHasTraits.__init__(self)

    def _flippen_changed(self):
        self._change_mirror()
    
    def _change_mirror(self):
        self._trigger_task.Write(numpy.array((1,), dtype=numpy.uint8) )
        time.sleep(0.001)
        self._trigger_task.Write(numpy.array((0,), dtype=numpy.uint8) )

    view = View(Item('flippen', show_label=False), menubar = MenuBar(Menu(Action(action='_on_close', name='Quit'), name='File')), title='Flip mirror', width=100, height=100, buttons=[], resizable=True, handler=CloseHandler)
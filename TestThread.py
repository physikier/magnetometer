from PyQt4 import QtCore, QtGui

#============================================================================
class TestThread(QtCore.QThread):

  testSignal = QtCore.pyqtSignal(object)

  #--------------------------------------------------------------------------
  def __init__(self):
    QtCore.QThread.__init__(self)
    
  #--------------------------------------------------------------------------
  def __del__(self):
    self.wait()
    
  #--------------------------------------------------------------------------
  def run(self):
    
    string = "test string"
    self.testSignal.emit(string)
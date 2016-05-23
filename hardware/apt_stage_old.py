#import win32com.client

#ocx = win32com.client.dynamic.Dispatch("MGMOTOR.MGMotorCtrl.1")

#win32com.client.GetActiveObject(Class="MGMOTOR.MGMotorCtrl.1")
#win32com.client.GetActiveObject(Class='{2A833923-9AA7-4C45-90AC-DA4F19DC24D1}')

import win32com.client
import wx 
import wx.activex

#from wx.lib.activexwrapper import MakeActiveXClass

module = win32com.client.gencache.EnsureModule('{9460A175-8618-4753-B337-61D9771C4C14}', 0, 1, 2) # system
frame = wx.Frame(None)
wx.activex.ActiveXWindow(frame, clsId=wx.activex.CLSID('{00020813-0000-0000-C000-000000000046}') )

#AptClass = MakeActiveXClass(module.MG17System, eventObj=frame)
#AptClass = MakeActiveXClass(module.MG17System)

#apt_instance = AptClass(frame, -1)


#frame.Show()
#wx.activex.ActiveXWindow(frame, clsId=wx.activex.CLSID('{00020813-0000-0000-C000-000000000046}') )

#excel = win32com.client.Dispatch('Excel.Application')
#excel.Visible=True

#win32com.client.gencache.EnsureModule({00020813-0000-0000-C000-000000000046}', 0, 1, 2) # Excel

#win32com.client.gencache.EnsureModule('{9460A175-8618-4753-B337-61D9771C4C14}', 0, 1, 2) # system
#win32com.client.gencache.EnsureModule('{2A833923-9AA7-4C45-90AC-DA4F19DC24D1}', 0, 1, 2)


#apt_stage = win32com.client.Dispatch("MGMOTOR.MGMotorCtrl.1")
#apt_stage.HWSerialNum = 83838311

#frame = wx.Frame(None)
#frame.Show()
#wx.activex.ActiveXWindow(frame, clsId=wx.activex.CLSID('{9460A175-8618-4753-B337-61D9771C4C14}') )
#apt_system = win32com.client.Dispatch('MG17SYSTEM.MG17SystemCtrl.1')
#apt_system = win32com.client.Dispatch('MG17SYSTEM.MG17SystemCtrl.1')

#MakeActiveXClass(browserModule.WebBrowser, eventObj=self)


#class evt:
#  def OnTransportNewState(self, newState=None, oldState=None):
#    print "Changing State, %s to %s" %(oldState, newState)
#  # ...
  
#class mainwindow(wx.Frame):
#  def __init__(self):
#    wx.Frame.__init__(self, None , wx.ID_ANY, "Test")

    # turns out that this isn't necessary   
#    self.Show()

    #ctrl = wx.activex.ActiveXWindow(self,
    #               clsId=wx.activex.CLSID('{2A833923-9AA7-4C45-90AC-DA4F19DC24D1}'),
    #               id=-1,
    #               name="MGMOTOR.MGMotorCtrl.1"
    #               )

    # the dispatch to send messages to the control
    #self.d = win32com.client.Dispatch("MGMOTOR.MGMotorCtrl.1")
    # Event object with call backs to receive events
    #self.e = win32com.client.WithEvents(self.d, evt)

    # this lets you poke around
    #self.shell = wx.py.shell.ShellFrame()
    #self.shell.Show()
    # and this shouldn't fail badly, at least for this control
    #print self.d.GetVersion()

#if __name__== '__main__':
#    frame = wx.Frame(None)
#    frame.Show()
#    wx.activex.ActiveXWindow(frame,
#                             clsId=wx.activex.CLSID('{2A833923-9AA7-4C45-90AC-DA4F19DC24D1}'),
                             #id=-1,
                             #name="MGMOTOR.MGMotorCtrl.1"
#                             )
    
  #app = wx.PySimpleApp()
  #app = wx.App()
  #frame = mainwindow()
  #app.MainLoop()
  
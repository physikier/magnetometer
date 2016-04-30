import sys 
#import numpy as no
#import PyQt4
#import sympy as sy
#import scipy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, minimize
from lmfit import minimize, Parameters, Parameter, fit_report, report_fit
import numpy as np
import PyQt4
## this will force pyqtgraph to use PySide instead of PyQt4
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui, uic



# Main QT Window Class
# The Class which conations all QT Widgets and so on
class CompensatorGui(QtGui.QMainWindow):
    # compensator_utils is an instance of the CompensatorUtils class (Singleton)
    compensator_utils = None
    # ui_utils is an instance of the UIUtils class (Singleton)
    ui_utils = None

    def __init__(self):
        super(CompensatorGui, self).__init__()
        uic.loadUi("fieldcompensator.ui", self)

        CompensatorGui.compensator_utils = CompensatorUtils(self)
        CompensatorGui.ui_utils = UIUtils(self)

       # self.compensator_utils.plot3()
       # self.compensator_utils.plot2()
    #self.compensator_utils.fit()
        #self.compensator_utils.comp()
        self.compensator_utils.fit2()
        self.plot.setTitle(title='titel')
        self.plot.setLabel('left', "Y Axis", units='A')
        self.plot.setLabel('bottom', "X Axis", units='B')
        

        self.show()

# Compensator Utils
class CompensatorUtils():
    # the gui is the instance of the main Qt Window (CompensatorGui class)
    gui = None

    def __init__(self, gui):
        CompensatorUtils.gui = gui

    def plot(self):
        x = np.random.normal(size=10000)
        y = np.random.normal(size=10000)
        self.gui.plot.plot(x,y, pen=None, symbol='o')

    def plot2(self):
        x = np.linspace(-30000.0, 30000.0, num=5000)
        y = UIUtils.pz_bxy_scan(B=x, B01=0, B02=0, B03=0, T_long=2.5*0.002, T_trans=0.002, Rp=1./(2*0.002), Rprb=1./(4*0.002), gamma=2.2, s=-1.0)
        #self.gui.plot.plot(x,y, pen=None, symbol='o')
        self.gui.plot.plot(x,y, pen=(255,0,0))

    def plot3(self):
        x = np.linspace(-30000.0, 30000.0, num=1000)
        y = UIUtils.pz_bxy_scan_data(B=x, B01=0, B02=0, B03=0, T_long=2.5*0.002, T_trans=0.002, Rp=1./(2*0.002), Rprb=1./(4*0.002), gamma=2.2, s=-1.0, xdata=x)
        self.gui.plot.plot(x,y, pen=(0,0,255))

    def fit(self):
        xdata = np.linspace(-30000.0, 30000.0, num=5000)
        ydata = UIUtils.pz_bxy_scan_data(B=xdata, B01=130, B02=100, B03=-800, T_long=2.5*0.002, T_trans=0.002, Rp=1./(2*0.002), Rprb=1./(4*0.002), gamma=2.2, s=-1.0, xdata=xdata)
        x0 = np.array([200.0, 200.0, -1000.0, 0.01, 0.01, 300.0, 100.0])
        self.gui.plot.plot(xdata, ydata, pen=(0,0,255))

        func = UIUtils.fit
        popt, pcov = curve_fit(func, xdata, ydata, x0, maxfev=1000000)
        self.gui.plot.plot(xdata, UIUtils.fit(xdata, *popt), pen=(0,255,0))
        print(*popt)

    def comp(self):
        xdata = np.linespace(-30000.0, 30000.0, num=5000)
        #############
        B=xdata
        B01=0
        B02=100
        B03=-100
        T_trans=0.002
        
        ydata =UIUtils.data(B, B01, B02, B03, T_long, T_trans, Rp, Rprb, xdata)
        self.gui.plot.clear()

    def fit2(self):
        xdata = np.linspace(-30000.0, 30000.0, num=8000)
        #ydata = UIUtils.pz_bxy_scan_data(B=xdata, B01=130, B02=-830, B03=-800, T_long=2.5*0.002, T_trans=0.002, Rp=1./(2*0.002), Rprb=1./(4*0.002), gamma=2.2, s=-1.0, xdata=xdata)
        #ydata = UIUtils.pz_bxy_scan(B=xdata, B01=100, B02=1000, B03=0, T_long=2.5*0.002, T_trans=0.002, Rp=1./(2*0.002), Rprb=1./(4*0.002), gamma=2.2, s=-1.0)
        ydata = UIUtils.func_scan(B=xdata, B01=0, B02=100, B03=-100, T1=2.5*0.002, T2=0.002, Rp=1./(2*0.002), Rpr=1./(4*0.002), gamma=2.2, s=-1)
        #self.gui.plot.plot(xdata, ydata, pen=(0,0,255))

        # create a set of Parameters
        # 'value' is the initial condition
        # 'min' and 'max' define your boundaries
        params = Parameters()
        params.add('B01', value= 0.0, vary=True, min=-10., max=300.)
        params.add('B02', value= 0.0, vary=True, min=-10., max=300.)
        params.add('B03', value= 0.0, vary=True, min=-300., max=300.)
        params.add('T_long', value= 2.5*0.002, vary=False, min=0, max=1.0)
        params.add('T_trans', value= 0.002, vary=False, min=0, max=1.0)
        params.add('Rp', value= 250.0, vary=False, min=0.001, max=500)
        params.add('Rprb', value= 125.0, vary=False, min=0.001, max=500)
        params.add('off', value=0.0, min=0.0, max = 0.5)

        # do fit
        result = minimize(UIUtils.fit2, params, args=(xdata, ydata), method='nelder')

        #rp = result.values['B01'], result.values['B02'], result.values['B03'], result.values['T_long'], result.values['T_trans'], result.values['Rp'], result.values['Rprb']
        # write error report
        print(fit_report(result))
        #print(result.residual)
        xplot = np.linspace(min(xdata), max(xdata), 1000)
        final = ydata + result.residual
        try:
            self.gui.plot.plot(xdata, ydata, pen=(0,0,255), symbol='o')
            self.gui.plot.plot(xdata, final, pen=(0,255,0))
        except:
            print('fit not successful')
            pass


        #print(*params)
        #print(result.values['B01'])
        print(final)



    # def fit(self):
    #     xdata = np.linspace(-30000.0, 30000.0, num=50)
    #     ydata = 1*xdata+np.random.uniform(-5000.0,5000.0, size=len(xdata))
    #     self.gui.plot.plot(xdata, ydata, pen=None, symbol='o')
    #     def func(x,a,b):
    #         return a*x+b
    #     popt, pcov = curve_fit(func, xdata, ydata)
    #     self.gui.plot.plot(xdata, func(xdata, *popt))

# User Interface Utils
class UIUtils():
    gui = None

    def __init__(self, gui):
        UIUtils.gui = gui

    def pz_bxy_scan(B, B01, B02, B03, T_long, T_trans, Rp, Rprb, gamma, s):
        pz = (Rp*s*(Rp+Rprb+1./T_trans)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)-((-B-B03)*Rp*s*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma))/gamma)/(-((B01*(B+B02))/gamma**2-((-B-B03)*(Rp+Rprb+1./T_long))/gamma)*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma)+(-(Rp+Rprb+1./T_long)*(Rp+Rprb+1./T_trans)+((-B-B02)*(B+B02))/gamma**2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma))
        return pz

    def func_scan(B, B01, B02, B03, T1, T2, Rp, Rpr, gamma, s):
        return (Rp*s*(Rp+Rpr+1./T2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rpr+1./T2))/gamma)-((-B-B03)*Rp*s*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rpr+1./T2))/gamma))/gamma)/(-((B01*(B+B02))/gamma**2-((-B-B03)*(Rp+Rpr+1./T1))/gamma)*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rpr+1./T2))/gamma)+(-(Rp+Rpr+1./T1)*(Rp+Rpr+1./T2)+((-B-B02)*(B+B02))/gamma**2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rpr+1./T2))/gamma))

    def pz_bxy_scan_data(B, B01, B02, B03, T_long, T_trans, Rp, Rprb, gamma, s, xdata):
        pz = (Rp*s*(Rp+Rprb+1./T_trans)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)-((-B-B03)*Rp*s*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma))/gamma)/(-((B01*(B+B02))/gamma**2-((-B-B03)*(Rp+Rprb+1./T_long))/gamma)*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma)+(-(Rp+Rprb+1./T_long)*(Rp+Rprb+1./T_trans)+((-B-B02)*(B+B02))/gamma**2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)) + np.random.uniform(-0.005,0.005, size=len(xdata))
        return pz

    def data(B, B01, B02, B03, T_long, T_trans, Rp, Rprb, xdata):
        gamma = 2.2
        s = -1
        return (Rp*s*(Rp+Rprb+1./T_trans)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)-((-B-B03)*Rp*s*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma))/gamma)/(-((B01*(B+B02))/gamma**2-((-B-B03)*(Rp+Rprb+1./T_long))/gamma)*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma)+(-(Rp+Rprb+1./T_long)*(Rp+Rprb+1./T_trans)+((-B-B02)*(B+B02))/gamma**2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)) + np.random.uniform(-0.005,0.005, size=len(xdata))

    def fit(B, B01, B02, B03, T_long, T_trans, Rp, Rprb):
        gamma=2.2
        s=-1
        y = (Rp*s*(Rp+Rprb+1./T_trans)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)-((-B-B03)*Rp*s*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma))/gamma)/(-((B01*(B+B02))/gamma**2-((-B-B03)*(Rp+Rprb+1./T_long))/gamma)*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma)+(-(Rp+Rprb+1./T_long)*(Rp+Rprb+1./T_trans)+((-B-B02)*(B+B02))/gamma**2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma))
        return y

    def fit2(params, B, data):
        B01 = params['B01'].value
        B02 = params['B02'].value
        B03 = params['B03'].value
        T_long = params['T_long'].value
        T_trans = params['T_trans'].value
        Rp = params['Rp'].value
        Rprb = params['Rprb'].value
        off = params['off'].value
        gamma=2.2
        s=-1
        model = (Rp*s*(Rp+Rprb+1./T_trans)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)-((-B-B03)*Rp*s*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma))/gamma)/(-((B01*(B+B02))/gamma**2-((-B-B03)*(Rp+Rprb+1./T_long))/gamma)*(((B+B02)*(B+B03))/gamma**2+(B01*(Rp+Rprb+1./T_trans))/gamma)+(-(Rp+Rprb+1./T_long)*(Rp+Rprb+1./T_trans)+((-B-B02)*(B+B02))/gamma**2)*((B01*(-B-B03))/gamma**2+((B+B02)*(Rp+Rprb+1./T_trans))/gamma)) + off
        return model - data

    # def lmfit(xdata, ydata, method):
    #     # create a set of Parameters
    #     # 'value' is the initial condition
    #     # 'min' and 'max' define your boundaries
    #     params = Parameters()
    #     params.add('B01', value= 0.0, vary=True, min=-10., max=300.)
    #     params.add('B02', value= 0.0, vary=True, min=-10., max=300.)
    #     params.add('B03', value= 0.0, vary=True, min=-300., max=300.)
    #     params.add('T_long', value= 2.5*0.002, vary=False, min=0, max=1.0)
    #     params.add('T_trans', value= 0.002, vary=False, min=0, max=1.0)
    #     params.add('Rp', value= 250.0, vary=False, min=0.001, max=500)
    #     params.add('Rprb', value= 125.0, vary=False, min=0.001, max=500)
    #     params.add('off', value=0.0, min=0.0, max = 0.5)

    #     # do fit
    #     result = minimize(fit2, params, args=(xdata, ydata), method)

    #     #rp = result.values['B01'], result.values['B02'], result.values['B03'], result.values['T_long'], result.values['T_trans'], result.values['Rp'], result.values['Rprb']
        
    #     # write error report
    #     print(fit_report(result))
    #     #print(result.residual)
    #     #xplot = np.linspace(min(xdata), max(xdata), 1000)
    #     final = ydata + result.residual
    #     return final
    #     # try:
    #     #     self.gui.plot.plot(xdata, ydata, pen=(0,0,255), symbol='o')
    #     #     self.gui.plot.plot(xdata, final, pen=(0,255,0))
    #     # except:
    #     #     print('fit not successful')
    #     #     pass


    #     #print(*params)
    #     #print(result.values['B01'])
    #     #print(final)




    


def main():
    app = QtGui.QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon("icon1.png"));
    window = CompensatorGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
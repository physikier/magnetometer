import logging, os

import numpy as np

from utility import GetSetItemsMixin 

from traits.api import HasTraits, Float, Instance, Array, Range, Enum, Bool, on_trait_change, Str, Trait, Int, NO_COMPARE
from traitsui.api import View, VSplit, HSplit,  HGroup, VGroup, Item, TextEditor

from chaco.api import ArrayPlotData, PlotLabel
from chaco_addons import SavePlot as Plot, SaveTool
from enable.api import ComponentEditor

from helpers import find_closest


class FFTAnalyzer(GetSetItemsMixin):
	
	_fft_data = Instance(ArrayPlotData)
	_fft_plot = Instance(Plot(), editor=ComponentEditor())
	_signal_data = Instance(ArrayPlotData)
	_signal_plot = Instance(Plot(), editor=ComponentEditor())

	x = Array(comparison_mode=NO_COMPARE)
	y = Array(comparison_mode=NO_COMPARE)

	frequency = Array(comparison_mode=NO_COMPARE)
	intensity = Array(comparison_mode=NO_COMPARE)

	enable_highpass  = Bool(default_value=True,desc='Do not show DC components.', label='DC filter')
	enable_normalize = Bool(default_value=False,desc='Normalize to max. value', label='Normalization')

	_freq_res_label = Str(label='Freq. res. [?]')

	freq_res = Float(default_value=0., editor=TextEditor(evaluate_name='_freq_res_label'))

	freq_min = Trait( 'auto', Str('auto'), Float(0.), desc='Lower frequency limit in fft plot', editor=TextEditor(auto_set=False, enter_set=True, evaluate=float))
	freq_max = Trait( 'auto', Str('auto'), Float(1.), desc='Upper frequency limit in fft plot', editor=TextEditor(auto_set=False, enter_set=True, evaluate=float))

	_fft_index_min = Int(0)
	_fft_index_max = Int(100)

	_frequency_raw = Array()
	_freq_max_multiplicator = Float(default_value=1.)
 	

 	time_unit = Enum('s','ms','us','ns','ps', label='time unit')
 	_time_unit_multiplier = Float(default_value=1.)
 	
 	frequency_unit = Enum('Hz','kHz','MHz','GHz','THz', label='freq. unit')
 	_frequency_unit_multiplier = Float(default_value=1.)

 	fft_type = Enum('abs', 'real', 'imag', 'phase', label="type") #checkeditor


	def __init__(self, *args, **kwargs):
		super(FFTAnalyzer,self).__init__(**kwargs)
		
		self._select_frequency_unit()

		self._create_signal_data()
		self._create_fft_data()
		self._create_signal_plot()
		
		self._create_fft_plot()



		self.on_trait_change(self._update_fft, 'frequency,intensity,_fft_index_min,_fft_index_max', dispatch='ui')
		self.on_trait_change(self._update_freq_res, 'frequency', dispatch='ui')
		self.on_trait_change(self._update_signal, 'x,y', dispatch='ui')

		self.on_trait_change(self.calc_fft, 'fft_type,y',dispatch='ui')

		self.on_trait_change(self._select_frequency_unit, 'frequency_unit', dispatch='ui')
		self.on_trait_change(self._select_time_unit, 'time_unit', dispatch='ui')

		self.on_trait_change(self.create_plots,'frequency_unit,time_unit',dispatch='ui')
		self.on_trait_change(self._update_freq_max,'frequency_unit,time_unit,x', dispatch='ui')
		self.on_trait_change(self._set_boundary_frequencies,'_freq_max_multiplicator,_frequency_raw', dispatch='ui')

		self.on_trait_change(self._calc_indices, 'freq_min,freq_max,frequency', dispatch='ui')

		self.on_trait_change(self._update_DC_filter,'enable_highpass,_intensity_raw', dispatch='ui')
		self.on_trait_change(self._normalize,'enable_normalize,_intensity_raw', dispatch='ui')

	

 	
	def save_all(self,filename):
		self.save(filename)
		self.fft_plot.save(os.path.splitext(filename)[0]+'_fft.png')
		self.signal_plot.save(os.path.splitext(filename)[0]+'_signal.png')   
 	
	def _set_boundary_frequencies(self):
		self.frequency = self._frequency_raw *self._freq_max_multiplicator

	def _calc_indices(self):
		if self.freq_min == 'auto':
			freq_min = 0.
		else:
			freq_min = self.freq_min
		if self.freq_max == 'auto':
			try:
				freq_max = np.max(self.frequency)
			except: freq_max = 1.
		else:
			freq_max = self.freq_max

		if freq_min > freq_max:
			tmp_max = freq_max
			freq_max = freq_min
			freq_min = tmp_max

		try:
			_fft_index_min =  find_closest(self.frequency, freq_min)
			_fft_index_max =  find_closest(self.frequency, freq_max)+1

			if _fft_index_max >= len(self.frequency):
				_fft_index_max =  len(self.frequency)-1
			if _fft_index_min <0:
				_fft_index_min = 0					
			if np.abs(_fft_index_min - _fft_index_max) <= 1:
				if _fft_index_max == 0:
					_fft_index_max = 2
				else:
					_fft_index_min -= 2						
			self._fft_index_min = _fft_index_min
			self._fft_index_max = _fft_index_max

		except:
			self._fft_index_min = 0
			self._fft_index_max = len(self.frequency)-1



 	
	def _select_frequency_unit(self):
		if self.frequency_unit == 'Hz':
			self._frequency_unit_multiplier = 1.
		elif self.frequency_unit == 'kHz':
			self._frequency_unit_multiplier = 1e-3
		elif self.frequency_unit == 'MHz':
			self._frequency_unit_multiplier = 1e-6
		elif self.frequency_unit == 'GHz':
			self._frequency_unit_multiplier = 1e-9
		elif self.frequency_unit == 'THz':
			self._frequency_unit_multiplier = 1e-12			
 	
	def _select_time_unit(self):
		if self.time_unit == 's':
			self._time_unit_multiplier = 1.
		elif self.time_unit == 'ms':
			self._time_unit_multiplier = 1e3
		elif self.time_unit == 'us':
			self._time_unit_multiplier = 1e6		
		elif self.time_unit == 'ns':
			self._time_unit_multiplier = 1e9
		elif self.time_unit == 'ps':
			self._time_unit_multiplier = 1e12
 		
	def _update_freq_max(self):
		self._freq_max_multiplicator = len(self.x)/abs(max(self.x)-min(self.x)) * self._frequency_unit_multiplier * self._time_unit_multiplier

	
	def _update_freq_res(self):
		try:
			self.freq_res = np.abs(self.frequency[1]-self.frequency[0])
		except:
			self.freq_res = 0.
 	
	def _update_fft(self):
		self._fft_data.set_data('frequency', self.frequency[self._fft_index_min:self._fft_index_max])
		self._fft_data.set_data('intensity', self.intensity[self._fft_index_min:self._fft_index_max])

	def _update_signal_index(self):
		self._update_freq_max()
 	
	def _update_signal(self):
		self._signal_data.set_data('x', self.x)
		self._signal_data.set_data('y', self.y)
		 	
	def index_to_frequency(self,index):
		if type(index) is int:
			freq = [self.freq[index] / self.unit_multiplier]
		else:
			freq = [self.freq[i]/self.unit_multiplier for i in index]
		return freq


	def calc_fft(self):
		if len(self.y):
			if not len(self.x):
				raise ValueError("x values missing length!")
				return
			if self.fft_type == 'abs':
				fft = np.abs(np.fft.fft(self.y))
				freq = np.fft.fftfreq(len(fft))
					
			elif self.fft_type == 'real':
				fft = np.real(np.fft.fft(self.y))
				freq = np.fft.fftfreq(len(fft)) 
			elif self.fft_type == 'imag':
				fft = np.imag(np.fft.fft(self.y))
				freq = np.fft.fftfreq(len(fft)) 
			elif self.fft_type == 'phase':
				fft = np.angle(np.fft.fft(self.y))
				freq = np.fft.fftfreq(len(fft)) 
			else:
				raise ValueError('No case'+str(self.fft_type)+'in Enum fft_type')


			fft = fft[np.argsort(freq)]
			freq = np.sort(freq)
			self._intensity_raw = fft
			self._frequency_raw = freq

			self._DC_index = find_closest(self._frequency_raw,0.)
			self._DC = self._intensity_raw[self._DC_index]	

			#self._set_boundary_frequencies()
			self._update_DC_filter()
			self._normalize()

	def _update_DC_filter(self):
		if self.enable_highpass:
			self._intensity_raw[self._DC_index] = 0.
		else:
			self._intensity_raw[self._DC_index] = self._DC
		self._normalize()
		self._update_fft()		
 	
	def create_plots(self):
		self._create_fft_plot()
		self._create_signal_plot()

	def _create_fft_data(self):
		self._fft_data = ArrayPlotData(frequency=np.array((0.,1.)), intensity=np.array((0.,0.)))
 	
	def _create_fft_plot(self):
		fft_plot = Plot(self._fft_data, padding=8, padding_left=64, padding_bottom=32)
		fft_plot.plot(('frequency','intensity'), style='line', color='blue')
		fft_plot.index_axis.title = 'frequency ['+self.frequency_unit+']'
		fft_plot.value_axis.title = 'intensity'
		fft_plot.tools.append(SaveTool(fft_plot))
		self._fft_plot = fft_plot

	def _create_signal_data(self):
		self._signal_data = ArrayPlotData(x=np.array((0.,1.)), y=np.array((0.,0.))) 

 			
	def _create_signal_plot(self):
		signal_plot = Plot(self._signal_data, padding=8, padding_left=64, padding_bottom=32)
		signal_plot.plot(('x','y'), style='line', color='blue', line_with=1.1)
		signal_plot.index_axis.title = 'time ['+self.time_unit+']'
		signal_plot.value_axis.title = 'signal'
		signal_plot.tools.append(SaveTool(signal_plot))
		self._signal_plot = signal_plot
	get_set_items = ['x','y','frequency','intensity','time_unit','frequency_unit']


	def _normalize(self):
		self.__normalization = np.max(self._intensity_raw)
		if self.enable_normalize:
			self.intensity = self._intensity_raw/self.__normalization
		else:
			self.intensity = self._intensity_raw
		



class FFTAnalyzerUI(FFTAnalyzer):

	traits_view = View(
		VGroup(
			HSplit(
				VSplit(
					HGroup(
						VGroup(
							HGroup(
								Item('_signal_plot', style='custom', show_label=False),
								),
							label='Signal',
							),
						),
					HGroup(
						VGroup(
							HGroup(
								Item('_fft_plot', style='custom', show_label=False, width=820),
								),
							HGroup(
								Item('fft_type'),
								Item('frequency_unit'),
								Item('time_unit'),
								Item('enable_highpass'),
								Item('enable_normalize'),
								Item('freq_min'),
								Item('freq_max'),
								Item('freq_res',style='readonly'),
								),
							label='FFT',	
							),					
						),
					),
				),
			),
			title='FFT Analyzer', 
			resizable=True,
			height=700,
			width=1000,
		)



if __name__ == '__main__':
	fft_analyzer = FFTAnalyzerUI()
	fft_analyzer.configure_traits()
	fft_analyzer.x = np.linspace(0.,200.,1e3)
	fft_analyzer.y = 3*np.sin(np.linspace(0.,200.,1e3)*np.pi*10)+5*np.random.rand(len(fft_analyzer.x))




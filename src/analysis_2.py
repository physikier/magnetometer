import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import ruamel.yaml


from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def _get_measurement_range_for_output(output_key, output, method):
#         method = output['method']
#         config = output[method]
#         return np.arange(config['start'], config['stop'], config['step'])
    
    method_keys = method.split('.')  # e.g. ['freq_mod', 'span']
    config = output
    # find the method configuration inside the output-config
    for key in method_keys:
        config = config[key]
    return np.arange(config['start'], config['stop'], config['step'])


cell='8'
measno='33'

filename='N:/data/emily/magnetometer_test/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))
files=glob.glob(filename+"/*.csv")
files=sorted(files)


a=np.loadtxt(files[0], delimiter=',')
a_fft=abs(np.fft.rfft(a[:,0]))




config_name = glob.glob(filename+'/config*.yaml')
with open(config_name[0], 'r') as ymlfile:
	cfg = ruamel.yaml.load(ymlfile)

stack = cfg['stack']
meas_ranges = [None] * len(stack)
keys = [None] * len(stack)
outputs = [None] * len(stack)
methods = [None] * len(stack)


for i, stack_entry in enumerate(stack):
    keys[i], method_index = stack_entry.split('.')  # e.g. key='B1', method_index = '0'
    method_index = int(method_index) # index gives the position of the method in the methods array
    outputs[i] = cfg['outputs'][keys[i]]
    methods[i] = outputs[i]['methods'][method_index]
    meas_ranges[i] = _get_measurement_range_for_output(keys[i], outputs[i], methods[i])

b0_amp = cfg['outputs']['B0']['amp']['start']
b1_freq_center = cfg['outputs']['B1']['freq_mod']['center']
b1_freq_span = cfg['outputs']['B1']['freq_mod']['span']['start']



downsampling_factor = cfg['devices']['nidaq']['downsampling_factor']
measurement_time = cfg['devices']['nidaq']['measurement_time_s']
sample_rate = cfg['devices']['nidaq']['sample_rate']

x_axis_label = cfg['outputs'][keys[0]][methods[0]]['label']


data_points = sample_rate*measurement_time/downsampling_factor


data_fft=np.zeros([a_fft.shape[0], a.shape[1]])

for i in range(a.shape[1]):
	#data_fft[:,i]=np.abs(np.fft.rfft(a[:,i]))
	plt.plot()


plt.imshow(data_fft[-1::-1], aspect='auto', interpolation='nearest',
             extent=[meas_ranges[0][0], meas_ranges[0][-1], 0, a_fft.shape[0]], cmap='gnuplot', vmax=40)
plt.xlabel(x_axis_label, fontsize=16)
plt.ylabel('Frequency (Hz)', fontsize=16)
plt.colorbar()
plt.show()
plt.savefig(filename+"/all_together{0:s}_fft.pdf".format(measno))

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
measno='39'

basis = 'N:\\data\\emily\\magnetometer_test\\cell{0:s}\\remote'.format(str(cell))
add = "\\offset_coils_adjust\\b0_sweep_lockin"
measurement = "\\meas{}".format(measno)

filename= basis +  measurement

name = filename+"/*.csv"
files = glob.glob(name)

files = sorted(files)



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

y_axis_label = cfg['outputs'][keys[0]][methods[0]]['label']
data_points = sample_rate*measurement_time/downsampling_factor

for i in range(len(files)):
    data = np.loadtxt(files[i], delimiter=',')
    if "-.csv" in files[i]:
        if cfg['outputs']['B0']['active'] is True and cfg['outputs']['B0']['func'].upper() in ['RAMP']:
            x_axis_label = cfg['outputs']['B0']['amp']['label']
            x_axis = np.linspace(b0_amp/2, -b0_amp/2,  
                                 num=len(data[data_points/4:data_points/4*3,:]))         
            # X,Y = np.meshgrid(meas_ranges[0], y_axis)
            # plt.pcolor(X,Y, data[data_points/4:data_points/4*3,:], cmap="gnuplot")
            # plt.axis([X.min(), X.max(), Y.min(), Y.max()])
            plt.imshow(np.transpose(data[data_points/4:data_points/4*3:,-1::-1]), aspect='auto', interpolation='nearest',
             extent=[x_axis[-1], x_axis[0], meas_ranges[0][0]*1000,meas_ranges[0][-1]*1000], cmap='gnuplot')
            plt.xlabel('$B_0$ voltage (V)', fontsize=22)
            plt.ylabel('R$_4$ offset (mV)', fontsize=22)
            plt.tick_params(axis='both', which='major', labelsize=22)
            plt.colorbar()
            plt.savefig(filename+"/all_together{0:s}_raw_b0_basis.png".format(measno), dpi=200, bbox_inches='tight')
            plt.savefig(filename+"/all_together{0:s}_raw_b0_basis.pdf".format(measno), dpi=200)
            plt.clf()
        if cfg['outputs']['B1']['active'] is True and cfg['outputs']['B1']['freq_mod']['active'] is True:
            y_axis_label = cfg['outputs']['B1']['freq_mod']['span']['label']
            y_axis = np.linspace(b1_freq_center - b1_freq_span/2, b1_freq_center + b1_freq_span/2,  
                                 num=len(data[0:data_points/2,:]))
            # X,Y = np.meshgrid(meas_ranges[0], y_axis)
            # plt.pcolor(X,Y, data[0:data_points/2,:], cmap="gnuplot")
            plt.imshow( data[0:data_points/2,:], aspect='auto', interpolation='nearest',
             extent=[meas_ranges[0][0],meas_ranges[0][-1], y_axis[0], y_axis[-1]], cmap='gnuplot')
            # plt.axis([X.min(), X.max(), Y.min(), Y.max()])
            plt.xlabel(x_axis_label, fontsize=22)
            plt.ylabel(y_axis_label, fontsize=22)
            plt.colorbar()
            plt.tick_params(axis='both', which='major', labelsize=22)
            #plt.show()
            plt.savefig(filename+"/all_together{0:s}_raw_b1_basis.png".format(measno))
            plt.savefig(filename+"/all_together{0:s}_raw_b1_basis.pfd".format(measno))
            plt.clf()
        else: 
            y_axis = np.linspace(0, measurement_time, num=sample_rate/downsampling_factor*measurement_time)
            y_axis_label = 'time (s)'
            # X,Y = np.meshgrid(meas_ranges[0], y_axis)
            # plt.pcolor(X,Y, data, cmap="gnuplot")
            plt.imshow( data[-1::-1], aspect='auto', interpolation='nearest',
             extent=[meas_ranges[0][0],meas_ranges[0][-1], y_axis[0], y_axis[-1]], cmap='gnuplot')
            # plt.axis([X.min(), X.max(), Y.min(), Y.max()])
            plt.xlabel(x_axis_label, fontsize=22)
            plt.ylabel(y_axis_label, fontsize=22)
            plt.tick_params(axis='both', which='major', labelsize=22)
            plt.colorbar()
            #plt.show()
            plt.savefig(filename+"/all_together{0:s}_raw.png".format(measno))
            plt.savefig(filename+"/all_together{0:s}_raw.pdf".format(measno))
            plt.clf()

  #   if 'fft.csv' in files[i]:
		# y_axis = np.linspace(0, sample_rate/downsampling_factor/2, num=len(data[:,0]))
		# y_axis_label = 'frequency (Hz)'
		# X,Y = np.meshgrid(meas_ranges[0], y_axis)
		# # #z_min=data[110:].min()
		# # #z_max=0.5
		# # #plt.pcolor(X,Y, data, cmap="gnuplot", vmax=z_max, vmin=z_min)
		# plt.pcolor(X,Y, data, cmap="gnuplot", vmax=10)
		# plt.axis([X.min(), X.max(), Y.min(), Y.max()])
		# plt.xlabel(x_axis_label)
		# plt.ylabel(y_axis_label)
		# plt.colorbar()
		# #plt.show()
		# plt.savefig(filename+"/all_together{0:s}_fft.png".format(measno))
		# plt.clf()


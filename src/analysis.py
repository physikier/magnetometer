import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import ruamel.yaml
import matplotlib.colors as colors
import matplotlib.cm as cmx


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



def color_generator(N, colormap='gnuplot'):
    """ Color generator for a given matplotlib colormap.
    
    Usage:
    ------------------------------------------
    import matplotlib.pylab as plt
    import matplotlib.cm as cmx
    import matplotlib.colors as colors
    
    N = 20
    color_gen = color_generator(N)
    for i in N:
        color = next(color_gen)
        # do something with the color ...
    """
    
    
    cm_map = plt.get_cmap(colormap)
    c_norm  = colors.Normalize(vmin=0, vmax=N)
    scalar_map = cmx.ScalarMappable(norm=c_norm, cmap=cm_map)
    for i in xrange(N):
        yield scalar_map.to_rgba(i)


cell='4'
measno='3'

filename='N:/data/emily/magnetometer_test/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))
files=glob.glob(filename+"/*.csv")
files=sorted(files)

start=100
steps=100

a=np.loadtxt(files[0], delimiter=',')
a_fft=np.abs(np.fft.rfft(a, axis=0))
b=np.sum(a_fft[start::steps,:], axis=1)

color_gen = color_generator(len(b))


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


datanew=np.zeros([len(b), len(files)])
plt.clf()
# for j in range(len(b)-1):
#     #if j!=9: continue
#     color = next(color_gen)
#     plt.plot(a_fft[:,j], label=str(meas_ranges[1][j]), color=color)
#     plt.title("$B_1$ frequency (Hz)",  fontsize=16)
#     plt.ylabel("FFT signal (a.u).", fontsize=16)
#     plt.xlabel("Frequency (Hz)", fontsize=16)
#     plt.ylim((0,8))
#     plt.legend(ncol=3,  prop={'size':10})
# plt.show()
# plt.savefig(filename+"/fft_0mV_{}.png".format(measno), dpi=300)
# plt.savefig(filename+"/fft_0mV_{}.pdf".format(measno))
# plt.clf()

# plt.plot(b)
# plt.ylabel("FFT signal a.u.", fontsize=16)
# plt.xlabel("Frequency (Hz)", fontsize=16)
# plt.ylim((0,9))
# plt.savefig(filename+"/fft_sum_0mV_{}.png".format(measno), dpi=300)
# plt.savefig(filename+"/fft_sum_0mV_{}.pdf".format(measno))
# plt.clf()
# raise

for i in range(len(files)):
	data=np.loadtxt(files[i], delimiter=',')
	data_fft=np.abs(np.fft.rfft(data, axis=0))
	datanew[:,i]=np.sum(data_fft[start::steps,:], axis=1)


plt.imshow(datanew[-1::-1], aspect='auto', interpolation='nearest',
             extent=[meas_ranges[0][0]*1000, meas_ranges[0][-1]*1000,  start/1000, data_fft.shape[0]/1000], cmap='gnuplot')
plt.xlabel('R$_4$ offset (mV)', fontsize=20)
plt.ylabel('Frequency (kHz)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.colorbar()
plt.show()
plt.savefig(filename+"/all_together{0:s}_steps{1:s}.png".format(measno, str(steps)), dpi=300)
plt.savefig(filename+"/all_together{0:s}_steps{1:s}.pdf".format(measno, str(steps)))

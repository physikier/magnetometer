import numpy as np
import matplotlib.pyplot as plt
import glob
import matplotlib.colors as colors
import matplotlib.cm as cmx
import ruamel.yaml


from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')



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
measno='37'

filename='N:/data/emily/magnetometer_test/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))

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

key = keys[0]
method=methods[0]


files=glob.glob(filename+"/b0Offset_fft0.050.csv")
data=np.loadtxt('N:\\data\\emily\\magnetometer_test\\cell{0:}\\remote\\meas{1:}\\{2:}-{3:}-.csv'.format(cell, measno, key, method), delimiter=',')


downsampling_factor = cfg['devices']['nidaq']['downsampling_factor']
measurement_time = cfg['devices']['nidaq']['measurement_time_s']
sample_rate = cfg['devices']['nidaq']['sample_rate']

data_points = sample_rate*measurement_time/downsampling_factor

b0_amp = cfg['outputs']['B0']['amp']['start']

title = cfg['outputs'][keys[0]][methods[0]]['label']


color_gen = color_generator(data.shape[1])
plt.clf()

for j in range(data.shape[1]):

    color = next(color_gen)
    plt.plot(np.linspace(b0_amp/2, -b0_amp/2,  
                num=len(data[data_points/4:data_points/4*3,:])),
                data[data_points/4:data_points/4*3,j]+(5-j)*0.004, label=str(meas_ranges[0][j]), linewidth=1, color=color)
    plt.ylabel("Magnetometer output (a.u.)", fontsize=16)
    plt.title(title)
    plt.xlabel(cfg['outputs']['B0']['amp']['label'], fontsize=16)
    plt.legend(ncol=3,  prop={'size':9})

plt.savefig(filename+"/waterfall.pdf",  bbox_inches='tight')
plt.clf()

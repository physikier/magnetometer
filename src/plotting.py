import numpy as np
import matplotlib.pyplot as plt
import glob
import matplotlib.colors as colors
import matplotlib.cm as cmx
import ruamel.yaml

cell='8'
measno='34'



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




filename='N:/data/emily/magnetometer_test/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))
files=glob.glob(filename+"/b0Offset_fft0.050.csv")
data=np.loadtxt('N:\\data\\emily\\magnetometer_test\\cell{0:}\\remote\\meas{1:}\\R2-offset-.csv'.format(cell, measno), delimiter=',')




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


#title = cfg['outputs'][keys[0]][methods[0]]['label']
steps = range(data.shape[1])
color_gen = color_generator(len(steps)+1)

fft=np.zeros([data.shape[0]/2+1, data.shape[1]])

for j in range(data.shape[1]):

	color = next(color_gen)

	fft[:,j]=np.abs(np.fft.rfft(data[:, j]))
	#color = next(color_gen)
	plt.plot(data[:, j], label=str(meas_ranges[0][j]), linewidth=1)
	plt.ylabel("FFT signal a.u.")
	plt.xlabel("Frequency (Hz)")
	plt.legend(ncol=3,  prop={'size':9})
	#plt.yscale('log')
	plt.savefig(filename+"/B0-offset_{0:s}_{1:s}.png".format(measno, str(j)), dpi=200)
    plt.savefig(filename+"/B0-offset_{0:s}_{1:s}.png".format(measno, str(j)), dpi=200)
	plt.show()



# datanew=np.sum(fft[500::500], axis=1)
# plt.plot(np.arange(500, 10500, 500), datanew, color='r', linewidth=2)

	#plt.plot(fft[100:], color=color, label=str(meas_ranges[1][j]), linewidth=2)





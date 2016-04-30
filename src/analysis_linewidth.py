import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import ruamel.yaml
import scipy.optimize as so
import matplotlib.colors as colors
import matplotlib.cm as cmx
from scipy.interpolate import interp1d

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








cell='8'
measno='35'
basis = 'N:\\data\\emily\\magnetometer_test\\cell{0:s}\\remote'.format(str(cell))
add = "\\offset_coils_adjust\\b0_sweep_lockin"
measurement = "\\meas{}".format(measno)
filename= basis + measurement
name = filename+"/*-.csv"

files = glob.glob(name)

files = sorted(files)
 #correction factor of measurement 80

config_name = glob.glob(filename+'\\config*.yaml')
with open(config_name[0], 'r') as ymlfile:
	cfg = ruamel.yaml.load(ymlfile)

stack = cfg['stack']
meas_ranges = [None] * len(stack)
keys = [None] * len(stack)
outputs = [None] * len(stack)
methods = [None] * len(stack)

corr_factor_HzperVolts = 5.328860208969956875e+04

for i, stack_entry in enumerate(stack):
    keys[i], method_index = stack_entry.split('.')  # e.g. key='B1', method_index = '0'
    method_index = int(method_index) # index gives the position of the method in the methods array
    outputs[i] = cfg['outputs'][keys[i]]
    methods[i] = outputs[i]['methods'][method_index]
    meas_ranges[i] = _get_measurement_range_for_output(keys[i], outputs[i], methods[i])

b0_amp = cfg['outputs']['B0']['amp']['start']
b1_freq_center = cfg['outputs']['B1']['freq_mod']['center']
b1_freq_span = cfg['outputs']['B1']['freq_mod']['span']['start']




# hsv=[(1.*l/len(meas_ranges[0]), 1, 0.9+0.1*l/len(meas_ranges[0])) for l in range(len(meas_ranges[0]))]
# rgb=cl.hsv_to_rgb(hsv)

downsampling_factor = cfg['devices']['nidaq']['downsampling_factor']
measurement_time = cfg['devices']['nidaq']['measurement_time_s']
sample_rate = cfg['devices']['nidaq']['sample_rate']

title = cfg['outputs'][keys[0]][methods[0]]['label']
data_points = sample_rate*measurement_time/downsampling_factor

def lorentz(x,a,g,phi,xs,bg):
	return a*((g/2)*np.sin(phi)+(x-xs)*np.cos(phi))/((g/2)**2+(x-xs)**2)+bg

def pseudo_voigt(x, eta, w, xs, bg):
	return eta/(1+((x-xs)/w)**2)+(1-eta)*np.exp(-np.log(2)*((x-xs)/w)**2)+bg # TODO add phi --> ask Ilja

start_meas=2

xstart = 0.0
end_meas = 30
fig = plt.figure()
ax = plt.subplot(111)

steps = range(len(meas_ranges[0][start_meas:end_meas]))
color_gen = color_generator(len(steps))

for i in range(len(files)):
    data = np.loadtxt(files[i], delimiter=',')
    poptsave = np.zeros([data.shape[1], 5])
    np.ma.filled(poptsave, None)
    if cfg['outputs']['B0']['active'] is True and cfg['outputs']['B0']['func'].upper() in ['RAMP']:
        x_axis_label = cfg['outputs']['B0']['amp']['label']
        x_axis = np.linspace(b0_amp/2,  -b0_amp/2,
                             num=len(data[data_points/4:data_points/4*3,:])) 
       
        for j in range(data.shape[1]):
        	if j<start_meas: continue
        	if j>=end_meas: continue
        	#if j!= 30: continue
        	f = interp1d(x_axis, data[data_points/4:data_points/4*3,j])
        	
        	x_axis_trunc = np.linspace(b0_amp/2 - xstart,  0-xstart,
                             num=len(data[data_points/4:data_points/4*2,:]))
        	data_trunc = f(x_axis_trunc)
        	popt, pcov = so.curve_fit(lorentz, x_axis_trunc,
        			data_trunc, p0=[0.0001, 0.001, -0.1, 0.0, -0.0017])
        	color = next(color_gen)
        	ax.plot(x_axis_trunc, data_trunc,  label=str(meas_ranges[0][j]), linewidth='1', color=color)
        	if j==data.shape[1]-end_meas:
        		ax.plot(x_axis_trunc, lorentz(x_axis_trunc, *popt), linewidth='1', linestyle='--', color='k', label='fit')
        	else:
        		ax.plot(x_axis_trunc, lorentz(x_axis_trunc, *popt), linewidth='1', linestyle='--', color='k')
        	poptsave[j,:] = popt
        	
		ax.set_ylabel("Lock in Y output a.u.")
		ax.set_xlabel(x_axis_label)
		ax.set_title(title)

		handles, labels = ax.get_legend_handles_labels()
		lgd = ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5), ncol=4, prop={'size':9})


        fig.savefig(filename+"/all_together{0:s}_fit.pdf".format(measno), 
        	#bbox_extra_artists=(lgd,), 
        	bbox_inches='tight', dpi=300)
        fig.clf()
        np.savetxt(filename+"/popt{0:s}.txt".format(measno), poptsave)
        b0_diffs = np.diff(poptsave[start_meas:end_meas,3])
        my_list = [x for x in b0_diffs if x>0 and x<0.1]
        b0_diff=np.mean(my_list)
        hz_diff=np.mean(np.abs(np.diff(meas_ranges[0])))
    	corr_factor=hz_diff/b0_diff
    	popt_corr=np.abs(poptsave[:,1])*corr_factor


        np.savetxt(filename+"/popt_linewidths_hz{0:s}.txt".format(measno), popt_corr)

        plt.plot(meas_ranges[0][start_meas:end_meas], popt_corr[start_meas:end_meas])
        plt.xlabel(title)
        plt.ylabel('Line widths (Hz)')
        plt.savefig(filename+'/widths.png', dpi=300)

        plt.show()
        plt.clf()
        mean_width_and_std=[ np.mean(popt_corr[start_meas:end_meas]), np.std(popt_corr[start_meas:end_meas])]
        np.savetxt(filename+'/mean_width_and_std.txt', mean_width_and_std)
        plt.scatter(poptsave[start_meas:end_meas, 3], meas_ranges[0][start_meas:end_meas])
        plt.xlabel(title)
        plt.ylabel('Center (Hz)')
        plt.show()
  


    if cfg['outputs']['B1']['active'] is True and cfg['outputs']['B1']['freq_mod']['active'] is True:
        x_axis_label = cfg['outputs']['B1']['freq_mod']['span']['label']
        x_axis = np.linspace(b1_freq_center - b1_freq_span/2, b1_freq_center + b1_freq_span/2,  
                             num=len(data[0:data_points/2,:]))
        for j in range(data.shape[1]):
        	popt, pcov = so.curve_fit(lorentz, x_axis, 
        				data[0:data_points/2,j], p0=[90, 300, 1, 1975, -0.0017])
        	color = next(color_gen)
        	plt.plot(x_axis, data[0:data_points/2,j],  label=str(meas_ranges[0][j]), linewidth='1', color=color)
        	if j==0:
        		plt.plot(x_axis, lorentz(x_axis, *popt), linewidth='1', linestyle='--', color='k', label='fit')
        	else:
        		plt.plot(x_axis, lorentz(x_axis, *popt), linewidth='1', linestyle='--', color='k')

        	poptsave[j,:] = popt 

        plt.ylabel("Lock in Y output a.u.")
        plt.legend(loc='upper right', bbox_to_anchor=(1, 0.5), ncol=4, prop={'size':10})
        plt.xlabel(x_axis_label)
        plt.title(title)
        plt.show()
        plt.savefig(filename+"/all_together{0:s}_fit.png".format(measno))
        plt.clf()
        mean_width_and_std=[ np.mean(poptsave[:,1]), np.std(poptsave[1,:])]
        np.savetxt(filename+'/mean_width_and_std.txt', mean_width_and_std)
        np.savetxt(filename+"/popt{0:s}.txt".format(measno), poptsave)

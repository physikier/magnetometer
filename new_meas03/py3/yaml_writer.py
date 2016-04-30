import ruamel.yaml as yaml


def yaml_writer_hanle(active_B1='false', method_B1='const', freq_start_B1=0, freq_stop_B1=0, freq_step_B1=0, ampl_start_B1=0, ampl_stop_B1=0, ampl_step_B1=0, off_start_B1=0, off_stop_B1=0, off_step_B1=0, active_B0='false', method_B0='const', freq_start_B0=0, freq_stop_B0=0, freq_step_B0=0, ampl_start_B0=0, ampl_stop_B0=0, ampl_step_B0=0, off_start_B0=0, off_stop_B0=0, off_step_B0=0, samples=200000., meas_time=1., downsampling=100., cell=0, measurement=0, temp=0, power=0, diode_gain=0):

    output_file = 'config_hanle.yaml'
    open(output_file, 'w+')

    fname = "raw.yaml"
    stream = open(fname, 'r')
    data = yaml.load(stream, Loader=yaml.RoundTripLoader)

    #B1 Field
    data['outputs']['B1']['active'] = active_B1 # true/false
    data['outputs']['B1']['methods'] = method_B1
    data['outputs']['B1']['freq']['start'] = freq_start_B1
    data['outputs']['B1']['freq']['stop'] = freq_stop_B1
    data['outputs']['B1']['freq']['step'] = freq_step_B1
    data['outputs']['B1']['amp']['start'] = ampl_start_B1
    data['outputs']['B1']['amp']['stop'] = ampl_stop_B1
    data['outputs']['B1']['amp']['step'] = ampl_step_B1
    data['outputs']['B1']['offset']['start'] = off_start_B1
    data['outputs']['B1']['offset']['stop'] = off_stop_B1
    data['outputs']['B1']['offset']['step'] = off_step_B1

    #B0 Field
    data['outputs']['B0']['active'] = active_B0 #true/false
    data['outputs']['B0']['methods'] = method_B0
    data['outputs']['B0']['freq']['start'] = freq_start_B0
    data['outputs']['B0']['freq']['stop'] = freq_stop_B0
    data['outputs']['B0']['freq']['step'] = freq_step_B0
    data['outputs']['B0']['amp']['start'] = ampl_start_B0
    data['outputs']['B0']['amp']['stop'] = ampl_stop_B0
    data['outputs']['B0']['amp']['step'] = ampl_step_B0
    data['outputs']['B0']['offset']['start'] =off_start_B0
    data['outputs']['B0']['offset']['stop'] = off_stop_B0
    data['outputs']['B0']['offset']['step'] = off_step_B0

    #Compensation Fields
    data['outputs']['R2']['active'] = 'true'
    data['outputs']['R3']['active'] = 'true'
    data['outputs']['R4']['active'] = 'true'
    data['outputs']['lock_in']['active'] = 'false'
    data['outputs']['motor']['active'] = 'false'

    #DAQ properities
    data['devices']['nidaq']['sample_rate'] = samples
    data['devices']['nidaq']['measurement_time_s'] = meas_time
    data['devices']['nidaq']['downsampling_factor'] = downsampling

    #Global mesurement parameters
    data['measurement']['cell_id'] = cell
    data['measurement']['measurement_id'] = measurement
    data['measurement']['temperature_C'] = temp
    data['measurement']['laser_power_uW'] = power
    data['measurement']['photo_diode_gain_dB'] = diode_gain


    with open(output_file, 'w') as yaml_file:
        yaml_file.write( yaml.dump(data, Dumper=yaml.RoundTripDumper, indent=4))
    
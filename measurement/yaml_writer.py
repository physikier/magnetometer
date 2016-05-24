import ruamel.yaml as yaml
from ruamel.yaml.comments import CommentedSeq

class YamlConfigHandler(object):
    measurement_nr = None
    yaml_data = None
    config_file_path = None
    data = {
        'active_B1' : None,
        'method_B1' : None,
        'freq_start_B1' : None,
        'freq_stop_B1' : None,
        'freq_step_B1' : None,
        'ampl_start_B1' : None,
        'ampl_stop_B1' : None,
        'ampl_step_B1' : None,
        'off_start_B1' : None,
        'off_stop_B1' : None,
        'off_step_B1' : None,
        'active_B0' : None,
        'method_B0' : None,
        'freq_start_B0' : None,
        'freq_stop_B0' : None,
        'freq_step_B0' : None,
        'ampl_start_B0' : None,
        'ampl_stop_B0' : None,
        'ampl_step_B0' : None,
        'off_start_B0' : None,
        'off_stop_B0' : None,
        'off_step_B0' : None,
        'samples' : None,
        'meas_time' : None,
        'downsampling' : None,
        'cell' : None,
        'temp' : None,
        'power' : None,
        'diode_gain' : None
    }

    # to instantiate a YamlHandler object you have to pass
    #   measurement number (to identify the YamlHandler) and
    #   config file (path to config file; default is the raw.yaml)
    # to the new instance
    def __init__(self, measurement_nr, load_config_file="raw.yaml"):
        self.measurement_nr = measurement_nr
        self.load_data_from_config(load_config_file)
        self.yaml_data['measurement']['measurement_id'] = measurement_nr
        # the values in the raw.yaml mustn't be changed so the data are saved to a temporary config file
        self.config_file_path = 'C:\\Users\\johnny\\dev\\magnetometer\\measurement\\configs\\config-' + str(measurement_nr) + '.yaml'

    # this method loads all data from the 'load_config_file' into the data dictionary to keep the config in memory
    def load_data_from_config(self, load_config_file):
        stream = open(load_config_file, 'r')
        self.yaml_data = yaml.load(stream, Loader=yaml.RoundTripLoader)
        stream.close()

    # this function saves the values from the data dictionary back to the data_yaml dictionary
    def write_data_to_config(self):
        self.yaml_data['outputs']['B1']['active']                 = self.data['active_B1']
        self.yaml_data['outputs']['B1']['methods']                = CommentedSeq([self.data['method_B1']])
        self.yaml_data['outputs']['B1']['freq']['start']          = self.data['freq_start_B1']
        self.yaml_data['outputs']['B1']['freq']['stop']           = self.data['freq_stop_B1']
        self.yaml_data['outputs']['B1']['freq']['step']           = self.data['freq_step_B1']
        self.yaml_data['outputs']['B1']['amp']['start']           = self.data['ampl_start_B1']
        self.yaml_data['outputs']['B1']['amp']['stop']            = self.data['ampl_stop_B1']
        self.yaml_data['outputs']['B1']['amp']['step']            = self.data['ampl_step_B1']
        self.yaml_data['outputs']['B1']['offset']['start']        = self.data['off_start_B1']
        self.yaml_data['outputs']['B1']['offset']['stop']         = self.data['off_stop_B1']
        self.yaml_data['outputs']['B1']['offset']['step']         = self.data['off_step_B1']
        self.yaml_data['outputs']['B0']['active']                 = self.data['active_B0']
        self.yaml_data['outputs']['B0']['methods']                = CommentedSeq([self.data['method_B0']])
        self.yaml_data['outputs']['B0']['freq']['start']          = self.data['freq_start_B0']
        self.yaml_data['outputs']['B0']['freq']['stop']           = self.data['freq_stop_B0']
        self.yaml_data['outputs']['B0']['freq']['step']           = self.data['freq_step_B0']
        self.yaml_data['outputs']['B0']['amp']['start']           = self.data['ampl_start_B0']
        self.yaml_data['outputs']['B0']['amp']['stop']            = self.data['ampl_stop_B0']
        self.yaml_data['outputs']['B0']['amp']['step']            = self.data['ampl_step_B0']
        self.yaml_data['outputs']['B0']['offset']['start']        = self.data['off_start_B0']
        self.yaml_data['outputs']['B0']['offset']['stop']         = self.data['off_stop_B0']
        self.yaml_data['outputs']['B0']['offset']['step']         = self.data['off_step_B0']
        self.yaml_data['devices']['nidaq']['sample_rate']         = self.data['samples']
        self.yaml_data['devices']['nidaq']['measurement_time_s']  = self.data['meas_time']
        self.yaml_data['devices']['nidaq']['downsampling_factor'] = self.data['downsampling']
        self.yaml_data['measurement']['cell_id']                  = self.data['cell']
        self.yaml_data['measurement']['temperature_C']            = self.data['temp']
        self.yaml_data['measurement']['laser_power_uW']           = self.data['power']
        self.yaml_data['measurement']['photo_diode_gain_dB']      = self.data['diode_gain']
        self.yaml_data['outputs']['R2']['active']                 = True
        self.yaml_data['outputs']['R3']['active']                 = 'true'
        self.yaml_data['outputs']['R4']['active']                 = 'true'
        self.yaml_data['outputs']['lock_in']['active']            = False
        self.yaml_data['outputs']['motor']['active']              = 'false'

        with open(self.config_file_path, 'w') as yaml_config:
            yaml_config.write( yaml.dump(self.yaml_data, Dumper=yaml.RoundTripDumper, indent=4))

    # call this function from the ui when you want to save changes to the config file
    def write_hanle_config(self, **kwargs):
        try:
            for argument in kwargs.keys():
                if argument not in self.data.keys():
                    raise Exception('The argument ' + argument + ' cannot be handled from the YamlHandler! It seems to be invalid.')
        except Exception as error:
            print('Error: ' + repr(error))

        for arg, value in kwargs.items():
            self.data[arg] = value

        self.write_data_to_config()

    def delete_config_files(self):
        from glob import glob
        from os import remove, chdir
        chdir('C:\\Users\\johnny\\dev\\magnetometer\\measurement\\configs')
        filelist = glob('*.yaml')
        for f in filelist:
            remove(f)


# self.data = {
# 'active_B1' : yaml_data['outputs']['B1']['active'],
# 'method_B1' : yaml_data['outputs']['B1']['methods'],
# 'freq_start_B1' : yaml_data['outputs']['B1']['freq']['start'],
# 'freq_stop_B1' : yaml_data['outputs']['B1']['freq']['stop'],
# 'freq_step_B1' : yaml_data['outputs']['B1']['freq']['step'],
# 'ampl_start_B1' : yaml_data['outputs']['B1']['amp']['start'],
# 'ampl_stop_B1' : yaml_data['outputs']['B1']['amp']['stop'],
# 'ampl_step_B1' : yaml_data['outputs']['B1']['amp']['step'],
# 'off_start_B1' : yaml_data['outputs']['B1']['offset']['start'],
# 'off_stop_B1' : yaml_data['outputs']['B1']['offset']['stop'],
# 'off_step_B1' : yaml_data['outputs']['B1']['offset']['step'],
# 'active_B0' : yaml_data['outputs']['B0']['active'],
# 'method_B0' : yaml_data['outputs']['B0']['methods'],
# 'freq_start_B0' : yaml_data['outputs']['B0']['freq']['start'],
# 'freq_stop_B0' : yaml_data['outputs']['B0']['freq']['stop'],
# 'freq_step_B0' : yaml_data['outputs']['B0']['freq']['step'],
# 'ampl_start_B0' : yaml_data['outputs']['B0']['amp']['start'],
# 'ampl_stop_B0' : yaml_data['outputs']['B0']['amp']['stop'],
# 'ampl_step_B0' : yaml_data['outputs']['B0']['amp']['step'],
# 'off_start_B0' : yaml_data['outputs']['B0']['offset']['start'],
# 'off_stop_B0' : yaml_data['outputs']['B0']['offset']['stop'],
# 'off_step_B0' : yaml_data['outputs']['B0']['offset']['step'],
# 'samples' : yaml_data['devices']['nidaq']['sample_rate'],
# 'meas_time' : yaml_data['devices']['nidaq']['measurement_time_s'],
# 'downsampling' : yaml_data['devices']['nidaq']['downsampling_factor'],
# 'cell' : yaml_data['measurement']['cell_id'],
# 'temp' : yaml_data['measurement']['temperature_C'],
# 'power' : yaml_data['measurement']['laser_power_uW'],
# 'diode_gain' : yaml_data['measurement']['photo_diode_gain_dB'],
# }

# def write_hanle_config(self, active_B1=None, method_B1=None, freq_start_B1=None, freq_stop_B1=None, freq_step_B1=None, ampl_start_B1=None, ampl_stop_B1=None, ampl_step_B1=None, off_start_B1=None, off_stop_B1=None, off_step_B1=None, active_B0=None, method_B0=None, freq_start_B0=None, freq_stop_B0=None, freq_step_B0=None, ampl_start_B0=None, ampl_stop_B0=None, ampl_step_B0=None, off_start_B0=None, off_stop_B0=None, off_step_B0=None, samples=None, meas_time=None, downsampling=None, cell=None, temp=None, power=None, diode_gain=None):

# #B1 Field
# data['outputs']['B1']['active'] = active_B1 # true/false
# data['outputs']['B1']['methods'] = method_B1
# data['outputs']['B1']['freq']['start'] = freq_start_B1
# data['outputs']['B1']['freq']['stop'] = freq_stop_B1
# data['outputs']['B1']['freq']['step'] = freq_step_B1
# data['outputs']['B1']['amp']['start'] = ampl_start_B1
# data['outputs']['B1']['amp']['stop'] = ampl_stop_B1
# data['outputs']['B1']['amp']['step'] = ampl_step_B1
# data['outputs']['B1']['offset']['start'] = off_start_B1
# data['outputs']['B1']['offset']['stop'] = off_stop_B1
# data['outputs']['B1']['offset']['step'] = off_step_B1


# #B0 Field
# data['outputs']['B0']['active'] = active_B0 #true/false
# data['outputs']['B0']['methods'] = method_B0
# data['outputs']['B0']['freq']['start'] = freq_start_B0
# data['outputs']['B0']['freq']['stop'] = freq_stop_B0
# data['outputs']['B0']['freq']['step'] = freq_step_B0
# data['outputs']['B0']['amp']['start'] = ampl_start_B0
# data['outputs']['B0']['amp']['stop'] = ampl_stop_B0
# data['outputs']['B0']['amp']['step'] = ampl_step_B0
# data['outputs']['B0']['offset']['start'] =off_start_B0
# data['outputs']['B0']['offset']['stop'] = off_stop_B0
# data['outputs']['B0']['offset']['step'] = off_step_B0

# #Compensation Fields
# data['outputs']['R2']['active'] = 'true'
# data['outputs']['R3']['active'] = 'true'
# data['outputs']['R4']['active'] = 'true'
# data['outputs']['lock_in']['active'] = 'false'
# data['outputs']['motor']['active'] = 'false'

# #DAQ properities
# data['devices']['nidaq']['sample_rate'] = samples
# data['devices']['nidaq']['measurement_time_s'] = meas_time
# data['devices']['nidaq']['downsampling_factor'] = downsampling

# #Global mesurement parameters
# data['measurement']['cell_id'] = cell
# data['measurement']['measurement_id'] = self.measurement_nr
# data['measurement']['temperature_C'] = temp
# data['measurement']['laser_power_uW'] = power
# data['measurement']['photo_diode_gain_dB'] = diode_gain
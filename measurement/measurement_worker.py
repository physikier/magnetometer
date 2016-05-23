import os
import numpy as np
import matplotlib.pyplot as plt
import shutil
import pyfits
import time

from threading import Thread
from queue import Queue 


class MeasurementWorker(object):
    TEKTRONIX = 'tektronix'
    HAMEG = 'hameg'
    LOCKIN = 'SR830'
    MOTOR = 'motor_driver'
    
    def __init__(self, config=None, nidaq=None, tektronix=None, hameg=None, lock_in=None, motor=None, logger=None):
        # if nidaq is None or tektronix is None or hameg is None or lock_in is None or motor is None:
        #     raise RuntimeError("MeasurementWorker must be called with instances of nidaq, tektronix, hameg, motor and Lock-in")
        if nidaq is None or tektronix is None or hameg is None or motor is None:
            raise RuntimeError("MeasurementWorker must be called with instances of nidaq, tektronix, hameg, motor and Lock-in")
        self.logger = logger

        self._nidaq = nidaq
        self._tektronix = tektronix
        self._hameg = hameg
        #self._lock_in = lock_in
        self._motor = motor
        
        self._config = config
        self._cell_id = None  # identifier of the cell in this measurement
        self._measurement_id = None  # unique id of the measurement
        self._filepath = b''
        
        self._measurement = None
        
    def __str__(self):
        return "cell: {}, measurement: {}".format(self._cell_id, self._measurement_id)
    
    def set_base_path(self, path):
        # TODO: test if path exists and create any subfolders
        self._filepath = os.path.join(
            path, 'cell{}'.format(self._cell_id), 'remote', 'meas{}'.format(self._measurement_id))
        if os.path.exists(self._filepath):
            # shutil.rmtree(self._filepath)
            raise RuntimeError("The folder '{}' already exists. Aborting.".format(self._filepath))    
    
    def get_filepath(self):
        return self._filepath
    
    def set_config(self, config):
        self._config = config
        measurement = config['measurement']
        
        self._cell_id = measurement['cell_id']
        self._measurement_id = measurement['measurement_id']
        
    def _get_measurement_range_for_output(self, output_key, output, method):
#         method = output['method']
#         config = output[method]
#         return np.arange(config['start'], config['stop'], config['step'])
        
        method_keys = method.split('.')  # e.g. ['freq_mod', 'span']
        config = output
        # find the method configuration inside the output-config
        for key in method_keys:
            config = config[key]
        return np.arange(config['start'], config['stop'] + config['step'], config['step'])
    
    def _base_config_tektronix(self, output):
        """ Basic configuration for every TEKTRONIX device.
        """
        channel = output['channel']
        
        self._tektronix.set_waveform(output['func'].upper(), ch=channel)
        self._tektronix.set_freq(output['freq']['start'], ch=channel)
        self._tektronix.set_amp(output['amp']['start'], ch=channel)
        self._tektronix.set_offset(output['offset']['start'], ch=channel)

        # default modes
        self._tektronix.set_frequency_mode('CW', ch=channel)
        self._tektronix.set_FMmod_state('OFF', ch=channel)
        self._tektronix.set_AMmod_state('OFF', ch=channel)
        self._tektronix.burst_state('OFF', ch=channel)
        #

        # frequency modulation
        if 'freq_mod' in output and output['freq_mod']['active'] is True:
            freq_mod = output['freq_mod']

            self._tektronix.set_sweep_mode('MAN', ch=channel)
            self._tektronix.set_frequency_mode('SWE', ch=channel)

            self._tektronix.set_frequency_sweep_span(freq_mod['span']['start'], ch=channel)
            self._tektronix.set_center_frequency(freq_mod['center'], ch=channel)
            self._tektronix.set_sweep_time(freq_mod['sweep_time']['start'], ch=channel)
            self._tektronix.set_sweep_rtime(freq_mod['return_time']['start'], ch=channel)
            self._tektronix.set_sweep_htime(freq_mod['hold_time'], ch=channel)
            self._tektronix.set_sweep_form(freq_mod['form'].upper(), ch=channel)


        # amplitude modulation
        if 'amp_mod' in output and output['amp_mod']['active'] is True:
            amp_mod = output['amp_mod']

            self._tektronix.set_AMmod_state('ON', ch=channel)
            self._tektronix.set_AMmod_internal('INT', ch=channel)
            self._tektronix.set_AMmod_waveform(amp_mod['waveform'].upper(), ch=channel)
            self._tektronix.set_AMmod_freq(amp_mod['freq']['start'], ch=channel)
            self._tektronix.set_AMmod_depth(amp_mod['depth']['start'], ch=channel)
            
    def _base_config_hameg(self, output):
        """ Basic configuration for every HAMEG device.
        """
        channel = output['channel']
        
        self._hameg.set_max_voltage(max_voltage=5., ch=channel)
        self._hameg.set_max_current(max_current=0.070, ch=channel)
        self._hameg.set_voltage(output['offset']['start'], ch=channel)

    def _base_config_lockin(self, output):
        time = output['time_constant']['start']
        sensi = output['sensitivity']['start']
        slope = output['slope']
        sync = output['sync_filter']
        ground = output['ground']
        filters = output['filters']
        reserve = output['reserve']
        phase = output['phase']['start']
        harmonic = output['harmonic']['start']

        self._lock_in.set_reference_mode(mode=0)
        self._lock_in.set_time_constant(time=time)
        self._lock_in.set_sensitivity(sensi=sensi)
        self._lock_in.set_low_pass_filter(fil=slope)
        self._lock_in.set_sync(sync=sync)
        self._lock_in.set_grounding(grounding=ground)
        self._lock_in.set_filter_status(filters=filters)
        self._lock_in.set_reserve_mode(reserve=reserve)
        self._lock_in.set_phase(phase=phase)
        self._lock_in.set_harmonic(harm=harmonic)

    def _base_config_motor(self, output):
        channel = output['channel']
        position = output['position']['start']

        self._motor.moveToAbsolutePosition(motor=channel, pos=position)
        time.sleep(1)
        while self._motor.isMoving(motor=channel):
            time.sleep(0.5)
        
    def _configure_output(self, key, output, stack):
        device = output['device']
        channel = output['channel']
        
        # power off inactive outputs
        if not output['active']:
            if device == self.TEKTRONIX:
                self._tektronix.stop(ch=channel)
            if device == self.HAMEG:
                self._hameg.stop(ch=channel)
            if device == self.LOCKIN:
                # TODO: disable device
                pass
            if device == self.MOTOR:
                # TODO: disable device
                pass

            # exit function if output is inactive
            return True
        
        # run the base configuration for each output
        if device == self.TEKTRONIX:
            self._base_config_tektronix(output)
        if device == self.HAMEG:
            self._base_config_hameg(output)
        if device == self.LOCKIN:
            self._base_config_lockin(output)
        if device == self.MOTOR:
            self._base_config_motor(output)
            
        # device specific additional settings
        if key == 'B0' and output['func'].upper() == 'RAMP':
            self._tektronix.burst_state('ON', ch=channel)
            self._tektronix.burst_mode('TRIG', ch=channel)
            self._tektronix.burst_cycles(1, ch=channel)
            self._tektronix.trig_source('EXT')
        
        # power on active outputs
        if device == self.TEKTRONIX:
            self._tektronix.run(ch=channel)
        if device == self.HAMEG:
            self._hameg.run(ch=channel)
        if device == self.LOCKIN:
            # TODO: enable device
            pass
        if device == self.MOTOR:
            # TODO: enable device
            pass
            
        return True
    
    def _adjust_output_setting(self, value, key, index):
        output = self._config['outputs'][key]
        device = output['device']
        channel = output['channel']
        method = output['methods'][index]
        
        if device == self.TEKTRONIX:
            if method == 'freq':
                if self.logger is not None:
                    self.logger.info('{}: set freq to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_freq(value, ch=channel)
                return
            elif method == 'amp':
                if self.logger is not None:
                    self.logger.info('{}: set amp to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_amp(value, ch=channel)
                return
            elif method == 'offset':
                if self.logger is not None:
                    self.logger.info('{}: set offset to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_offset(value, ch=channel)
                return
            elif method == 'freq_mod.span':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set freq_mod.span to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_frequency_sweep_span(value, ch=channel)
                return
            elif method == 'freq_mod.sweep_time':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set freq_mod.sweep_time to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_sweep_time(value, ch=channel)
                return
            elif method == 'freq_mod.return_time':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set freq_mod.return_time to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_sweep_rtime(value, ch=channel)
                return
            elif method == 'amp_mod.depth':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set amp_mod.depth to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_AMmod_depth(value, ch=channel)
                return
            elif method == 'amp_mod.freq':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set amp_mod.freq to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._tektronix.set_AMmod_freq(value, ch=channel)
                return
            raise RuntimeException("Method '{}' unknown for device {}".format(method, device))
        elif device == self.HAMEG:
            if method == 'offset':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set offset to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._hameg.set_voltage(value, ch=channel)
                return
            raise RuntimeException("Method '{}' unknown for device {}".format(method, device))
        elif device == self.LOCKIN:
            if method == 'time_constant':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set time constant to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._lock_in.set_time_constant(time=value)
                return
            elif method == 'sensitivity':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set sensitivity to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._lock_in.set_sensitivity(sensi=value)
                return
            elif method == 'phase':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set phase to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._lock_in.set_phase(phase=value)
                return
            elif method == 'harmonic':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set harmonic to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._lock_in.set_harmonic(harm=value)
                return
        elif device == self.MOTOR:
            if method == 'position':
                if self.logger is not None:
                    self.logger.info(
                            '{}: set position to {}. dev: {}, ch: {}'.format(key, value, device, channel))
                self._motor.moveToAbsolutePosition(motor=channel, pos=value)
                time.sleep(1)
                while self._motor.isMoving(motor=channel):
                    time.sleep(1)
                return
        
        raise RuntimeException("Device '{}' unknown".format(device))
            
    def _send_trigger_to_tekronix_if_required(self):
        """ Sends a trigger to the tektronix device if it is needed.
        If a trigger signal is necessary is determined by testing the configuration of the measurement.
        """
        cfg = self._config
        stack = cfg['stack']
        
        def should_send():
            """ Tests if a trigger should be sent, which is the case if output 'B0' is in stack and has method 
            'RAMP', or if 'freq_mod' is active for output 'B1'.
            """
            outputs = cfg['outputs']
            
            if outputs['B0']['active'] is True and outputs['B0']['func'].upper() in ['RAMP']:
                return True
            if outputs['B1']['active'] is True and outputs['B1']['freq_mod']['active'] is True:
                return True

            return False
        
        if should_send():
            # send trigger signal to tektronix device
            self.logger.info('Send trigger signal.')
            self._tektronix.trig()
    
    def measure(self, save=True, config_path=None):
        if self._config is None:
            raise RuntimeError('MeasurementWorker must be configured first')
        
        cfg = self._config
        
        # load stack
        stack = cfg['stack']
        
        # (pre-)configure all outputs
        for key in cfg['outputs'].keys():  # e.g. key='B0'
            output = cfg['outputs'][key]  # get dictionary for output, e.g. 'B0'
            self._configure_output(key, output, stack)
            
        # actively manage the outputs in the stack
        # create the measurement ranges for each entry in the stack
        meas_ranges = [None] * len(stack)
        for i, stack_entry in enumerate(stack):
            key, method_index = stack_entry.split('.')  # e.g. key='B1', method_index = '0'
            method_index = int(method_index) # index gives the position of the method in the methods array
            output = cfg['outputs'][key]
            method = output['methods'][method_index]
            meas_ranges[i] = self._get_measurement_range_for_output(key, output, method)
                
        # create data cubus
#         outputs_in_stack=[{'key': key, 'config': cfg['outputs'][key]} for key in stack]
#         self._measure_rec(meas_ranges, data, max_level=len(stack)-1, outputs=outputs_in_stack)
        
        # create the data arrays that should hold the measurement data
        data = np.zeros([self._nidaq.numberPointsComp] + [x.shape[0] for x in meas_ranges])
        data_fft = np.zeros([self._nidaq.numberPointsComp/2+1] + [x.shape[0] for x in meas_ranges])
        
        self._nidaq.setup_task()

        if save:
            # create dir
            os.makedirs(self.get_filepath())

            # copy config file
            if config_path is not None:
                shutil.copy2(config_path, self.get_filepath())
        
        # perform the actual measurement
        if len(stack) == 2:
            for i, v1 in enumerate(meas_ranges[0]):
                key1, index1 = stack[0].split('.')  # e.g. key1='B1', index1='0'
                index1 = int(index1)  # index1 is a integer value
                self._adjust_output_setting(v1, key1, index1)  # send signal to remote device
                q=Queue()
                for j, v2 in enumerate(meas_ranges[1]):
                    key2, index2 = stack[1].split('.')  # e.g. key2='B2', index2='0'
                    index2 = int(index2)  # index2 is a integer value
                    self._adjust_output_setting(v2, key2, index2)  # send signal to remote device
                    
                    # Some configurations require a trigger signal to be sent to the tektronix device, this MUST
                    # be sent before the measurement takes place.
                    #self._send_trigger_to_tekronix_if_required()
                    
                    # request the data from the nidaq device and perform downsampling
                  
                    get_thread = Thread(target=self._nidaq.get_data, args=[q])
                    get_thread.start()
                    self._nidaq.pulse()
                    get_thread.join()
                    batch=self._nidaq.get_data(q)


                    #batch = self._nidaq.get_data()
                    downsampled_data = self._nidaq.downsampling(batch)
                    
                    data[:, i, j] = downsampled_data
                    data_fft[:, i, j] = np.abs(np.fft.rfft(downsampled_data))
                
                if save:
                    # create generic name, with some variables, which will be used later for saving the data to disk
                    name = "{output:}-{method:}-{value:.3f}{suffix:}.{ending:}".format(
                        output=key1, method=','.join(cfg['outputs'][key1]['methods']), value=v1, 
                        # 'suffix' and 'ending' values will be filled later. This trick allows to use 'format' again
                        # at a later point
                        suffix='{suffix:}', ending='{ending:}' 
                    )

                    # save the measurement to disk
                    np.savetxt(os.path.join(
                            self.get_filepath(), name.format(suffix='', ending='csv')), data[:, i, :], delimiter=',', fmt='%.4e')
                    # np.savetxt(os.path.join(
                    #         self.get_filepath(), name.format(suffix='_fft', ending='csv')), data_fft[:, i, :], delimiter=',', fmt='%.4e')

                    # create plots from measurement data
                    plt.clf()
                    plt.plot(data[:, i, :])

                    plt.savefig(os.path.join(self.get_filepath(), name.format(suffix='', ending='png')))
                    plt.clf()
                    # ATTENTION: we throw away the first 100 values, because in a FFT those values are super large and
                    # the other values are too small to be combined in a single plot.
                    
                    plt.plot(data_fft[100:, i, :]) 
                    plt.savefig(os.path.join(self.get_filepath(), name.format(suffix='_fft', ending='png')))
                    plt.clf()
            
            # hdu = pyfits.PrimaryHDU(data=data)
            # hdu.writeto(os.path.join(
            #                 self.get_filepath(), '{0:}_{1:}.fits'.format(key1, key2)))
                    
        if len(stack) == 1:

            q=Queue()
            for i, v in enumerate(meas_ranges[0]):
                key, index = stack[0].split('.')  # e.g. key2='B2', index2='0'
                index = int(index)  # index2 is a integer value
                self._adjust_output_setting(v, key, index)  # send signal to remote device
                
                get_thread = Thread(target=self._nidaq.get_data, args=[q])
                get_thread.start()
                self._nidaq.pulse()
                get_thread.join()
                batch=self._nidaq.get_data(q)

                
                # # Some configurations require a trigger signal to be sent to the tektronix device, this MUST
                # # be sent before the measurement takes place.
                # self._send_trigger_to_tekronix_if_required()
                
                # # request the data from the nidaq device and perform downsampling
                # batch = self._nidaq.get_data()
                downsampled_data = self._nidaq.downsampling(batch)
                
                data[:, i] = downsampled_data
                data_fft[:, i] = np.abs(np.fft.rfft(downsampled_data))
                
            if save:
                # create generic name, with some variables, which will be used later for saving the data to disk
                name = "{output:}-{method:}-{suffix:}.{ending:}".format(
                    output=key, method=','.join(cfg['outputs'][key]['methods']),
                    # 'suffix' and 'ending' values will be filled later. This trick allows to use 'format' again
                    # at a later point
                    suffix='{suffix:}', ending='{ending:}' 
                )

                # save the measurement to disk
                np.savetxt(os.path.join(
                        self.get_filepath(), name.format(suffix='', ending='csv')), data, delimiter=',', fmt='%.4e')
                # np.savetxt(os.path.join(
                #         self.get_filepath(), name.format(suffix='_fft', ending='csv')), data_fft, delimiter=',', fmt='%.4e')

                # create plots from measurement data
                plt.clf()
                plt.plot(data)

                plt.savefig(os.path.join(self.get_filepath(), name.format(suffix='', ending='png')))
                plt.clf()
                # ATTENTION: we throw away the first 100 values, because in a FFT those values are super large and
                # the other values are too small to be combined in a single plot.
                plt.plot(data_fft[100:]) 
                plt.savefig(os.path.join(self.get_filepath(), name.format(suffix='_fft', ending='png')))
                plt.clf()

        if len(stack) == 0:
            # TODO: implement this
            #raise NotImplemented('Stack with size 1 is not implemented yet.')

            self._send_trigger_to_tekronix_if_required()
                    
                    # request the data from the nidaq device and perform downsampling
            batch = self._nidaq.get_data()
            downsampled_data = self._nidaq.downsampling(batch)
                    
            data = downsampled_data
            data_fft = np.abs(np.fft.rfft(downsampled_data))
                
            if save:
                # create generic name, with some variables, which will be used later for saving the data to disk
                name = "single_mesurement{suffix:}.{ending:}".format(
                    suffix='{suffix:}', ending='{ending:}' 
                )

                # save the measurement to disk
                np.savetxt(os.path.join(
                        self.get_filepath(), name.format(suffix='', ending='csv')), data, delimiter=',', fmt='%.4e')
                np.savetxt(os.path.join(
                        self.get_filepath(), name.format(suffix='_fft', ending='csv')), data_fft, delimiter=',', fmt='%.4e')

                # create plots from measurement data
                plt.clf()
                plt.plot(data)

                plt.savefig(os.path.join(self.get_filepath(), name.format(suffix='', ending='png')))
                plt.clf()
                # ATTENTION: we throw away the first 100 values, because in a FFT those values are super large and
                # the other values are too small to be combined in a single plot.
                plt.plot(data_fft[100:]) 
                plt.savefig(os.path.join(self.get_filepath(), name.format(suffix='_fft', ending='png')))
    
        self._measurement = data
        return data
    
#     def _measure_rec(self, x, data, level=0, max_level=0, outputs=[]):
#         if len(x) == 0:
#             return
#         xnew = copy.copy(x)
#         range_ = xnew.pop()
        
#         key, output = outputs[level]['key'], outputs[level]['config']
#         device = output['device']
#         method = output['method']
#         channel = output['channel']
        
#         for i, value in enumerate(range_):
#             if device == self.TEKTRONIX:
#                 if method == 'freq':
#                     self._tektronix.set_freq(value, ch=channel)
#                 elif method == 'amp':
#                     self._tektronix.set_amp(value, ch=channel)
#                 elif method == 'offset':
#                     self._tektronix.set_offset(value, ch=channel)
#             elif device == self.HAMEG:
#                 if method == 'offset':
#                     self._hameg.set_voltage(value, ch=channel)
                    
#             if level == max_level:
#                 # TODO: do measurement!
                
#             rec(xnew, data, level=level+1, maxlevel=maxlevel, outputs=outputs)
    
    def save():
        raise NotImplemented
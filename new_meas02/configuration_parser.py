import ruamel.yaml

class ConfigIntegrityException(BaseException):
    pass

def load_config(filepath, allowed_outputs=['B0', 'B1', 'R2', 'R3', 'R4']):
    """ Loads the configuration file and checks its integrity.
    
    throws: ConfigIntegrityException
    """
    def _check_integrity(config):
        """ Check the integrity of the configuration file. 
        Raises ConfigIntegrityException if there are problems in the configuration file.
        """
        all_outputs = config['outputs']
        active_outputs_keys = [key for key in all_outputs.keys() if all_outputs[key]['active'] is True]
        stack = config['stack']
        
        # test if any output has been registered, that is not listed in `allowed_outputs`
        if any([(output not in allowed_outputs) for output in all_outputs.keys()]):
            raise ConfigIntegrityException('Config contains outputs, that are not listed as allowed outputs.')
        
        # test if all stack contains only registered outputs
        if any([(output.split('.')[0] not in all_outputs.keys()) for output in stack]):
            raise ConfigIntegrityException(
                "'stack' contains unknown outputs. Make sure that the stack only contains outputs that are listed " +
                "in the outputs section"
            )
        
        # test if stack contains only up to 2 values
        if len(stack) > 2:
            raise ConfigIntegrityException('Stack only allows up to two entries.')
        
        # test if the stack contains only active outputs that do not use the method 'const'
        for stack_entry in stack:
            output_key, _ = stack_entry.split('.')
            output = all_outputs[output_key]
            if not output['active']:
                raise ConfigIntegrityException("'stack' contains outputs that are not active")
            if 'const' in output['methods']:
                raise ConfigIntegrityException("'stack' contains outputs that has method 'const'") 
                
        # tests for B1:
        key = 'B1'
        if key in active_outputs_keys:
            output = all_outputs[key]
            if output['amp_mod']['active'] is True and output['freq_mod']['active'] is True:
                raise ConfigIntegrityException(
                    "'amp_mod' and 'freq_mod' cannot be used at the same time for output {}".format(key)) 
            if 'freq' in output['methods'] and output['freq_mod']['active'] is True:
                raise ConfigIntegrityException(
                    "method 'freq' and 'freq_mod' cannot be used at the same time for output {}".format(key))
            if output['amp_mod']['active'] is True:
                if output['amp_mod']['freq']['start'] > output['freq']['start']:
                    raise ConfigIntegrityException(
                        "'amp_mod.freq' must be smaller than 'freq.start' for output {}".format(key))
                if 'freq' in output['methods'] and output['amp_mod']['freq']['start'] > output['freq']['stop']:
                    raise ConfigIntegrityException(
                        "'amp_mod.freq' must be smaller than 'freq.stop' for output {}".format(key))
        
        # tests for B0
        key = 'B0'
        if key in active_outputs_keys:
            output = all_outputs[key]
            if output['func'] == 'DC' and any(m in output['methods'] for m in ('freq', 'amp')):
                raise ConfigIntegrityException(
                    "func 'DC' cannot be used with methods 'freq' or 'amp' for output {}".format(key))
    
    with open(filepath, 'r') as ymlfile:
        cfg = ruamel.yaml.load(ymlfile)
    _check_integrity(cfg)
    
    return cfg
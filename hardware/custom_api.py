"""
Example file for custom hardware API hooks. To provide custom hardware api,
create a file 'custom_api.py', copy and paste desired elements from this
file and adapt them to your needs.
"""

from tools.utility import singleton

@singleton
def PowerMeter():
    from power_meter import PM100D
    return PM100D()



import TimeTagger
TimeTagger._Tagger.setSerial('gVnTlaoxYl')


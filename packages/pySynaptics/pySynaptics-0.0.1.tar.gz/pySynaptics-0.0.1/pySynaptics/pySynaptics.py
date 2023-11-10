import os
import sys

# Add the directory containing csynaptics.so to the PYTHONPATH
current_directory = os.path.dirname(os.path.realpath(__file__))
so_directory = os.path.join(current_directory, 'lib')
sys.path.append(so_directory)

import csynaptics


#import csynaptics

def list_synaptics_devices():
    devices = csynaptics.enum()
    return devices


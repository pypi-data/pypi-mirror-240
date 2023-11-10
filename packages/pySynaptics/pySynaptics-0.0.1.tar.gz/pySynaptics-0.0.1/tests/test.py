import sys
import os
# Add the current directory to the PYTHONPATH


import pySynaptics

print(sys.path)

def main():
    print(sys.path)
    print(pySynaptics.__file__)
    devices = pySynaptics.list_synaptics_devices()
    for device in devices:
        #print(hex(device['pid']))
        print(device)

if __name__ == "__main__":
    main()
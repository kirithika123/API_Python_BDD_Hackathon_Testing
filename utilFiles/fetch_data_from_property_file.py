from utilFiles.CONSTANTS import *
from jproperties import Properties

def readProperties(fpath):

    configs = Properties()
    with open(fpath, 'rb') as config_file:
        configs.load(config_file)
    return configs

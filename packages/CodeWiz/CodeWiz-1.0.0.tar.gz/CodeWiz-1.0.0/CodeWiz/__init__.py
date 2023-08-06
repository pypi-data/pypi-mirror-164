import os
import sys
# print(sys.path, type(sys.path))
_path = os.path.dirname(__file__)
if _path not in sys.path:
    sys.path.append(_path)
# print(os.path.dirname(__file__))

# global WizData
# WizData = __import__('WizData', globals(), locals())
# global WizSerial
# WizSerial = __import__('WizSerial', globals(), locals())
# global WizDefaultSensor
# WizDefaultSensor = __import__('WizDefaultSensor', globals(), locals())
# from WizData import *
# from WizDefaultSensor import *
# from WizSerial import *

__version__ = '1.0.0'

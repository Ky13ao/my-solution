import sys
from ctypes import cdll


kFile = 'C:\\Windows\\System32\\kernel32.dll'
try:
    k32 = cdll.LoadLibrary(kFile)
except OSError as e:
    print("ERROR %s" % e)
    sys.exit()

k32Attrs = dir(k32._FuncPtr.__subclasses__())
print(k32Attrs)

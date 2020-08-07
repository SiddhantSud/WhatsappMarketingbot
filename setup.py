import sys
is_py2 = sys.version[0] == '2'
if is_py2:
    import Queue as queue
else:
    import queue as queue
from cx_Freeze import setup, Executable

setup(name = "WhatsAppMessageBot" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("WhatsappBot.py")])

import eel
import subprocess
import time

eel.init("www")

os.system('start msedge.exe --app="https://localhost:8000/index.html"')
eel.start('index.html',mode=None, host='localhost', block=True)
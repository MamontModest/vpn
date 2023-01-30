import subprocess
import sys
import time

client = subprocess.Popen([sys.executable, 'main.py'])
time.sleep(10)

client2 = subprocess.Popen([sys.executable, 'waller.py'])
time.sleep(5)
client3 = subprocess.Popen([sys.executable, 'time_manager.py'])
client.wait()
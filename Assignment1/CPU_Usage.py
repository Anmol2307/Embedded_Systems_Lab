import threading
import os
import time

count = 1000
tmp = 0

def printit():
  global tmp
    # threading.Timer(1.0, printit).start()
  for i in xrange(0,1000):
    os.system("date +%H:%M:%S.%3N")
    os.system("grep 'cpu ' /proc/stat")
    time.sleep(1)

printit()
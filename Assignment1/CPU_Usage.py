import threading
import os

count = 1000
tmp = 0

def printit():
  global tmp
  if tmp < count:
    threading.Timer(1.0, printit).start()
    os.system("date +%H:%M:%S.%3N")
    os.system("grep 'cpu ' /proc/stat")
    tmp += 1

printit()
import matplotlib.pyplot as plt
import pylab
import numpy as np

time_arr = []
cpu_arr = []

tot = 0
idle = 0
use = 0

prevtot = 0
previdle = 0
prevuse = 0

prevtime = []
time_now = []

def cpu_time(location):
  fig = plt.figure()
  ax = fig.add_subplot(111)

  ax.set_ylim(0,100)
  
  ax.set_ylabel('Recorded CPU Usage')
  ax.set_title('Time')

  plt.plot(cpu_arr)
  plt.show()
  # pylab.savefig(location)


def plot_cpu():
    fi = open("readings","r+")
    fo = open("TimeDiff.dat","r+")
    fi.write("Timestamp \t CPU-Usage\n")
    start = True
    with open("output") as f:
        while True:
          line1 = f.readline()
          line2 = f.readline()
          if not line1:
            break;
          time = line2.split(' ')
          global tot
          global idle
          global use
          global prevtot
          global previdle
          global prevuse
          global prevtime
          global time_now

          prevtot = tot
          previdle = idle
          prevuse = use
          prevtime = time_now
          
          
          if start == True:
            start = False
            time_now = line1.split(':')
            time_now[2] = time_now[2].rstrip('\n')
          else:
            time_now = line1.split(':')
            hr = int(time_now[0]) - int(prevtime[0])
            mi = int(time_now[1]) - int(prevtime[1])
            time_now[2] = time_now[2].rstrip('\n')
            sec = float(time_now[2]) - float(prevtime[2])
            diff = (3600*hr + 60*mi + sec)*1000
            diff = str(diff)
            diff = diff.rstrip('0').rstrip('.') if '.' in diff else diff
            fo.write(str(diff) + '\n')  
          idle = int(time[5]) + int(time[6])
          use = int(time[2]) + int(time[3]) + int(time[4]) + int(time[7]) + int(time[8]) + int(time[9])
          tot = use + idle
          percent_use = 100*((tot - prevtot) - (idle - previdle))/(tot - prevtot);

          time_arr.append(line1)
          cpu_arr.append(percent_use)
          line1 = line1.rstrip('\n')
          out = line1 + ' ' + str(percent_use) + '\n'
          fi.write(out)
    fi.close()
    # print time_arr
    # print cpu_arr
    # print len(time_arr)
    # print len(cpu_arr)
    cpu_time('CPU-Usage.png')

plot_cpu()
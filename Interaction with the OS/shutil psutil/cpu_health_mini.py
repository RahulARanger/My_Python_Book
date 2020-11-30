import shutil
# install psutil from pip commands it is not provided by default
import psutil
def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    print('Your CPU Usage is:',usage)
    if usage>75.0:return False
    else:return True    
def memory_left():
           memory=shutil.disk_usage('/')
           print('The Free and Total Memory is: ',memory.free,memory.total)
           free=memory.free/memory.total*100
           print('Hence {:.2f}% memory is left'.format(free))
           if free<20:return False
           else: return True
if memory_left() and check_cpu_usage():print('Your CPU has Normal Health')
else:print('It is Sick')    

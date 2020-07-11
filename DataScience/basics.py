import datetime
import time
# getting the epoch time
a=time.time()
print(a)
dtnow=datetime.datetime.fromtimestamp(a)
print(dtnow)
print('Date:',dtnow.date())
print('Time:',dtnow.time())
print('Day: {} ,Month: {}, Year: {}'.format(dtnow.day,dtnow.month,dtnow.year))
print('Hour:{}, Minutes:{}, Seconds: {}'.format(dtnow.hour,dtnow.minute,dtnow.second))

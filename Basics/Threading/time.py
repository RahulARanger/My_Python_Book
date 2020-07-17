import time
seconds=time.time()
print(seconds)
time.sleep(2)
seconds-=time.time()
print(abs(seconds))
# time.ctime() returns in the form of the local time
print(time.ctime(time.time()))
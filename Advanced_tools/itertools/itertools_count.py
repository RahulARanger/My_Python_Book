import itertools
import time
check1=time.time()
for i in itertools.count(5,5):
    if i==35000000:
        print(i)
        break
    else:pass
check2=time.time()
print()
print('Time taken:',check2-check1)    
check1=time.time()
for i in range(35000000):
    pass
check2=time.time()
print('Time taken:',check2-check1)    
# this is the difference between the speed of the normal loop with itertools ones

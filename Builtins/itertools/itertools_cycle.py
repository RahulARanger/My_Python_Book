import itertools
import time
check=0
lst=list(range(0,350000))
check1=time.time()
for i in itertools.cycle(lst):
    if i==lst[-1]:
        check+=1
    if check==2:
        print(i)
        break
check2=time.time()    
print('Time:',check2-check1)
for i in range(2):
    for j in range(0,350000):
        pass
check3=time.time()
print('Time:',check3-check2)           
    
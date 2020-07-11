import time
lst=list(range(10000000,0,-1))
check=time.time()
print(min(lst))
print(time.time()-check)
check=time.time()
lst.sort()
print(lst[0])
print(time.time()-check)

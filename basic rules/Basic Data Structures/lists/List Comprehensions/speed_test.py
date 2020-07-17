import time
check=time.time()
for i in range(1,100000):
    if i==100:print(i)
check2=time.time()
[print(_) for _ in range(1,100000) if _ ==100]    
check3=time.time()
print(check3-check2)
print(check2-check)
# differs sometimes list comprehension is fastest or sometimes loop is fastest
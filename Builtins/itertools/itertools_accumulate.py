import itertools
import time
# adds the element + prev elements in the list
lst=list(range(1,100000))
check_1=time.time()
lst_add=[]
for i in range(len(lst)):
    lst_add.append(sum(lst[:i+1]))
check_2=time.time()
lst_add=list(itertools.accumulate(lst))
print(time.time()-check_2)
print(check_2-check_1)
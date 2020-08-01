import time
lst=[i for i in range(10000)]
check=time.time()
count=0
for i in range(len(lst)):
    for j in range(len(lst)):
        count+=1
print(time.time()-check)  
print(count)  
mid=len(lst)//2
lst_l=lst[:mid]
lst_r=lst[mid:]
print(len(lst),len(lst_l),len(lst_r))
check=time.time()
count=0
for i in range(len(lst_l)):
    for j in range(len(lst_l)):
        count+=1
for i in range(len(lst_r)):
    for j in range(len(lst_r)):
        count+=1
for i in range(len(lst_l)):
    for j in range(len(lst_r)):
        count+=1
for i in range(len(lst_r)):
    for j in range(len(lst_l)):
        count+=1        
print(time.time()-check)
print(count)
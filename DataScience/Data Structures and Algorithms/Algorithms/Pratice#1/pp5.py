lst=[int(i) for i in input().split()]
check=None
for i in range(len(lst)-1):
    if check is None: 
        check=lst[i]-lst[i+1] 
    else: check=lst[i]-lst[i+1] if lst[i]-lst[i+1]>check else check
print(check)

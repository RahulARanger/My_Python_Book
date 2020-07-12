lst=[int(i) for i in input('Enter the Keys: ').split()]
d=dict()
collect=input('Enter it\'s values now: ').split()
for i in range(len(collect)):
    d[lst[i]]=int(collect[i])
print(d)    
print('After sorting by values: ')
check=sorted(d)
for i in check:
    print(d[i],end=' ')
print('\nAfter sorting by keys: ')
check=sorted(d,key=lambda x:d[x])
for i in check:
    print(d[i],end=' ')

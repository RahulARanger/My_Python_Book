import itertools

def calc(lst,m):
    red=sum([i**2 for i in lst])       
    return red%m
k,m=[int(i) for i in input().split()]
lsts=[]
for i in range(k):
    lst=[int(i) for i in input().split()]
    lst=lst[1:]
    lsts.append(list(set(lst)))
found=(list(itertools.product(*lsts)))
print(max(list(map(lambda x:calc(x,m),found))))
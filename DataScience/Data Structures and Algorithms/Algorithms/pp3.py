import itertools
a=[int(i) for i in input().split()]
k=int(input())
collect=[]
for i in itertools.count(0):
    v=max(a)
    a.remove(v)
    collect.append(v)
    if sum(collect)>k:break
    if len(a)==0:break
print(collect)
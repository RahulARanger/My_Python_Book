n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
collection=set()
round_1=a.index(min(a))
round_2=b.index(max(b))
for i in range(len(b)):
    print(round_1,i)
    collection.add(a[round_1]+b[i])
for i in range(len(a)):
    if a[i]+b[round_2] not in collection:
        print(i,round_2)
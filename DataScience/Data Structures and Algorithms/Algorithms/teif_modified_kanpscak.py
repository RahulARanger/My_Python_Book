# this is the solution for the problem 2 of the week 3 assignment
n,w=[int(i) for i in input().split()]
w=float(w)
pairs=[]
collected=0
for i in range(n):
    pair=[float(i) for i in input().split()]
    pair.insert(0,pair[0]/pair[1])
    pairs.append(pair)
pairs.sort()
pairs.reverse()
for i in pairs:
    if w==0:
        break
    if w>=i[2]:
        w-=i[2]
        collected+=i[1]
    else:
        remaining=w/i[2]
        collected+=remaining*i[1]
        w=0
print('{:.4f}'.format(collected))
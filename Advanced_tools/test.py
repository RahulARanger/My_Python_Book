import time
check=time.time()
a=[6,3]
b=[3,6]
n,m=len(a),len(b)
pos = []
min_a = a[0]
index_a = 0
for i in range(1,n):
    if min_a > a[i]:
        min_a = a[i]
        index_a = i
max_b = b[0]
index_b = 0
for i in range(1,m):
    if max_b < b[i]:
        max_b = b[i]
        index_b = i
for i in range(m):
    pos.append([index_a,i])
for i in range(n):
    if i == index_a:
        continue
    pos.append([i,index_b])
for i in range(n+m-1):
    print(pos[i][0],pos[i][1])
print(time.time()-check)    
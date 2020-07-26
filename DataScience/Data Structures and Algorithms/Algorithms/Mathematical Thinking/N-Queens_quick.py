import sys
n=int(input())
if n>1 and n<4:
    print('Not Possible')
    sys.exit(0)
if n==1:
    print('q')
    sys.exit(0)
check=[[0,i] for i in range(n-1,-1,-1)]
check.append(None)
print(check)
consider=[check[-2]]
while True:
    index=consider[-1][0]+1
    pts=[]
    for j in range(n):
        pt=[index,j]
        for k in range(len(consider)):
            wow=consider[k]
            _=abs(wow[0]-pt[0])
            __=abs(wow[1]-pt[1])
            if _==__ or wow[1]==pt[1]:break
            if k==len(consider)-1:pts.append(pt)
    #print(pts)
    if len(pts)!=0:
        pts.reverse()
        check.extend(pts)
        check.append(None)
    else:
        flags=[]
        while True:
            if check[-1] is None:
                flags.append(False)
            else:
                flags.append(True)
            if flags[-1]==False and flags[-2]==True:
                
    consider.append(check[-2])
    print(check,consider)



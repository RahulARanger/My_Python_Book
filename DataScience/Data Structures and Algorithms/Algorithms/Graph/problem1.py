i=int(input())
a=[int(i) for i in input().split()]
p=[int(i) for i in input().split()]
inc={}
for i in range(len(p)):
    inc[i+1]=[]
salary={}
for i in range(len(a)):
    salary[i+1]=a[i]
head=None
for i in range(len(p)):    
    if p[i]==-1:
        head=i+1
    else:
        inc[p[i]].append(i+1)
        inc[i+1].append(p[i])
stack=[head]
maxi=[salary[head]]
checklist={}
for i in range(1,len(p)+1):
    checklist[i]=False
checklist[head]=True
check=None
while True:
    if len(stack)==0:break    
    current=stack[-1]
    flag=False
    for i in inc[current]:
        if checklist[i] is False:
            checklist[i]=True
            stack.append(i)
            maxi.append(salary[i])
            flag=True
            break    
    if flag:
        pass
    else:
        current=maxi[-1]
        length=len(maxi)
        point=None
        if length>1:
            for i in range(length-1):
                
                if point is None: point=maxi[i]-current
                else:
                    e=maxi[i]-current
                    if e>point:point=e            
            if check is None:
                check=point
            else:
                if check<point:check=point
        stack.pop()
        maxi.pop()
print(check)

n=int(input())
flag=1
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
        else:flag=1
    if flag==1:print(str(i)+' ',end='')
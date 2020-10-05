
#? Idea is to collect the points and classify them as left,point,right end

# ? and then sort them and then we can go through the list 

# * In simple words we can do the same as infix to postfix expressions

n,s=[int(i) for i in input().split()]
boundary=[]
for i in range(n):
    pt=[int(j) for j in input().split()]
    boundary.append([pt[0],0])
    boundary.append([pt[1],2])
pts_1=[int(i) for i in input().split()]
pts=pts_1.copy()
for i in pts:
    boundary.append([i,1])
boundary.sort()
check=0
test={}
for i in range(len(boundary)):
    if boundary[i][1]==0:check+=1
    elif boundary[i][1]==1:
        test[boundary[i][0]]=check if check>=0 else check
    else:
        check-=1
[print(test[_],end= ' ') for _ in pts_1]


# ! Algorithm is O(n+k) which is better than the O(n^2) {naive algorithm}

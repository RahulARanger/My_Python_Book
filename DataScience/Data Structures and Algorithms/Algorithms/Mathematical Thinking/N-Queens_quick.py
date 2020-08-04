import sys
def print_it(path,n):
    for i in range(n):
        for j in range(n):
            pt=[i,j]
            if pt in path:
                print('q',end=' ')
            else:print('_',end=' ')
        print()
n=int(input('Enter the length of the chessboard:'))
if n>1 and n<4:
    print('Not Possible')
    sys.exit(0)
if n==1:
    print('q')    
    sys.exit(0)
board=[]
def check(path,pt):
    for i in path:
        if pt[1]==i[1]:return False
        x_=abs(pt[0]-i[0])
        y_=abs(pt[1]-i[1])
        if x_==y_:return False
    return True    
path=[]
axis=[]
i=0
while i<n:
    choices=[]
    for j in range(n):
        pt=[i,j]
        if i==0:
            choices.append(pt)
        else:
            if check(path,pt):
                choices.append(pt)
            else:pass
    if len(choices)!=0:
        path.append(choices[0])
        axis.append(choices)  
        i+=1
    else:
        if len(axis[-1])==1 and len(axis[-2])==1:
            while True:
                if len(axis[-1])==1:
                    axis.pop()
                    path.pop()
                else:
                    del axis[-1][0]
                    path.pop()
                    path.append(axis[-1][0])   
                    i=path[-1][0]+1 
                    break
        else:
            path.pop()
            if len(axis[-1])==1:
                axis.pop()
                del axis[-1][0]    
                path.pop()
                i-=1
            else:
                del axis[-1][0]    
            path.append(axis[-1][0])
    if len(path)==n:break
print_it(path,n)

# This is the better algorithm than the previous ones (can execute within 10 sec for n=20)
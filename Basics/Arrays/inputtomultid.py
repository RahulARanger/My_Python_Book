from numpy import*
n,m=input().split(' ')
list=input().split(' ')
try:
 m,n=int(m),int(n)
 list=[int(i) for i in list]
 arr=array(list)
 arr=reshape(arr,(n,m))
 for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')
    print()    
except:
    print("You have Entered the Elements more than the %d"% (m*n))
    print('Please Try again')     
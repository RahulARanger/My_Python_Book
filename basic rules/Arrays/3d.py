from numpy import*
x,y,z=input().split(' ')
try:
   x,y,z=int(x),int(y),int(z)
   list=input().split(' ')
   list=[int(i) for i in list]
   arr=array(list)
   arr=reshape(arr,(x,y,z))
   for i in range(len(arr)):
       for j in range(len(arr[i])):
           for k in range(len(arr[i][j])):
               print(arr[i][j][k],end=' ')
           print()    
       print()
   print()     
except:
    print("The Number of elements is not equal to %d "% (x*y*z))

from numpy import*
n,m=int(input()),int(input())
liste=[]
for i in range(n):
    for j in range(m):
        liste.append(int(input()))
arr=array(liste)
arr=reshape(arr,(3,3))
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')
    print()              
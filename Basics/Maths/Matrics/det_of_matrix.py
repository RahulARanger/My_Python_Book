from numpy import *
n,mat=int(input('Enter the Number of the rows in the matrix: ')),[]
print('Enter the elements in the matrix style')
for i in range(n):
    mat.append([float(i) for i in input().split()])
try:
    det=linalg.det(mat)
    print(det)    
except:
    print('The Given Input is an error')    
from numpy import*
n,mat=int(input('Enter the Number of the rows in the matrix: ')),[]
print('Enter the elements in the matrix style')
for i in range(n):
    mat.append([float(i) for i in input().split()])
mat=linalg.inv(mat)
print(mat)
    # we can also use the linalg.inv from nupy package
    
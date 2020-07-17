from numpy import*
A=[int(i) for i in input('Enter the row and columns of the matrix A space seperated: ').split()]
B=[int(i) for i in input('Enter the row and columns of the matrix B space seperated: ').split()]
print('Enter the elements in the matrix style')
print('Enter the elements of the Matrix A: ')
MatrixA,MatrixB=[],[]
for i in range(A[0]):
        MatrixA.append([float(j) for j in input().split()])
print('Enter the elements of the Matrix B: ')
for i in range(B[0]):
    MatrixB.append([float(j) for j in input().split() ])
MatrixA=matrix(MatrixA)
MatrixB=matrix(MatrixB)
f=linalg.solve(MatrixA,MatrixB)
print(f)

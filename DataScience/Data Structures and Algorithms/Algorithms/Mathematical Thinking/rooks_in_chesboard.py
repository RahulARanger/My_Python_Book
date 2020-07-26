'''
problem statement:  place n rooks in n*n chessboard so that they can't attack each other
'''
def print_it(n):
    for  i in range(n):
        for j in range(n):
            if i==j:print('R',end=' ')
            else:print('0',end=' ')
        print()    
print_it(int(input('Enter the length of the chessboard: ')))

# note the maximum number of rooks in n*n chessboard is n
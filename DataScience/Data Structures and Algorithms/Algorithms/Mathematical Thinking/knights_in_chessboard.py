def print_it(n):
    for i in range(n):
        for j in range(n):
            print('K' if (i+j)%2==0 else '_',end=' ')
        print()    
print_it(int(input('Enter the Length of the Chessboard: ')))

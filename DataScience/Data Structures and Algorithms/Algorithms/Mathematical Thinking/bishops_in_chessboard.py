def print_it(n):
    for i in range(n):
        for j in range(n):
            if j==0:
                print('B',end=' ')
            elif j==n-1 and(i!=0 and i!=n-1):print('B',end=' ')
            else:print('_',end=' ')
        print()
print_it(int(input('Enter the length of the chessboard: ')))                
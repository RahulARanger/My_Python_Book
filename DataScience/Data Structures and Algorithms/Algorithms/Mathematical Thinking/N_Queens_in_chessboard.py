'''
Question : Place N Queens in N*N Chessboard so that they don't attack each other. 
There are cases where it may be possible
'''
# this algorithm works only for small input since it O(n!)
import itertools
def print_it(board):
    print('\nq means queens and 0 for empty places \n')
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=' ')
        print()    
def check_this(pt):
    for i in range(len(pt)):
        for j in range(i+1,len(pt)):
            pts=abs(pt[j]-pt[i])
            check_=abs(j-i) 
            if pts==check_:return False
    return True        
n=int(input())
board=[[0 for i in range(n)]for  j in range(n)]
check=[i for i in range(n)]
check_plus=itertools.permutations(check)
check_plus=(list(check_plus))
flag=False
for i in check_plus:
    pt=list(i)
    if check_this(pt):
        for j in range(len(pt)):
            board[j][pt[j]]='q'
        flag=True
        print_it(board)
        break
    else:continue
if not flag:print('Not Possible')
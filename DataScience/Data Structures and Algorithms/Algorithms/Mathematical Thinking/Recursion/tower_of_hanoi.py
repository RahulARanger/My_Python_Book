#   Tower of Hanoi is a very Intersting Problem 
#        Refer this Website: https://www.mathsisfun.com/games/towerofhanoi.html for problem statement
def find(n):
    if n==1:
        return 1
    else:
        return 2*find(n-1)+1
n=int(input('Enter the Number of the Blocks: '))
print(find(n))        

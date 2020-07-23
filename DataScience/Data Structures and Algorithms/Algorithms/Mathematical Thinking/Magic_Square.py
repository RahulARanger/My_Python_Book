# https://www.geeksforgeeks.org/magic-square/ refer this link in order to understand the algorithm used here
def print_matrix(table):
    for i in  range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j],end=' ')
        print()
def check(number,n):
    if number<0:
        return n+number
    elif number>n-1:
        return number-(n)
    else: return number
def fill_it(table,n):
    table=[[0 for _ in range(n)] for j in range(n)]
    starting_x=n//2
    starting_y=n-1
    encountered=[[starting_x,starting_y]]
    table[starting_x][starting_y]=1
    number=2
    for _ in range(n**2-1):
        starting_x-=1
        starting_y+=1
        starting_x=check(starting_x,n)
        starting_y=check(starting_y,n)
        if [starting_x,starting_y] in encountered:
            starting_x+=1
            starting_y-=2
            starting_x=check(starting_x,n)
            starting_y=check(starting_y,n)
        encountered.append([starting_x,starting_y])
        table[starting_x][starting_y]=number
        number+=1    
    return table
print_matrix(fill_it([],int(input('Enter the Number: '))))    

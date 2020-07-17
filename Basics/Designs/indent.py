# the rjust is for right indenting 
# and ljust is for left indenting
# and center is for center indenting
def adjust(string):
    answer=string[2:]
    
    answers=''
    for i in answer:
        if  i.isalpha():answers+=i.upper()
        else: answers+=i
    return answers
def print_formatted(n):
    pad=bin(n)
    pad=len(pad)-2
    
    for i in range(1,n+1):
        Number=str(i)
        print(Number.rjust(pad,' '),end='')
        Number=adjust(oct(i))
        print(Number.rjust(pad+1,' '),end='')
        Number=adjust(hex(i))
        print(Number.rjust(pad+1,' '),end='')
        Number=adjust(bin(i))
        print(Number.rjust(pad+1,' '),end='')
        if i!=n:print()
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
     
     
    
    
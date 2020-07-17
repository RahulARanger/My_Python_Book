#this is a lamba function that returns the largest or smallest of the two numbers
def decide():
    print('Enter any two numbers; ')
    a,b=input().split()
    a,b=int(a),int(b)
    print('1 for max of them or 2 for min of them any other to retry again \n So your call: ',end='')
    choice=int(input())
    if choice==1 or choice ==2:
        return choice,a,b
    else: return decide()    
large=lambda x,y:x if x>y else y
small=lambda x,y:y if x>y else x
ch,a,b=decide()
if ch==1:print(large(a,b))
else: print(small(a,b))
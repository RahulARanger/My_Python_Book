'''Find an unknown integer 1 ≤ x ≤ N by asking k questions “Is x = y?” (for any 1 ≤ y ≤ N ). When you ask such a question,
simply enter "y" instead of "Is x=y?" Your opponent will reply either “Yes”, or “x < y”, or “x > y.”'''
import numpy
n=int(input())
x=numpy.random.randint(0,n+1)
k=int(input())
flag=False
for i in range(k):
    y=int(input())
    if y==x:
        print('Congratulations!!! You Guessed it right')
        flag=True
        break
    else:
        if y>x:
            print('you guessed a larger number')    
        else:print('you guessed a smaller number')    
if flag:pass
else:
    print('You didn\'t guess within first k tries')        

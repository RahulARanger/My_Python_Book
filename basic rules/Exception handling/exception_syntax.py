c=None
for i in range(2):
   try: 
    numbers=[int(i) for i in input().split()]
    c=float(numbers[1])/float(numbers[0])
   except ZeroDivisionError:
       print('The answer is not defined because the division is done by zero')
   except:
       print('The input is not given as numbers')    
   else:
       print('The Answer is: %d '%c)
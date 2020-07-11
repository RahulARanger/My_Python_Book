# this program counts the sum of the numbers in the Test1.txt
#look at the regular expression for more details
import re
import functools as e
hand=open('Test1.txt')
numbers=[]
for i in hand:
    numbers+=re.findall('[0-9]+',i)
numbers=e.reduce(lambda x,y:int(x)+int(y),numbers)
print(numbers)
hand.close()    
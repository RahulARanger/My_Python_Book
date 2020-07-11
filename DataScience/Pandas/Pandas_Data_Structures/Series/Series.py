import pandas
import numpy
animals=['Tiger','Cheetah']
s=pandas.Series(animals)
print(s)
multi=pandas.Series(['Hello',69])
print(multi)
num=pandas.Series([69,420],dtype=int)
print(num)
none=pandas.Series([69,420,None])
print(none)
for i in none:
    if numpy.isnan(i):
        print('yes')
    else:print(i)    
lst=[i for i in input('Test:').split()]    
test=pandas.Series(lst,dtype=int)
print(test)
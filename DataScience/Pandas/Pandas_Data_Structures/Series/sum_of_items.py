import numpy
import pandas
lst=[float(i) for i in input('Enter the Prices of the Items: ').split()]
series=pandas.Series(lst)
# this is one of the method for finding the sum of the items in the list
print(sum(series))
print('The values for this series is now automatically generated using numpy.random.randint()')
print('The first 5 rows are: ')
lst=numpy.random.randint(0,1000,10000)
series=pandas.Series(lst)
# fastest method for summing up items in the list,series or in any data type
print(numpy.sum(series))
total=0
for i in series:
    total+=i
print(total)    

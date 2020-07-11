from numpy import *
from scipy import stats
lst=[int(i) for i in input('Enter the List of Numbers: ').split()]
x=stats.mode(lst)
#print(x)
print(type(x))
print(x.count[0])
print(x.mode[0])
print('''
The General Properties of the Given Data is:

Mean: {:.3f}
Median: {:.3f}
Mode: {}
Varience: {:.3f}
Standard Deviation: {:.3f}
'''.format(mean(lst),median(lst),x.mode[0],std(lst)**2,std(lst)))

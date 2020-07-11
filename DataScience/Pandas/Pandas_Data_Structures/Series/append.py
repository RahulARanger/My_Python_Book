import pandas
import numpy
lst=[i for i in input('First List of Numbers: ').split()]
series_1=pandas.Series(lst)
lst=[i for i in input('Second List of Numbers: ').split()]
series_2=pandas.Series(lst)
print(series_1,'\n',series_2,sep='')
series_combined=(series_1.append(series_2,ignore_index=True))
print(series_combined)
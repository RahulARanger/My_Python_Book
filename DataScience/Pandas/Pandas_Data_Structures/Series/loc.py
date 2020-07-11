import pandas
import numpy
lst=[i for i in input('Enter the Fruits Name: ').split()]
indexes=[i for i in input('Enter their respective colors: ').split()]
series=pandas.Series(lst,index=indexes)
print(series)
print('Now Enter the proper color names to access them: ')
while(True):
    print('To quit enter the wrong ones')
    num=(input('Enter the Color name:'))
    try:
        print('The Element at the index: {} is : {}'.format(num,series.loc[num]))
    except:
        break    
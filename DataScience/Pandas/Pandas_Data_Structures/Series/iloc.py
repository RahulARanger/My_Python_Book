import pandas
import numpy
lst=[i for i in input('Enter the Fruits Name: ').split()]
indexes=[i for i in input('Enter their respective colors: ').split()]
series=pandas.Series(lst,index=indexes)
print(series)
print('Now we will use the Indexes numbers to access them: ')
while(True):
    print('To quit enter the wrong ones')
    num=int(input('Enter the proper index Number to access them: '))
    try:
        print('The Element at the index: {} is : {}'.format(num,series.iloc[num-1]))
    except:
        break    
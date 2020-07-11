import os
import datetime
fname=input('Enter the name of the file: ')
try:
    size=os.path.getsize(fname)
    print(size)
    a=(datetime.datetime.fromtimestamp(os.path.getmtime(fname)))
    print('{}-{}-{}'.format(a.year,a.month,a.day))
    print(os.path.isfile(fname))
    print(os.path.isdir('test'))
    print(os.path.abspath(fname))
except:
    print('Error')    
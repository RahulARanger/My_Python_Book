import os
fname=input('Enter the name of the File: ')
try:
    os.remove(fname)
    print('{} has been deleted successfully'.format(fname))
except:
    print('The file may not exist or it is open or it may be due to some other errors')    
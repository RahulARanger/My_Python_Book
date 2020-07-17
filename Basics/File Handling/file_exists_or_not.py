import os
fname=input('Enter the name of the file: ')
try:
    if os.path.exists(fname):
        print('{} exists'.format(fname))
    else:print('{} doesn\'t exists'.format(fname))
except:
    print('Error')        
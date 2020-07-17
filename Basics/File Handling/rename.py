import os
fname=input('Enter the name of the file: ')
try:
    os.rename(fname,input('Enter the new name of the file: '))
except:
    print('There is an error to rename tht file')    
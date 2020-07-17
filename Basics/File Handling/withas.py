fname=input('Name of the file: ')
with open(fname) as hand:
    for i in hand:
       print(i,end='')


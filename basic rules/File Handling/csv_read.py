import csv
fname=input('Enter the name of the File: ')
with open(fname) as hand:
    r=csv.reader(hand)
    for i in r:
        name,age,email=i
        if name=='Name':continue
        print('''
                 Name: {}
                 Age: {}
                 Email: {}
        '''.format(name,age,email))
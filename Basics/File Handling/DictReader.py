import csv
fname=input('Enter the File name: ')
try:
    with open(fname) as hand:
        w=csv.DictReader(hand)
        for i in w:
            print('''
            Name: {} 
            Age: {}
            Email: {} '''.format(i['Name'],i['Age'],i['Email']))
except:
    pass            
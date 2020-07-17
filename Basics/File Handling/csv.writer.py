import csv
fname=input('Enter the name of the File: ')
print('Enter the Column names (space seperated);')
cols=input().split()
n=int(input('Number of Rows(entries): '))
with open(fname,'w') as hand:
    w=csv.writer(hand)
    w.writerow(cols)
    print(cols)
    for y in range(n):
        rc=[]
        for i in cols:
            rc.append(input('Enter the {}: '.format(i)))
        w.writerow(rc)
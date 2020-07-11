import csv
fname=input('Enter the File Name: ')
try:
    cols=input('Enter the Column Names : ').split()
    rows=[]
    for i in range(int(input('Enter the Number of the Rows: '))):
        row={}
        for j in cols:
            row[j]=(input('{}: '.format(j)))
        rows.append(row) 
    print(rows)     
    with open(fname,'w') as hand:
        w=csv.DictWriter(hand,fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
except:pass        

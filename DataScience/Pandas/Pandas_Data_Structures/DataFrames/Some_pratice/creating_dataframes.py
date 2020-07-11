import pandas
fname=input('Enter the Name of the File: ' )
table={}
try:
    cols=input('Enter the Column names for the Table (space seperated): ').split()
    n=int(input('Enter the Number of the rows: '))
    for i in cols:
        table[i]=[]
    print(table)    
    for i in cols:
        rows=input('Fill the rows of {}: '.format(i)).split()
        for j in range(len(rows)):
            try:
                rows[i]=int(rows[i])
            except:pass 
            table[i]=rows         
except:pass 
print(table)
table=pandas.DataFrame(table)
table.to_csv(fname)
import pandas
def create_table():
    cols=input('Enter the Column names for the Table (space seperated): ').split()
    n=int(input('Enter the Number of the rows: '))
    table={}
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
    return pandas.DataFrame(table)
n=int(input('Number of the Data Frames to be merged: '))
dfs=[]
try:
    for i in range(n):
        dfs.append(create_table())
    new_df=pandas.merge(*dfs,on='city')
    new_df1=pandas.merge(*dfs,on='city',how='outer')
    newfname=input('Save as: ')
    newfname1='ojoin'+newfname
    new_df.to_csv(newfname)
    new_df.to_excel(newfname[:newfname.find('.')]+'.xlsx')
    new_df1.to_csv(newfname1)
    new_df1.to_excel(newfname1[:newfname1.find('.')]+'.xlsx')
except:pass
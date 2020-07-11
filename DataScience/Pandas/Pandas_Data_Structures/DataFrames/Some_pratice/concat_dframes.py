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
n=int(input('How many Tables to concatenate: '))
dfs=[]
try:
    for i in range(n):
        dfs.append(create_table())
    new_df=pandas.concat([*dfs])
    new_df1=pandas.concat([*dfs],ignore_index=True)
    new_df2=pandas.concat([*dfs],axis=0)
    print(new_df)   
    newfname=input('The Result should be saved to file name: ')
    newfnamea=newfname[:newfname.find('.')]+'axis0'+'.csv'
    newfnamei=newfname[:newfname.find('.')]+'ignoreindex'+'.csv'
    new_df.to_csv(newfname)
    new_df1.to_csv(newfnamei)
    new_df2.to_csv(newfnamea)
except:pass
import pandas
try:
    df=pandas.read_csv(input('Enter the File Name: '))
    col=input('Column name so it will be dropped: ')
    dropped=df.drop(col,axis=1)
    print(dropped)
    dropped.to_csv(input('Save As: '))
except:pass    
import pandas
fname=input('Enter the File name: ')
try:
    df=pandas.read_csv(fname)
    print(df[['color','x','y','z']][df.color=='E'])
except:pass    
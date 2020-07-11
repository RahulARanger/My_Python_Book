import pandas
fname=input('Enter the File Name: ')
try:
    df=pandas.read_csv(fname)
    cols=input('Enter the Column names to print them (space seperated): ').split()
    print(df[cols])
except:pass

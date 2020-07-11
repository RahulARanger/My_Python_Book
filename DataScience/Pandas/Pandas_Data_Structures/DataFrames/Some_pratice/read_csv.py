import pandas
fname=input('Enter the Name of the File: ')
try:
    df=pandas.read_csv(fname,skiprows=1)
    print(df)
    print(type(df['depth']))
except:
    pass            
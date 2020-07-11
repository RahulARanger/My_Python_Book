# this .py file uses weather.csv as it's study material
import pandas
fname=input('File Name: ')
try:
    df=pandas.read_csv(fname)
    f=df.groupby('city')
    print(f.get_group('paris'))
    print(type(f.get_group('mumbai')))
    print(type(df))
    print(f.max())
    print(f.describe())
except:pass    
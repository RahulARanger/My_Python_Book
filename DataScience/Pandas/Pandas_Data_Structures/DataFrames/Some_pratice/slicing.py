import pandas
fname='nba.csv'
try:
    df=pandas.read_csv(fname)
    print(type(df.loc[0]))
    print(df.loc[0:6:2])
except:pass    
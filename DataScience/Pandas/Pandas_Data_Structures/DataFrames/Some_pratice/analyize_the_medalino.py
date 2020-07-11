import pandas
fname='medalsino.csv'
try:
    df=pandas.read_csv(fname)
    # to pass the output in the form of the csv
    #df.City[df.Medal=='Gold'].to_csv('modified.csv')
    print(df[df.Medal=='Gold'].median())
except:pass    
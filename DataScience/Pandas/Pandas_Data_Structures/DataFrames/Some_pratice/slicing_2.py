import pandas
fname=input('Enter the File Name: ')
try:
    df=pandas.read_csv(fname)
    print(df[2:5])
    # there is a differnce between this both slicing
    # top ones is usual slicing
    # bottom ones doesnt ignore the ending element
    print(df.loc[2:5])
    print()
    print()
    print(df.iloc[0:3,0:2])
except: pass    
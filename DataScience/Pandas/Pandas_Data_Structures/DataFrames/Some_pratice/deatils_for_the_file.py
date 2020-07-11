import pandas
fname=input('Enter the Name of the File: ')
try:
    df=pandas.read_csv(fname)
    rows,columns=df.shape
    # returns the tuple containing info abt rows and columns 0th - row and 1st - column
    print('There are rows: {} and columns: {} '.format(rows,columns))
    print()
    # gives the description for the numerical columns of the table 
    print(df.describe())  
except:pass
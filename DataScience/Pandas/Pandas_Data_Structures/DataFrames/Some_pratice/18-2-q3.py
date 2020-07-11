# this is related to the question 3 of the assignment 18 
# question is to find the shape and display the statistic information of the dataframe
import pandas
fname=input('Enter the Name of the File: ')
try:
    df=pandas.read_csv(fname)
    rows,colums=df.shape
    print('This dataframe has {} rows and {} columns '.format(rows,colums))
    print(df.describe())
except:pass    

# this file is related to the question 1 in html doc  of assignment 18-2
# question: to print the  first 5 rows and last 5 columns
import pandas
fname=input('Enter the File Name: ')
try:
    df=pandas.read_csv(fname)
    # for priniting the first 5 rows
    print(df.head(),end='\n\n')
    # for priniting the last 5 rows
    print(df.tail())    
except:pass    
# this is related to the question 2 of the assignment 18
# question is to print the entries in the Father column in the father_son.csv
import pandas
fname='father_son.csv'
try:
    df=pandas.read_csv(fname)
    print(df.Father)    
except:pass    
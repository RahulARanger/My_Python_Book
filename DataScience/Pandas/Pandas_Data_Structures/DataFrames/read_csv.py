import pandas
import os
from tkinter import filedialog
try:
    name=filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (('CSV files','*.csv'),('Excel Files','*.xlsr'),("all files","*.*")))
    # plain conversion
    df=pandas.read_csv(name)
    print(df.head())
    print('\n')
    # it's indexes
    print(df.index.values)
    print()
    # after skipping a row
    df=pandas.read_csv(name,skiprows=1)
    print(df.head())
    print('\n')
    # after making a column as the index 
    df=pandas.read_csv(name,index_col=2)
    print(df.head())
    print('\n')
    
    
except:
    print('Error File Cannot be Opened ')

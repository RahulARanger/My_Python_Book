import pandas
from tkinter import filedialog
import os
# we can actually drop the rows that has the NaN values in them
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('CSV Files','*.csv'),('All Files','*.*')))
try:
    df=pandas.read_csv(name,skiprows=1,index_col=0)
    df=df.where(df['01 !']>0)
    print('Before Dropping the null rows now number of rows is: {}'.format(len(df)))
    print(df.head())
    print('\n')
    df_new=df.dropna()
    print('After Dropping the Null rows now the number of rows is: {} '.format(len(df_new)))
    print('\n')
    print(df_new.head())
except:pass    

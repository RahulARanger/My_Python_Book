import pandas
import numpy
import os
from tkinter import filedialog
# try to open the Olympics.csv
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('CSV Files','*.csv'),('All Files','*.*')))
try:
    df=pandas.read_csv(name,skiprows=1,index_col=0)
    for i in df.columns:
        if i[:2]=='01':
            df.rename(columns={i:'Gold'+i[4:]},inplace=True)
        elif i[:2]=='02':
            df.rename(columns={i:'Sliver'+i[4:]},inplace=True)
        elif i[:2]=='03':    
            df.rename(columns={i:'Bronze'+i[4:]},inplace=True)    
    print(df.head())       
    # this is a boolean mask
    print('\n')
    df_new=df.where(df['Gold']>0 and not numpy.isnan(df['Gold']))
    print(df_new.head(5))
    print('\n')
    # we can use where to create a new df based on the boolean mask

except:pass    
import pandas
from tkinter import filedialog
import os
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Files',filetypes=(('CSV Files','*.csv'),('All Files','*.*')))
try:
    df=pandas.read_csv(name,skiprows=1,index_col=0)
    print(df.head(5))
    for i in df.columns:
        if i[:2]=='01':
            df.rename(columns={i:'Gold'+i[4:]},inplace=True)
        elif i[:2]=='02':
            df.rename(columns={i:'Sliver'+i[4:]},inplace=True)
        elif i[:2]=='03':    
            df.rename(columns={i:'Bronze'+i[4:]},inplace=True)
    print('\n')
    print(df.head(5))
except:pass    
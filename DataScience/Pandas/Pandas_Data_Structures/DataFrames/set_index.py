import pandas
from tkinter import filedialog
import os
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('CSV Files','*.csv'),('All Files','*.*')))
df=pandas.read_csv(name,skiprows=1,index_col=0)
print()
df['Country']=df.index
df=df.set_index('Total')
print(df.head())
# resetting the indexes
print()
df=df.reset_index()
print(df.head())
print()
df=df.reset_index()
print(df.head())
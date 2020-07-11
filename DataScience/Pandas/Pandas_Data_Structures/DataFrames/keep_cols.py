import pandas
from tkinter import filedialog
import os
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('CSV Files','*.csv'),('All Files','*.*')))
df=pandas.read_csv(name,skiprows=1,index_col=0)
print(df.head())
print('\n')
lst=[i for i in input('Enter the Column names to keep them: (comma seperated) ').split(',')]
print('After Choosing : ')
print(df[lst].head())

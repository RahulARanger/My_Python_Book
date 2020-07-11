import pandas
import os
from tkinter import filedialog
name=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(('CSV File','*.csv'),('All Files','*.*')),title='Open File')
df=pandas.read_csv(name)
#before the multiple indexes
print(df.head())
print()
#after multiple indexes
df=df.set_index(['STNAME','CTYNAME'])
print(df.head())
print()
print()
# to access the parts we have to use this way
print(df.loc['Alabama','Bibb County'])
print()
print()
# for accessing the particular cell
print(df.loc['Alabama','Bibb County']['REGION'])
print()
print()
# the access level for the columns doesn't change at all
# now we can also create the hierarachal index to create that we have to know that
# by doing transpose the index will become the columns name and vice versa
df_transpose=df.T
print(df_transpose.head())
print()
    
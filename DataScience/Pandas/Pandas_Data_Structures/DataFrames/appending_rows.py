import pandas
import os
from tkinter import filedialog
#try opening the test.csv
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('CSV Files','.*csv'),('All Files','*.*')))
df=pandas.read_csv(name)
df=df.append({'2':'11','3':'12','4':'13'},ignore_index=True)
print(df)
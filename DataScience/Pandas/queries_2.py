import pandas,os
from tkinter import filedialog
# this is based on census.csv
name=filedialog.askopenfilename(title='Open File',initialdir=os.getcwd(),filetypes=(('CSV Files','*.csv'),('ALL Files','*.*')))
df=pandas.read_csv(name)
df_query=sorted(df['CENSUS2010POP'])
df_query.reverse()
df_query=df_query[:3]
names=[]
for i in df_query:
    name=df.where(df['CENSUS2010POP']==i).dropna()['STNAME']
    name=name.iloc[0]
    names.append(name)
print(names)    
print()
print()
print()
max_differnce=0
index=0
print(df[['POPESTIMATE2015','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2011','POPESTIMATE2010','POPESTIMATE2014']].max())
print(df[['POPESTIMATE2015','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2011','POPESTIMATE2010','POPESTIMATE2014']].min())

for i in df.index:
    lst=[]
    lst.append(df.iloc[i]['POPESTIMATE2015'])
    lst.append(df.iloc[i]['POPESTIMATE2014'])
    lst.append(df.iloc[i]['POPESTIMATE2013'])
    lst.append(df.iloc[i]['POPESTIMATE2012'])
    lst.append(df.iloc[i]['POPESTIMATE2011'])
    lst.append(df.iloc[i]['POPESTIMATE2010'])    
    diff=max(lst)-min(lst)
    if max_differnce<diff:
        max_differnce=diff
        index=i
print(df.iloc[index]['STNAME'])

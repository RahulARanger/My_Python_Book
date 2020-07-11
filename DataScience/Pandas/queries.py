import pandas
import os
from tkinter import filedialog
name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('CSV Files','*.csv'),('All Files','*.*')))
df=pandas.read_csv(name,skiprows=1,index_col=0)
print(df.head())
#print(df.where(df['01 !']>100).dropna().drop('Totals'))
df=df.drop('Totals')
# the one with the largest gold medals
print(df.where(df['01 !']==max(df['01 !'])).dropna())
print(df['01 !'].max())
print(df.max())
if 'Totals'  in df.index:
    print(df.drop('Totals'))
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)
print(df.head())            
print()
df_new=max(df['# Summer']-df['# Winter'])
#print(df.where())
print(df.where(df['# Summer']-df['# Winter']==df_new).dropna())
print()
print()
df_new=max((df['# Summer']-df['# Winter'])/len(df['Gold']))
print(df.where(((df['# Summer']-df['# Winter'])/len(df['Gold']))==df_new).dropna())

print()
print()
df_new=df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2']
print(df_new.head())
print(type(df_new))
# population status

import pandas
fname=input('Enter the File Name: ')
df,df_e=None,None
try:
    df=pandas.read_csv(fname)
except:pass
try:
    df_e=pandas.read_excel(fname)
except:pass
try:
    if df==None and df_e==None:
     print('Wrong Format')
     quit()
    elif df==None:
      df=df_e        
    else:pass
except:pass    
# print(type(df.columns)) this is of Index Type
print('columns in given file is:',list(df.columns))
    
import pandas
fname=input('Enter the File Name: ')
try:
    df=pandas.read_csv(fname)
    colors=['E','I']
    for index,i in enumerate(colors):
     print(df[df.color==i])
     print()
except:pass    

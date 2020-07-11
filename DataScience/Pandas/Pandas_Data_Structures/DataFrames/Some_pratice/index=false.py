import pandas
fname=input('Enter the file Name: ')
try:
    df=pandas.read_csv(fname)
    print(df)
    print('The index can be avoided in the save as file ')
    newfname=input('Save as: ')
    df.to_csv('without'+newfname)
    df.to_csv(newfname,index=False)
except:print('why')
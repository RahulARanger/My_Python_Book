import pandas
fname=input('Enter the File Name: ')
try:
    extension=fname[fname.find('.')+1:]
    newfname=input('Enter the new File name: ')
    print(extension)
    if extension=='csv':
        df=pandas.read_csv(fname)
        df.to_excel(newfname,index=False)
    elif extension=='xlsx':
        df=pandas.read_excel(fname)
        df.to_csv(newfname,index=False)
    else:
        print('Wrong Format')
except:pass    
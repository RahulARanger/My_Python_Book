import pandas
url=input('Enter the URL: ')
newfname=input('Enter the new File name: ')
extension=url[-3:]
try:
    if extension=='csv':
        df=pandas.read_csv(url)
        df.to_csv(newfname)
    elif extension=='xlsx':
        df=pandas.read_excel(url)
        df.to_excel(newfname)
    else:
        print('Wrong Format')
except:
    pass                
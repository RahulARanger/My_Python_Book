import pandas
index=[i for i in input('Cols. Names: ').split()]
n=int(input('Enter the Number of the Rows: '))
total=[]
for i in range(n):
    row={}
    for i in index:
        row[i]=input('{}: '.format(i))
        print()
    total.append(row)    
print('You have created a dataframe')
df=pandas.DataFrame(total)
print(df) 
   
    
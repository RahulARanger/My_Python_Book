# there are lot of ways to create a dataframe
# we can choose anything according to our convience
# first way is like the dictonary of lists wehere we will fill the values of the rows (column by column)
# second way is like the list of tuples where we will fill row by row (mostly used method)
import pandas
n=int(input('Enter the Number of Rows: '))
table=[]
print('Enter the Data in the Rows;')
for i in range(n):
    row=input().split()
    for i in range(len(row)):
        try:
            row[i]=int(row[i])
        except:
            pass
    table.append(tuple(row))
cols=input('Enter the Column names: ').split()
df=pandas.DataFrame(table,columns=cols)
newfname=input('New File(.csv) Name: ')
df.to_csv(newfname)         

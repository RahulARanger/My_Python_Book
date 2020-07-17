#in this program we will find the top 10 most occuring word in the test5.txt
name=input("Enter the Name of the file: ")
hand=open(name)
d={}
for i in hand:
    s=i.split()
    for j in s:
        d[j]=d.get(j,0)+1
lists=([(x,y) for y,x in d.items()])
lists=sorted(lists)
lists.reverse()
print('Rankings of the top 10 most occured words in the file \n \n ')
for i in  range(10):
    print('%d. place to \'%s\' which occured \'%d\' times'%(i+1,lists[i][1],lists[i][0]))
    
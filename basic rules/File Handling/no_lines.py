handler=open('test1.txt','r')
count=0
for i in handler:
    print(i,end='')
    count+=1
print('The total number of lines in the file is: %d'%count)    
#now the file handler reached to the end of the file hence it cannot read any data
inp=handler.read()
print(len(inp))#0 since this is at the end of the file
handler.close()
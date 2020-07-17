name=input("Enter the name of the File to be created: ")
hand=open(name,'w')
print('Enter the ctrl+z to stop writing')
str=' '
while(True):
#we used try and except to capture the eof exception
    try:
     str=input()+'\n'
     hand.write(str)
    except:
        break
hand.close() 
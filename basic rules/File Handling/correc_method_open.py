name=input('Enter The File Name to be opened: ')
try:
    hand=open(name)
except:
    print('The File doesn\'t exist')
    quit()
count=0    
print('The contents in the File is: ')
for i in hand:        
    count+=1
    print(i,end='')
print('')
print('The Total Number of the Lines in the File is: %d'%count)    
hand.close()

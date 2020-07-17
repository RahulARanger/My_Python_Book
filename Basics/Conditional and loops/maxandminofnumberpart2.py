large=small=None
while True:
    number=input('Enter any Number')
    try:
        n=int(number)
        if large is None:
            large=small=n
        if large<n:large=n
        if small>n:small=n    
    except:
        if number!='Done':
         print('Invalid input')
        else:
         break  
print('Maximum is',large)
print('Minimum is',small)             
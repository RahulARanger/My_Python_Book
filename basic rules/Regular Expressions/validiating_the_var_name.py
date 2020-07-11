import re
name=input('Enter the Variable name: ')
result=re.search(r'^[a-zA-Z_][a-z0-9A-Z_]*$',name)
if result is None:
    print('Invalid Name')
else:
    print('Valid Name')    
import re
# we are gonna accept a word with length extactly 6
main=input('Enter the a Word: ')
result=re.search(r'\b[a-zA-Z]{6}\b',main)
if result is None:
    print('Invalid Word')
else:
    print('Yes it is valid')    

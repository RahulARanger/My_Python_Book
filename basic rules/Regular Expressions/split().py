import re
main=input('Enter the main String: ')
result=re.split(r'[.?!]',main)
print(result)
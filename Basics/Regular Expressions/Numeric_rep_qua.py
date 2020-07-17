import re
# we can also give range to repeat in the regex
main=input('Enter the main String: ')
print(re.findall(r'[a-zA-Z]{5}',main))
print(re.findall(r'[a-zA-Z]{5,20}',main))
print(re.findall(r'[a-zA-Z]{,20}',main))

import re
main=input('Enter the main String: ')
# makes the . as the searching parameter
print(re.search(r'\.com',main))
# \w for matching the alphanumerc or underscore character
print(re.search(r'\w*','This_is an'))
# \d for matching the digit
print(re.search(r'\d*',main))
# \s for matching the space
print(re.findall(r'\s+',main))
# for counting the number of the words more efficiently and quickly
main=main.strip()
print('The number of the words is {} '.format(len(re.findall(r'\s+',main))+1))
import keyword
check=input('Enter the Word to check whether it is a Keyword or not: ')
print('Yes it is' if keyword.iskeyword(check) else 'No it\'s nt') 
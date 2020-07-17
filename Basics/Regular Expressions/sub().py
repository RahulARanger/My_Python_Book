import re
# sub() is used for replacing the strings with the sub string with the matched patterns
main=input('Enter the main String: ')
sub_string=input('Enter the String to replace with: ')
result=re.sub(r'[\w.%+-]+@[\w.-]+',sub_string,main)
print(result)
# remember that when we use the groups we can actually use \2 for referring to 2nd group or \1 ,... in regex 
# now we will use that to replace a string with a regex using a sub()
result=re.sub(r'',r'',main)
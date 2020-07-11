import re
main=input('Enter the main String: ')
sub='[0-9]'
# findall lists all the matched strings or returns empty list if it can't  find any
print(re.findall(r'{}'.format(sub),main))
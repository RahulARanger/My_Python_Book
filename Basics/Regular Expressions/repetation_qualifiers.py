import re
# we have two main repetatin qualifiers in python 
# they are * (minium rep:0) and + (minium rep:1)
main=input('Enter the main String: ')
print(re.search(r'Py.*n',main))
# there are lot of chances for the regex to become greedy
# refer greedy.py to remove that using a special way else prefer other regex patterns
print(re.search(r'[aA]+.*[aA]+',main))
# this make sures that they atleast two aS inside the main else returs None
# ? is another repetative qualifer which matches only a single character either true or False
print(re.search(r'p?',main))
#checks for p that's it
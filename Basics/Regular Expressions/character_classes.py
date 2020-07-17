import re
main=input('Enter the String: ')
# [abc] matches for single bit either if it's 'a'/'b' or 'c'
sub='[a-z,A-Z]way'
print(re.search(r'{}'.format(sub),main))
# to chcek whether there is a punction marks
print(re.search(r"[,:'.!?]",main))
#multiple sequences in []
# this one search for character being either alphabet or a number
print(re.search(r'[a-zA-z0-9]',main))
# ^ inside[] acts as a not operator 
# works as not only when used first inside [] else becomes the search character
print(re.search(r'[^0-9]',main))
# note the differnce
print(re.search(r'[w^0-9]',main))
# | acts as a or operator
# it's like the two regex and either one of them is accepted
print(re.search(r'[cC][aA][tT]|[dD][oO][Gg]',main))
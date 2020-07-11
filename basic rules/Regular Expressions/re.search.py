import re
main=input('Enter the String to be Searched for: ')
sub=input('Enter the Sub string to look for in the main: ')
ignorecase=bool(input('Do u want to Ignorecase (True/False):'))
if ignorecase:
   result=re.search(r'{}'.format(sub),main,re.IGNORECASE)
else:   
    result=re.search(r'{}'.format(sub),main)
if result is not None:
     print(result.pos)
     print(result.endpos)
else:
    print('The {} is not there in {} '.format(sub,main))   

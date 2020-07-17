# this is one of the ways to extract text from the data using the regular expresssions
import re
main=input('Enter the Main String: ')
results=re.search(r'(^\w*) (\w*) (\w*)$',main)
print(results)
if results is not None: 
    print(results[0])
    print(results[1])
    print(results[2])
    print(results[3])
    print(results.groups())
else:
    print('No Search Results Found')    
# grouping is only possible when the results is of match object typre else it will be an error
# () are the prime reasons for the existence of the groups
# the groups contain the matched string in the ()
# len(results.groups())==number of the parenthesis in the regex pattern
     
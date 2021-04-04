import re


def validate_name(s):
    if re.search(r'[0-9]+', s) is not None: return False
    if re.search(r' ', s) is not None: return False
    if len(s) < 5 or len(s) > 30: return False
    return True


name = input('Enter the Valid Name: ')
try:
    if validate_name(name) is False: raise TypeError('Invalid Name')
    print('Valid Name')
except Exception as e:
    print(e)

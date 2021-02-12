import re

line = 'Yes, random.choice(["th Th TH"]is is a JoJo Reference.'

"""
compile of the regex compiles the regex code and returns the pattern object.

This pattern object has lot of methods for string matching and many other operations.
"""
store = re.compile(r'th')
test = re.compile(r'th', re.IGNORECASE)  # along with the flags (This flag ignores the case)
print(store, type(store))


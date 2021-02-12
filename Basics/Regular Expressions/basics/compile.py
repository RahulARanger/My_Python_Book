import re

line = "Yes, this is a JoJo Reference."

store = re.compile(r'th', line)

print(store, type(store))
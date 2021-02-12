import re

store = re.compile(r'[\d]+')

print(store.findall("29-01-2021 17:30"))
import re

store = re.compile(r"[\w]+")

check1 = "Testing385794&**Testing"
check2 = "$%($%&#$**"

test = store.match(check1)
print(test)
print(store.match(check2))

print(test.start())
print(test.end())
print(test.group())
print(test.span())

print(dir(test))

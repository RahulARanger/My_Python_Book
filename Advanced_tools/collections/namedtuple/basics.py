import collections
Student=collections.namedtuple('Student',['Name',"Age"])
S=Student('Rahul',19)
print(S)
print(S.Name)
print(getattr(S,'Age'))
# namedtuple is immutable and Ordered
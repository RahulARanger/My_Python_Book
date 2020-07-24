import collections
Student=collections.namedtuple('Student',['Name',"Age",'Class'])
S=Student('Rahul',19,'k19hv')
# converts the namedtuple to the Dictionary
print(S._asdict())
print(type(S._asdict()))
new_s=S._replace(Age=20)
print(new_s)
# we cannot change the value of the keys byt we may change the values but it can only be done by creating/returning another namedtuple
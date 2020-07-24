import collections
Student=collections.namedtuple('Student',['Name',"Age",'Class'])
S=Student('Rahul',19,'k19hv')
# converts the namedtuple to the Dictionary(ordered at first)
print(S._asdict())
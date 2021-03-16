import collections
a=collections.Counter(a=2,b=3,c=0,d=-2)
print(a)
# displays the elements (keys)
print(sorted(a.elements()))
# displays the first n most commonly occuring elements
print(a.most_common(2))
# update will update or add the values based on the argument (which can be of the list,dict or Counter type)
b={'r':6,'s':9}
a.update(b)
print(a)
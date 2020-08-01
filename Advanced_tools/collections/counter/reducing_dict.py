import collections
a={4:3,3:3,2:3}
b={4:1,3:4,9:1}
_=collections.Counter(a)
__=collections.Counter(b)
print(dict(_-__))
# reduces the values of the keys in left (if common to right) else leaves as it is and removes if result<=0

# works as per our expectation using the keys of integer type
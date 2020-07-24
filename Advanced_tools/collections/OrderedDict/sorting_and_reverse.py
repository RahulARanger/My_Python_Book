import collections
a=collections.OrderedDict({1:'4',2:'3',3:'2',4:'1'})
print(sorted(a,reverse=True))
# we cannot use sort and reverse methods 
# sorting of OrderedDict is same as the Dictionary
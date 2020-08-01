import collections
a={1:2,2:3,3:6}
b={1:2,2:3}
c={}
c.update(a)
c.update(b) 
print('Updation using the update():',c)
c=collections.Counter()
c.update(a)
c.update(b) 
print('Updation using the collections.Counter()',dict(c))
# works only when the keys are of integer type
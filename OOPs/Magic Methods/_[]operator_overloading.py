class test:
    def __init__(self):
        self.lst=[int(i) for i in input('Enter the List Elements: ').split()]
    def __getitem__(self,key):
        return self.lst[key]
    def __setitem__(self,key,value):
        self.lst[key]=value
    def __str__(self):
        return str(self.lst)
    def __delitem__(self,key):
        del self.lst[key]
a=test()
print(a)
a[6]=6
# we can even slice it 
print(a[3:6])
print(a)
del a[3]
print(a)
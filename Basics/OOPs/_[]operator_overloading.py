class test:
    def __init__(self):
        self.lst=[int(i) for i in input('Enter the List Elements: ').split()]
    def __getitem__(self,key):
        return self.lst[key]
    def __setitem__(self,key,value):
        self.lst[key]=value
    def __str__(self):
        return str(self.lst)
a=test()
print(a)
a[6]=6
print(a)
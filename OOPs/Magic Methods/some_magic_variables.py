class test:
    ''' this is a testing class '''
    def __init__(self):
        self.__a=2
        self.b=3
print(test().b)
# ? obj._ class_name _ _privatemembername(without -) note: there is no space between _s in code 
print(test()._test__a)
f=test()
#print(f.__dict__())
#print(help(f))
#print(test().__class__.__name__)
print(test.__doc__)
print(test.__module__)
print(test.__dict__)

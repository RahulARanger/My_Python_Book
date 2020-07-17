class test:
    def print_this(self):
        print('Printed from the Base class')
class test_sub(test):
    def print_this(self,which_one):
        if which_one=='base': 
            super().test()
        else:
            print('Printed from sub class')        
test_sub().print_this('base')
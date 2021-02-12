
# ! when there is same elements in base and dervied class they are often treated as same

#! when there is same function names in base and dervied dervied ones will dominate (in dervied object)
#! but we can still refer tht in base class using super()

class A:
    def __init__(self):
        self.test=1
    def check(self):
        print('hi')
class B(A):
    def __init__(self):
        super().__init__()
        self.test+=2
    def check(self):
        super().check()
        print('bye')
a=B()
print(a.test)
a.check()

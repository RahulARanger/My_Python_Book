class A:
    a='a'
    def print_it(self):
        print(self.a)
x=A()
print(hasattr(A,'a'))
print(hasattr(A,'print_it'))
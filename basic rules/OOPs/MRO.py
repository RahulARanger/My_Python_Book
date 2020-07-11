class A:
    def __init__(self):
        self.a='A'
        super().__init__()
class B:
    def __init__(self):
        self.b='B'
        super().__init__()
class C(A,B):
    def __init__(self):
        self.c='C'
        super().__init__()
        
    def print_it(self):
        print(self.a)
        print(self.b)
        print(self.c)
x=C()
x.print_it()
print(hasattr(C,'print_it'))        
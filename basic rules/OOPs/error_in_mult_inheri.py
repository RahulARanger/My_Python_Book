class A:
    def __init__(self):
          self.a='A'
class B:
    def __init__(self):
         self.b='B'
class C(A,B):
    def __init__(self):
         self.c='C'
         super().__init__()
        
    def print_it(self):
        print(self.c)
        print(self.a)
        # print(self.b) this is an error because the constructor of the class B is never called from C 
x=C()

x.print_it()
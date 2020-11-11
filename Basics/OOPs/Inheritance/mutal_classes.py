class A:
    def fromA():
        print('Yes i am from the class A')
class B(A):
    def fromB():
        print('Yes I am from class B')        
class D:
    pass
class C(A,B):
    pass   
# error don't be oversmart
# we can't create a two classes which can share the data (methods,variables) or inherit in both ways


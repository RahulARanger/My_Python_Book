class A:
    pass
class B:
    pass
class C(A,B):
    pass
print(C.__bases__)
print(A.__bases__)
print(B.__bases__)
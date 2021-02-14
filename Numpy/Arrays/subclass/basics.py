import numpy

# ? Normally we cant easily subclass numpy arrays (since numpy.array is a function that returns numpy.ndarray)
# ? numpy.ndarray is also not easily inheritable (closer to c object)

# * so we decided to create a view object and then subclass that
# * a view of a numpy.array is just its view (whatever changes we make in it or in original object they both get affected)
# * view() is a method for the numpy arrays for creating the arrays

class test(numpy.ndarray):
    
    def __new__(self, *args, **kwargs):
        return numpy.ndarray.__new__( *args, **kwargs)

if __name__ == "__main__":
    a = test([1, 2, 3], dtype=int)
    print(type(a))
    print(a)
    
# ! Normally this fails this returns a TypeError
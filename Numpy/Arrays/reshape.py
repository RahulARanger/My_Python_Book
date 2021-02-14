import numpy
#! reshape() doesn't change the current array it returns the modified numpy.array
a = numpy.arange(36)
print(a)
b = a.reshape(6,6)
print(b)
print(a)
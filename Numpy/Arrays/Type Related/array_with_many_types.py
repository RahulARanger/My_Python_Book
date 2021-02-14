import numpy
class testing:
    pass
store = numpy.array([1, "check", testing()], dtype=object) 
# ? object makes the numpy array store multiple data types
print(store)
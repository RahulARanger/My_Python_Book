import numpy
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# we can do mutliple slicing for a row and a column in an array
# prints  5 6 8 9
print(a[1:,1:])
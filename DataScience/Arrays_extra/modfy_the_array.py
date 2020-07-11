# create an array
import numpy
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# after creating we have to lay a condition
# here we are gonna change the elements in the array where the elements > 3 will be rest to 6
print(a[a>3],end='\n')
print('ignored')
print(a,end='\n')
print()
a[a>3]=6
print(a)
print(type(a))


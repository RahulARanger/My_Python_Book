import numpy
# zip creates tuple of the list or arrays or any data type
a=numpy.array([1,2,3])
b=numpy.array([4,5,6])
c=numpy.array([7,8,9])
print('We can use any types other than arrays inside the zip()')
print('zip releases the zip object which can be converted to tuple or the list easily')
raw_d=zip(a,b,c)
for x,y,z in raw_d:
    print(x,y,z)
#d=list(raw_d)
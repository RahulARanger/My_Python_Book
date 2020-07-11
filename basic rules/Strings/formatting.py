# below ones is for indicating the existance of the positional arguments
print('{0} {2} {1} and again {0} {2} {1}'.format('Hello','Rahul','There')) 
# below ones is for variable arguments 
print('{name}, {color}, {quality}'.format(       
    name=input('Enter the Name of the Product: '),
    color=input('Color of the product: '),         
    quality=input('Quality: '))
 )
 # this is one is an error 
  #print('{}{}{}'.format(6,9)) because the there are three 
# decimal precision
f=float(input('Enter the Number: '))
d=int(input('Till Precision: '))
print('{0:.{1}f}'.format(f,d))
# some types in format component
print('{:b}'.format(3))
print('{:s}'.format('Hello'))
#below ones is for padding
print('{:60}'.format(696969))
# adjust ments
print('There are Six spaces after this {:>6} see'.format(69)) 
print('There are Six spaces after this {:<6} see'.format(69))
# dynamic indent
# first argument is for the argument to be printed
# second is for the number of spaces to be indented  to
i=6
print('{:{}}'.format(69,i)) 
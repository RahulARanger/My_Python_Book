# we can use a default method to print the description of the object
class Apple:
    ''' this class generally is generally the template for any apple using this we can store different kinds of apple'''
    color=''
    taste=''
    def __init__(self,name):
        self.name=name
        self.color=input('Color of the Apple: ')
        self.taste=input('Kind of taste: ')
    def __str__(self):
        # by default this returns the memory address of the object and the class name
        return ('This is an {} apple which is in {} color and has a {} taste'.format(self.name,self.color,self.taste))
Pro1=Apple(input('Enter the name of the Apple: '))
# now prints the description of the object
print(Pro1)
#help() uses the doc strings inside the class
print(help(Apple))

""" we can also use docstrings for the normal functions
    help(name_of_the_function)
    example:
    def wow():
        '''test'''
    print(help(wow))
     """
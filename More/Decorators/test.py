def check(func):
    print('se no~')
    a=2
    def call_this():
        func()
        print('The Value of a local variable in check() is:',a)
        print('Called a Wrapper Function')
    print('bye!')
    return call_this

@check
def test() -> None:
    print('Now this is the Test Function')

# now this will be easy and nice way to do the things as in why.py
print('object id: ',test) # ? this will execute the function check and prints the object id returned by the check()

test() # ! this will not execut the contents of the check() but executes the function returned by it


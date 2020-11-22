def check(func):
    def ohho():
        print('This is a Decorator Function')
        func()
    return ohho

def modified_func():
    print('imma gonna get modified')

modified_func=check(modified_func) # ? This is active form of the Decorder function in python # 1

modified_func()

@check # ? this is shorthand repr. of #1
def anotherfunc():
    print('another modifed function')
anotherfunc()
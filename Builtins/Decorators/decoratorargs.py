def check(a):
    print('Arguments passed to closure is:',a)
    def dec(func):
        print('This function is now the decorator')
        def wrapper(*args):
            print('Arguments for the wrapper function is:',args)
            func(*args)
        return wrapper
    return dec
@check(6)
def test(*args):
    print('Decorated this function')
test()
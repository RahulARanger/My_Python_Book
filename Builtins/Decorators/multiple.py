def dec1(func):
    def wrapper(*args):
        print('First Decorator')
        return func(*args)
    return wrapper

def dec2(func):
    def wrapper(*args):
        print('Second Decorator')
        return func(*args)
    return wrapper

@dec1
@dec2
def test(*args):
    print('Finished Decorating this function')
test()

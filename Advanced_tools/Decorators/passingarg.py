def check(func,*args,**kwargs):
    def wrapper():
        print('wrapped')
        func(*args,**kwargs)
    return wrapper
@check
def test(a,b):
    print(a,b)

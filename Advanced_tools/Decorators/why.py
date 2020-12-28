def check(func):
    print('se no~')
    def call_this():
        print('Called a Wrapper Function')
        func()
    return call_this

def test() -> None:
    print('Now this is the Test Function')

test()

print('test Object: ',check(test))

check(test)()


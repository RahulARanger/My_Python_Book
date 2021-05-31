def check(func):
    print('se no~')
    def call_this():
        func()
        print('Called a Wrapper Function')
    print('bye!')
    return call_this

@check # ? this first executes the check() and prints se no~
def test() -> None:
    print('Now this is the Test Function')
# ! The output will be produced even if we didnt include any line below this (due to that @check)

# now this will be easy and nice way to do the things as in why.py
print(69*'-')
print('object id: ',test) # ? this will execute the function check and prints the object id returned by the check()
print(69*'-')
test()



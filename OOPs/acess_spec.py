class test:
    def __init__(self):
        self.__name = 'Rahul'
        self._age = 20
        self.student = True

    def ask(self):
        return self.__name


a = test()
print('Student' if a.student else 'Not a Student')
try:
    print(a.__name)
except:
    print('You can\'t access private members directly')
try:
    print(a._age)
    # ! this _ variable actually means a protected member but it does allow access
    # and modification right outside the class
    # ? hence one shouldn't access tht directly (rules that one must follow quietly)
    a._age = 21
except Exception as e:
    print('You can view the protected members but u can\'t modify it')
print(a._age)

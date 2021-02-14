class Test:
    def __new__(cls, *args, **kwargs):
        # we can play the args or even reject the object creation (things that may not be present in __init__)
        print("Called the __new__ of: {}".format("test"))
        return super().__new__(cls)

    def __init__(self, *args):
        print("Called the constructor of the: {}".format("test"))


class Testing(Test):
    def __new__(cls, *args, **kwargs):
        print("Called the __new__ of: {}".format("testing"))
        if args[0] == 1:
            return super().__new__(cls)
        else:
            return object.__new__(cls)

    def __init__(self, *args):
        super().__init__()
        print("Called the constructor of the: {}".format("testing"))


s = Testing(1)
d = Testing(0)


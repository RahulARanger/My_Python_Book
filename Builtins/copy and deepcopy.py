import copy


# TODO: copy() allows us to copy the object but still all pointers/mutable objects like lists, custom class still
# TODO: make changes to the original ones

# TODO: deepcopy() creates entirely new object from the existing ones
# TODO: and changes in new ones doesn't affect old ones

# ! copy() takes small time but fails for reference objects

# ! deepcopy() may take more time but will be successful in creating an entire new object

class Test:
    def __init__(self, string_type="Rahul", list_type=None, dict_type=None):
        if list_type is None:
            list_type = [1, 2, 3]
        if dict_type is None:
            dict_type = {"module": "copy"}

        self.string_type = string_type
        self.dict_type = dict_type
        self.list_type = list_type

    def ids(self):
        print(f"""
Object: {id(self)},
list_type: {id(self.list_type)},
dict_type: {id(self.dict_type)},
string_type: {id(self.string_type)}
""")

    def modify_those(self):
        self.string_type = "check"
        self.list_type.extend([4, 5, 6])
        self.dict_type["built-ins"] = "True"

    def status(self):
        print(f"""
        list_type: {self.list_type},
        string_type: {self.string_type},
        dict_type: {self.dict_type}
        """)

    def bring_back(self):
        self.string_type = "Rahul"
        self.list_type = [1, 2, 3]
        self.dict_type = {"module": "copy"}


original = Test()

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original.ids()
shallow_copy.ids()
deep_copy.ids()

original.status()

# 1: shallow_copy can still modify the mutable types of the original copy
shallow_copy.modify_those()
original.status()
shallow_copy.status()
shallow_copy.bring_back()
original.bring_back()

# 2: deep copy is entirely other copy of the original ones
deep_copy.modify_those()
original.status()
deep_copy.status()
deep_copy.bring_back()

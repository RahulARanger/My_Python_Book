import copy

# TODO: copy() allows us to copy the object but still all pointers/mutable obects like lists, custom classe still
# TODO: make changes to the original ones

# TODO: deepcopy() creates entriely new object from the exisiting ones
# TODO: and changes in new ones doesn't affect old ones

# ! copy() takes small time but fails for reference objects

# ! deepcopy() may take more time but will be successfull in creating an entire new object

class Container:
    def __init__(self):
        self.lst=[1,2,3]
        self.index=0
    def copy(self):
        return copy.copy(self)
    def deepcopy(self):
        return copy.deepcopy(self)
    def __str__(self):return str(self.lst)+'  '+str(self.index)
test1=Container()
test2=test1
test3=test1.copy()
test4=test1.deepcopy()
test2.lst.append(6)
test2.index=6
test3.lst.append(9)
test3.index=3
test4.index=4
test4.lst.append(12)
print(test1,test2,test3,test4)

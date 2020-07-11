class CreateButton:
    def create_It(self):
        print('Created a first button')
class CreateAnotherButton:
    def create_It(self):
        super().create_It()
        print('Created a second button')
class WrapUp(CreateAnotherButton,CreateButton):
    def do_It(self):
        super().create_It()
a=WrapUp()
a.do_It()
print('Class order is {}'.format(WrapUp.mro()))
#  calls the first base class in the sub class which inherits the multiple base classes
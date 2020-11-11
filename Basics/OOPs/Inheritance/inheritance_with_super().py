class intro:
    class dob:
        def __init__(self):
            print('Enter the date of bith in the asked format;')
            self.day=input('Enter the Day: ')
            self.month=input('Enter the Month: ')
            self.year=input('Enter the Year: ')
        def print_it(self):
            print('Date of Birth: {}-{}-{} '.format(self.day,self.month,self.year))    
    def __init__(self,Person):
        print('Enter the {}\'s name: '.format(Person),end='')
        self.name=input()
        self.age=input('Age: ')
        self.gender=input('Gender: ')
        self.id=input('ID: ')
        self.x=self.dob()
    def describe_yourself(self):
        print('Name:',self.name)    
        print('Age:',self.age)
        print('Gender:',self.gender)
        print('ID:',self.id)
        self.x.print_it()
class student(intro):
    def __init__(self,Person='Student'):
        super().__init__(Person)
    def introduce(self):
        super().describe_yourself() # same as describe_yourself() since it is not a overloaded methods or we can also use super()
class teacher(intro):
    def __init__(self,Person='Teacher'):
        super().__init__(Person)
    def describe_yourself(self):
        super().describe_yourself()    
a=student()
a.introduce()
b=teacher()
b.describe_yourself()
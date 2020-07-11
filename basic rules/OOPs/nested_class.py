class me:
    def __init__(self):
        self.name=input('My Name: ')
        self.age=int(input('My Age: '))
        self.gender=input('Gender: ')
    class dob:
        def __init__(self):
            print('For Your Date of Birth: ')
            self.date=input('Enter the date: ')
            self.month=input('Enter the Month: ')
            self.year=input('Enter the Year: ')
    def display(self):
        x=me.dob() # we can also use x=self.dob()
        print('Name:',self.name)
        print('Age:',self.age)
        print('Gender:',self.gender)
        print('Date-of-birth:',x.date+'-'+x.month+'-'+x.year)
rahul=me()
rahul.display()                  
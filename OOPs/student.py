# we cannot declare the variables in a class but we can inside the methods
# we can use __init__ for the declaration and initialization purposes
class student:
    school_code=123 # static variable
    total=0 # static variable
    def __init__(self):
        self.name=input('Enter the name of the Student: ') # instance variable
        self.age=int(input('Enter the age of the student: '))# instance variable
        student.total+=1
    def display(self):
        print('Name:',self.name)# instance variable
        print('Age:',self.age)# instance variable
a=int(input('Enter the Number of the Students to be added to the database: '))
students={}
print('school code: ',student.school_code)
for i in range(a):
    roll=int(input('Enter the Roll number of the Student: '))
    students[roll]=student()
roll_no=int(input('Enter the Roll Number of the Student: '))
if roll_no in students:students[roll_no].display()
else: print('not there')
print('Total Number of the students: ',student.total)
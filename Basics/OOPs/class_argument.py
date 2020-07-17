class emp:
    def __init__(self):
        self.name=input('Enter the name of the employee: ')
        self.age=int(input('Enter the age: '))
        self.gender=input('Enter the gender: ')
        self.salary=int(input('Enter the salary of the employee: '))
    def status(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Gender: ',self.gender)
        print('Salary: ',self.salary)    
class update:
    @staticmethod
    def increase_salary(a):
        a.salary+=500000
        print('The salary of the employee has increased by 5,00,000')
emps=[]
for i in range(int(input('Enter the Number of the employees: '))):
       emps.append(emp())
       status=bool(input('Do You want to increase the salary of this employee (True/False): '))
       if status:
           update.increase_salary(emps[i])
       else:pass
       status=bool(input('Do you want to view the employee (True/False): '))    
       if status:
           emps[i].status()
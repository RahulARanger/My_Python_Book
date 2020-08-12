
# TODO: eval() takes the string format for the input of any object
# TODO: exec(statement) runs the statement
# * use this Site to know their difference: https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile
exec('''
name=input('Enter Your Name: ')
age=int(input('Enter Your Age: '))
print(name+','+' Your Age is: '+str(age))
''')
a=eval('[int(i) for i in input("Enter the Numbers: ").split()]')
eval('print(a)')
# ! output statements doesn't actually return anythin except None
a=compile('for i in range(6):print(i+1)','','exec')
exec(a)
a=compile('print("Hello there")','','eval')
eval(a)
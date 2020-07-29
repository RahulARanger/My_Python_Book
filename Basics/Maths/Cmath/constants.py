import cmath
while True:
    try:
        a=eval(input('Enter the Complex Number: '))
        if type(a)==complex:break
        else:print(1/0)
    except:
        print('Wrong Number!!! Please try Again')   
        continue
print('The real part of the Given Number is {} and Imaginary Number is {}'.format(a.real,a.imag))
print()
print('The Value of pie is {}'.format(cmath.pi))
print('The Value of Euler\'s Number is {}'.format(cmath.e))
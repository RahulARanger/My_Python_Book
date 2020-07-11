number=input('Enter any Number ')
try:
    intnumber=int(number)
    if intnumber%2==0:
        print('The Number is Even')
    else:
        print('The Number is Odd')
except:
    if type(number)==str:
        print('The entered value is a string')
    elif type(number)==float:
        print('The number given is Floating point values')
    else:
        print('the type u entered is something else that we are about to study in near future')      




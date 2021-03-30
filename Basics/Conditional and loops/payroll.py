hrs = input("Enter Hours:")
h = float(hrs)
extra = 0
if h > 40:
    extra = h - 40
    h = 40
rate = float(input('enter the rate: '))
payroll = rate * h
payroll += extra * rate * 1.5
print(payroll)

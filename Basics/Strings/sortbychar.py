string = input('Enter the String so that we can sort it by character by character: ')
check = [i for i in string]
check1 = sorted(check)
string = ''.join(check1)
print(string)

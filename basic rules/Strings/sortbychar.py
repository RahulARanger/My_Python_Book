str=input('Enter the String so that we can sort it by character by character: ')
check=[i for i in str]
check1=sorted(check)
str=''.join(check1)
print(str)
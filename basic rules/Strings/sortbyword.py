str=input('Enter some Sentence so that we can sort it word by word: ')
check=str.split(' ')
check1=sorted(check)
str=' '.join(check1)
print(str)
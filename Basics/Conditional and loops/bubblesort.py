import array as a

marks = a.array('i', [])
n = int(input('Enter the Number of the students '))

for i in range(n):
    print('Enter the Marks of the Student %d ', i + 1, ' ', end='')
    marks.append(int(input()))
    print('')
    
for i in range(len(marks)):
    for j in range(i + 1, len(marks)):
        if marks[i] > marks[j]:
            b = marks[i]
            marks[i] = marks[j]
            marks[j] = b

for i in marks:
    print(i, end=' ')

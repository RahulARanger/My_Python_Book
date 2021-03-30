import array as a

marks = a.array('i', [])
n = int(input('Enter the Number of students: '))
for i in range(n):
    print('Enter the Marks of the Student %d ' % (i + 1), ' ', end='')
    marks.append(int(input()))
    print('')
print('Enter the marks to search for that student id')
n = int(input())
print('The Index is : ', marks.index(n) + 1)

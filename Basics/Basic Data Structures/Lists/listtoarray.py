import array as m

marks = input().split(" ")
liste = [int(n) for n in marks]
sum = 0
student = m.array("i", liste)
for i in student:
    sum += i
print("The sum of the marks secured by the Student", sum)

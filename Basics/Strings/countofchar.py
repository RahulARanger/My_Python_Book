string = input()
count = 0
for i in string:
    if i.isalpha() is True:
        count += 1
print("The Number of the Characters in the String is: %d" % count)

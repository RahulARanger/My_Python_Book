name = input()
cat, hat = 0, 0
for i in range(len(name)):
    if name[i:i + 3] == 'cat':
        cat += 1
    elif name[i:i + 3] == 'hat':
        hat += 1
print(cat, hat)

def count():
    counter = {}
    print("Enter the name and press ctrl+z to stop writing the names")
    while True:
        try:
            name = input()
            counter[name] = counter.get(name, 0) + 1
        except:
            break
    m = 0
    index = None
    for x in counter:
        if counter[x] > m:
            m = counter[x]
            index = x
    print("The Name: %s occured most number of times (%d)" % (index, m))


if __name__ == "__main__":
    count()

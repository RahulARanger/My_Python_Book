from operator import itemgetter

# we can actually sort the multiple lists
def person_lister(f):
    names = []

    def inner(people):

        for i in range(len(people)):
            change = people[i]
            a = int(change[2])
            del change[2]
            change.insert(0, a)
            names.append(change)
        # print(names)
        names.sort(key=itemgetter(0))
        # print(names)

        if names[0][0] > names[len(names) - 1][0]:
            names.reverse()
            # print('yes')
        # print(names)
        for i in names:
            if i[3] == "M":
                print("Mr. " + i[1] + " " + i[2])
            else:
                print("Ms. " + i[1] + " " + i[2])

        return ""

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")

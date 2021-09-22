def key_value_interchange(d):
    list1 = list(d.items())
    list2 = []
    for x, y in list1:
        list2.append((y, x))
    return list2


def choice():
    print(
        "Do you want to Sort the Dictionary based on values or key press 1 or 2 respectively"
    )
    ch = int(input())
    if ch == 1 or ch == 2:
        return ch
    else:
        return choice()


if __name__ == "__main__":
    print("Enter the values of the Dictionary in the {} format ", end="")
    d = eval(input())
    ch = choice()
    if ch == 1:
        d = dict(key_value_interchange(d))
        d = dict(sorted(d.items()))
        d = dict(key_value_interchange(d))
    else:
        d = dict(sorted(d.items()))
    print(d)

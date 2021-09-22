from linked_list import SingleNode


# find the mid point of the singly linked list


def mid(test: "SingleNode"):
    speed = test

    while speed:
        speed = speed.next
        test = test.next

        speed = speed.next if speed else speed

        if not speed or not speed.next:
            return test

    return test


if __name__ == "__main__":
    sample1 = SingleNode()

    [sample1.append(SingleNode(_ * 6)) for _ in range(1, 31)]

    sample2 = SingleNode()

    [sample2.append(SingleNode(_ * 6)) for _ in range(1, 12)]

    print(sample1, sample2)

    print(mid(sample1).value)
    print(mid(sample2).value)

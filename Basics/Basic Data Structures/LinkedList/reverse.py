from linked_list import SingleNode


def reverse_list(test):
    prev = None

    while test:
        temp = prev

        prev = test
        test = test.next
        prev.next = temp

    return prev


Sample1 = SingleNode()

[Sample1.append(SingleNode(6 * _)) for _ in range(6)]

print(reverse_list(Sample1))

Sample1 = SingleNode()

[Sample1.append(SingleNode(6 * _)) for _ in range(9)]

print(reverse_list(Sample1))

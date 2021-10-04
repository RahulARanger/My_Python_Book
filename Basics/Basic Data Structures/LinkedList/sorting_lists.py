from linked_list import SingleNode


def sort_them(node: SingleNode):
    temp: SingleNode = node
    container = []
    while temp:
        container.append(SingleNode(temp.value))
        temp = temp.next

    del node

    length = len(container)
    container.sort(key=lambda x: x.value)

    for index in range(length):
        if index + 1 < length:
            container[index].next = container[index + 1]
    store = container[0]
    container.clear()

    return store

from linked_list import SingleNode

# returns true if there's cycle else False
def floyd_cycle(node: SingleNode):
    first = node
    second = node.next  # you can start with one step ahead but not always

    while second:
        if second.next:
            second = second.next.next
        else:
            return False

        first = first.next

        if first == second:
            return True

    return False


def cycle_length(node: SingleNode):
    pass

# we use two pointer method
from linked_list import SingleNode


def reverse_this(head: SingleNode):
    current = head
    if not current or head.next:
        return head  # no need to do anything

    step: SingleNode = head.next

    while step:
        temp = step.next  # save this for next iteration
        step.next = current
        current = step
        step = temp

    return current

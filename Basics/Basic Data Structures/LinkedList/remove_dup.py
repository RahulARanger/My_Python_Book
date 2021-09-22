from linked_list import SingleNode

# given a sorted singly linked list remove the duplicate elements

def remove_dup(test: SingleNode):
    while test:
        if not test.next:
            test = test.next
            continue
    
        if test.value == test.next.value:
            test.next = test.next.next
            
        else:
            test = test.next

Sample1 = SingleNode()
Sample1.append(SingleNode(6))
Sample1.append(SingleNode(6))
Sample1.append(SingleNode(12))
Sample1.append(SingleNode(12))
Sample1.append(SingleNode(18))
Sample1.append(SingleNode(18))


print(Sample1)

remove_dup(Sample1)

print(Sample1)

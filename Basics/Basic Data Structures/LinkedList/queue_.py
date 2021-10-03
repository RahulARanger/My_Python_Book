from linked_list import DoubleNode

# follows FIFO, first in first out
class Queue:
    def __init__(self, container=tuple()):
        super().__init__()

        self.head, self.tail = None, None

        for element in container:
            self.append(element)

    def empty(self):
        return not bool(self.head)

    def append(self, element):
        if not self.head:
            self.head = DoubleNode(element)
            self.tail = self.head
            return

        self.tail.append(DoubleNode(element))
        self.tail = self.tail.next

    def pop(self):
        if not self.head:
            return None

        store = self.head
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return store.value

    def __str__(self):
        return str(self.head)

    def front(self):
        """[summary] returns the first element of the queue"""
        return self.head.value if self.head else None

    def extend(self, queue: "Queue"):
        # O(N)

        while not queue.empty():
            self.append(queue.pop())

    def extend(self, queue: "Queue"):
        if not self.tail:
            self.tail = queue.head
        else:
            self.tail.append(queue.head)

    def peek(self):
        return self.head.value if self.head else None


class Deque:
    def __init__(self):
        self.head, self.tail = None, None

    def append(self, value):
        node = DoubleNode(value)
        if not self.head:
            self.head = node
        elif not self.tail:
            self.tail = node
            self.head.add_next(self.tail)
        else:
            self.tail.add_next(node)
            self.tail = node

    def extend(self, queue: "Deque"):
        self.tail.add_next(queue.head)
        self.tail = queue.tail

    def replace_head(self, value):
        if not self.head:
            return self.append(value)

        node = DoubleNode(value)
        node.value, self.head.value = self.head.value, node.value
        self.head.add_next(node)



if __name__ == "__main__":
    sample = Queue()

    sample.append(2)
    sample.append(3)

    print(sample.head)

    sample.pop()

    print(sample.head)

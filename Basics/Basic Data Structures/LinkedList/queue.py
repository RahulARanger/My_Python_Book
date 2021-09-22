from linked_list import DoubleNode

# follows FIFO, first in first out
class Queue:
    def __init__(self, container=tuple()):
        super().__init__()

        self.head, self.tail = None, None

        for element in container:
            self.append(element)

    def empty(self):
        return bool(self.head)

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


if __name__ == "__main__":
    sample = Queue()

    sample.append(2)
    sample.append(3)

    print(sample.head)

    sample.pop()

    print(sample.head)

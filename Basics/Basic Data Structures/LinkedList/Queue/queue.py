import sys
import os

sys.path.remove(__file__) if __file__ in sys.path else None
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from LinkedList.linked_list import DoubleNode

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

        self.head.delete_this()
        self.head = self.head.next

        if not self.head:
            self.tail = None

    def __str__(self):
        return str(self.head)


if __name__ == "__main__":
    sample = Queue()

    sample.append(2)
    sample.append(3)

    print(sample.head)

    sample.pop()

    print(sample.head)

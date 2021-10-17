from linked_list import DoubleNode
from collections import OrderedDict


class LRU:
    def __init__(self, cap):
        self.cache = {}
        self.head = None
        self.tail = None
        self.capacity = cap

    def set(self, key, value):
        if key in self.cache:
            self.removeNode(self.cache[key][0])
            self.set(key, value)
        else:
            node = DoubleNode(key)
            self.cache[key] = node, value

            if not self.tail:
                self.tail = self.head

            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node

            if len(self.cache) > self.capacity:
                self.removeTail()

        print(self.head, len(self.cache), "$", key)  # for testing

    def removeNode(self, node: DoubleNode):
        self.cache.pop(node.value)
        node.delete_this()
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev

    def removeTail(self):
        self.removeNode(
            self.tail if self.tail else self.head
        )  # in case it's size was 1

    def get(self, key):
        if key in self.cache:
            note =  self.cache[key][-1]
            self.set(self.cache[key][0].value, self.cache[key][-1])
            return note
        else:
            return -1


class OrderedLRU(OrderedDict):
    def __init__(self, cap):
        self.cap = cap
        self.length = 0

    def get(self, key):
        note = super().get(key, -1)
        if key in self:
            self.move_to_end(key, False)
        return note

    def set(self, key, value):
        self[key] = value
        self.move_to_end(key, False)

        if len(self) > self.cap:
            self.popitem(True)
        print(self)


if __name__ == "__main__":
    sample = LRU(4)
    sample.set(2, 3)
    sample.set(3, 4)
    sample.set(4, 5)
    sample.set(5, 6)
    sample.set(2, 3)
    sample.set(2, 3)

    print(sample.get(2))
    print(sample.get(3))

    sample = LRU(4)
    sample2 = OrderedLRU(4)
    data_set = "SET 97 30 GET 43 GET 13 SET 48 56 GET 67 GET 60 SET 74 43 SET 72 39 SET 100 59 GET 85 SET 91 62 GET 72 SET 1 4 GET 1 GET 53 GET 5 SET 59 60 SET 18 95 GET 37 GET 61 GET 15 SET 66 38 GET 22 GET 10 SET 33 1 GET 5 SET 57 59 SET 69 11 SET 29 70 SET 75 47 GET 6 GET 2 SET 68 90 GET 27 GET 39 SET 1 6 GET 58 GET 49 SET 8 18 SET 70 98 GET 29 SET 71 19 SET 81 93 GET 55 SET 44 8 GET 51 SET 89 86 GET 91 GET 35 SET 84 26 SET 43 95 GET 92 SET 21 21 GET 39 GET 93 GET 23 GET 86 GET 95 GET 9 GET 3 SET 23 85 SET 58 26 SET 93 3 GET 97 GET 31 GET 50 SET 57 13 SET 49 55 GET 29 GET 58 GET 77 SET 21 98 SET 6 95 GET 83 GET 24 SET 16 37 SET 54 85 SET 55 25 GET 37 GET 93 GET 59 GET 24".split(
        " "
    )
    length = len(data_set)
    index = 0
    while index < length:
        if data_set[index] == "SET":
            data = int(data_set[index + 1]), int(data_set[index + 2])
            # sample.set(data)
            sample2.set(*data)
            index += 3
        else:
            data = int(data_set[index + 1])
            # print(sample.get(data))
            print(sample2.get(data))
            index += 2

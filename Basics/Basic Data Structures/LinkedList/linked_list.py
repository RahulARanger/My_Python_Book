# Note;
"""
if we had tail reference for the singly linked list and doubly linked list
then we can insert or delete end with O(1)
"""


class SingleNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __getitem__(self, key):
        count = 0
        temp = self

        while temp:
            if count == key:
                return temp

            count += 1
            temp = temp.next

    def __iter__(self):
        self.temp = self
        return self

    def __next__(self):
        if not self.temp:
            raise StopIteration

        note = self.temp
        self.temp = self.temp.next if self.temp else None

        return note

    def pre_append(self, node: "SingleNode"):
        node.value, self.value = self.value, node.value
        node.next, self.next = self.next, node

    def insert(self, node: "SingleNode"):
        if self.is_empty():
            return self.replace_head(node)

        node.next, self.next = self.next, node

    def delete_child(self):
        node = self.next
        if not node:
            return None

        self.next, node.next = node.next, None
        return node

    def delete_this(self):
        temp = self.next
        store = self.value

        if temp:
            self.value, self.next = temp.value, temp.next
        else:
            del self
        return SingleNode(store)

    def delete_last(self):
        temp = self

        if self.is_empty():
            return None

        if not temp.next:
            return self.delete_this()

        while temp.next.next:
            temp = temp.next

        return temp.delete_child()

    def append(self, node: "SingleNode"):
        temp = self

        if self.is_empty():
            return self.replace_head(node)

        while temp.next:
            temp = temp.next

        temp.next = node

    def __str__(self):
        temp = self

        print("Singlely Linked List(", end="")

        while temp:
            print(temp.value, end=", ")
            temp = temp.next

        print(")", end="")
        return ""

    def length(self):
        temp = self
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def replace_head(self, node: "SingleNode"):
        self.value = node.value

    def is_empty(self):
        return not bool(self.value or self.next)

    def insert_at(self, index, value: "SingleNode"):
        if index == 0:
            return self.pre_append(value)

        temp = self[index - 1]
        temp.insert(value)

    def index(self, key):
        temp = self
        count = 0

        while temp:
            if temp.value == key:
                return count

            temp = temp.next
            count += 1

        return -1


class DoubleNode(SingleNode):
    def __init__(self, value=None):
        super().__init__(value)
        self.prev = None

    def pre_append(self, node: "DoubleNode"):
        if self.is_empty():
            return self.append(node)

        temp_next = self.next
        self.next, node.prev, node.next = node, self, temp_next

        if temp_next:
            temp_next.prev = node

        self.value, node.value = node.value, self.value

    def append(self, node: "DoubleNode"):
        temp = self

        while temp.next:
            temp = temp.next

        temp.next = node
        node.prev = temp

    def is_empty(self):
        return not (self.next or self.prev or self.value)

    def insert(self, index, key):
        pass

    def __str__(self):
        temp = self
        print("Doubly Linked List(", end="")

        while temp:
            print(temp.value, end=", ")
            temp = temp.next

        print(" )", end="")

        return ""

    def reverse(self):
        temp = self

        while temp:
            temp.next, temp.prev = temp.prev, temp.next

            if not temp.prev:
                return temp

            temp = temp.prev

    def delete_this(self):
        if self.is_empty():
            return

        if self.next:
            self.next.prev = self.prev

        if self.prev:
            self.prev.next = self.next

        return self.prev if self.prev else self.next

    def delete_last(self):
        temp = self

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None

        return temp.value


class CircularNode:
    def __init__(self, value=None):
        self.head, self.tail = None, None

        if value:
            self.append(SingleNode(value))

    def __getitem__(self, index):
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def pre_append(self, node: "SingleNode"):
        if not self.head:
            self.append(node)
        else:
            node.next = self.head
            self.head = node

            if self.tail:
                self.tail.next = self.head
            else:
                self.head.next = self.head

    def append(self, node: "SingleNode"):
        if not self.head:
            self.head = node
            self.head.next = self.head

        elif not self.tail:
            self.tail = node
            self.head.next = self.tail
            self.tail.next = self.head

        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

    def __str__(self):
        print("Singly Circular Node(", end="")
        temp = self.head

        while True:
            if temp:
                print(temp.value, end=", ")
                temp = temp.next

            if not temp or temp == self.head:
                break

        print(")")
        return ""

    def pop_front(self):
        if self.head == self.tail:
            self.head, self.tail = None, None
            return

        self.head = self.head.next
        self.tail.next = self.head

    def pop(self, index):
        if index == 0:
            return self.pop_front()

        if self.head == self.tail:
            self.head, self.tail = None, None
            return

        refer = self[index - 1]

        found = refer.next
        refer.next = found.next

        found.next = None

    def is_empty(self):
        return not self.head

    def test(self):
        print(
            self.head.value,
            self.head.next.value,
            self.head.next.next.value,
            self.head.next.next.next.value,
            self.head.next.next.next.next.value,
            "#$",
        )


class CircularDoublyNode:
    def __init__(self, value=None):
        self.head = None
        self.append(DoubleNode(value)) if value else None

    def append(self, node: "DoubleNode"):
        if self.head:
            tail = self.head.prev
            node.next = tail.next
            node.prev = tail

            tail.next = node
            tail.prev = node if tail.prev == tail else tail.prev

        else:
            self.head = node
            self.head.prev = self.head
            self.head.next = self.head

    def pre_append(self, node: "DoubleNode"):
        if not self.head:
            return self.append(node)

        node.next = self.head
        self.head.prev.next = node

        self.head.prev = node
        node.prev = self.head.prev

        self.head = node

    def __str__(self):
        return str(list(self.iter_them()))

    def iter_them(self):
        temp = self.head

        while True:

            if temp:
                yield temp.value

            temp = temp.next if temp else temp

            if not temp or temp == self.head:
                break


if __name__ == "__main__":

    Sample = SingleNode(6)
    Sample.insert(SingleNode(12))
    Sample.pre_append(SingleNode(18))
    Sample.insert(SingleNode(24))
    Sample.insert(SingleNode(30))

    # above all are O(1) in arrays it ain't O(1)

    Sample.append(SingleNode(36))
    Sample.append(SingleNode(48))
    Sample.append(SingleNode(54))  # O(n)

    print(Sample)
    print(Sample.length(), Sample.index(48), Sample.index(6), Sample.index(42))

    Sample.insert_at(6, SingleNode(42))  # O(index)

    print(Sample, "#$")
    print(Sample[1].value, Sample[0].value)

    for node in Sample:
        print(node.value, end=" ")
    print()

    Sample.delete_this()  # deletes the front node in O(1)
    print(Sample)

    Sample.delete_child()  # deletes the child of the head in O(1)
    print(Sample)

    Sample.delete_last()  # deletes the last element in O(n)
    print(Sample)

    Sample.delete_last()
    Sample.delete_last()
    Sample.delete_last()
    Sample.delete_last()

    print(Sample.is_empty())
    Sample.delete_last()

    print(Sample)

    print(Sample.is_empty())

    # Doubly Linked List

    Sample2 = DoubleNode(12)
    Sample2.append(DoubleNode(18))
    Sample2.append(DoubleNode(24))  # appends element O(n)
    Sample2.pre_append(DoubleNode(6))  # replaces head  # O(1)
    print(Sample2)
    Sample2 = Sample2.reverse()  # O(n)
    print(Sample2)

    print(Sample2.delete_last())
    print(Sample2)
    Sample2.delete_last()
    Sample2.delete_last()

    print(Sample2)

    Sample2.append(DoubleNode(6))

    print(Sample2)
    Sample2 = Sample2.delete_this()
    print(Sample2, Sample2.is_empty())

    Sample2 = Sample2.delete_this()
    print(Sample2)

    Sample3 = CircularNode(12)
    Sample3.append(SingleNode(18))
    Sample3.append(SingleNode(24))
    Sample3.pre_append(SingleNode(6))
    Sample3.pre_append(SingleNode(8))

    Sample3.test()

    print(Sample3)

    Sample3.pop_front()

    print(Sample3)
    Sample3.pop_front()
    Sample3.pop_front()
    Sample3.pop_front()
    print(Sample3)
    Sample3.pop_front()
    print(Sample3)

    Sample3.append(SingleNode(6))
    Sample3.append(SingleNode(12))
    Sample3.append(SingleNode(18))
    Sample3.append(SingleNode(24))
    Sample3.append(SingleNode(30))
    Sample3.append(SingleNode(36))
    Sample3.append(SingleNode(42))

    print(Sample3)
    Sample3.pop(6)
    print(Sample3)
    Sample3.pop(3)
    print(Sample3)

    Sample4 = CircularDoublyNode(6)
    print(Sample4)

    Sample4.append(DoubleNode(12))
    print(Sample4)

    Sample4.pre_append(DoubleNode(18))
    print(Sample4)

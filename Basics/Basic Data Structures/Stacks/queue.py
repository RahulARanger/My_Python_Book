from stack import Stack


class QueueUsingStackEasePush:
    def __init__(self):
        self.actual = Stack()

        self.backup = Stack()

    def push(self, value):
        self.actual.append(value)

    def pop(self):
        while self.actual:
            self.backup.append(self.actual.pop())

        store = self.backup.pop() if self.backup else False

        while self.backup:
            self.actual.append(self.backup.pop())

        return store


class QueueUsingStackEasePop(QueueUsingStackEasePush):
    def pop(self):
        return self.actual.pop() if self.actual else None

    def push(self, value):
        while self.actual:
            self.backup.append(self.actual.pop())

        self.backup.append(value)

        while self.backup:
            self.actual.append(self.backup.pop())

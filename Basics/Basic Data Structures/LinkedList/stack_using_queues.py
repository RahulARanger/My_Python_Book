from queue_ import Queue


class StackEasePush:
    def __init__(self):
        self.actual = Queue()
        self.backup = Queue()

    def push(self, x):
        self.actual.append(x)

    def pop(self):
        store = None

        while not self.actual.empty():
            store = self.actual.pop()
            if self.actual.empty():
                break
            self.backup.append(store)

        while not self.backup.empty():
            self.actual.append(self.backup.pop())

        return store


class StackEasePop(StackEasePush):
    def pop(self):
        return self.actual.pop()

    def push(self, x):
        pass

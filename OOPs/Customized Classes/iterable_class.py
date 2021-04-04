# two ways

class Test1:
    def __init__(self):
        self._lst = list(range(10))

    def __len__(self):
        return len(self._lst)

    def __iter__(self):
        self._count = 0
        return self

    def __next__(self):
        if self._count > len(self):
            raise StopIteration

        note = self._lst[self._count]
        self._count += 1
        return note


class Test2:
    def __init__(self):
        self._lst = list(range(10))

    def __len__(self):
        return len(self._lst)

    def __getitem__(self, item):
        return self._lst[item]


if __name__ == '__main__':

    cases = (Test1(), Test2())

    for case in cases:
        try:
            for _ in case:
                print(_, end=' ')

            print(f"iter: {iter(case)}, next: {next(case)}")  # fails for the Test2 class

        except Exception as e:
            print(e)

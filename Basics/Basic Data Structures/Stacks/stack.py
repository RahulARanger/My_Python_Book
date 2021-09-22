class Stack(list):
    # append is like push

    def push(self, value):
        return self.append(value)

    # pop works same as list's pop

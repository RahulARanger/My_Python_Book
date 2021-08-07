class Test:
    def __getitem__(self, index):
        return index

    def __setitem__(self, index, key):
        print(index, key)

    def __delitem__(self, key):
        print(key)


sample = Test()
print(sample["test"])

sample["pos"] = 69

del sample["del"]

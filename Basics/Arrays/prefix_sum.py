import array

class PrefixSumArray:
    def __init__(self, data_type, data):
        self._back = array.array(data_type, data)
        self._cache = []
    
    def __call__(self):
        return self._back

    def prepare(self):
        self._cache = [self._back[0]]
        
        for index in range(1, len(self._back)):
            self._cache.append(self._back[index] + self._cache[-1])
            
    def getSum(self, start, end):
        # O(1)
        return self._cache[end] if start == 0 else self._cache[end] - self._cache[start - 1]

sample1 = PrefixSumArray('i', [2, 8, 3, 9, 6, 5, 4])
sample1.prepare()

print(sample1.getSum(0, 2))
print(sample1.getSum(1, 3))
print(sample1.getSum(2, 6))

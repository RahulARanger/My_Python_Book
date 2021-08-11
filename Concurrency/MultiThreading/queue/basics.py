import queue

test = queue.Queue()

test.put("a")  # puts the item into the queue
test.put(1)
test.put(queue.Queue())

print(test.get())  # gets the first item

print(test.qsize())  # returns the length of the queue

print(test.get())
print(test.get())

print(test.empty())

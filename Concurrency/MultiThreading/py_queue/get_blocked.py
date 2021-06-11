import queue

check = queue.Queue()

check.put('a')
check.get()

print(check.get())  # this will be blocked forever

# this is very important feature

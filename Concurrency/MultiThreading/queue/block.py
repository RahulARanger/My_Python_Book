import queue

check = queue.Queue(maxsize=1)

check.put('a')
check.get()

try:
    print(check.get(block=False))  # this will be blocked forever
except queue.Empty:
    # prints quickly and it doesnt block
    print("Queue is empty! no work to do")

check.put('a')

try:
    check.put('b', block=False)
except queue.Full:
    # prints quickly and it doesnt block
    print("Queue if filled! wait")


# this is very important feature

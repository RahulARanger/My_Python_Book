import queue

check = queue.Queue(maxsize=1)

check.put('a')
check.get()

try:
    print(check.get(timeout=2))  # this will be blocked forever
except queue.Empty:
    # after a sec
    print("Queue is empty! no work to do")

check.put('a')

try:
    check.put('b', timeout=2)
except queue.Full:
    # after a sec
    print("Queue if filled! wait")


# this is very important feature

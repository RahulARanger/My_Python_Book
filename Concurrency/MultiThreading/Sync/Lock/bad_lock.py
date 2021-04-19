import threading

"""
Note:

1. we may forget to release the lock which results another threads which is like the infinite loop

2. when there's exception, it would also result the same so try to handle the exception caused inside the locked area
"""


def check_this():
    lock.acquire()
    print("locked")
    a, b = 1, 0
    print(a // b)
    lock.release()


lock = threading.Lock()
[threading.Thread(target=check_this).start() for _ in range(2)]

# This will run forever since we haven't released the lock when the exception raises
# This will make the other thread to wait forever

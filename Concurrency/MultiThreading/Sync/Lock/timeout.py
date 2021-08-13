import threading
import time

SAFE = threading.Lock()

'''
timeout is the argument for the acquire method of the lock, it takes float value(in millie seconds)
it makes the waiting thread to wait for at most for that much time.


if there are no waiting threads then the timeout does nothing

default value for the timeout is -1 (make the waiting thread for infinite amount of time)

'''


def sample():
    tried = SAFE.acquire(timeout=2)  # returns False if timeout expires

    if not tried:
        print(threading.currentThread(), "can't wait no more!")
        return

    print(threading.currentThread(), "preparing noodles")
    time.sleep(3)  # 3-minute noodles


for _ in range(2):
    threading.Thread(None, sample).start()
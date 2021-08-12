# we can see, a Lock object can be unlocked by any thread regardless of thread that locked it
# RLock can only be unlocked and locked by the same thread

import threading
import time

SAFE = threading.Lock()


def lock_it():
    SAFE.acquire()
    print("locked", threading.currentThread())

    while SAFE.locked():
        pass

    print("unlocked", threading.currentThread())


def unlock_it():
    time.sleep(2)
    print("unlocking", threading.currentThread())
    SAFE.release()


_ = threading.Thread(None, lock_it)
_.start()

__ = threading.Thread(None, unlock_it)
__.start()

import threading
import time


def test_this():
    # add some tasks that can be done concurrently
    # print(f"thread entered: {threading.currentThread().name}")
    lock.acquire()
    print("some")
    time.sleep(0.100)  # some other process
    print("message")
    lock.release()


lock = threading.Lock()  # lock is also a shared resource
note = [threading.Thread(target=test_this) for _ in range(6)]
[_.start() for _ in note]
print(lock.locked())  # says whether the lock is acquired or not at this instant


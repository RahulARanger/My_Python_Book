import threading

SAFE = threading.Lock()


def sample():
    with SAFE:  # acquire(timeout=None, blocking=True)
        print(threading.currentThread())
        print(1 / 0)  # in finally: it's released


for _ in range(3):
    threading.Thread(None, sample).start()

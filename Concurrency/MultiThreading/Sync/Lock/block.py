import threading
import time

SAFE = threading.Lock()


def sample():
    print("waiting", threading.currentThread())

    SAFE.acquire(blocking=False)  # default: TRUE
    # doesn't block even if locked

    print("entered", threading.currentThread())

    time.sleep(2)

    try:
        SAFE.release()
    except Exception as error:
        print(error)  # coz thread_1 releases and thread_2  releases unlocked lock


for _ in range(2):
    threading.Thread(None, sample).start()

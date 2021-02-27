import threading
import time


def all_threads():
    print(threading.enumerate())


def dummy_work():
    time.sleep(2)


for i in range(10):
    status = threading.Thread(target=dummy_work, name=f"Thread{i}")
    status.start()
    all_threads()



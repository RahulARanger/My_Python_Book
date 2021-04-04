import threading


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

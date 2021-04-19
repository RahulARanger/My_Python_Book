import threading


# good lock practices

def check_this():
    with lock:  # context switching is recommended
        a, b = 1, 0
        print("locked")
        try:
            print(a // b)
        except Exception as _:
            print(_)
        print("lock is released")


def also_this():
    try:
        lock.acquire()
        print("acquired lock for", threading.currentThread().name)
        a, b = 1, 0
        print(a / b)
    except ArithmeticError as error:
        print(error)
    finally:
        print("releasing lock")
        lock.release()


lock = threading.Lock()
[threading.Thread(target=check_this).start() for _ in range(2)]
[threading.Thread(target=also_this).start() for _ in range(2)]
# both are same

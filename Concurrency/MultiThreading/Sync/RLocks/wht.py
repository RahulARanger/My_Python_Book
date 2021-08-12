import threading

ABT = threading.RLock()
COUNT = 0


# * A RLock can be acquired by a single thread any number of times
# ! But it must be released same number of times to actually "unlock" that RLock

def test():
    global COUNT

    for _ in range(10):
        ABT.acquire()
        COUNT += 1
        print("lock count: ", COUNT, "by", threading.currentThread())

    print("unlock count: ", COUNT, "by", threading.currentThread())
    for _ in range(10):
        ABT.release()
        COUNT -= 1


def check():
    # waits until the first thread unlocks RLock
    with ABT:
        print("finally", threading.currentThread())


threading.Thread(target=test).start()
threading.Thread(target=check).start()

import threading

NUMBER = 0


def note():
    global NUMBER
    NUMBER += 1

    print(threading.local())  # local variables in current thread
    print(f"Current count: {NUMBER}")  # here they share the global elements


for _ in range(6):
    __ = threading.Thread(target=note)
    __.start()

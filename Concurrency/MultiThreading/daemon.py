import threading


def sample():
    print("test it here")
    print(threading.enumerate())


check = threading.Thread(target=sample, daemon=True)
check.start()
check.join()

print(threading.enumerate())
import threading


def note(*values):
    print("This are the values passed:", values)


check = threading.Thread(target=note, args=range(10))
check.start()

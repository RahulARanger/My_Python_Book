import threading

NUMBER = 0


def note():
    global NUMBER
    NUMBER += 1
    print(f"Current count: {NUMBER}")  # here they share the global elements


for _ in range(6):
    threading.Thread(target=note).start()

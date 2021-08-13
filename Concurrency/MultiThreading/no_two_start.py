import threading
import time


def say_no():
    print("In a thread")
    time.sleep(5)
    print("At the end of the thread")


note = threading.Thread(target=say_no, name="note1")

# a thread object is like a tissue paper
# after use, it can't be re-used unless recycled

note.start()

try:
    print(note.is_alive())
    note.start()
except Exception as error:
    print("Already was started", error)
note.join()

try:
    print(note.is_alive())
    note.start()
except Exception as error:
    print("Already was started", error)

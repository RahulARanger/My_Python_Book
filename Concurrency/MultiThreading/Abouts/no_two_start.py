import threading
import time


def say_no():
    print("In a thread")
    time.sleep(5)
    print("At the end of the thread")


note = threading.Thread(target=say_no, name="note1")
note.start()
try:
    print(note.is_alive())
    note.start()
except:
    print("Already was started")
note.join()
try:
    print(note.is_alive())
    note.start()
except:
    print("Already was started")

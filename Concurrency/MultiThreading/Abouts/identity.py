import threading
import time


# ident stores the identity of the Thread, it is None before the Thread starts. but after it starts,
# it will be of some value

# All running Threads has unique identity value. they may have the same name

def know_it():
    print("you are inside a thread")
    time.sleep(3)
    print("exiting the thread")


note = threading.Thread(target=know_it, name="checking")
note2 = threading.Thread(target=know_it, name="checking")

print(f"{note.name}: {note.ident}, {note2.name}: {note2.ident}")  # ident would be None if the  thread was not started
note.start()
note2.start()
# print(note.ident) same as the last line
note.join()
note2.join()
print(f"{note.name}: {note.ident}, {note2.name}: {note2.ident}")  # works as same as note2.get_indent()

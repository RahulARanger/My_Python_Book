import threading


def note():
    print(threading.currentThread())  # info about the current thread


note = threading.Thread(target=note, name='checking')
note.setName("checking again")
print(note.name)
# can also be note.get_name()
note.start()

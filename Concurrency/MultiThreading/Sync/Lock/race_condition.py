import threading
import time


def test_this():
    print("some")
    time.sleep(0.100)
    print("message")


note = [threading.Thread(target=test_this) for _ in range(2)]
[_.start() for _ in note]


"""
One of the sample Output:

some
some
some
some
some
some
message
messagemessage
messagemessagemessage




"""

"""
What's happening:
----------------

All threads try to access global print(), and print() responds by printing the some messages in single line
(those are from threads trying to access the print() at the same time)

and then prints the /n after that (see many blank lines)

Goal:
-----

When they are multiple threads trying to access global parameters like print() (especially when they are modfying it)

They need to wait until the thread that's using it finishes it's job.s

"""
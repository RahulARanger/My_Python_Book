# this is just to inform that python maintains GIL (Global Interpreter Lock)
# which doesn't allow different threads to modify the same python object at the same time
# when one thread tries to something on a object, it locks tht object
# so another thread has to wait until it can get the access


# so threading in python over same objects is not parallel

import threading
import time


def py_theorem(n):
    # CPU - bound process
    # GIL maintains Global lock for the CPU - bound processes

    return [
        (a, b, c)

        for c in range(n)
        for b in range(c)
        for a in range(b)

        if a ** 2 + b ** 2 == c ** 2
    ]


works = 200, 300

note1 = time.time()

py_theorem(works[0])
py_theorem(works[1])

note2 = time.time()

print(f"Main Thread takes: {note2 - note1}")

note2 = time.time()

person_1 = threading.Thread(target=py_theorem, args=(works[0],))
person_2 = threading.Thread(target=py_theorem, args=(works[1],))

person_1.start()
person_2.start()
person_1.join()
person_2.join()

note3 = time.time()

print("Multiple Threads takes:", note3 - note2)


# mostly we can it's greater than the single thread or closer to it
# GIL doesn't allow multiple threads to access CPU core at the same time for a single process

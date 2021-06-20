import time
import multiprocessing
import threading


def py_theorem(n):
    # CPU - bound process
    # GIL doesn't allow this in parallel execution

    return [
        (a, b, c)

        for c in range(n)
        for b in range(c)
        for a in range(b)

        if a ** 2 + b ** 2 == c ** 2
    ]


print(__name__)  # this changes for every process

if __name__ == '__main__':
    works = 300, 400  # multiprocessing has good effect over larger values

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

    # True parallelism

    note2 = time.time()

    person_1 = multiprocessing.Process(target=py_theorem, args=(works[0],))
    person_2 = multiprocessing.Process(target=py_theorem, args=(works[1],))

    person_1.start()
    person_2.start()

    person_1.join()
    person_2.join()

    note1 = time.time()

    print("MultiProcessing takes:", note1 - note2)

    person_2.close()
    person_1.close()



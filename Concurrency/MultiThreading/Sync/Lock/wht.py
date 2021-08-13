import threading
import time

# Solves Race Condition
SAFE = threading.Lock()
VALUE = 0
BAD = 0


def unsafe():
    global BAD

    # same as VALUE += 1 but hard way to show where it might fail

    temp = BAD
    time.sleep(1)  # in-reality, due to GIL, python swaps b/w threads for CPU-related threads
    # so it might swap here (who knows)
    BAD = temp + 1


def safe():
    global VALUE

    try:
        SAFE.acquire()

        temp = VALUE
        time.sleep(1)
        VALUE = temp + 1

    finally:
        SAFE.release()


def arrange(do_tht):
    collect = [
        threading.Thread(None, do_tht) for _ in range(10)
    ]

    tuple(
        (
            _.start() for _ in collect
        )
    )

    tuple(
        (
            _.join() for _ in collect
        )
    )


arrange(safe)
arrange(unsafe)

print(VALUE, BAD)
# see BAD <= VALUE

# RACE condition

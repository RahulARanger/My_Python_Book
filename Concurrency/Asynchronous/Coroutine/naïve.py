import time


def sample(delay, msg):
    time.sleep(delay)
    print(msg)


def this():
    sample(3, "Test 1")
    sample(2, "Test 2")


tok = time.time()
this()
print("Took:", time.time() - tok)  # naïve

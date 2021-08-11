import concurrent.futures
import threading
import time


# NOTE1 : add_done_callback is part of the code inside it's own thread
# i.e. if thread-1 created thread-2 add_done_callback is executed in thread-2


# NOTE2: ThreadPoolExecutor creates threads inside a queue
# so that they can be reused
# i.e when u create a thread, and after it's work that thread isn't dead it waits for the next thread
# so we don't need to create a thread again

def testing(_=None):
    print(threading.enumerate(), "#")


sample = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="test")
collect = []
for _ in range(2):
    collect.append(sample.submit(testing))
    collect[-1].add_done_callback(testing)

time.sleep(2)
print([_.running() for _ in collect])
print(threading.enumerate(), "3")  # we can see that past threads are done but they are still alive
sample.shutdown()
print(threading.enumerate(), "3")  # now its normal

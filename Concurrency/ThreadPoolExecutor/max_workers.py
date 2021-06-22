import concurrent.futures
import time


def work():
    print('started')
    time.sleep(3)
    print('ended')


sample = concurrent.futures.ThreadPoolExecutor(max_workers=2, thread_name_prefix="work")
sample.submit(work)
sample.submit(work)

sample.submit(work)  # this waits for the queue to end

import time
from concurrent.futures import ThreadPoolExecutor, Future


def test():
    print("testing this")
    time.sleep(2)
    return "got"


sample = ThreadPoolExecutor(thread_name_prefix="sample")
got: Future = sample.submit(test)
print(got.result(timeout=3))  # waits for the result (like the join)  # raise TimeoutError  (doesn't quit thread tho)


sample.shutdown(cancel_futures=True)  # refer: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown




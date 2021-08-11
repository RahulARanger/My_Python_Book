# [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)

ThreadPoolExecutor helps us to create a pool of threads, it internally maintains a queue, so we have limit for the number of threads


## Difference

Thread in [threading](https://docs.python.org/3/library/threading.html#module-threading), helps us to create a single thread.
But **Note: Creating or Destroying a thread is very costly**. So we can use ThreadPoolExecutor which will create a thread whenever necessary and that thread waits for another process.

so it won't be deleted and recreated unless we shut Executor down

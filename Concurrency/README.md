# Concurrency

One of the way to make our scripts use more core CPU / I/O resources


## MultiProcessing

We can achieve Parallelism through [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) or [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor).
But creating them can be costly.


## Multi Threading

We can also achieve Parallelism through [`threading`](https://docs.python.org/3/library/threading.html) or [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor).
Threads consume less space than process.

But creating them / deallocating them, is also costly, but relative process it's very less.

**For CPU-bound tasks, we cannot achieve pure Parallelism in python, due to GIL.**
we can however use multithreading to achieve parallelism for **I/O Bound tasks**.

## Reference

* https://medium.com/swift-india/concurrency-parallelism-threads-processes-async-and-sync-related-39fd951bc61d
* https://realpython.com/python-concurrency/
* https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
* https://realpython.com/python-concurrency/
* https://stackoverflow.com/questions/18114285/what-are-the-differences-between-the-threading-and-multiprocessing-modules
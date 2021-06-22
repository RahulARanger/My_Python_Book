import multiprocessing
import concurrent.futures

Store = 0


def process():
    global Store
    print(Store)
    Store += 1


if __name__ == "__main__":
    tests = (multiprocessing.Process(target=process) for _ in range(3))

    for _ in tests:
        _.start()

    # this will change the globals
    test2 = concurrent.futures.ProcessPoolExecutor(max_workers=3)
    for _ in range(3):
        test2.submit(process)

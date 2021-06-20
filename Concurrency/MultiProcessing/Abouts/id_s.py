import os
import multiprocessing


def introduce():
    print(multiprocessing.current_process(), ";")
    print("module:", __name__)
    print("process id:", os.getpid(), "parent process id:", os.getppid())

    # i guess parent id is the command line/ terminal 's ones
    # so it would be same unless and until we kill parent process


if __name__ == '__main__':
    introduce()
    test = multiprocessing.Process(target=introduce)
    test.start()
    test.join()
    test.close()

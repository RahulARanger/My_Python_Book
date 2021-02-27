import threading
import time


# This is same as calling work_1()

def work_1():
    print("This is just for", end='')
    time.sleep(2)
    # there 's a gap here (imagine there's a process that takes this much time)
    print(" Testing")


doing = threading.Thread(target=work_1)
doing.start()

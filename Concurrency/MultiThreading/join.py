import threading
import time


def work_1():
    print("Working...")
    time.sleep(2)


status = threading.Thread(target=work_1, name="checking")
status.start()
print(status.is_alive())
# This part of the main thread's code can executed in parallel
status.join()
# this part will only be executed only after the checking thread finishes
print("$", status.is_alive())

import threading
import time


def work_1():
    print("Working...")
    time.sleep(2)


status = threading.Thread(target=work_1, name="checking")
print(status.is_alive())
# ALWAYS FALSE
status.start()
print(status.is_alive())
# Maybe False if main thread executes before the checking Thread

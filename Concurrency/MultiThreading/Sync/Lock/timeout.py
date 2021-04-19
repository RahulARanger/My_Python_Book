import threading
import time
check = threading.Lock()

'''
timeout is the argument for the acquire method of the lock, it takes float value(in millie seconds)
it makes the waiting thread to wait for at most for that much time.


if there are no waiting threads then the timeout does nothing

default value for the timeout is -1 (make the waiting thread for infinite amount of time)

'''

def checking():
    print(f"{threading.currentThread().name} has entered")
    
    check.acquire(timeout=0.01)  # time out is 1 sec
    
    print(f"{threading.currentThread().name} has acquired the lock")
    time.sleep(3)  
    
normal_thread = threading.Thread(target=checking, name='first thread')
waiting_thread = threading.Thread(target=checking, name='last thread')
normal_thread.start()
waiting_thread.start()

normal_thread.join()
waiting_thread.join()
print(check.locked())  # proof of why timeout doesn't unlock if there are no waiting threads

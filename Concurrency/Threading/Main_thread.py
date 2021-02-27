import threading
print('The main thread that is created when we run this Program is:',threading.currentThread().getName())
name=input('Let\'s rename the main thread to : ')
threading.currentThread().setName(name)
# below ones we can use this current thread for any threads
print('The main thread that is created when we run this Program is:',threading.currentThread().getName())
# below ones this is only for the main_thread()
print('Another Way of Knowing the Main thread: ',threading.main_thread().getName())

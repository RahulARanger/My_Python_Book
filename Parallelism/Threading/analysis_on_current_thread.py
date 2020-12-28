import threading
# TODO: object that has the current thread
a=threading.current_thread()
# ? Name of the thread
print(a.getName())
print(dir(a))
# ? Returns the current number of the threads 
print(threading.active_count())
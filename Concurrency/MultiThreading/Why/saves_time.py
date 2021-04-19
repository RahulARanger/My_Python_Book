import threading
import time

NOTE = []


def some_process():
    global NOTE
    time.sleep(1)
    return NOTE.append(threading.current_thread().name)


def redo_that():
    tempo = []
    for _ in range(6):
        temp = threading.Thread(target=some_process)
        temp.start()
        tempo.append(temp)
    [_.join() for _ in tempo]   # waits for the threads to finish


note1 = time.time()
redo_that()
note2 = time.time()
print("Verification for the multithreading", NOTE)
NOTE.clear()

note3 = time.time()
[some_process() for _ in range(6)]
note4 = time.time()
print("Verification for this single thread", NOTE)

print(f"Multithreading takes: {note2 - note1}s but single thread takes: {note4 - note3}s")

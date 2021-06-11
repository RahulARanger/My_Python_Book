import threading
import time

NOTE = []


def some_process():
    # I-O bound process
    # GIL allows parallel execution of threads for I-O bound processes

    global NOTE
    NOTE.append(threading.current_thread().name)
    time.sleep(1)
    NOTE.append(str(threading.current_thread().name) + " done")


def redo_that():
    tempo = []
    for _ in range(6):
        temp = threading.Thread(target=some_process)
        temp.start()
        tempo.append(temp)

    [_.join() for _ in tempo]  # waits for the threads to finish


# thing is that when one thread sleeps, cpu just executes another thread
# very useful when the work has no relation among them
# if they had relation, we need to learn more to synchronize them

note1 = time.time()
redo_that()
print("over?")
note2 = time.time()
print("Verification for the multithreading", NOTE)
NOTE.clear()

note3 = time.time()
[some_process() for _ in range(6)]
note4 = time.time()
print("Verification for this single thread", NOTE)

print(f"Multithreading takes: {note2 - note1}s but single thread takes: {note4 - note3}s")

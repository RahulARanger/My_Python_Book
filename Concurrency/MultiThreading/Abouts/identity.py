import threading
import time

sample = threading.Thread(target=time.sleep, args=(1,), name="demo")
sample2 = threading.Thread(target=time.sleep, args=(1,))
print(sample.ident)  # will be none before starting it

print(sample.name, sample2.name)

sample.start()
sample2.start()

print(sample.ident, sample2.native_id)  # note this values will get recycled after this thread dies

sample.join()
sample2.join()

print(threading.get_ident(), threading.get_native_id())  # for current thread
# i guess both are same, heard second one is given by os and first one is like index in dict

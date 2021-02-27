import concurrent.futures,time
def print_this(range_):
    for i in range_:
        print(i)
a=concurrent.futures.ThreadPoolExecutor(max_workers=3)
check1=time.time()
a.submit(print_this,range(100))
a.submit(print_this,range(100,201))
check2=time.time()

a.shutdown()
check3=time.time()
print_this(range(100))
print_this(range(200))
check4=time.time()
print('Single Thread: {} and multithreading: {}'.format(check4-check3,check2-check1)) # ? You can see the huge difference
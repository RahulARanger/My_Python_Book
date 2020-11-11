import threading

def testing(num):
    for i in range(100):
        print(i)
def testing_(num):
    for i in range(100):
        print(100+i)
a=threading.Thread(target=testing,args=(2,))
b=threading.Thread(target=testing_,args=(6,))
a.start()
b.start()
b.join()
for i in range(100):
    print(i+200)
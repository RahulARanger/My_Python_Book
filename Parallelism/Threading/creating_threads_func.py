import threading
import os
def installations(a):
    for i in range(100):
        print(i)
def show_gif():
    for i in range(100):
        print(i+100)
a=threading.Thread(target=installations,args=(6,))
print('*',threading.active_count())
b=threading.Thread(target=show_gif)
a.start()
b.start()
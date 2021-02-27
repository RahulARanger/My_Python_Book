import threading
import time
class First(threading.Thread):
    def __init__(self,stre):
        threading.Thread.__init__(self)
        self.stre=stre
    def run(self):
        for i in range(1,7):
            print(i,self.stre)
lst=[]
for i in range(1,7):
    lst.append(First('Rahul'))
for i in range(6):
    print('******{}*****'.format(i+1))
    lst[i].start()
    print(lst[i].is_alive())
    lst[i].join() 
    print(lst[i].is_alive())
    
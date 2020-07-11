import threading
import time
def check(name):
    print('Running',name)
    print('Thread Name:',threading.currentThread().getName())
    time.sleep(3)
    print('Back to thread:',threading.currentThread().getName())
    print('end')
def skipped():
    print('Skipped2')
    print('The Thread Name:',threading.currentThread().getName())
def skiiped_part_two():
    print('The Thread Name:',threading.currentThread().getName())
    print('skipped3')     
c=threading.Thread(target=check,name='Actual',args=('Rahul',))
d=threading.Thread(target=skipped,name='Thread_skip_part_one')
e=threading.Thread(target=skiiped_part_two,name='Thread_skip_part_two')
c.start()
print('pause')
d.start()
d.join()
print('pause')
e.start()
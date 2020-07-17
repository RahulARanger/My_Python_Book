from ctypes import *
from time import * 
import threading
import msvcrt
STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
def charcater_count(s):
    print_at(80,6,str(len(s)))
def enter_it():
   overall=''
   while True: 
    s=(msvcrt.getch())
    s=s.decode()
    if s=='$':break
    else:
        overall+=s
        charcater_count(overall)
    sleep(0.1)
    
def time_print():
    while True:
        check=time()
        correct=ctime(check)
        print_at(80,25,correct)
        sleep(0.1)
    
length_thread=threading.Thread(target=enter_it,name='LENGTH')
time_thread=threading.Thread(target=time_print,name='TIME')
time_thread.start()
length_thread.start()
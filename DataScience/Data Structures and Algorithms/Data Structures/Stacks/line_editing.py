import itertools
from Stack import *
import msvcrt
def analyize(ch,a):
    if ord(ch)==13:
        return False
    else:
        if ord(ch)==8:
            a.pop()
        else:
            a.push(ch.decode())
        print(a.__str__(''))
    return True
if __name__=='__main__':
    a=Plate(10000000)
    for i in itertools.count(0):
        b=msvcrt.getch()
        if not analyize(b,a):
            print('\n')
            a.__str__('')
            break
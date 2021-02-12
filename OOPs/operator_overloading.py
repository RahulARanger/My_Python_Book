import re

import sys
class Complex:
    def __init__(self,answer):
        results=re.findall(r'[0-9]+',answer)
        #print(results)
        if len(results)==0:
            print('Incorrect Input Terminating...')
            sys.exit(0)
        if 'i' in answer:
            if len(results)==1:
                self.real=0
                self.imaginary=int(results[0])
            else:
                self.real=int(results[0])
                self.imaginary=int(results[1])
        else:
            self.real=int(results[0])
            self.imaginary=0
    def print_it(self):
        print('{} + {}i'.format(self.real,self.imaginary))
    def __add__(self,other):
        sum_result=str(self.real+other.real)+'+'+str(self.imaginary+other.imaginary)+'i'
        return sum_result
while True:
    print('let\'s add the two complex numbers: ')
    print('A: ',end='')
    a=Complex(input())
    print()
    print('B: ',end='')
    b=Complex(input())
    print()
    C=Complex(a+b)
    C.print_it()
    print('press q to quit else press any other key')
    ch=input()
    if ch=='q':break

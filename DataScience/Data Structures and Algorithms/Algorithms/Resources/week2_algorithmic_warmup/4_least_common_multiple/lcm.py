# Uses python3
import sys
import time

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    a,b=[int(i) for i in input().split()]
    check=time.time()
    print(lcm_naive(a, b))
    print(time.time()-check)
    



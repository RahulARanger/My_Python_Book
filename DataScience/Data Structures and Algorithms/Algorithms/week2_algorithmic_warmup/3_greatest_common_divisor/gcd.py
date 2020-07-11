# Uses python3
import sys
import time
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    a, b = [int(i) for i in input().split()]
    check=time.time()
    print(gcd_naive(a, b))
    print(time.time()-check)

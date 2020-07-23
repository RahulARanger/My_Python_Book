# Uses python3
import sys
import time
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    
    n = int(input())
    check=time.time()
    print(get_fibonacci_last_digit_naive(n))
    print(time.time()-check)

import math


def check_prime(n):
    if n < 4:
        return n > 1
    for prev in range(2, int(math.sqrt(n)) + 2):
        if n % prev == 0:
            return False
    return True


if __name__ == "__main__":
    print(check_prime(69))
    print(check_prime(601))

from sieve_eratosthenes import sieve_era


def bs_search(container, key):
    left, right = 0, len(container) - 1

    while left <= right:
        mid = (left + right) // 2

        if container[mid] == key:
            return True

        if container[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return False


def return_values(n):
    if n % 2 != 0:
        raise ValueError("It is not a Even Number")

    primes = sieve_era(n)

    for prime in primes:
        other = n - prime

        if bs_search(primes, other):
            return prime, other


if __name__ == "__main__":
    print(return_values(5250))

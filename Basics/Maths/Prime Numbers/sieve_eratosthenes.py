import math


def sieve_era(n):
    n += 1
    limit = [True for _ in range(n)]
    limit[0], limit[1] = False, False  # they can't be

    # since the last number can be determined within sqrt(n)
    for index in range(2, int(math.sqrt(n)) + 2):
        for fact in range(index * index, n):
            if fact % index == 0:
                limit[fact] = False

    return tuple(index for index in range(n) if limit[index])


if __name__ == "__main__":
    print(sieve_era(69))

"""Generator Expression Exercises."""
from collections.abc import Iterable
from itertools import zip_longest


def sum_all(container):
    """Return the sum of all numbers in the given list-of-lists."""
    return sum(sum(_) for _ in container)


def all_together(*args):
    """String together all items from the given iterables."""
    return (_ for __ in args for _ in __)


def interleave(i1, i2):
    """Return iterable of one item at a time from each list."""
    """
    for _ in zip(i1, i2):
        for __ in _:
            print(__)
    """

    return (__ for _ in zip_longest(i1, i2, fillvalue="") for __ in _ if __ != "")


def deep_add(__):
    return sum((deep_add(_) if isinstance(_, Iterable) else _ for _ in __))


def parse_ranges(ranges):
    """Return a list of numbers corresponding to number ranges in a string"""

    return (____ for __, ___ in (_.split("-") for _ in ranges.split(",")) for ____ in range(int(__), int(___) + 1))


def is_prime(n):
    """Return True if candidate number is prime."""
    return not any((n % _ == 0 for _ in range(2, int(n ** 0.5) + 2))) if n > 3 else True

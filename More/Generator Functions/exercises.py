"""Generator Function Exercises."""
from collections.abc import Iterable


def unique(container):
    """Yield iterable elements in order, skipping duplicate values."""
    collect = set()
    for _ in container:
        if _ not in collect:
            collect.add(_)
            yield _


def float_range(start, stop, step=1):
    """Return iterable of numbers from start to stop by step."""
    while start < stop:
        yield start
        start += step


def head(iterable, n):
    """Return first n items of a given iterable."""
    yield from iterable[: n]


def pairwise(container):
    """
    Yield a tuple containing each item and the item following it.

    The item after the last one is treated as ``None``.
    """
    limit = len(container)
    index = 0
    while index < limit:
        yield container[index], None if index + 1 >= limit else container[index + 1]
        index += 1


def around(container):
    """
    Yield a tuple of the previous, current, and next items.

    The previous item should start at ``None`` and the next item should
    be ``None`` for the last item in the iterable.
    """

    limit, index = len(container), 0

    while index < limit:

        yield None if index == 0 else container[index - 1], container[index], None if index + 1 >= limit else container[
            index + 1]
        index += 1


def stop_on(container, element):
    """Yield from the iterable until the given value is reached."""
    yield from container[: container.index(element) if element in container else None]


def deep_flatten(container):
    """Flatten an iterable of iterables."""
    for _ in container:
        if isinstance(_, Iterable):
            yield from deep_flatten(_)
        else:
            yield _


def get_primes_over(length):
    """Return given number of primes over 1,000,000."""
    index = 0
    starting = 1_000_003
    while index < length:
        if not any((starting % _ == 0 for _ in range(2, int(starting ** 0.5) + 2))):
            yield starting
            index += 1
        starting += 1


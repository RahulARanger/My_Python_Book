==============
Prime Numbers
==============

Prime Numbers are numbers that can't be divided by any number other than itself and 1.

Facts
-----

* 0 and 1 are not a prime Numbers
* Every Prime Number is of form ``(6 * n + 1)`` or ``(6 * n - 1)`` except 3 and 2
* 2 is the one even prime number
* No Prime Number is divisible by 5
* Product of Prime is known as semi primes


Prime Test
----------

Prime test enables us to check whether a positive integer is a prime or not.

Naive Method: **O(N)** check every numbers from 0 -> N - 1

But we can restrict our search within ``sqrt(n)``, that gives us time complexity: **O(sqrt(n))**

Sieve of Eratosthenes
---------------------

Using this algorithm, we can find prime numbers within a range ``(0, x]``.

* First we have a list of numbers with True (is a prime)
* Then check for the first ``sqrt(n)``. coz the last number can be proved prime or not based on the first number ``sqrt(n)`` numbers.
* Then for each check, modify the multiples of that number to False *(is not a prime number)*. We start with number * number, **since prev factors are already marked**.

GoldBach Conjecture
-------------------

It says, every even integer greater than 2 is a sum of two prime numbers. 

# -*- coding: utf-8 -*-
"""
Problem 37 - Truncatable primes
===============================

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in xrange(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if not is_prime(n) or n < 10:
        return False
    s = str(n)
    for i in xrange(1, len(s)):
        if not all(is_prime(n) for n in map(int, [s[:i], s[i:]])):
            return False
    return True

def gen_prime():
    i = 1
    yield 2
    yield 3
    while True:
        for n in (6 * i - 1, 6 * i + 1):
            if is_prime(n):
                yield n
        i += 1

sum = 0
count = 0
for prime in gen_prime():
    if count == 11:
        break
    if is_truncatable(prime):
        sum += prime
        count += 1
print sum

# Answer: 748317

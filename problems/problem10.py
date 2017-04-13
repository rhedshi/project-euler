# -*- coding: utf-8 -*-
"""
Problem 10 - Summation of primes
================================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
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
for prime in gen_prime():
    if prime < 2000000:
        sum += prime
    else:
        break
print sum

# Answer: 142913828922

# -*- coding: utf-8 -*-
"""
Problem 7 - 10001st prime
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10,001st prime number?
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

def nth_prime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    i = 1
    while True:
        for prime in (6 * i - 1, 6 * i + 1):
            n -= is_prime(prime)
            if n - 2 == 0:
                return prime
        i += 1

print nth_prime(10001)

# Answer: 104743

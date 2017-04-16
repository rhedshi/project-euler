# -*- coding: utf-8 -*-
"""
Problem 35 - Circular primes
============================

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
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

def rotate(n):
    p = []
    s = str(n)
    for i in xrange(len(s)):
        p.append(int(s[i:] + s[0:i]))
    return p

circular_primes = set([])
for i in xrange(2, 1000000):
    if i not in circular_primes:
        if all(is_prime(n) for n in rotate(i)):
            circular_primes.update(rotate(i))
print len(circular_primes)

# Answer: 55

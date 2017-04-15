# -*- coding: utf-8 -*-
"""
Problem 27 - Quadratic primes
=============================

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 ≤ n ≤ 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0 ≤ n ≤ 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
    where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
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

primes = []
for i in xrange(1000):
    if is_prime(i):
        primes.append(i)

m = 0
p = 0
for b in primes:
    for a in xrange(-999, 1000):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > m:
            m = n
            p = a * b
print p

# Answer: -59231

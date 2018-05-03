#!/usr/bin/env python3
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

from utils.prime import is_circular_prime, gen_prime

s = set()
for prime in gen_prime():
    if prime > 1000000:
        break
    if is_circular_prime(prime):
        s.add(prime)

print(len(s))

# Answer: 55

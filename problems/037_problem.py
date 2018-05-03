#!/usr/bin/env python3
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

from utils.prime import is_truncatable_prime, gen_prime

count = 0
sum = 0
for prime in gen_prime():
    if is_truncatable_prime(prime):
        sum += prime
        count += 1
    if count == 11:
        break

print(sum)

# Answer: 748317

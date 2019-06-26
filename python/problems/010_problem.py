#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 10 - Summation of primes
================================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils.prime import gen_prime

sum = 0
for prime in gen_prime():
    if prime > 2000000:
        break
    sum += prime

print(sum)

# Answer: 142913828922

# -*- coding: utf-8 -*-
"""
Problem 5 - Smallest multiple
=============================

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]
powers = [int(math.log(20) // math.log(p)) for p in primes]

print reduce(lambda x, y: x * y, map(lambda (p, a): p**a, zip(primes, powers)))

# Answer: 232792560

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 5 - Smallest multiple
=============================

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from functools import reduce
from math import log
import operator

primes = [2, 3, 5, 7, 11, 13, 17, 19]
powers = [
    int(log(20) // log(p))
    for p in primes
]

print(reduce(operator.mul, (n ** p for n, p in zip(primes, powers))))

# Answer: 232792560

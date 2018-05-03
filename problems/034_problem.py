#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 34 - Digit factorials
=============================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from utils.number import is_factorion

sum = 0
for n in range(10, 100000):
    if is_factorion(n):
        sum += n

print(sum)

# Answer: 40730

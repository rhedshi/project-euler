# -*- coding: utf-8 -*-
"""
Problem 34 - Digit factorials
=============================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

total = 0
for i in xrange(10, 1000000):
    if i == sum(map(lambda n: math.factorial(int(n)), str(i))):
        total += i
print total

# Answer: 40730

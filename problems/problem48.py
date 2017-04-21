# -*- coding: utf-8 -*-
"""
Problem 48 - Self powers
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

sum = 0
for i in xrange(1000):
    n = 1
    for j in xrange(i + 1):
        n *= i + 1
        n %= 10000000000
    sum += n
    sum %= 10000000000
print sum

# Answer: 9110846700

# -*- coding: utf-8 -*-
"""
Problem 9 - Special Pythagorean triplet
=======================================

A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which, a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which

a + b + c = 1000.

Find the product abc.
"""

def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2

for a in xrange(1, 999):
    for b in xrange(a + 1, 999):
        c = 1000 - a - b
        if is_pythagorean(a, b, c):
            print a * b * c

# Answer: 31875000

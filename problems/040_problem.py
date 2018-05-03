#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 40 - Champernowne's constant
====================================

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from functools import reduce
import operator

s = ''
i = 0
while len(s) < 1000001:
    s += str(i)
    i += 1

print(reduce(operator.mul, (int(s[10 ** i]) for i in range(7))))

# Answer: 210

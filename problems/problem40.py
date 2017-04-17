# -*- coding: utf-8 -*-
"""
Problem 40 - Champernowne's constant
====================================

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

i = 1
s = ''
while len(s) < 1000000:
    s += str(i)
    i += 1
print reduce(lambda x, y: x * y, [int(s[10**i - 1]) for i in xrange(7)])

# Answer: 210

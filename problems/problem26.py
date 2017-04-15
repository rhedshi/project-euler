# -*- coding: utf-8 -*-
"""
Problem 26 - Reciprocal cycles
==============================

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

 1/2 = 0.5
 1/3 = 0.(3)
 1/4 = 0.25
 1/5 = 0.2
 1/6 = 0.1(6)
 1/7 = 0.(142857)
 1/8 = 0.125
 1/9 = 0.(1)
 1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""
from operator import itemgetter

def frac_cycle_len(n, d):
    n %= d
    i = 0
    remainder = {}
    while n != 0 and n not in remainder:
        remainder[n] = i
        n = (n * 10) % d
        i += 1
    return i - remainder[n] if n != 0 else 0

def frac_to_str(n, d):
    if d == 0:
        return 'undefined'
    string = '' if n * d >= 0 else '-'
    n = abs(n)
    d = abs(d)
    string += str(n / d)
    n %= d
    if n == 0:
        return string
    else:
        string += '.'
    remainder = {}
    while n != 0 and n not in remainder:
        remainder[n] = len(string)
        n *= 10
        string += str(n / d)
        n %= d
    if n == 0:
        return string
    else:
        i = remainder[n]
        return string[:i] + '(' + string[i:] + ')'

print max([(i, frac_cycle_len(1, i)) for i in xrange(1, 1000)], key=itemgetter(1))[0]

# Answer: 983

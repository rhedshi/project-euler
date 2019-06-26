#!/usr/bin/env python3
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

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""

from utils.number import decimal_fraction


def len_cycle(fraction: str) -> int:
    """
    Returns the length of a recurring cycle in a string decimal fraction
    if there are any.
    """
    if fraction[-1] != ')':
        return 0
    else:
        return len(fraction) - fraction.find('(') - 1


max_cycle = 0
for d in range(1000):
    max_cycle = max(len_cycle(decimal_fraction(1, d)), max_cycle)

print(max_cycle)

# Answer: 983

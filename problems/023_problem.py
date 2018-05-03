#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 23 - Non-abundant sums
==============================

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

from utils.number import is_abundant

MAX_ABUNDANT_SUM = 28123
MIN_ABUNDANT_SUM = 24

abundant_nums = set()

sum = 0
for n in range(MAX_ABUNDANT_SUM):
    if is_abundant(n):
        abundant_nums.add(n)

    not_abundant_sum = True
    for a in abundant_nums:
        if n - a in abundant_nums:
            not_abundant_sum = False
            break

    sum += n if not_abundant_sum else 0

print(sum)

# Answer: 4179871

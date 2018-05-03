# -*- coding: utf-8 -*-
"""
Problem 1 - Multiples of 3 and 5
================================

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

print sum(set(range(0, 1000, 3) + range(0, 1000, 5)))

# Answer: 233168

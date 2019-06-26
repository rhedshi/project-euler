#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 32 - Pandigital products
================================

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from utils.number import is_pandigital

sum = 0
for N in range(1000, 10000):
    for i in range(1, int(N ** 0.5)):
        if N % i == 0 and is_pandigital(str(i) + str(N // i) + str(N)):
            sum += N
            break

print(sum)

# Answer: 45228

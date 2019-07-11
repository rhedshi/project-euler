#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 39 - Integer right triangles
====================================

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from utils.number import is_pythagorean

memoize = {}  # type: ignore

for a in range(1, 1001):
    for b in range(a + 1, 1001 - a):
        for c in range(b + 1, 1001 - a - b):
            if is_pythagorean(a, b, c):
                memoize[a + b + c] = memoize.get(a + b + c, 0) + 1

print(max(memoize, key=memoize.get))

# Answer: 840

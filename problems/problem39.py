# -*- coding: utf-8 -*-
"""
Problem 39 - Integer right triangles
====================================

If p is the perimeter of a right angle triangle with integral length sides,
{a, b, c}, there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2

triples = {}
for a in xrange(1, 1000):
    for b in xrange(a, 1000 - a):
        for c in xrange(b, 1000 - a - b):
            if is_pythagorean(a, b, c):
                triples[a + b + c] = triples.get(a + b + c, 0) + 1
print max(triples, key=triples.get)

# Answer: 840

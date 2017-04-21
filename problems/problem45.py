# -*- coding: utf-8 -*-
"""
Problem 45 - Triangular, pentagonal, and hexagonal
==================================================

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle    T_n = n(n + 1)/2    1, 3, 6, 10, 15, ...
Pentagonal  P_n = n(3n − 1)/2   1, 5, 12, 22, 35, ...
Hexagonal   H_n = n(2n − 1)     1, 6, 15, 28, 45, ...

It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

def gen_hexagonal(n=1):
    while True:
        yield n * (2 * n - 1)
        n += 1

for hexagon in gen_hexagonal():
    if hexagon == 1 or hexagon == 40755:
        continue
    n = int((2.0 * hexagon / 3)**0.5) + 1
    if n * (3 * n - 1) / 2 == hexagon:
        print hexagon
        break

# Answer: 1533776805

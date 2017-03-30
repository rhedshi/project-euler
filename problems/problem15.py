# -*- coding: utf-8 -*-
"""
Problem 15 - Lattice paths
==========================

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def choose(n, k):
    if 0 <= k <= n:
        N = 1
        K = 1
        for i in range(1, min(k, n - k) + 1):
            N *= n
            K *= i
            n -= 1
        return N / K
    else:
        return 0

print choose(40, 20)

# Answer: 137846528820

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 14 - Longest Collatz sequence
=====================================

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from utils.number import gen_collatz

memoize = {}  # type: ignore

for start in range(1, 1000000):
    length = 0
    for n in gen_collatz(start):
        if n in memoize:
            length += memoize[n]
            break
        length += 1
    memoize[start] = length

print(max(memoize, key=memoize.get))

# Answer: 837799

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 41 - Pandigital prime
=============================

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils.number import gen_permutation
from utils.prime import is_prime

digits = [9, 8, 7, 6, 5, 4, 3, 2, 1]

found = False
i = 0
while not found and i < len(digits):
    for permutation in gen_permutation(digits[i:]):
        n = int(''.join(map(str, permutation)))
        if is_prime(n):
            found = True
            print(n)
            break
    i += 1

# Answer: 7652413

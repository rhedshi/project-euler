# -*- coding: utf-8 -*-
"""
Problem 24 - Lexicographic permutations
=======================================

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""
import math

def kth_permutation(A, n, k):
    if n == 0:
        return ''
    i = (k - 1) / math.factorial(n - 1)
    return A[i] + kth_permutation(A[:i] + A[i + 1:], n - 1, k - i * math.factorial(n - 1))

print kth_permutation('0123456789', 10, 1000000)

# Answer: 2783915460

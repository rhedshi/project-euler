#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 4 - Largest palindrome product
======================================

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils.number import is_palindrome

product = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(x * y):
            product = max(product, x * y)

print(product)

# Answer: 906609

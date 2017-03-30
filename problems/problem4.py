# -*- coding: utf-8 -*-
"""
Problem 4 - Largest palindrome product
======================================

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

product = 0
for a in range(100, 1000):
    for b in range(a, 1000):
        product = max(a * b, product) if is_palindrome(a * b) else product
print product

# Answer: 906609

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 36 - Double-base palindromes
====================================

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from utils.number import is_palindrome

sum = 0
for n in range(1000000):
    if is_palindrome(n, base=10) and is_palindrome(n, base=2):
        sum += n

print(sum)

# Answer: 872187

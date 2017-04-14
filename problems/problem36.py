# -*- coding: utf-8 -*-
"""
Problem 36 - Double-base palindromes
====================================

The number, 585 (decimal) = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def is_palindrome(n, base=10):
    r = 0
    k = n
    while k > 0:
        r = r * base + k % base
        k /= base
    return n == r

print sum(filter(lambda n: is_palindrome(n, 2) and is_palindrome(n, 10), xrange(1000000)))

# Answer: 872187

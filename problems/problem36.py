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

def is_palindrome_bin(n):
    return bin(n)[2:] == bin(n)[-1:1:-1]

def is_palindrome_dec(n):
    return str(n) == str(n)[::-1]

print sum(filter(lambda n: is_palindrome_bin(n) and is_palindrome_dec(n), xrange(1000000)))

# Answer: 872187

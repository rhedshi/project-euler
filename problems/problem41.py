# -*- coding: utf-8 -*-
"""
Problem 41 - Pandigital prime
=============================

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in xrange(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def backtrack(digits, pandigital):
    if len(digits) == 0:
        if is_prime(int(''.join(pandigital))):
            return True
    for i in xrange(len(digits)):
        pandigital.append(digits[i])
        if backtrack(digits[:i] + digits[i + 1:], pandigital):
            return True
        pandigital.pop()
    return False

digits = '987654321'
prime = []
for i in xrange(len(digits)):
    if backtrack(digits[i:], prime):
        print ''.join(prime)
        break

# Answer: 7652413

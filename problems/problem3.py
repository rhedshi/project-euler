# -*- coding: utf-8 -*-
"""
Problem 3 - Largest prime factor
================================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(n):
    factor = 1
    while n % 2 == 0:
        n /= 2
        factor = 2
    for i in xrange(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n /= i
            factor = i
    return n if n != 1 else factor

print largest_prime_factor(600851475143)

# Answer: 6857

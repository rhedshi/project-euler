# -*- coding: utf-8 -*-
"""
Problem 32 - Pandigital products
================================

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

def is_pandigital(s):
    return ''.join(sorted(s)) == '123456789'

sum = 0
for n in xrange(1000, 10000):
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0 and is_pandigital(str(i) + str(n / i) + str(n)):
            sum += n
            break
print sum

# Answer: 45228

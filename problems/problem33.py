# -*- coding: utf-8 -*-
"""
Problem 33 - Digit cancelling fractions
=======================================

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""
import fractions

n = 1
d = 1
for a in xrange(1, 10):
    for b in xrange(a + 1, 10):
        for c in xrange(a + 1, 10):
            if 1.0 * (c * 10 + b) / (a * 10 + c) == 1.0 * b / a:
                n *= a
                d *= b
print d / fractions.gcd(n, d)

# Answer: 100

#!/usr/bin/env python3
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

from fractions import Fraction

f = Fraction(16, 64) * Fraction(19, 95) * Fraction(26, 65) * Fraction(49, 98)

print(f.denominator)

# Answer: 100

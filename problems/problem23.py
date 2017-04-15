# -*- coding: utf-8 -*-
"""
Problem 23 - Non-abundant sums
==============================

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

def sum_divisors(n):
    sum = 1
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i + (n / i if i != n / i else 0)
    return sum

def get_abundant_numbers(limit=28123):
    s = set([])
    for i in xrange(1, limit):
        if sum_divisors(i) > i:
            s.add(i)
    return s


abundant_numbers = get_abundant_numbers()
total = 0
for i in xrange(1, 28123):
    found = False
    for j in xrange(1, i / 2 + 1):
        if j in abundant_numbers and i - j in abundant_numbers:
            found = True
            break
    total += 0 if found else i
print total

# Answer: 4179871

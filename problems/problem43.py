# -*- coding: utf-8 -*-
"""
Problem 43 - Sub-string divisibility
====================================

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way,
we note the following:

 d_2d_3d_4 = 406 is divisible by 2
 d_3d_4d_5 = 063 is divisible by 3
 d_4d_5d_6 = 635 is divisible by 5
 d_5d_6d_7 = 357 is divisible by 7
 d_6d_7d_8 = 572 is divisible by 11
 d_7d_8d_9 = 728 is divisible by 13
 d_8d_9d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def check(s):
    z = zip([int(s[i:i + 3]) for i in xrange(1, 8)], [2, 3, 5, 7, 11, 13, 17])
    return all(n % p == 0 for (n, p) in z)

def backtrack(digits, pandigital, sum):
    if len(digits) == 0:
        if check(''.join(pandigital)):
            return int(''.join(pandigital))
        else:
            return 0
    for i in xrange(len(digits)):
        pandigital.append(digits[i])
        sum += backtrack(digits[:i] + digits[i + 1:], pandigital, 0)
        pandigital.pop()
    return sum

print backtrack('0123456789', [], 0)

# Answer: 16695334890

# -*- coding: utf-8 -*-
"""
Problem 17 - Number letter counts
=================================

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The
use of "and" when writing out numbers is in compliance with British usage.
"""

IS_BRITISH = True

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tweens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
bases = ['', 'thousand']

def num_to_str(n):
    string = ''
    base = 0
    while n > 0:
        number = ''
        i = n % 1000
        n /= 1000
        if 0 < i < 10:
            number += ones[i]
        if 10 <= i < 20:
            number += tweens[i % 10]
        if 20 <= i < 100:
            number += tens[i / 10] + ('-' + num_to_str(i % 10) if i % 10 > 0 else '')
        if 100 <= i < 1000:
            number += num_to_str(i / 100) + ' hundred' + \
                      ((' and ' if IS_BRITISH else ' ') + num_to_str(i % 100) if i % 100 > 0 else '')
        string = number + (' ' + bases[base] if base > 0 else '') + (' ' + string if len(string) > 0 else '')
        base += 1
    return string

total = 0
for i in xrange(1, 1001):
    total += len(num_to_str(i).replace(' ', '').replace('-', ''))
print total

# Answer: 21124

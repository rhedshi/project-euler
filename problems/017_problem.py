#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 17 - Number letter counts
=================================

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?



NOTE: Do not count spaces or hyphens.

For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.
"""

ONES = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
TWEENS = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]
TENS = [
    '',
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]
BASES = [
    '',
    'thousand',
    'million',
    'billion',
    # ...
]


def int_to_word(n: int, is_british: bool = True) -> str:
    """
    Returns the written word form of the number.
    """
    if n == 0:
        return 'zero'
    if n < 0:
        return f'negative {int_to_word(abs(n))}'

    base = 0
    word = ''
    while n > 0:
        buffer = ''
        m = n % 1000

        # Ones
        if 0 < m < 10:
            buffer = ONES[m]
        # Tweens
        if 10 <= m < 20:
            buffer = TWEENS[m % 10]
        # Tens
        if 20 <= m < 100:
            one = m % 10
            ten = m // 10
            if one == 0:
                buffer = TENS[ten]
            else:
                buffer = f'{TENS[ten]}-{ONES[one]}'
        # Hundreds
        if 100 <= m < 1000:
            ten = m % 100
            hundred = m // 100
            if ten == 0:
                buffer = f'{ONES[hundred]} hundred'
            else:
                _and_ = ' and ' if is_british else ' '
                buffer = f'{ONES[hundred]} hundred{_and_}{int_to_word(ten)}'

        # Add base suffix
        if m != 0:
            if base == 0:
                word = buffer
            else:
                word = f'{buffer} {BASES[base]} {word}'

        n = n // 1000
        base += 1

    return word


num_letters = 0
for n in range(1, 1001):
    num_letters += len(
        int_to_word(n)
            .replace(' ', '')  # noqa: E131
            .replace('-', ''),
    )

print(num_letters)

# Answer: 21124

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 31 - Coin sums
======================

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

from typing import List

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sum(coins: List[int], total: int) -> int:
    """
    Returns the number of ways to reach the total sum with the given
    set of coins.
    """
    memoize = [0] * (total + 1)
    memoize[0] = 1
    for coin in coins:
        for i in range(coin, total + 1):
            memoize[i] += memoize[i - coin]
    return memoize[total]


print(coin_sum(COINS, 200))

# Answer: 73682

# -*- coding: utf-8 -*-
"""
Problem 31 - Coin sums
======================

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_sum(coins, sum):
    memo = [0] * (sum + 1)
    memo[0] = 1
    for coin in coins:
        for i in xrange(coin, sum + 1):
            memo[i] += memo[i - coin]
    return memo[sum]

print coin_sum(coins, 200)

# Answer: 73682

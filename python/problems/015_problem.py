#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 15 - Lattice paths
==========================

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from utils.number import choose

print(choose(40, 20))

# Answer: 137846528820

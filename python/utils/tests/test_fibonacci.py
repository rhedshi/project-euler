#!/usr/bin/env python3

from typing import List
import unittest

from parameterized import parameterized

from utils.fibonacci import gen_fibonacci


class TestFibonacci(unittest.TestCase):
    @parameterized.expand([
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],),
    ])
    def test_gen_fibonacci(self, expected: List[int]) -> None:
        fibonacci = gen_fibonacci(zero=True)
        for i in expected:
            self.assertEqual(next(fibonacci), i)


if __name__ == '__main__':
    unittest.main()

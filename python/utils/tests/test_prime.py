#!/usr/bin/env python3

from typing import List, Optional
import unittest

from parameterized import parameterized

from utils.prime import (
    is_prime,
    is_circular_prime,
    is_truncatable_prime,
    gen_prime,
    nth_prime,
    prime_factors,
    largest_prime_factor,
)


class TestPrime(unittest.TestCase):
    @parameterized.expand([
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
    ])
    def test_is_prime(self, n: int, expected: bool) -> None:
        self.assertEqual(is_prime(n), expected)

    @parameterized.expand([
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (37, True),
        (79, True),
        (113, True),
        (197, True),
    ])
    def test_is_circular_prime(self, n: int, expected: bool) -> None:
        self.assertEqual(is_circular_prime(n), expected)

    @parameterized.expand([
        (2, False),
        (3, False),
        (5, False),
        (7, False),
        (23, True),
        (37, True),
        (53, True),
        (73, True),
        (313, True),
        (317, True),
        (373, True),
        (797, True),
        (3137, True),
        (3797, True),
        (739397, True),
    ])
    def test_is_truncatable_prime(self, n: int, expected: bool) -> None:
        self.assertEqual(is_truncatable_prime(n), expected)

    @parameterized.expand([
        ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],),
    ])
    def test_gen_prime(self, expected: List[int]) -> None:
        prime = gen_prime()
        for i in expected:
            self.assertEqual(next(prime), i)

    @parameterized.expand([
        (0, None),
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
        (6, 13),
        (7, 17),
        (8, 19),
        (9, 23),
        (10, 29),
    ])
    def test_nth_prime(self, n: int, expected: Optional[int]) -> None:
        self.assertEqual(nth_prime(n), expected)

    @parameterized.expand([
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2]),
        (5, [5]),
        (6, [2, 3]),
        (7, [7]),
        (8, [2]),
        (9, [3]),
        (10, [2, 5]),
        (11, [11]),
        (12, [2, 3]),
        (13, [13]),
        (14, [2, 7]),
        (15, [3, 5]),
    ])
    def test_prime_factors(self, n: int, expected: List[int]) -> None:
        self.assertEqual(prime_factors(n), expected)

    @parameterized.expand([
        (0, None),
        (1, None),
        (13195, 29),
        (600851475143, 6857),
    ])
    def test_largest_prime_factor(
        self,
        n: int,
        expected: Optional[int],
    ) -> None:
        self.assertEqual(largest_prime_factor(n), expected)


if __name__ == '__main__':
    unittest.main()

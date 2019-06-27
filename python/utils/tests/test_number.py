#!/usr/bin/env python3

from math import factorial
from typing import Any, List, Optional
import unittest

from parameterized import parameterized

from utils.number import (
    choose,
    gen_permutation,
    kth_permutation,
    cyclic_permutations,
    is_factorion,
    is_palindrome,
    is_lychrel,
    is_pandigital,
    is_pythagorean,
    is_square,
    is_triangular,
    gen_triangular,
    nth_triangular,
    is_pentagonal,
    gen_pentagonal,
    nth_pentagonal,
    is_hexagonal,
    gen_hexagonal,
    nth_hexagonal,
    divisors,
    num_divisors,
    sum_divisors,
    is_abundant,
    is_deficient,
    is_perfect,
    is_amicable,
    gen_collatz,
    decimal_fraction,
)


class TestNumber(unittest.TestCase):
    @parameterized.expand([
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 1),
        (1, 1, 1),
        (2, 1, 2),
        (3, 2, 3),
        (4, 2, 6),
        (5, 2, 10),
    ])
    def test_choose(self, n: int, k: int, expected: int) -> None:
        self.assertEqual(choose(n, k), expected)

    @parameterized.expand([
        (
            [],
            [
                [],
            ],
        ),
        (
            [1, 2, 3, 4],
            [
                [1, 2, 3, 4],
                [1, 2, 4, 3],
                [1, 3, 2, 4],
                [1, 3, 4, 2],
                [1, 4, 2, 3],
                [1, 4, 3, 2],
                [2, 1, 3, 4],
                [2, 1, 4, 3],
                [2, 3, 1, 4],
                [2, 3, 4, 1],
                [2, 4, 1, 3],
                [2, 4, 3, 1],
                [3, 1, 2, 4],
                [3, 1, 4, 2],
                [3, 2, 1, 4],
                [3, 2, 4, 1],
                [3, 4, 1, 2],
                [3, 4, 2, 1],
                [4, 1, 2, 3],
                [4, 1, 3, 2],
                [4, 2, 1, 3],
                [4, 2, 3, 1],
                [4, 3, 1, 2],
                [4, 3, 2, 1],
            ],
        ),
    ])
    def test_gen_permutation(
        self,
        items: List[Any],
        expected: List[List[Any]],
    ) -> None:
        permutation = gen_permutation(items)

        for item in expected:
            self.assertEqual(next(permutation), item)

        with self.assertRaises(StopIteration):
            next(permutation)

    @parameterized.expand([
        ([],),
        ([1, 2, 3, 4],),
    ])
    def test_kth_permutation(self, items: List[Any]) -> None:
        permutation = gen_permutation(items)

        N = len(items)
        for k in range(factorial(N)):
            self.assertEqual(kth_permutation(items, k + 1), next(permutation))

    @parameterized.expand([
        (
            0,
            [
                0,
            ]
        ),
        (
            111,
            [
                111,
            ],
        ),
        (
            123,
            [
                123,
                231,
                312,
            ],
        ),
        (
            3254,
            [
                2543,
                3254,
                4325,
                5432,
            ],
        ),
    ])
    def test_cyclic_permutations(self, n: int, expected: List[int]) -> None:
        self.assertEqual(cyclic_permutations(n), expected)

    @parameterized.expand([
        (1, True),
        (2, True),
        (145, True),
        (40585, True),
    ])
    def test_is_factorion(self, n: int, expected: bool) -> None:
        self.assertEqual(is_factorion(n), expected)

    @parameterized.expand([
        (1, None, True),
        (10, None, False),
        (101, None, True),
        (10, 2, False),
        (10, 8, False),
        (10, 10, False),
        (585, 2, True),
        (585, 8, True),
        (585, 10, True),
        (719848917, 2, True),
        (719848917, 8, True),
        (719848917, 10, True),
    ])
    def test_is_palindrome(
        self,
        n: int,
        base: Optional[int],
        expected: bool,
    ) -> None:
        if base is None:
            self.assertEqual(is_palindrome(n), expected)
        else:
            self.assertEqual(is_palindrome(n, base), expected)

    @parameterized.expand([
        (196, None, True),
        (349, None, False),
        (4994, None, True),
        (10677, 53, False),
    ])
    def test_is_lychrel(
        self,
        n: int,
        iterations: Optional[int],
        expected: bool,
    ) -> None:
        if iterations is None:
            self.assertEqual(is_lychrel(n), expected)
        else:
            self.assertEqual(is_lychrel(n, iterations), expected)

    @parameterized.expand([
        (123456789, False, True),
        (381654729, False, True),
        (987654321, False, True),
        (1023456789, True, True),
        (1234567890, True, True),
        (3816547290, True, True),
        (9876543210, True, True),
    ])
    def test_is_pandigital(
        self,
        n: int,
        zero: bool,
        expected: bool,
    ) -> None:
        self.assertEqual(is_pandigital(n, zero), expected)

    @parameterized.expand([
        (3, 4, 5, True),
        (5, 12, 13, True),
        (8, 15, 17, True),
        (7, 24, 25, True),
        (20, 21, 29, True),
        (12, 35, 37, True),
        (9, 40, 41, True),
        (28, 45, 53, True),
        (11, 60, 61, True),
        (16, 63, 65, True),
        (33, 56, 65, True),
        (48, 55, 73, True),
        (13, 84, 85, True),
        (36, 77, 85, True),
        (39, 80, 89, True),
        (65, 72, 97, True),
    ])
    def test_is_pythagorean(
        self,
        a: int,
        b: int,
        c: int,
        expected: bool,
    ) -> None:
        self.assertEqual(is_pythagorean(a, b, c), expected)

    @parameterized.expand([
        (0, True),
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
        (8, False),
        (9, True),
        (10, False),
    ])
    def test_is_square(self, n: int, expected: bool) -> None:
        self.assertEqual(is_square(n), expected)

    @parameterized.expand([
        (0, False),
        (1, True),
        (2, False),
        (3, True),
        (4, False),
        (5, False),
        (6, True),
        (7, False),
        (8, False),
        (9, False),
        (10, True),
    ])
    def test_is_triangular(self, n: int, expected: bool) -> None:
        self.assertEqual(is_triangular(n), expected)

    def test_is_triangular_zero(self) -> None:
        self.assertEqual(is_triangular(0, zero=True), True)
        self.assertEqual(is_triangular(0, zero=False), False)

    @parameterized.expand([
        ([0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55],),
    ])
    def test_gen_triangular(self, expected: List[int]) -> None:
        triangle = gen_triangular(zero=True)
        for i in expected:
            self.assertEqual(next(triangle), i)

    @parameterized.expand([
        (0, 0),
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (6, 21),
        (7, 28),
        (8, 36),
        (9, 45),
        (10, 55),
    ])
    def test_nth_triangular(self, n: int, expected: int) -> None:
        self.assertEqual(nth_triangular(n), expected)

    @parameterized.expand([
        (0, False),
        (1, True),
        (2, False),
        (3, False),
        (4, False),
        (5, True),
        (6, False),
        (7, False),
        (8, False),
        (9, False),
        (10, False),
        (11, False),
        (12, True),
        (13, False),
        (14, False),
        (15, False),
    ])
    def test_is_pentagonal(self, n: int, expected: bool) -> None:
        self.assertEqual(is_pentagonal(n), expected)

    def test_is_pentagonal_zero(self) -> None:
        self.assertEqual(is_pentagonal(0, zero=True), True)
        self.assertEqual(is_pentagonal(0, zero=False), False)

    @parameterized.expand([
        ([0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145],),
    ])
    def test_gen_pentagonal(self, expected: List[int]) -> None:
        pentagon = gen_pentagonal(zero=True)
        for i in expected:
            self.assertEqual(next(pentagon), i)

    @parameterized.expand([
        (0, 0),
        (1, 1),
        (2, 5),
        (3, 12),
        (4, 22),
        (5, 35),
        (6, 51),
        (7, 70),
        (8, 92),
        (9, 117),
        (10, 145),
    ])
    def test_nth_pentagonal(self, n: int, expected: int) -> None:
        self.assertEqual(nth_pentagonal(n), expected)

    @parameterized.expand([
        (0, False),
        (1, True),
        (2, False),
        (3, False),
        (4, False),
        (5, False),
        (6, True),
        (7, False),
        (8, False),
        (9, False),
        (10, False),
        (11, False),
        (12, False),
        (13, False),
        (14, False),
        (15, True),
    ])
    def test_is_hexagonal(self, n: int, expected: bool) -> None:
        self.assertEqual(is_hexagonal(n), expected)

    def test_is_hexagonal_zero(self) -> None:
        self.assertEqual(is_hexagonal(0, zero=True), True)
        self.assertEqual(is_hexagonal(0, zero=False), False)

    @parameterized.expand([
        ([0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190],),
    ])
    def test_gen_hexagonal(self, expected: List[int]) -> None:
        hexagon = gen_hexagonal(zero=True)
        for i in expected:
            self.assertEqual(next(hexagon), i)

    @parameterized.expand([
        (0, 0),
        (1, 1),
        (2, 6),
        (3, 15),
        (4, 28),
        (5, 45),
        (6, 66),
        (7, 91),
        (8, 120),
        (9, 153),
        (10, 190),
    ])
    def test_nth_hexagonal(self, n: int, expected: int) -> None:
        self.assertEqual(nth_hexagonal(n), expected)

    @parameterized.expand([
        (1, True, []),
        (2, True, [1]),
        (3, True, [1]),
        (4, True, [1, 2]),
        (5, True, [1]),
        (6, True, [1, 2, 3]),
        (7, True, [1]),
        (8, True, [1, 2, 4]),
        (9, True, [1, 3]),
        (10, True, [1, 2, 5]),
        (11, True, [1]),
        (12, True, [1, 2, 3, 4, 6]),
        (13, True, [1]),
        (14, True, [1, 2, 7]),
        (15, True, [1, 3, 5]),
        (1, False, [1]),
        (2, False, [1, 2]),
        (3, False, [1, 3]),
        (4, False, [1, 2, 4]),
        (5, False, [1, 5]),
        (6, False, [1, 2, 3, 6]),
        (7, False, [1, 7]),
        (8, False, [1, 2, 4, 8]),
        (9, False, [1, 3, 9]),
        (10, False, [1, 2, 5, 10]),
        (11, False, [1, 11]),
        (12, False, [1, 2, 3, 4, 6, 12]),
        (13, False, [1, 13]),
        (14, False, [1, 2, 7, 14]),
        (15, False, [1, 3, 5, 15]),
    ])
    def test_divisors(self, n: int, proper: bool, expected: List[int]) -> None:
        self.assertEqual(divisors(n, proper), expected)

    @parameterized.expand([
        (1, True, 0),
        (2, True, 1),
        (3, True, 1),
        (4, True, 2),
        (5, True, 1),
        (6, True, 3),
        (7, True, 1),
        (8, True, 3),
        (9, True, 2),
        (10, True, 3),
        (11, True, 1),
        (12, True, 5),
        (13, True, 1),
        (14, True, 3),
        (15, True, 3),
        (1, False, 1),
        (2, False, 2),
        (3, False, 2),
        (4, False, 3),
        (5, False, 2),
        (6, False, 4),
        (7, False, 2),
        (8, False, 4),
        (9, False, 3),
        (10, False, 4),
        (11, False, 2),
        (12, False, 6),
        (13, False, 2),
        (14, False, 4),
        (15, False, 4),
    ])
    def test_num_divisors(self, n: int, proper: bool, expected: int) -> None:
        self.assertEqual(num_divisors(n, proper), expected)

    @parameterized.expand([
        (1, True, 0),
        (2, True, 1),
        (3, True, 1),
        (4, True, 3),
        (5, True, 1),
        (6, True, 6),
        (7, True, 1),
        (8, True, 7),
        (9, True, 4),
        (10, True, 8),
        (11, True, 1),
        (12, True, 16),
        (13, True, 1),
        (14, True, 10),
        (15, True, 9),
        (1, False, 1),
        (2, False, 3),
        (3, False, 4),
        (4, False, 7),
        (5, False, 6),
        (6, False, 12),
        (7, False, 8),
        (8, False, 15),
        (9, False, 13),
        (10, False, 18),
        (11, False, 12),
        (12, False, 28),
        (13, False, 14),
        (14, False, 24),
        (15, False, 24),
    ])
    def test_sum_divisors(self, n: int, proper: bool, expected: int) -> None:
        self.assertEqual(sum_divisors(n, proper), expected)

    @parameterized.expand([
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (5, False),
        (6, False),
        (7, False),
        (8, False),
        (9, False),
        (10, False),
        (11, False),
        (12, True),
        (13, False),
        (14, False),
        (15, False),
    ])
    def test_is_abundant(self, n: int, expected: bool) -> None:
        self.assertEqual(is_abundant(n), expected)

    @parameterized.expand([
        (1, True),
        (2, True),
        (3, True),
        (4, True),
        (5, True),
        (6, False),
        (7, True),
        (8, True),
        (9, True),
        (10, True),
        (11, True),
        (12, False),
        (13, True),
        (14, True),
        (15, True),
    ])
    def test_is_deficient(self, n: int, expected: bool) -> None:
        self.assertEqual(is_deficient(n), expected)

    @parameterized.expand([
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (5, False),
        (6, True),
        (7, False),
        (8, False),
        (9, False),
        (10, False),
        (11, False),
        (12, False),
        (13, False),
        (14, False),
        (15, False),
    ])
    def test_is_perfect(self, n: int, expected: bool) -> None:
        self.assertEqual(is_perfect(n), expected)

    @parameterized.expand([
        (220, 284, True),
        (1184, 1210, True),
        (2620, 2924, True),
        (5020, 5564, True),
        (6232, 6368, True),
        (10744, 10856, True),
        (12285, 14595, True),
        (17296, 18416, True),
        (63020, 76084, True),
    ])
    def test_is_amicable(self, a: int, b: int, expected: bool) -> None:
        self.assertEqual(is_amicable(a, b), expected)

    @parameterized.expand([
        (1, [1]),
        (2, [2, 1]),
        (3, [3, 10, 5, 16, 8, 4, 2, 1]),
        (4, [4, 2, 1]),
        (5, [5, 16, 8, 4, 2, 1]),
        (6, [6, 3, 10, 5, 16, 8, 4, 2, 1]),
    ])
    def test_gen_collatz(self, start: int, expected: List[int]) -> None:
        collatz = gen_collatz(start)

        for i in expected:
            self.assertEqual(next(collatz), i)

        with self.assertRaises(StopIteration):
            next(collatz)

    @parameterized.expand([
        (0, 1, '0'),
        (1, 1, '1'),
        (1, 2, '0.5'),
        (1, 3, '0.(3)'),
        (1, 4, '0.25'),
        (1, 5, '0.2'),
        (1, 6, '0.1(6)'),
        (1, 7, '0.(142857)'),
        (1, 8, '0.125'),
        (1, 9, '0.(1)'),
        (-0, 1, '0'),
        (-1, 1, '-1'),
        (-1, 2, '-0.5'),
        (-1, 3, '-0.(3)'),
        (-1, 4, '-0.25'),
        (-1, 5, '-0.2'),
        (-1, 6, '-0.1(6)'),
        (-1, 7, '-0.(142857)'),
        (-1, 8, '-0.125'),
        (-1, 9, '-0.(1)'),
        (0, -1, '0'),
        (1, -1, '-1'),
        (1, -2, '-0.5'),
        (1, -3, '-0.(3)'),
        (1, -4, '-0.25'),
        (1, -5, '-0.2'),
        (1, -6, '-0.1(6)'),
        (1, -7, '-0.(142857)'),
        (1, -8, '-0.125'),
        (1, -9, '-0.(1)'),
    ])
    def test_decimal_fraction(
        self,
        numerator: int,
        denominator: int,
        expected: bool,
    ) -> None:
        self.assertEqual(decimal_fraction(numerator, denominator), expected)


if __name__ == '__main__':
    unittest.main()

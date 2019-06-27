#!/usr/bin/env python3

from math import factorial
from typing import Any, Dict, Generator, List, Union


def choose(n: int, k: int) -> int:
    """
    Returns the binomial coefficient for n choose k.
    """
    if 0 <= k <= n:
        N = 1
        K = 1
        for i in range(1, min(k, n - k) + 1):
            N *= n
            K *= i
            n -= 1
        return N // K
    else:
        return 0


def gen_permutation(A: List[Any]) -> Generator[List[Any], None, None]:
    """
    Generator function for ordered permutations of a list.
    """
    if len(A) == 0:
        yield []
    for i in range(len(A)):
        for B in gen_permutation(A[:i] + A[i + 1:]):
            yield [A[i]] + B


def kth_permutation(A: List[Any], k: int) -> List[Any]:
    """
    Returns the kth permutation of a list of items.
    """
    if A == []:
        return []

    N = len(A)
    i = (k - 1) // factorial(N - 1)

    return [
        A[i],
    ] + kth_permutation(
        A[:i] + A[i + 1:],
        k - i * factorial(N - 1),
    )


def cyclic_permutations(n: int) -> List[int]:
    """
    Returns all lexicographically sorted unique cyclic permutations of n.
    """
    permutations = set()
    s = str(n)
    for i in range(len(s)):
        permutations.add(int(s[i:] + s[:i]))
    return sorted(permutations)


def is_factorion(n: int) -> bool:
    """
    Returns True if n is a factorion.
    """
    return sum(map(lambda x: factorial(int(x)), str(n))) == n


def is_palindrome(n: int, base: int = 10) -> bool:
    """
    Returns True if n is a palindromic number.
    """
    if base == 10:
        return str(n) == str(n)[::-1]
    else:
        m = 0
        k = n
        while k > 0:
            m = m * base + k % base
            k = k // base
        return n == m


def is_lychrel(n: int, iterations: int = 50) -> bool:
    """
    Returns True if n is a Lychrel number within the number of iterations.
    """
    if iterations == 0:
        return True
    n += int(str(n)[::-1])
    return not (is_palindrome(n) or not is_lychrel(n, iterations - 1))


def is_pandigital(n: Union[int, str], zero: bool = False) -> bool:
    """
    Returns True if n is pandigital.
    """
    s = str(n)
    return [str(d) for d in range(0 if zero else 1, 10)] == sorted(s)


def is_pythagorean(a: int, b: int, c: int) -> bool:
    """
    Returns True if a, b, and c form a Pythagorean triple.
    """
    return (
        a > 0 and
        b > 0 and
        c > 0 and
        a ** 2 + b ** 2 == c ** 2
    )


def is_square(n: int) -> bool:
    """
    Returns True if n is a perfect square.
    """
    return int(n ** 0.5) ** 2 == n


def is_triangular(n: int, zero: bool = False) -> bool:
    """
    Returns True if n is a triangular number.
    """
    if n == 0:
        return zero
    i = int((n * 2) ** 0.5)
    return i * (i + 1) // 2 == n


def gen_triangular(zero: bool = False) -> Generator[int, None, None]:
    """
    Generator function for triangular numbers.
    """
    i = 0 if zero else 1
    while True:
        yield nth_triangular(i)
        i += 1


def nth_triangular(n: int) -> int:
    """
    Returns the nth triangular number.
    """
    return n * (n + 1) // 2


def is_pentagonal(n: int, zero: bool = False) -> bool:
    """
    Returns True if n is a pentagonal number.
    """
    if n == 0:
        return zero
    i = int((n * 2 / 3) ** 0.5) + 1
    return i * (3 * i - 1) // 2 == n


def gen_pentagonal(zero: bool = False) -> Generator[int, None, None]:
    """
    Generator function for pentagonal numbers.
    """
    i = 0 if zero else 1
    while True:
        yield nth_pentagonal(i)
        i += 1


def nth_pentagonal(n: int) -> int:
    """
    Returns the nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


def is_hexagonal(n: int, zero: bool = False) -> bool:
    """
    Returns True if n is a hexagonal number.
    """
    if n == 0:
        return zero
    i = int((n / 2) ** 0.5) + 1
    return i * (2 * i - 1) == n


def gen_hexagonal(zero: bool = False) -> Generator[int, None, None]:
    """
    Generator function for hexagonal numbers.
    """
    i = 0 if zero else 1
    while True:
        yield nth_hexagonal(i)
        i += 1


def nth_hexagonal(n: int) -> int:
    """
    Returns the nth hexagonal number.
    """
    return n * (2 * n - 1)


def divisors(n: int, proper: bool = False) -> List[int]:
    """
    Returns the list of divisors of n.
    """
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s) if not proper else sorted(s)[:-1]


def num_divisors(n: int, proper: bool = False) -> int:
    """
    Returns the number of divisors of n.
    """
    return len(divisors(n, proper))


def sum_divisors(n: int, proper: bool = False) -> int:
    """
    Returns the sum of all divisors of n.
    """
    return sum(divisors(n, proper))


def is_abundant(n: int) -> bool:
    """
    Returns True if n is an abundant number.
    """
    return sum_divisors(n, proper=True) > n


def is_deficient(n: int) -> bool:
    """
    Returns True if n is an deficient number.
    """
    return sum_divisors(n, proper=True) < n


def is_perfect(n: int) -> bool:
    """
    Returns True if n is a perfect number.
    """
    return sum_divisors(n, proper=True) == n


def is_amicable(a: int, b: int) -> bool:
    """
    Return True if a and b are amicable numbers and form an amicable pair.
    """
    return (
        sum_divisors(a, proper=True) == b and
        sum_divisors(b, proper=True) == a
    )


def gen_collatz(start: int) -> Generator[int, None, None]:
    """
    Generator function for the Collatz sequence.

    The sequence is defined over the set of positive integers by:
        n -> n / 2      (n is even)
        n -> 3 * n + 1  (n is odd)
    """
    n = start

    while True:
        yield n
        if n == 1:
            return
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


def decimal_fraction(numerator: int, denominator: int) -> str:
    """
    Returns the decimal representation of a fraction as a string with
    recurring cycles marked inside parentheses.
    """
    if denominator == 0:
        return 'Undefined'

    result = ''

    if numerator * denominator < 0:
        result += '-'

    n = abs(numerator)
    d = abs(denominator)

    result += str(n // d)
    n = n % d

    if n > 0:
        result += '.'

    memoize: Dict[int, int] = {}
    while n > 0 and n not in memoize:
        memoize[n] = len(result)
        result += str(n * 10 // d)
        n = n * 10 % d

    if n == 0:
        return result
    else:
        i = memoize[n]
        return f'{result[:i]}({result[i:]})'

#!/usr/bin/env python3

from typing import Generator, Optional, Set
from utils.number import cyclic_permutations


def is_prime(n: int) -> bool:
    """
    Returns True if n is a prime number.
    """
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n: int) -> bool:
    """
    Returns True if n is a circular prime.
    """
    return all(is_prime(p) for p in cyclic_permutations(n))


def is_truncatable_prime(n: int) -> bool:
    """
    Returns True if n is truncatable both from the left and from the right.
    """
    if not is_prime(n) or n < 10:
        return False
    s = str(n)
    for i in range(1, len(s)):
        left = int(s[:i])
        right = int(s[i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True


def gen_prime() -> Generator[int, None, None]:
    """
    Generator function for prime numbers.
    """
    yield 2
    yield 3

    i = 1
    while True:
        for n in (6 * i - 1, 6 * i + 1):
            if is_prime(n):
                yield n
        i += 1


def nth_prime(n: int) -> Optional[int]:
    """
    Returns the nth prime number.
    """
    for i, prime in enumerate(gen_prime(), start=1):
        if i == n:
            return prime
    return None


def prime_factors(n: int) -> Set[int]:
    """
    Returns the set of distinct prime factors of n.
    """
    factors = set()
    for prime in gen_prime():
        if prime > n:
            break
        while n % prime == 0:
            factors.add(prime)
            n = n // prime
    return factors


def largest_prime_factor(n: int) -> Optional[int]:
    """
    Returns the largest prime factor of n.
    """
    try:
        return max(prime_factors(n))
    except ValueError:
        return None

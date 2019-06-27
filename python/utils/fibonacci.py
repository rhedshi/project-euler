#!/usr/bin/env python3

from typing import Generator


def gen_fibonacci(zero: bool = False) -> Generator[int, None, None]:
    """
    Generator function for the Fibonacci sequence.
    """
    f0 = 0 if zero else 1
    f1 = 1

    yield f0
    yield f1

    while True:
        f0, f1 = f1, f0 + f1
        yield f1

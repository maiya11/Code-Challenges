"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
"""


def smallestEvenMultiple(n: int) -> int:
    num = 2
    while num % n != 0:
        num += 2
    return num

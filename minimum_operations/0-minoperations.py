#!/usr/bin/python3
""" define minOperation"""


def minOperations(n):
    """" finds the mininum operation """

    if not n or n < 2:
        return 0
    total_operation = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            total_operation += divisor
        else:
            divisor = divisor + 1 if divisor == 2 else divisor + 2

    return total_operation

#!/usr/bin/python3
""" Minimum operations """


def minOperations(n):
    """ method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file. """
    if (not isinstance(n, int) or n < 2):
        return 0

    i = 2
    res = 0
    while i <= n:
        if n % i == 0:
            res += i
            n = n / i
            i -= 1
        i += 1
    return int(res)

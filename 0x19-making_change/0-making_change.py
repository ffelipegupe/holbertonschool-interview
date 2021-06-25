#!/usr/bin/python3
""" Coins module """


def makeChange(coins, total):
    """ Function to determine the fewest number of coins """
    if total == 0:
        return 0
    coins.sort(reverse=True)
    sum = 0
    i = 0
    c = 0
    num_coins = len(coins)
    while sum < total and i < num_coins:
        while coins[i] <= total - sum:
            sum += coins[i]
            c += 1
            if sum == total:
                return c
        i += 1
    return -1

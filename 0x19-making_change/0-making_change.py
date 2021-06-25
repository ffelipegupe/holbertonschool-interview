#!/usr/bin/python3
""" Coins module """


def makeChange(coins, total):
    """ Function to determine the fewest number of coins """
    if total == 0:
        return 0
    coins.sort()
    res = 0
    for i in range(0, len(coins)):
        if coins[i] <= total:
            total -= coins[i]
            res += 1
        elif coins[i] > total:
            coins.pop()
            
            print(total)
    return res

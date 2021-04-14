#!/usr/bin/python3
""" Rain module """


def rain(walls):
    """ Function that Given a list of non-negative integers representing
        walls of width 1, calculate how much water will be retained after
        it rains.
    """
    return (sum(walls) - max(walls))

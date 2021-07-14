#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    function def island_perimeter(grid): that returns the perimeter of the
    island described in grid
    """
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                if x == 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                if y == 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                if x == len(grid) - 1 or grid[x + 1][y] == 0:
                    perimeter += 1
                if y == len(grid[x]) - 1 or grid[x][y + 1] == 0:
                    perimeter += 1
    return (perimeter)

#!/usr/bin/python3
'''
N queens puzzle challenge
'''
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    table = []

    def queens(row, n, table):
        if (row == n):
            print(table)
        else:
            for i in range(n):
                placement = [row, i]
                if validation(table, placement):
                    table.append(placement)
                    queens(row + 1, n, table)
                    table.remove(placement)

    def validation(table, placement):
        for q in table:
            if q[1] == placement[1]:
                return False
            if (q[0] + q[1]) == (placement[0] + placement[1]):
                return False
            if (q[0] - q[1]) == (placement[0] - placement[1]):
                return False
        return True

    queens(0, n, table)

#!/usr/bin/python3
""" Log parsing """
from sys import stdin


codes_dic = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

size = 0


def printing():
        """ Function that prints logs """
        print("File size: {}".format(size))
        for key in sorted(codes_dic.keys()):
            if codes_dic[key] and isinstance(int(key), int):
                print("{}: {}".format(key, codes_dic[key]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            count += 1
            data = line.split()
            size += int(data[-1])
            if len(data) > 2:
                    if data[-2] in codes_dic and isinstance(int(data[-2]),
                                                            int):
                            codes_dic[data[-2]] += 1
                            if count % 10 == 0:
                                    printing()
    except Exception:
        pass
    finally:
        printing()

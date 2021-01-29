#!/usr/bin/python3
""" Log parsing """
from sys import stdin


codes_dic = {
            "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
            "405": 0, "500": 0}
size = 0


def printing():
    """ Function that prints logs """
    print("File size: {}".format(size))
    for key in sorted(codes_dic.keys()):
        if codes_dic[key]:
            print("{}: {}".format(key, codes_dic[key]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                data = line.split()
                size += int(data[-1])
                if data[-2] in codes_dic:
                    codes_dic[data[-2]] += 1
            except:
                pass
            if count == 9:
                printing()
                count = -1
            count += 1
    except KeyboardInterrupt:
        printing()
        raise
    printing()

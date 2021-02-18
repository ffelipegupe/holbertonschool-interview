#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.

    Returns: True, if is a valid UTF-8 encoding; False, otherwise
    """
    n_bytes = 0

    for d in data:
        byte = format(d, '#010b')[-8:]
        if n_bytes == 0:
            if byte[0] == '1':
                n_bytes = len(byte.split('0')[0])
            if n_bytes > 4 or n_bytes == 1:
                return False
            if n_bytes == 0:
                continue
        else:
            if not byte.startswith('10'):
                return False
        n_bytes -= 1

    if n_bytes != 0:
        return False
    return True

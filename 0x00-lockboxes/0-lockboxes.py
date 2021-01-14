#!/usr/bin/python3
""" Method to unlock boxes """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened """
    for x in range(1, len(boxes) - 1):
        tar = False
        for idx in range(len(boxes)):
            tar = x in boxes[idx] and x != idx
            if tar:
                break
        if not tar:
            return tar
    return True                    

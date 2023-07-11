from os import *
from sys import *
from collections import *
from math import *


def abbrHelper(string, res, temp='', count=0, ind=0):
    if (ind >= len(string)):
        if (count > 0):
            temp += str(count)
        res.append(temp)
        return

    if (count == 0):
        abbrHelper(string, res, temp+string[ind], count, ind+1)
        abbrHelper(string, res, temp, count+1, ind+1)

    else:
        abbrHelper(string, res, temp + str(count) + string[ind], 0, ind+1)
        abbrHelper(string, res, temp, count+1, ind+1)


def findAbbr(str):
    # Write your code here.
    res = []
    abbrHelper(str, res)
    res.sort()
    return res

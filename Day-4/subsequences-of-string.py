from os import *
from sys import *
from collections import *
from math import *


def subSequenceHelper(str, res, temp='', start=0):
    if (start == len(str)):
        return

    for i in range(start, len(str)):
        res.append(temp+str[i])
        subSequenceHelper(str, res, temp+str[i], i+1)


def subsequences(str):

    # Write your code here
    res = []
    subSequenceHelper(str, res)
    return res


subsequences('abc')

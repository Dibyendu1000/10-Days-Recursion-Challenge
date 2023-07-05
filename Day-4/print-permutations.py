from os import *
from sys import *
from collections import *
from math import *


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def permutationHelper(arr, res, start=0):
    if (start >= len(arr)):
        res.append(''.join(arr))
        return

    for i in range(start, len(arr)):
        swap(arr, start, i)
        permutationHelper(arr, res, start+1)
        swap(arr, start, i)


def printPermutations(s):
    # Write your code here.
    arr = list(s)
    res = list()
    permutationHelper(arr, res)
    return res

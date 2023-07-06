from os import *
from sys import *
from collections import *
from math import *


def factorHelper(n, res, temp, prod=1, start=2):
    if (prod > n):
        return
    if (prod == n):
        res.append([]+temp)
        return
    for i in range(start, (n//2)+1):
        if (n % i == 0):
            prod *= i
            temp.append(i)
            factorHelper(n, res, temp, prod, i)
            temp.pop()
            prod //= i


def factorCombinations(n):
    # Write your code here.
    res, temp = [], []
    factorHelper(n, res, temp)
    return res


factorCombinations(12)

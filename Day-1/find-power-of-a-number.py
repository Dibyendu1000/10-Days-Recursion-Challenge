from os import *
from sys import *
from collections import *
from math import *


def pow(X, N):

    # If power is 0, then we return 1 as asked in question
    if (N == 0):
        return 1
    # At every recursion we calculate half power asked, in this way we prevent
    # redundant multiplications, which can be avoided
    halfPower = pow(X, N//2)
    if (N % 2 == 0):
        return halfPower*halfPower
    else:
        return halfPower*halfPower*X

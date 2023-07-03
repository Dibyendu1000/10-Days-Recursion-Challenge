from os import *
from sys import *
from collections import *
from math import *


def canNinjaWinHelper(str):
    for i in range(len(str)-1):
        if (str[i] == '$' and str[i+1] == '$'):
            newStr = str[:i]+'**'+str[i+2:]
            if (not canNinjaWinHelper(newStr)):
                return True

    return False


def canNinjaWin(str):
    # Write your code here.
    if (len(str) < 2):
        return False
    else:
        return canNinjaWinHelper(str)

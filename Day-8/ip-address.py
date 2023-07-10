from os import *
from sys import *
from collections import *
from math import *


def check(octet):
    n = len(octet)
    if (n == 1):
        return True
    if (n < 1 or n > 3 or octet[0] == '0'):
        return False

    octVal = int(octet)
    if (octVal > 255):
        return False
    else:
        return True


def helper(s, res, IP, start, segment):
    if (segment == len(IP) and start == len(s)):
        res.append('.'.join(IP))
        return

    if (segment >= len(IP) or start >= len(s)):
        return

    for i in range(1, 4):
        temp = s[start: start+i]
        if (check(temp)):
            IP[segment] = temp
            helper(s, res, IP, start+i, segment+1)


def generateIPAddress(s):
    # Write your code here.
    res = []
    IP = [None]*4
    if (len(s) <= 12 and len(s) >= 4):
        helper(s, res, IP, 0, 0)
    return res

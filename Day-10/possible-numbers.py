from os import *
from sys import *
from collections import *
from math import *


def pow(x, n):
    if (n == 0):
        return 1
    mid = pow(x, n//2)
    if (n & 1):
        return mid*mid*x
    else:
        return mid*mid


def lessDigitsValueCount(digitsCount, n):
    noOfDigits = int(log10(n))+1
    count = 0
    for i in range(1, noOfDigits):
        count = count + pow(digitsCount, i)
    return count


def intToList(x):
    l = []
    while (x):
        l.append(x % 10)
        x //= 10
    l.reverse()
    return l


def equalDigitsValueCount(n, m, digits, ind=0):
    if (ind == len(n)):
        return 1
    count = 0
    for i in range(m):
        if (digits[i] < n[ind]):
            count += pow(m, len(n)-ind-1)
        elif (digits[i] == n[ind]):
            count += equalDigitsValueCount(n, m, digits, ind+1)
        else:
            break
    return count


def possibleNumbers(n, m, digits):
    less = lessDigitsValueCount(m, n)
    listN = intToList(n)
    equal = equalDigitsValueCount(listN, m, digits)
    return less + equal


print(possibleNumbers(45, 3, [1, 4, 5]))

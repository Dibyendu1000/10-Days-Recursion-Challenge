from os import *
from sys import *
from collections import *
from math import *


def findKthElement(arr1, arr2, k):
    # Write your code here.
    i, j = 0, 0
    while (i < len(arr1) and j < len(arr2)):
        if (arr1[i] < arr2[j]):
            # print('i')
            if (k == 1):
                return arr1[i]
            i += 1
            k -= 1

        else:
            # print('j')
            if (k == 1):
                return arr2[j]
            j += 1
            k -= 1

    while (i < len(arr1)):
        # print('i')
        if (k == 1):
            return arr1[i]
        i += 1
        k -= 1

    while (j < len(arr2)):
        # print('j')
        if (k == 1):
            return arr2[j]
        j += 1
        k -= 1

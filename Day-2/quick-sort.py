from os import *
from sys import *
from collections import *
from math import *


def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l, r):
        if (arr[j] <= pivot):
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


def quickSortHelper(arr, l, r):
    if (l < r):
        pivot = partition(arr, l, r)
        quickSortHelper(arr, l, pivot-1)
        quickSortHelper(arr, pivot+1, r)


def quickSort(arr):
    # Write the function here.
    quickSortHelper(arr, 0, len(arr)-1)
    return arr

def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1: r+1]
    i, j, k = 0, 0, l
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while (i < len(left)):
        arr[k] = left[i]
        i, k = i+1, k+1

    while (j < len(right)):
        arr[k] = right[j]
        j, k = j+1, k+1


def mergeSortHelper(arr, l, r):
    if (l < r):
        m = (l + r)//2
        mergeSortHelper(arr, l, m)
        mergeSortHelper(arr, m+1, r)
        merge(arr, l, m, r)


def mergeSort(arr, n):
    # Write your code here.
    mergeSortHelper(arr, 0, n-1)
    return arr

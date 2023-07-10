from typing import List


def combHelper(arr, n, target, temp, res, currSum=0, start=0):
    if (currSum == target):
        tupleTemp = tuple(temp)
        if (tupleTemp not in res):
            res.add(tupleTemp)
        return res

    if (currSum > target):
        return

    for i in range(start, n):
        temp.append(arr[i])
        combHelper(arr, n, target, temp, res, currSum+arr[i], i+1)
        temp.pop()


def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
    # Write your code here.
    arr.sort()
    res = set()
    combHelper(arr, n, target, [], res)
    res = list(res)
    return sorted(res)


print(combinationSum2([1, 2, 6, 1, 5], 5, 8))

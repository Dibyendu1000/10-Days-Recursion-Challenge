def combSumHelper(arr, B, res, currSum, temp, start=0):
    if (currSum == B):
        res.append([]+temp)
        return

    if (currSum > B):
        return

    for i in range(start, len(arr)):
        temp.append(arr[i])
        combSumHelper(arr, B, res, currSum+arr[i], temp, i)
        temp.pop()


def combSum(ARR, B):
    # Write your code here
    res = []
    combSumHelper(ARR, B, res, 0, [])
    return res

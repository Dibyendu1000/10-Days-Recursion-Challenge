def helper(n, res, remain, ind=0):
    if (ind >= len(res)):
        return res

    if (res[ind] != 0):
        return helper(n, res, remain, ind+1)

    for i in range(n, 0, -1):
        if (remain[i] != 0):
            if (i == 1):
                res[ind] = i
                remain[i] = 0
                tempAns = helper(n, res, remain, ind+1)
                if (len(tempAns)):
                    return tempAns
                res[ind] = 0
                remain[i] = 1
            else:
                if (ind + i < len(res) and res[ind+i] == 0):
                    res[ind], res[ind+i] = i, i
                    remain[i] = 0
                    tempAns = helper(n, res, remain, ind+1)
                    if (len(tempAns)):
                        return tempAns
                    res[ind], res[ind+i] = 0, 0
                    remain[i] = 1
    return []


def validSequence(n):
    # Write your code here.
    res = [0]*(2*n-1)
    remain = [1]*(n+1)
    return helper(n, res, remain)

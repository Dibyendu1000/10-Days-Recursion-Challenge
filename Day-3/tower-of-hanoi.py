def solveTowerOfHanoi(n, res, start=1, aux=2, dest=3):
    if (n > 0):
        solveTowerOfHanoi(n-1, res, start, dest, aux)
        res.append([start, dest])
        solveTowerOfHanoi(n-1, res, aux, start, dest)


def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    res = []
    solveTowerOfHanoi(n, res)
    return res

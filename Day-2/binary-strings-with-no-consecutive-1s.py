from sys import stdin, setrecursionlimit
import sys
setrecursionlimit(10**6)


def generateStringHelper(k, temp, res):
    if (k == 0):
        res.append(temp)
        return

    if (len(temp) == 0):
        generateStringHelper(k-1, temp+'0', res)
        generateStringHelper(k-1, temp+'1', res)
    else:
        if (temp[-1] == '0'):
            generateStringHelper(k-1, temp+'0', res)
            generateStringHelper(k-1, temp+'1', res)
        else:
            generateStringHelper(k-1, temp+'0', res)


def generateString(k):
    # Write your code here.
    res = []
    generateStringHelper(k, '', res)
    return res


# Main.
n = int(input())
answer = generateString(n)
for x in answer:
    print(*x, sep='', end=' ')
print()

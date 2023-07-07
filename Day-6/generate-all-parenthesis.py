def parenthesisHelper(n, res, openB=0, closeB=0, temp=""):
    if (len(temp) == 2*n):
        res.append(temp)
        return

    if (openB > closeB):
        parenthesisHelper(n, res, openB, closeB+1, temp+")")

        if (openB < n):
            parenthesisHelper(n, res, openB+1, closeB, temp+"(")
    else:
        parenthesisHelper(n, res, openB+1, closeB, temp+"(")


def validParenthesis(n: int) -> int:
    # Write your code here.
    res = []
    parenthesisHelper(n, res)
    return res

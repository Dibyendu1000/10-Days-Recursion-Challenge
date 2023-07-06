def diagSafe(board, row, col):
    for i in range(1, len(board)):
        if (row-i >= 0 and col-i >= 0):
            if (board[row-i][col-i] == 1):
                return False
        else:
            break
    for i in range(1, len(board)):
        if (row-i >= 0 and col+i < len(board)):
            if (board[row-i][col+i] == 1):
                return False
        else:
            break
    return True


def topSafe(board, row, col):
    for i in range(1, len(board)):
        if (row-i >= 0):
            if (board[row-i][col] == 1):
                return False
        else:
            break
    return True


def leftSafe(board, row, col):
    for i in range(1, len(board)):
        if (col-i >= 0):
            if (board[row][col-i] == 1):
                return False
        else:
            break
    return True


def isSafe(board, row, col):
    leftIsSafe = leftSafe(board, row, col)
    topIsSafe = topSafe(board, row, col)
    diagIsSafe = diagSafe(board, row, col)

    if (leftIsSafe and topIsSafe and diagIsSafe):
        return True
    return False


def placeQueens(board, res, n, i=0):
    if (i >= n):
        temp = ""
        for i in range(n):
            for j in range(n):
                temp = temp + str(board[i][j])+" "
        res.append(temp)
        return

    for j in range(len(board)):
        if (isSafe(board, i, j)):
            board[i][j] = 1
            placeQueens(board, res, n, i+1)
            board[i][j] = 0
    return


def solveNQueens(n):
    # Write your code here.
    board = [[0]*n for i in range(n)]
    res = []
    placeQueens(board, res, n)
    return (res)


print(solveNQueens(4))

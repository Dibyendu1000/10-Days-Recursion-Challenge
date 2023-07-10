def isSafe(matrix, row, col, val):
    for i in range(9):
        if (matrix[i][col] == val):
            return False
        if (matrix[row][i] == val):
            return False
        if (matrix[3*(row//3) + i//3][3*(col//3) + i % 3] == val):
            return False
    return True


def isItSudoku(matrix):

    # Write your code here.
    for i in range(9):
        for j in range(9):
            if (matrix[i][j] == 0):
                for val in range(1, 10):
                    if (isSafe(matrix, i, j, val)):
                        matrix[i][j] = val
                        if (isItSudoku(matrix)):
                            return True
                        matrix[i][j] = 0
                return False
    return True


print(isItSudoku([[9, 0, 0, 0, 2, 0, 7, 5, 0], [6, 0, 0, 0, 5, 0, 0, 4, 0], [0, 2, 0, 4, 0, 0, 0, 1, 0], [2, 0, 8, 0, 0, 0, 0, 0, 0], [
      0, 7, 0, 5, 0, 9, 0, 6, 0], [0, 0, 0, 0, 0, 0, 4, 0, 1], [0, 1, 0, 0, 0, 5, 0, 8, 0], [0, 9, 0, 0, 7, 0, 0, 0, 4], [0, 8, 2, 0, 4, 0, 0, 0, 6]]))

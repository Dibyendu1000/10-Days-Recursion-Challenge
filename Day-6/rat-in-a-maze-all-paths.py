from os import *
from sys import *
from collections import *
from math import *


def moveRat(maze, n, solution, i=0, j=0):
    if (i == n-1 and j == n-1):
        solution[i][j] = 1
        for i in range(n):
            for j in range(n):
                print(solution[i][j], end=" ")
        return
    if (i >= n or j >= n or i < 0 or j < 0 or maze[i][j] == 0):
        return
    maze[i][j] = 0
    solution[i][j] = 1
    moveRat(maze, n, solution, i+1, j)
    moveRat(maze, n, solution, i, j+1)
    moveRat(maze, n, solution, i-1, j)
    moveRat(maze, n, solution, i, j-1)
    solution[i][j] = 0
    maze[i][j] = 1


def ratInAMaze(maze, n):
    # Write your code here.
    solution = [[0]*n for i in range(n)]
    moveRat(maze, n, solution)


# Main.
'''n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
ratInAMaze(maze , n)'''

import numpy as np
from collections import Counter

def isValidSudoku(board: list[list[str]]) -> bool:
    board = np.array(board)
    print(board.shape)


board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

for row in board:
    d = {}
    for val in row:
        if val == '.':
            continue
        else:
            if val in d:
                print("Error")
            else:
                d[val] = 1

print(board[:][0])





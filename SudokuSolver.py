
# precondition: (x, y) is a free spot
def check(sudoku, x, y, value):
    # first step: check the box
    pos = getPos(x, y)
    if pos == "bottomleft" and (sudoku[x+1][y] == value or sudoku[x+2][y] == value or
                                sudoku[x][y+1] == value or sudoku[x+1][y+1] == value or sudoku[x+2][y+1] == value or
                                sudoku[x][y+2] == value or sudoku[x+1][y+2] == value or sudoku[x+2][y+2] == value):
        return False
    if pos == "bottommid" and (sudoku[x+1][y] == value or sudoku[x-1][y] == value or
                               sudoku[x][y+1] == value or sudoku[x+1][y+1] == value or sudoku[x-1][y+1] == value or
                               sudoku[x][y+2] == value or sudoku[x+1][y+2] == value or sudoku[x-1][y+2] == value):
        return False
    if pos == "bottomright" and (sudoku[x-1][y] == value or sudoku[x-2][y] == value or
                                 sudoku[x][y+1] == value or sudoku[x-1][y+1] == value or sudoku[x-2][y+1] == value or
                                 sudoku[x][y+2] == value or sudoku[x-1][y+2] == value or sudoku[x-2][y+2] == value):
        return False
    if pos == "midleft" and (sudoku[x+1][y] == value or sudoku[x+2][y] == value or
                             sudoku[x][y+1] == value or sudoku[x+1][y+1] == value or sudoku[x+2][y+1] == value or
                             sudoku[x][y-1] == value or sudoku[x+1][y-1] == value or sudoku[x+2][y-1] == value):
        return False
    if pos == "midmid" and (sudoku[x+1][y] == value or sudoku[x-1][y] == value or
                            sudoku[x][y+1] == value or sudoku[x+1][y+1] == value or sudoku[x-1][y+1] == value or
                            sudoku[x][y-1] == value or sudoku[x+1][y-1] == value or sudoku[x-1][y-1] == value):
        return False
    if pos == "midright" and (sudoku[x-1][y] == value or sudoku[x-2][y] == value or
                              sudoku[x][y+1] == value or sudoku[x-1][y+1] == value or sudoku[x-2][y+1] == value or
                              sudoku[x][y-1] == value or sudoku[x-1][y-1] == value or sudoku[x-2][y-1] == value):
        return False
    if pos == "topleft" and (sudoku[x+1][y] == value or sudoku[x+2][y] == value or
                             sudoku[x][y-1] == value or sudoku[x+1][y-1] == value or sudoku[x+2][y-1] == value or
                             sudoku[x][y-2] == value or sudoku[x+1][y-2] == value or sudoku[x+2][y-2] == value):
        return False
    if pos == "topmid" and (sudoku[x+1][y] == value or sudoku[x-1][y] == value or
                            sudoku[x][y-1] == value or sudoku[x+1][y-1] == value or sudoku[x-1][y-1] == value or
                            sudoku[x][y-2] == value or sudoku[x+1][y-2] == value or sudoku[x-1][y-2] == value):
        return False
    if pos == "topright" and (sudoku[x-1][y] == value or sudoku[x-2][y] == value or
                              sudoku[x][y-1] == value or sudoku[x-1][y-1] == value or sudoku[x-2][y-1] == value or
                              sudoku[x][y-2] == value or sudoku[x-1][y-2] == value or sudoku[x-2][y-2] == value):
        return False
    # second step: check the horizontal
    for rightIter in range(x + 1, 9):
        if sudoku[rightIter][y] == value:
            return False
    for leftIter in range(0, x):
        if sudoku[leftIter][y] == value:
            return False
    # third step: check the vertical
    for upwardsIter in range(y + 1, 9):
        if sudoku[x][upwardsIter] == value:
            return False
    for downwartsIter in range(0, y):
        if sudoku[x][downwartsIter] == value:
            return False
    return True


# determine the position of the coordinate (x, y) in the 3x3 box
def getPos(x, y):
    pos = ""
    if y % 3 == 0:
        pos += "bottom"
    elif y % 3 == 1:
        pos += "mid"
    else:
        pos += "top"
    if x % 3 == 0:
        pos += "left"
    elif x % 3 == 1:
        pos += "mid"
    else:
        pos += "right"
    return pos

# get the next free spot of the sudoku grid


def nextSpot(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return [x, y]
    return None

# Solve a given sudoku
# Precondition: the sudoku is given as a matrix


def solveSudoku(sudoku):
    spot = nextSpot(sudoku)
    if spot == None:
        print("Solved!")
        return True
    x, y = spot
    for value in range(1, 10):
        if check(sudoku, x, y, value):
            sudoku[x][y] = value
            if solveSudoku(sudoku):
                return True
    sudoku[x][y] = 0
    return False


mySudoku1 = [[0, 9, 5, 0, 4, 6, 0, 0, 0],
             [0, 1, 0, 3, 2, 7, 5, 0, 6],
             [6, 3, 2, 0, 0, 0, 8, 0, 0],
             [0, 0, 7, 1, 3, 8, 0, 0, 0],
             [9, 4, 0, 0, 0, 0, 0, 8, 0],
             [0, 2, 0, 9, 5, 0, 0, 6, 0],
             [0, 0, 0, 0, 0, 0, 6, 1, 0],
             [4, 0, 3, 0, 0, 5, 2, 0, 0],
             [0, 0, 0, 0, 0, 9, 0, 0, 0]]

mySudoku2 = [[6, 5, 0, 3, 0, 0, 0, 0, 0],
             [0, 1, 0, 5, 0, 0, 0, 0, 7],
             [0, 3, 0, 2, 0, 0, 0, 0, 8],
             [0, 0, 0, 0, 0, 0, 7, 0, 5],
             [8, 0, 6, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 9, 3, 4, 0, 1],
             [9, 0, 4, 0, 0, 2, 0, 0, 0],
             [0, 0, 3, 0, 0, 6, 0, 5, 0],
             [0, 0, 7, 1, 0, 4, 0, 2, 6]]

solveSudoku(mySudoku2)
print(mySudoku2)

# This is a git push test

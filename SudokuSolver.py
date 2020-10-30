
# check if a given value is allowed at the given coordinate
def check(sudoku, x, y, value):
    # first step: check the box
    pos = getPos(x, y)
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for x in range(x0, x0 + 3):
        for y in range(y0, y0 + 3):
            if sudoku[x][y] == value:
                return False
    # second step: check the horizontal
    for horizontal in range(0, 9):
        if sudoku[horizontal][y] == value:
            return False
    # third step: check the vertical
    for vertical in range(0, 9):
        if sudoku[x][vertical] == value:
            return False
    return True


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

# all the logic function for the Game 2048

import random


# 1. start the game
def start():
    # create a 4x4 matrix with entries = 0
    mat = [[0 for i in range(4)] for j in range(4)]

    print('Please give a command: ')
    print('"W" or "w": Move UP')
    print('"S" or "s": Move Down')
    print('"A" or "a": Move Left')
    print('"D" or "d": Move Right')

    # then add a 2 to the matrix at a random place
    mat = add_new_2(mat)
    return mat


# 2. a function to add a 2 at a random place
def add_new_2(mat):
    # a new 2 will be pop up at a random empty place in the matrix
    # generate a random index(row/column) for the new 2
    row_2 = random.randint(0, 3)
    col_2 = random.randint(0, 3)

    # we do this for one more time, to ensure we choose a different cell
    # we have to make sure that this random place is empty
    # if there is no space for the new 2, then the game is over
    while mat[row_2][col_2] != 0:
        row_2 = random.randint(0, 3)
        col_2 = random.randint(0, 3)

    mat[row_2][col_2] = 2

    for row in mat:
        for val in row:
            print(val, end=" ")
        print()

    return mat


# 3. get the status of the game
def get_status(mat):
    # if you got 2048, then you win the game.
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'You won!'

    # As long as one of the cell is 0, the game is not over
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Game is not over.'

    # if any of the cell can be merged with the nearby(left/right one, up/down one) cell
    # then the game is not over
    for i in range(3):
        for j in range(3):
            if mat[i][j + 1] == mat[i][j] or mat[i + 1][j] == mat[i][j]:
                return 'Game is not over.'

    # since mat[i][4] or mat[4][j] will be out of range
    # we have to list them out separately
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'Game is not over.'

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'Game is not over.'

    else:
        return 'You lost!'


# 4. compress function
# compress all non-zero matrices towards one side of the board
# and eliminate the empty space between them
def compress(mat):
    # indicates whether any change happens or not
    changed = False
    new_mat = [[0 for i in range(4)] for j in range(4)]

    # shift each cell to its left extreme, row by row
    for i in range(4):
        pos = 0

        # traverse the columns each row
        # if it's non-zero, then we shift the number to the previous empty cell in that row
        # and the previous empty cell has col_index = pos
        for j in range(4):
            if mat[i][j] != 0:
                # the previous empty cell new_mat[i][pos] is replaced by mat[i][j]
                new_mat[i][pos] = mat[i][j]

                # if the column indexes are not the same
                # meaning that we make a change
                if j != pos:
                    changed = True

                pos += 1

    return new_mat, changed


# 5. merge function
# merge the cells if two values are the same (also non-empty)
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(4):
            # two cells have the same value, but they're not empty
            if mat[i][j] != 0 and mat[i][j] == mat[i][j + 1]:
                # merge cells
                # the first cell = 2 * previous value
                # the second cell = 0
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0

                # indicating that after merging, the matrix is different
                changed = True
    return mat, changed


# 6. reverse the cells in each row
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            # i, j = i, 3 - j
            new_mat[i].append(mat[i][3 - j])
    return new_mat


# 7. get the transpose of the matrix
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            # i, j => j, i
            new_mat[i].append(mat[j][i])
    return new_mat


# 8. move to the left
def move_left(grid):
    # we need to compress first, then merge
    # compress/merge function returns two output: new_mat and changed
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2

    # after merge, compress again
    new_grid, changed3 = compress(new_grid)

    return new_grid, changed


# 9. move to the right
def move_right(grid):
    # move_right = reverse the matrix, move_left, then reverse back
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed


# 10. move up
def move_up(grid):
    # move_up = transpose the matrix, move_left, then transpose back
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


# 11. move down
def move_down(grid):
    # move_down = transpose the matrix, move_right, then transpose back
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

matrix = [
    [-1, 3, -1, -1, -1, 1, -1, 9, -1],
    [2, -1, 8, -1, -1, 7, -1, -1, -1],
    [1, -1, -1, -1, -1, -1, 2, -1, 7],
    [-1, 5, 3, -1, 8, 9, 7, 2, -1],
    [-1, -1, -1, -1, 6, -1, -1, -1, -1],
    [-1, 7, 6, 3, 4, -1, 1, 5, -1],
    [7, -1, 9, -1, -1, -1, -1, -1, 8],
    [-1, -1, -1, 9, -1, -1, 4, -1, 2],
    [-1, 4, -1, 5, -1, -1, -1, 3, -1],
]

# replace -1 with [1...9], such that 

def check_avail(i, j, matrix: list[list]):
    avail = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if matrix[i][k] in avail:
            avail.remove(matrix[i][k])
        if matrix[k][j] in avail:
            avail.remove(matrix[k][j])
    # which box to check?
    box_i = (i // 3) * 3
    box_j = (j // 3) * 3
    for i in range(box_i, box_i + 3):
        for j in range(box_j, box_j + 3):
            if matrix[i][j] in avail:
                avail.remove(matrix[i][j])
    return avail

def sudoku_solver(matrix: list[list]):

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == -1:
                # check available options
                options = check_avail(i, j, matrix)
                if len(options) == 0:
                    return False
                for opt in options:
                    matrix[i][j] = opt
                    if sudoku_solver(matrix) == True:
                        return True
                    matrix[i][j] = -1
                return False
    return True


# print(check_avail(5, 1, matrix))
if sudoku_solver(matrix):
    for row in matrix:
        print(row)

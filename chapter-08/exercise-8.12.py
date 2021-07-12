"""
8.12 Eight Queens

Write an algorithm to print all ways of arranging eight queens on an 8x8
chess board so that none of them share the row, column, or diagonal. In
this case, "diagonal" means all diagonals, not just the two that bisect
the board.
"""
import copy

def place_queens(row, columns, results):
    if row == 8:
        results.append(copy.deepcopy(columns))
    else:
        for col in range(0,8):
            if check_valid(columns, row, col):
                columns[row] = col
                place_queens(row+1, columns, results)

def check_valid(columns, row1, column1):
    row2 = 0
    while row2 < row1:
        column2 = columns[row2]
        if column1 == column2:
            return False
        column_distance = abs(column2-column1)
        row_distance = row1-row2
        if column_distance == row_distance:
            return False
    return True
"""
10.9 Sorted Matrix Search

Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.

Solution 1: Taking advantage of one part of the sorting
"""

def find_element(matrix, elem):
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == elem:
            return True
        elif matrix[row][col] > elem:
            col -= 1
        else:
            row += 1
    return False

"""
10.9 Sorted Matrix Search

Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.

Solution 2: Binary Search
"""

def search_aux(mat, fromRow, toRow, fromCol, toCol, key):
    i = fromRow + (toRow - fromRow) // 2;
    j = fromCol + (toCol - fromCol) // 2;
    if (mat[i][j] == key):
        print("Found ", key, " at ", i, " ", j)
    else:
        if (i != toRow or j != fromCol):
            search_aux(mat, fromRow, i, j, toCol, key);

        if (fromRow == toRow and fromCol + 1 == toCol):
            if (mat[fromRow][toCol] == key):
                print("Found ", key, " at ", fromRow, " ", toCol);

        if (mat[i][j] < key):

            if (i + 1 <= toRow):
                search_aux(mat, i + 1, toRow, fromCol, toCol, key);

        else:
            if (j - 1 >= fromCol):
                search_aux(mat, fromRow, toRow, fromCol, j - 1, key);

def search(matrix, elem):
    search_aux(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, elem)

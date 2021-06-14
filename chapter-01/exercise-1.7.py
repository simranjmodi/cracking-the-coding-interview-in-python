"""
1.7 Rotate Matrix

Given an image represented by an NxN matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees.
"""

def rotate(matrix):
    if matrix.length == 0 or matrix.length != matrix[0].length:
        return False
    n = matrix.length

    for layer in range(n/2):
        first = layer
        last = n - 1 - layer
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i] # save top

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return True
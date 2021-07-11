"""
8.5 Recursive Multiply

Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit
shifting, but you should minimize the number of those operations.

Solution 1
"""

def min_product(a, b):
    if a < b:
        bigger = b
        smaller = a
    else:
        bigger = a
        smaller = b

    return min_product_helper(smaller, bigger)

def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1 # divide by 2
    side1 = min_product_helper(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller - s, bigger)
    return side1 + side2

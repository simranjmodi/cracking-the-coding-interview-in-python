"""
8.5 Recursive Multiply

Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit
shifting, but you should minimize the number of those operations.

Solution 3
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
    half_prod = min_product_helper(s, bigger)

    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger


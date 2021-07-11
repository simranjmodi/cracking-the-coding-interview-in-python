"""
8.5 Recursive Multiply

Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit
shifting, but you should minimize the number of those operations.

Solution 2
"""

def min_product(a, b):
    if a < b:
        bigger = b
        smaller = a
    else:
        bigger = a
        smaller = b

    memo = [0] * (smaller+1)
    return min_product_helper(smaller, bigger, memo)

def min_product_helper(smaller, bigger, memo):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif memo[smaller] > 0:
        return memo[smaller]

    s = smaller >> 1 # divide by 2
    side1 = min_product_helper(s, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller - s, bigger, memo)

    memo[smaller] = side1 + side2
    return memo[smaller]

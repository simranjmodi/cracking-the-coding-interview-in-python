"""
5.6 Conversion

Write a function to determine the number of bits you would need to flip
to convert integer A to integer B.
"""

def bit_swap_required(a, b):
    n = a ^ b
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count

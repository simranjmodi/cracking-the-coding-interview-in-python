"""
5.1 Insertion

You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at
bit i. You can assume that the bits j through i have enough space to fit
all of M.
"""


def insertion(n, m, i, j):
    clear_mask = -1 << (j + 1)
    capture_mask = (1 << i) - 1
    captured_bits = n & capture_mask

    n &= clear_mask
    m = m << i
    n |= m
    n |= captured_bits

    return n





"""
5.1 Insertion

You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at
bit i. You can assume that the bits j through i have enough space to fit
all of M.
"""


def update_bits(n, m, i, j):
    clear_mask = -1 << (j + 1)
    capture_mask = (1 << i) - 1

    # Capturing bits from i-1 to 0
    captured_bits = n & capture_mask

    # Clearing bits from j to 0
    n &= clear_mask

    # Shifting m to align with n
    m = m << i

    # Insert m into n
    n |= m

    # Insert captured bits
    n |= captured_bits

    return n





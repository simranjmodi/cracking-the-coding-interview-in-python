"""
5.4 Next Number

Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation.
"""

def get_next(n):
    # Compute c0 and c1 where c0 is the size of the block of
    # zeroes immediately to the left of the trailing ones and
    # c1 is the number of trailing ones and p = c1 = + c0
    c = n
    c0 = 0
    c1 = 0

    while (((c & 1) == 0) and (c != 0)):
        c0 += 1
        c >>= 1

    while ((c & 1) == 1):
        c1 += 1
        c >>= 1

    # Error: if n == 11...1100...00, then there is no bigger
    # number with the same number of 1s
    if ((c0 + c1) == 31) or ((c0 + c1) == 0):
        return -1

    p = c0 + c1 # Position of rightmost non-trailing zero

    n |= (1 << p) # Flip rightmost non-trailing zero
    n &= ~((1 << p) - 1) # Clear all bits to the right of p
    n |= (1 << (c1 - 1)) - 1 # Insert (c1-1) ones on the right

    return n

def get_prev(n):
    c = n
    c0 = 0
    c1 = 0
    while ((c & 1) == 1):
        c1 += 1
        c >>= 1

    if (c == 0):
        return -1

    while (((c & 1) == 0) and (c != 0)):
        c0 += 1
        c >>= 1

    p = c0 + c1 # Position of right most non-trailing one
    n &= ((~0) << (p+1)) # Clears from bit p onwards

    mask = (1 << (c1 + 1)) - 1 # Sequence of (c1 + 1) ones
    n |= mask << (c0 - 1) # (c1 + 1) ones followed by (c0 - 1) zeroes
    return n


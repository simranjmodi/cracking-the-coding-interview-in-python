"""
8.3 Magic Index

A magic index in an array A[1...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to
find a magic index, if one exists, in array A.

Solution 1: Elements are not distinct
"""

def magic_fast_aux(array, start, end):
    if end < start:
        return -1

    mid = (start+end)//2
    mid_value = array[mid]

    if mid_value == mid:
        return mid

    left = min(mid-1, mid_value)
    left = magic_fast_aux(array, start, left)
    if left >= 0:
        return left

    right = max(mid+1, mid_value)
    right = magic_fast_aux(array, right, end)

    return right

def magic_fast(array):
    return magic_fast_aux(array, 0, len(array) - 1)


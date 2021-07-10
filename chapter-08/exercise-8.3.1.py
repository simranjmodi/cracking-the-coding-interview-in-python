"""
8.3 Magic Index

A magic index in an array A[1...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to
find a magic index, if one exists, in array A.

Solution 1: Elements are distinct
"""

def magic_fast_aux(array, start, end):
    if end < start:
        return -1
    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return magic_fast_aux(array, start, mid-1)
    else:
        return magic_fast_aux(array, mid+1, end)

def magic_fast(array):
    return magic_fast_aux(array, 0, len(array) - 1)

"""
10.4 Sorted Search, No Size

You are given an array-like data structure Listy which lacks a size method.
It does, however, have an element_at(i) method that returns the element at
index i in O(1) time. If i is beyond the bounds of the data structure, it
returns -1. The data structure only supports positive integers. Given a
Listy which contains sorted, positive integers, find the index at which an
element x occurs. If x occurs multiple times, you may return any index.
"""

def search(list, value):
    index = 1
    while list.element_at(index) != -1 and list.element_at(index) < value:
        index *= 2
    return binary_search(list, value, index//2, index)

def binary_search(list, value, low, high):
    while low <= high:
        mid = (low + high)//2
        middle = list.element_at(mid)
        if middle > value or middle == -1:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
            return mid
    return -1

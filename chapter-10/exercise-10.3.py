"""
10.3 Search in Rotated Array

Given a sorted array of n integers that has been rotated an unknown number
of times, write code to find an element in the array. You may assume that
the array was originally sorted in increasing order.
"""

def search(a, left, right, x):
    mid = (left + right)//2
    if x == a[mid]:
        return mid

    if right < left:
        return -1

    if a[left] < a[mid]:                            # left is normally ordered
        if x >= a[left] and a < a[mid]:
            return search(a, left, mid-1, x)
        else:
            return search(a, mid+1, right, x)
    elif a[mid] < a[left]:                          # right is normally ordered
        if x > a[mid] and x <= a[right]:
            return search(a, mid+1, right, x)
        else:
            return search(a, left, mid-1, x)
    elif a[left] == a[mid]:                         # left or right half is all repeats
        if a[mid] != a[right]:                      # if right is different, search it
            return search(a, mid+1, right, x)
        else:                                       # else we have to search both halves
            result = search(a, left, mid-1, x)      # search left
            if result == -1:
                return search(a, mid+1, right, x)   # search right
            else:
                return result

    return -1

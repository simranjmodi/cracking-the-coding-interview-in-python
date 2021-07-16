"""
10.11 Peaks and Valleys

In an array of integers, a "peak" is an element which is greater than or
equal to the adjacent integers and a "valley" is an element which is less
than or equal to the adjacent integers. For example, in the array
{5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
array of integers, sort the array into an alternating sequence of peaks
and valleys.

Solution 1: Iterate through elements starting from index 1 and jumping
two elements at a time, swapping with previous element.
"""

def sort_valley(array):
    array = sorted(array)
    for i in range(1, len(array), 2):
        temp = array[i-1]
        array[i-1] = array[i]
        array[i] = temp
    return array

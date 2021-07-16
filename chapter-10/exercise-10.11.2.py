"""
10.11 Peaks and Valleys

In an array of integers, a "peak" is an element which is greater than or
equal to the adjacent integers and a "valley" is an element which is less
than or equal to the adjacent integers. For example, in the array
{5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
array of integers, sort the array into an alternating sequence of peaks
and valleys.

Solution 2: Remove sorting step
"""

def max_index(array, a, b, c):
    length = len(array)
    a_value = array[a] if (a >= 0 and a < length) else -1
    b_value = array[b] if (b >= 0 and b < length) else -1
    c_value = array[c] if (c >= 0 and c < length) else -1

    max_value = max(a_value, max(b_value, c_value))
    if a_value == max_value: return a
    elif b_value == max_value: return b
    else: return c

def sort_valley(array):
    for i in range(1, len(array), 2):
        biggest_index = max_index(array, i-1, i, i+1)
        if i != biggest_index:
            temp = array[i]
            array[i] = array[biggest_index]
            array[biggest_index] = temp
    return array


"""
10.5 Sparse Search

Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.
"""


def sparse_search(arr, key, low, high):
    left = 0
    right = 0

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == '':
            left = mid - 1
            right = mid + 1

            while True:
                if left < low and right > high:
                    return -1

                elif left >= low and arr[left] != '':
                    mid = left
                    break

                elif right <= high and arr[right] != '':
                    mid = right
                    break

                left -= 1
                right += 1

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            high = mid - 1

        elif arr[mid] < key:
            low = mid + 1

    return -1

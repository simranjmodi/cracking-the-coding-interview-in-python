"""
10.2 Group Anagrams

Write a method to sort an array of strings so that all the anagrams
are next to each other.
"""

from collections import defaultdict

def sort(array):
    map_list = defaultdict(list)

    for word in array:
        map_list["".join(sorted(word))].append(word)

    index = 0
    for key in map_list.keys():
        lst = map_list[key]
        for t in lst:
            array[index] = t
            index += 1
    return array

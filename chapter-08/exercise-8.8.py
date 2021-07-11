"""
8.8 Permutations with Duplicates

Write a method to print all permutations of a string whose characters
are not necessarily unique. The list of permutations should not have
duplicates
"""

def should_swap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1

def find_permutations(string, index, n):
    if index >= n:
        print(''.join(string))
        return

    for i in range(index, n):
        check = should_swap(string, index, i)
        if check:
            string[index], string[i] = string[i], string[index]
            find_permutations(string, index + 1, n)
            string[index], string[i] = string[i], string[index]

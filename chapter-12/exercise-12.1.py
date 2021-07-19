"""
12.1 Last K Lines

Write a method to print the last K lines of an input file.
"""

def last_n_lines(fname, N):
    with open(fname) as file:
        for line in (file.readlines()[-N:]):
            print(line, end='')

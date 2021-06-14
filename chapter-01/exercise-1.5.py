"""
1.5 One Away

There are three types of edits that can be performed on a string: insert a character,
remove a character, or replace a character. Given two strings, write a function to
check if they are one edit (or zero edits) away.
"""

def one_edit_replace(s1,s2):
    found_diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_diff:
                return False
            found_diff = True
    return True

def one_edit_insert(s1,s2):
    index1 = 0
    index2 = 0
    while index2<len(s2) and index1<len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def one_edit_away(first,second):
    if len(first) == len(second):
        return one_edit_replace(first,second)
    elif len(first)+1 == len(second):
        return one_edit_insert(first,second)
    elif len(first)-1 == len(second):
        return one_edit_insert(second,first)
    else:
        return False

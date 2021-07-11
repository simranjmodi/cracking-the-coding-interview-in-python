"""
8.9 Parens

Implement an algorithm to print all valid (i.e., properly opened and closed)
combinations of n pairs of parenthesis.
"""

def backtrack(ans,n, S=[], left=0, right=0):
    if len(S) == 2 * n:
        ans.append("".join(S))
        return ans
    if left < n:
        S.append("(")
        backtrack(ans,n, S, left + 1, right)
        S.pop()
    if right < left:
        S.append(")")
        backtrack(ans, n,S, left, right + 1)
        S.pop()

def generate_parenthesis(n):
    ans = []
    backtrack(ans,n)
    return ans


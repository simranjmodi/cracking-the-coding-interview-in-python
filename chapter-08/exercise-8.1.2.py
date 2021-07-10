"""
8.1 Triple Step

A child is running up a staircase with n steps and can hop either 1 step,
2 step or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.

Solution 2: Memoization
"""

def count_ways_aux(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways_aux(n-1, memo) \
                  + count_ways_aux(n-2,memo) \
                  + count_ways_aux(n-3, memo)
        return memo[n]

def count_ways(n):
    memo = [-1] * (n-1)
    count_ways_aux(n, memo)




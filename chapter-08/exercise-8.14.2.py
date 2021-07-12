"""
8.14 Boolean Evaluation

Given a boolean expression consisting of the symbols 0 (false), 1 (true),
& (AND), | (OR), and ^ (XOR), and a desired boolean result value result,
implement a function to count the number of ways of parenthesizing the
expression such that it evaluates to result. The expression should be
fully parenthesized (e.g., (0)^(1)) but not extraneously (e.g., (((0))^(1))).

Solution 2: Using memoization
"""

def count_eval(s, result, memo):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        if bool(s) == result: return 1
        else: return 0

    if (str(result) + s) in memo:
        return memo[str(result) + s]

    ways = 0

    for i in range(1, len(s), 2):
        c = s[i]
        left = s[0:i]
        right = s[i+1:len(s)]
        left_true = count_eval(left, True, memo)
        left_false = count_eval(left, False, memo)
        right_true = count_eval(right, True, memo)
        right_false = count_eval(right, False, memo)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == "^":
            total_true = left_true * right_false + left_false * right_true
        elif c == "&":
            total_true = left_true * right_true
        elif c == "|":
            total_true = left_true * right_true + left_false * right_true + left_true * right_false

        if result:
            sub_ways = total_true
        else:
            sub_ways = total - total_true
        ways += sub_ways

    memo[str(result) + s] = ways
    return ways

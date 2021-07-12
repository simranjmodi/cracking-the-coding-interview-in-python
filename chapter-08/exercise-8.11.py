"""
8.11 Coins

Given an infinite number of quarters (25 cents), dimes (10 cents), nickels
(5 cents), and pennies (1 cent), write code to calculate the number of ways
of representing n cents.
"""

def make_change(n):
    denoms = [25, 10, 5, 1]
    map = [[0 for i in range(len(denoms))] for j in range(n+1)]
    return make_change_aux(n, denoms, 0, map)

def make_change_aux(amount, denoms, index, map):
    if map[amount][index] > 0:
        return map[amount][index]

    if index >= len(denoms) - 1:
        return 1

    denom_amount = denoms[index]
    ways = 0

    i=0
    while i*denom_amount <= amount:
        amount_remaining = amount - i * denom_amount
        ways += make_change_aux(amount_remaining, denoms, index + 1, map)
        i+= 1

    map[amount][index] = ways
    return ways


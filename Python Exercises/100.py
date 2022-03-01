""""
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
"""


def solve(heads, legs):
    for i in range(heads + 1):
        j = heads - i
        if 2 * i + 4 * j == legs:
            return i, j

    return "No solutions!", "No solutions!"


num_heads = 35
num_legs = 94
solutions = solve(num_heads, num_legs)
print(solutions)

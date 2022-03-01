import itertools


def permutation(l):

    return list(itertools.permutations(l))


l = [1, 2, 3]
print(permutation(l))

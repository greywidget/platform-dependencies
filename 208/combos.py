from itertools import combinations


def find_number_pairs(numbers, N=10):
    return [pair for pair in combinations(numbers, 2) if pair[0] + pair[1] == N]

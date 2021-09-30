from itertools import combinations, permutations


def friends_teams(friends, team_size, order_does_matter):
    func = permutations if order_does_matter else combinations
    return func(friends, team_size)

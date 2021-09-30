from itertools import combinations, permutations


def friends_teams(friends, team_size=2, order_does_matter=False):
    func = permutations if order_does_matter else combinations
    return func(friends, team_size)

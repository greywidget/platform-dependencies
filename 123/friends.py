from collections import defaultdict

names = "bob julian tim martin rod sara joyce nick beverly kevin".split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (5, 9),
    (6, 8),
    (7, 8),
    (8, 9),
]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
    parse it to see who has most friends, return a tuple
    of (name_friend_with_most_friends, his_or_her_friends)"""
    user_friends = defaultdict(list)
    for id in users.keys():
        for friend1, friend2 in friendships:
            if friend1 == id:
                user_friends[id].append(users[friend2])
            elif friend2 == id:
                user_friends[id].append(users[friend1])

    best = sorted(
        [
            (
                users[k],
                sorted(v),
            )
            for k, v in user_friends.items()
        ],
        key=lambda x: len(x[1]),
    )[-1]
    return best


if __name__ == "__main__":
    result = get_friend_with_most_friends(friendships, users=users)
    print(result)

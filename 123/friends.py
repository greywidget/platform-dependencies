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


# PyBites solution
def get_friend_with_most_friends2(friendships, users=users):
    """Receives the friendships list of user ID pairs,
    parse it to see who has most friends, return a tuple
    of (name_friend_with_most_friends, his_or_her_friends)"""
    user_friends = defaultdict(list)  # use list, set would delete dups
    for p1, p2 in friendships:
        p1_name, p2_name = users.get(p1), users.get(p2)
        # use unique IDs as keys, not names
        user_friends[p1].append(p2_name)
        user_friends[p2].append(p1_name)

    idx, friends = sorted(user_friends.items(), key=lambda x: len(x[1]), reverse=True)[
        0
    ]
    breakpoint()
    return users.get(idx), friends


if __name__ == "__main__":
    result = get_friend_with_most_friends2(friendships, users=users)
    print(result)

from functools import reduce


def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
    of programming languages, return the common languages"""

    common = reduce(
        lambda x, y: x & y, [set(languages) for languages in programmers.values()]
    )
    return common

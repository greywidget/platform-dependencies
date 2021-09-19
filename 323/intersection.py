import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:

    sets = [set(item) for item in args if item]

    return functools.reduce(lambda x, y: x & y, sets) if sets else set()
